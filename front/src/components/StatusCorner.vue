<template>
  <div class="absolute top-0 right-0 text-white">
    <div class="transition-opacity ease-linear duration-500"
         :class="isShowingError? 'opacity-100': 'opacity-0'">
      <ErrorToast :message="errorMessage"/>
    </div>
    <div class="absolute right-0 top-0 transition-opacity ease-in-out duration-500"
         :class="!isShowingError? 'opacity-100': 'opacity-0'">
      <div class="bg-blue-300 rounded-bl-full w-10 h-10 pl-4 pt-1"
           v-if="isWorking">
        <font-awesome-icon class="animate-spin" :icon="['fas', 'cog']"/>
      </div>
      <div v-else-if="!isWorking && !isLastRequestSuccess" class="bg-green-400 rounded-bl-full w-10 h-10 pl-4 pt-1">
        <font-awesome-icon :icon="['fas', 'check']"/>
      </div>
      <div v-else-if="!isWorking && isLastRequestSuccess" class="bg-red-400 rounded-bl-full w-10 h-10 pl-4 pt-1">
        <font-awesome-icon :icon="['fas', 'times']"/>
      </div>
    </div>
  </div>
</template>

<script>
import ErrorToast from "./toast/ErrorToast";
import {timer} from "rxjs";

export default {
  name: "StatusCorner",
  components: {ErrorToast},
  data() {
    return {
      errorDuration: 4000,
      isShowingError: false
    }
  },
  props: {
    isWorking: Boolean,
    isLastRequestSuccess: Boolean,
    errorMessage: {
      type: String,
      default: "",
      required: false
    }
  },
  mounted() {
    if (this.errorMessage) {
      this.isShowingError = true
    }
  },
  watch: {
    errorMessage (newValue, oldValue) {
      if (newValue !== oldValue) {
        this.setErrorVisible(true)
      }
    }
  },
  methods: {
    setErrorVisible(isVisible) {
      this.isShowingError = isVisible
      if (isVisible) {
        const twoSecondsLater = timer(this.errorDuration)
        twoSecondsLater.subscribe(() => {
          this.isShowingError = false
        })
      }
    }
  }
}
</script>

<style scoped>

</style>
