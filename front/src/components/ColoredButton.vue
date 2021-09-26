<template>
  <button class="rounded text-white font-bold px-4 w-full"
          v-bind:class="[!!thick ? 'py-2' : 'py-1', bgColor]"
          v-on:click="$emit('click')">
    <slot></slot>
  </button>
</template>

<script>
/**
 * @props Color: green/yellow/blue/red => bg-{color}-{variant}
 * @event click
 */
export default {
  name: "ColoredButton",
  props: {
    color: {
      type: String,
      default: "green"
    },
    thick: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    bgColor() {
      const classes = []
      switch (this.color) {
        case ("green"): {
          classes.push("bg-green-500")
          classes.push("hover:bg-green-700")
          break;
        }
        case ("yellow"): {
          classes.push("bg-yellow-500")
          classes.push("hover:bg-yellow-700")
          break;
        }
        case ("red") : {
          classes.push("bg-red-500")
          classes.push("hover:bg-red-700")
          break;
        }
        case ("blue") : {
          classes.push("bg-blue-500")
          classes.push("hover:bg-blue-700")
          break;
        }
        default: {
          throw Error(`Unexpected button color ${this.color}`)
        }
      }
      return classes
    }
  }
}
</script>

<style scoped>

</style>
