<template>
  <el-container>

    <el-header
        style="text-align: left;line-height: 60px;align-items: center;display: flex;box-shadow: 0 0 5px #ccc;z-index: 999;">
      <img :src="require('@/assets/logo.png')" alt="" height="30">
    </el-header>
    <el-main style="padding: 20px 50px;">
      <el-row>
        <el-col :span="12">
          <h3 style="text-align: left;">{{ code_submission['first_submission']['name'] }}</h3>
        </el-col>
        <el-col :span="12">
          <h3 style="text-align: left;">{{ code_submission['second_submission']['name'] }}</h3>
        </el-col>
      </el-row>
      <el-divider></el-divider>
      <el-scrollbar height="70vh">
        <el-row>
          <el-col :span="12">
            <pre style="text-align: left;">{{ code_submission['first_submission']['code'] }}</pre>
          </el-col>
          <el-col :span="12">
            <pre style="text-align: left;">{{ code_submission['second_submission']['code'] }}</pre>
          </el-col>
        </el-row>
      </el-scrollbar>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: "codeView",
  data() {
    return {
      code_submission: {
        first_submission: {name: ''},
        second_submission: {name: ''},
      }
    }
  },
  mounted() {
    let id = this.$route.params.id
    let first = this.$route.params.first
    let sec = this.$route.params.second
    console.log(id, first, sec)
    this.code_submission['first_submission'] = {name: first}
    this.code_submission['second_submission'] = {name: sec}
    this.$axios.get('/overview/sourceFile', {
      params: {
        file: id,
        first: first,
        second: sec,
      }
    }).then(res => {
      this.first_submission = res.data['first_submission']
      this.code_submission['first_submission']['code'] = res.data['first_submission']
      this.code_submission['second_submission']['code'] = res.data['second_submission']
    })
  }
}
</script>

<style scoped>

</style>