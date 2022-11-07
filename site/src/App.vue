<template>
  <router-view name="indexView" :key="$route.fullPath"/>
  <router-view name="adminView" :key="$route.fullPath"/>
  <router-view name="overView" :key="$route.fullPath"/>
  <router-view name="codeView" :key="$route.fullPath"/>
</template>

<script>
export default {
  mounted() {
    document.title = '鸡山OJ查重系统'
  }
}
</script>

<style lang="scss">
* {
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
