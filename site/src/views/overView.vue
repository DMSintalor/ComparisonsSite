<template>
  <el-container>
    <el-header
        style="text-align: left;line-height: 60px;align-items: center;display: flex;box-shadow: 0 0 5px #ccc;z-index: 999;">
      <img :src="require('@/assets/logo.png')" alt="" height="30">
    </el-header>
    <el-main style="padding: 0;">
      <el-row>
        <el-col :span="4">
          <el-scrollbar height="calc(100vh - 60px)">
            <el-collapse v-model="side_activeName" accordion>
              <el-collapse-item v-for="user in submission_user"
                                :key="user" :title="user">
                <ul>
                  <li v-for="(key,val) in submissions[user]" :key="key" style="text-align: left;">
                    <el-row style="display: flex;align-items: center;">
                      <el-col :span="20">
                        <el-button type="info" text @click="changePage(user,val)">{{ val }}</el-button>
                      </el-col>
                      <el-col :span="4">
                        {{ formatNumber(submission_map[user][val]) }}
                      </el-col>
                    </el-row>
                    <template v-if="1===0">{{ val }}</template>
                  </li>
                </ul>
              </el-collapse-item>
            </el-collapse>
          </el-scrollbar>
        </el-col>
        <el-col :span="12">
          <div id="main" style="height: 60vh;width: 100%;padding-left: 10px;padding-top: 20px;"></div>
          <div style="height: calc(40vh - 100px);margin-top: -30px;padding-left: 20px;">
            <h3 style="margin-bottom: 20px;text-align: left;">Average Repetition Rate Top 3</h3>
            <el-scrollbar height="calc(40vh - 110px)">
              <el-collapse v-model="top_activeName" accordion>
                <el-collapse-item v-for="(item,index) in submission_total.slice(0,3)" :key="item">
                  <template #title>
                    <div
                        style="display: flex;justify-content: space-between;width: 100%;padding-right: 20px;align-items: center;">
                      <span>{{ item.name }}</span>
                      <div style="display: flex;align-items: center;width: 10%;justify-content: space-between;">
                        <span style="display: inline-block;width: 50%;text-align: right;">{{ formatNumber(item.result) }}</span>
                        <el-icon v-if="index === 0" :size="24" color="rgb(255,213,105)">
                          <Medal/>
                        </el-icon>
                        <el-icon v-if="index === 1" :size="24" color="rgb(212,215,220)">
                          <Medal/>
                        </el-icon>
                        <el-icon v-if="index === 2" :size="24" color="rgb(255,187,124)">
                          <Medal/>
                        </el-icon>
                      </div>
                    </div>
                  </template>
                  <el-row v-for="(key,val) in submission_map[item.name]" :key="key"
                          style="text-align: left;">
                    <el-col :offset="1" :span="8">
                      <span>{{ val }}</span>
                    </el-col>
                    <el-col :span="4" style="text-align: center;">
                      <span>{{ formatNumber(key) }}</span>
                    </el-col>
                  </el-row>
                </el-collapse-item>
              </el-collapse>
            </el-scrollbar>
          </div>
        </el-col>
        <el-col :span="8">
          <result-board :res="overview" v-if="showResultBoard"></result-board>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import * as echarts from 'echarts';
import ResultBoard from "@/components/ResultBoard";

export default {
  name: "overView",
  components: {ResultBoard},
  data() {
    return {
      submission_user: [],
      submission_result: [],
      submissions: [],
      submission_total: [],
      submission_map: [],
      overview: {},
      top_activeName: '',
      side_activeName: '',
      result_ration: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      showResultBoard: false
    }
  },
  methods: {
    changePage(id1, id2) {
      this.$router.push('/overview/compare_code/' + this.$route.params.folder + '/' + id1 + '/' + id2)
    },
    formatNumber(x) {
      return (x * 100).toFixed(2)
    }
  },
  mounted() {
    document.title = '鸡山OJ查重系统'
    var myChart = echarts.init(document.getElementById('main'));
    var data = [];
    let option = {
      title: {
        text: '查重比例结果图'
      },
      tooltip: {},
      xAxis: {
        max: 'dataMax'
      },
      yAxis: {
        type: 'category',
        data: ['0-10%', '11%-20%', '21%-30%', '31%-40%', '41%-50%', '51%-60%', '61%-70%', '71%-80%', '81%-90%', '91%-100%'],
      },
      series: [
        {
          name: '查重比例',
          type: 'bar',
          data: data,
          label: {
            show: true,
            position: 'right',
            valueAnimation: true
          }
        }
      ]
    };

    function SortResult(a, b) {
      return b.result - a.result;
    }

    this.$axios.get('/overview', {params: {title: this.$route.params.folder}}).then(res => {
      this.overview = res.data
      this.showResultBoard = true
    })

    this.$axios.get('/overview/submission', {params: {title: this.$route.params.folder}}).then(res => {
      this.submission_user = res.data.submission_user
      this.submission_result = res.data.submission_result
      this.submission_total = res.data.submission_total
      this.submission_map = res.data.submission_map
      this.submission_total.sort(SortResult)
      let result = {}
      for (const user of this.submission_user) {
        result[user] = {}
        for (const item of this.submission_result) {
          if (item.id1 === user) {
            result[user][item.id2] = item.similarity
          }
          if (item.id2 === user) {
            result[user][item.id1] = item.similarity
          }
        }
      }
      for (const it of this.submission_result) {
        this.result_ration[parseInt((it.similarity - 0.001) * 10)] += 1
      }
      option['series'][0].data = this.result_ration
      myChart.setOption(option);
      this.submissions = result
    })
  }
}
</script>

<style scoped lang="scss">
::v-deep(.el-collapse-item__header) {
  padding-left: 20px;
}
</style>