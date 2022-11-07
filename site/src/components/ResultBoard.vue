<template>
  <div style="padding-top: 20px;">
    <div style="text-align: left;">
      <el-radio-group v-model="showBox" @change="showBox = parseInt(showBox)">
        <el-radio-button :label="0">Avg</el-radio-button>
        <el-radio-button :label="1">Max</el-radio-button>
      </el-radio-group>
    </div>
    <h3 style="text-align: left;margin: 10px 0;">Top Comparisons:</h3>
    <div style="height: calc(100vh - 160px)">
      <el-scrollbar height="calc(100vh - 160px)">
        <el-table :data="res.metrics[showBox]['topComparisons']" style="text-align: center;">
          <el-table-column label="No." type="index" align="center"></el-table-column>
          <el-table-column label="Submission 1" prop="first_submission" align="center"></el-table-column>
          <el-table-column align="center" width="40">
            <template #default="">
              <el-icon>
                <DArrowRight/>
              </el-icon>
            </template>
          </el-table-column>
          <el-table-column label="Submission 2" prop="second_submission" align="center"></el-table-column>
          <el-table-column label="Match %" align="center">
            <template #default="slot">
              {{
                formatNumber(slot.row.similarity)
              }}
            </template>
          </el-table-column>
          <el-table-column align="left" width="60">
            <template #default="slot">
              <el-button type="primary" plain
                         @click="showDetail(res['id'],slot.row.first_submission,slot.row.second_submission)"
                         size="small">
                <el-icon>
                  <Search/>
                </el-icon>
                <!--          查看-->
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-scrollbar>
    </div>
  </div>
</template>

<script>
export default {
  name: "ResultBoard",
  props: ['res'],
  data() {
    return {
      showBox: 0,
      tableData: []
    }
  },
  methods: {
    showDetail(id, first, sec) {
      this.$router.push('/overview/compare_code/' + id + '/' + first + '/' + sec)
    },
    formatNumber(x) {
      return (x * 100).toFixed(2)
    }
  }
}
</script>

<style scoped>

</style>