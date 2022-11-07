<template>
  <el-container>
<!--    <el-header>1</el-header>-->
    <el-container>
<!--      <el-aside>-->
<!--      </el-aside>-->
      <el-container>
        <side-menu :now-i-x="showStatus"></side-menu>
        <el-main style="padding: 0 30px;">
          <el-page-header style="margin-bottom: 20px;" title="Back" @click="showStatus -= 1"
                          v-if="showStatus > 0"></el-page-header>
          <div v-if="showStatus!==2" style="height: calc(100vh - 200px)">
            <el-scrollbar height="calc(100vh - 200px)">
              <UPLoadZIP v-if="showStatus === 0" @imgShow="showResult"></UPLoadZIP>
              <result-board v-if="showStatus === 1" :res="response" @showCode="showCode"></result-board>
            </el-scrollbar>
          </div>
          <div v-if="showStatus === 2">
            <el-row>
              <el-col :span="12">
                <h3 style="text-align: left;">{{ code_submission['first_submission']['name'] }}</h3>
              </el-col>
              <el-col :span="12">
                <h3 style="text-align: left;">{{ code_submission['second_submission']['name'] }}</h3>
              </el-col>
            </el-row>
            <el-divider></el-divider>
            <el-scrollbar height="60vh">
              <el-row>
                <el-col :span="12">
                  <pre style="text-align: left;">{{ code_submission['first_submission']['code'] }}</pre>
                </el-col>
                <el-col :span="12">
                  <pre style="text-align: left;">{{ code_submission['second_submission']['code'] }}</pre>
                </el-col>
              </el-row>
            </el-scrollbar>
          </div>
        </el-main>
        <el-footer>4</el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
import sideMenu from "@/components/sideMenu";
import UPLoadZIP from "@/components/UPLoadZIP";
import ResultBoard from "@/components/ResultBoard";

export default {
  name: "indexView",
  components: {ResultBoard, sideMenu, UPLoadZIP},
  data() {
    return {
      response: {},
      showStatus: 0,
      code_submission: {}
    }
  },
  methods: {
    showResult(res) {
      this.response = res
      this.showStatus = 1
    },
    showCode(id, first, sec) {
      this.code_submission['first_submission'] = {name: first}
      this.code_submission['second_submission'] = {name: sec}
      this.$axios.get('/overview/sourceFile', {
        params: {
          file: id,
          first: first,
          second: sec,
        }
      }).then(res => {
        console.log(res)
        this.first_submission = res.data['first_submission']
        this.code_submission['first_submission']['code'] = res.data['first_submission']
        this.code_submission['second_submission']['code'] = res.data['second_submission']
        this.showStatus = 2
      })
    }
  }
}
</script>

<style scoped>

</style>