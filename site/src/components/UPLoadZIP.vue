<template>
  <div
      style="width: 50%;margin: 0 auto;height: calc(100vh - 200px);display: flex;justify-content: center;align-items: center;">
    <el-upload style="width: 100%;"
               ref="upload"
               class="upload-demo"
               drag
               action="http://127.0.0.1:8000/api/overview/upload"
               multiple
               name="file"
               :show-file-list="false"
               :on-success="successUpload"
               :data="{
                 title:new Date().getTime()
               }"
               v-model:file-list="fileList"
    >
      <el-icon class="el-icon--upload">
        <upload-filled/>
      </el-icon>
      <div class="el-upload__text">
        Drop file here or <em>click to upload</em>
      </div>
      <template #tip>
        <div class="el-upload__tip">
          jpg/png files with a size less than 500kb
        </div>
      </template>
    </el-upload>
  </div>
</template>

<script>
export default {
  name: "UPLoadZIP",
  data() {
    return {
      fileList: [],
      res_cnt: 0
    }
  },
  methods: {
    // eslint-disable-next-line no-unused-vars
    successUpload(response, uploadFile, uploadFiles) {
      this.res_cnt += 1
      if (this.res_cnt === uploadFiles.length)
        this.$axios.get('/overview', {params: {title: response}}).then(res => {
          this.$emit('imgShow', res.data)
        })
    },
  },
  mounted() {
  }
}
</script>

<style scoped lang="scss">
</style>