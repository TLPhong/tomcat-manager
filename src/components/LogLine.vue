<template>
  <div class="flex">
    <div class="opacity-50 text-gray-300 select-none font-mono text-xs w-auto  pr-1">
      {{index}}
    </div>
    <pre class="text-gray-200 font-mono text-xs border-l-2 pl-1 border-opacity-30">{{source.text}}</pre>
  </div>
</template>

<script>
export default {
  name: "LogLine",
  props: {
    index: {
      type: Number
    },
    source: {
      type: Object,
      default(){
        return {
          text: ""
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
