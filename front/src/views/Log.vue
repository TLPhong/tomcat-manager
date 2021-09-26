<template>
  <div id="container">
    <div class="flex justify-between border-b-2 border-green-400 p-2 my-2 mx-4">
      <div class="flex">
        <label class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4">
          Application
        </label>
        <select class="border-2 w-32"
                v-on:change="setContext($event.target.value)">
          <option value="tomcat">
            Tomcat
          </option>
          <option>
            /dee
          </option>
        </select>
        <div class="flex mx-3">
          <label class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-2">
            Follow
          </label>
          <input type="checkbox" v-model="isFollow">
        </div>
      </div>
      <div class="flex items-center opacity-70">
        <div class="bg-green-400 rounded-full w-3 h-3 mr-0.5"/>
        <span class="font-medium">Running</span>
      </div>
    </div>
      <virtual-list class="bg-gray-800 border-2 py-2 pl-1 pr-2 mx-4 overflow-y-auto"
                    style="height: 600px"
                    ref="logBox"
                    data-key="index"
                    :keeps="60"
                    :data-sources="log"
                    :data-component="itemComponent"

      />

  </div>
</template>

<script>
import LogService from "../services/Log"
import LogLine from "@/components/LogLine";
import VirtualList from 'vue-virtual-scroll-list';

export default {
  name: "Log",
  components: {VirtualList},
  mounted() {
    this.setContext("tomcat")
  },
  data() {
    return {
      isFollow: true,
      itemComponent: LogLine,
      log: [],
      logStreamSubscription: null
    }
  },
  methods: {
    setContext(context) {
      if (this.logStreamSubscription) {
        this.logStreamSubscription.unsubscribe()
        this.log = []
      }

      this.logStreamSubscription = LogService.getLogStream(context)
          .subscribe(log => {
            this.log.push(log)
            if (this.isFollow) {
              this.$refs.logBox.scrollToBottom()
            }
          })
    }
  },
  beforeDestroy() {
    if (this.logStreamSubscription) {
      this.logStreamSubscription.unsubscribe()
    }
  }
}
</script>

<style scoped>

</style>
