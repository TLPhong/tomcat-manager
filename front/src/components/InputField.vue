<template>
  <div class="md:flex md:items-center my-1">
    <div class="md:w-1/3 lg:w-1/6" v-if="label">
      <label class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-4">
        {{ label }}
      </label>
    </div>
    <div v-bind:class="label ? 'md:w-2/3 lg:w-5/6' : 'w-full'">
      <input
          class="appearance-none border-2 border-gray-200 rounded w-full py-1 px-2 text-gray-700 leading-tight focus:outline-none focus:border-green-500"
          v-bind:placeholder="placeHolder"
          v-bind:disabled="disabled"
          v-bind:type="type"
          v-bind:value="value"
          v-on:keyup="newValue => this.$emit('keyup', newValue)"
          v-on:change="newValue => this.$emit('change', newValue)">
    </div>
  </div>
</template>

<script>
/**
 * @prop label
 * @prop disabled
 * @prop value
 * @prop type
 * @prop placeHolder
 *
 * @event change
 * @event keyup
 */
export default {
  name: "InputField",
  props: {
    label: String,
    disabled: {
      type: Boolean,
      default: false
    },
    value: String,
    type: String,
    placeHolder: String
  }
}
</script>

<style scoped>

</style>
