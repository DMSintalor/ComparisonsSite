<template>
  <!--  <el-menu-->
  <!--      :default-active="nowIX"-->
  <!--      style="min-height: calc(100vh - 60px)"-->
  <!--      disabled-->
  <!--  >-->
  <!--    <el-menu-item :index="0" disabled>上传文件</el-menu-item>-->
  <!--    <el-menu-item :index="1" disabled>结果展示</el-menu-item>-->
  <!--    <el-menu-item :index="2" disabled>结果展示</el-menu-item>-->
  <!--  </el-menu>-->
  <el-steps :active="nowIX" align-center>
    <el-step title="上传文件"/>
    <el-step title="结果展示"/>
    <el-step title="代码分析"/>
  </el-steps>
</template>

<script>
export default {
  name: "sideMenu",
  props: ['nowIX']

}
</script>

<style scoped>

</style>