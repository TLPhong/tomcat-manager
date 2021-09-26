<template>
  <div class="py-4 w-32 h-full">
    <div class="flex-col text-center font-medium">
      <div class="p-3 my-2 cursor-pointer"
           v-on:click="changeRoute('Users')"
           v-bind:class="selectedRoute === 'Users' ? selectedClass : 'text-gray-400'">
        <span>Users</span>
      </div>
      <div class="p-3 my-2 cursor-pointer"
           v-on:click="changeRoute('Log')"
           v-bind:class="selectedRoute === 'Log' ? selectedClass : 'text-gray-400'">
        <span>Log</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      selectedRoute: "users",
      selectedClass: "text-white rounded-full shadow bg-green-400"
    }
  },
  watch:{
    "$route"(currentRoute){
      this.selectedRoute = currentRoute.name
    }
  },
  methods: {
    //Route names: Log, Users
    changeRoute(routeName) {
      if(this.$route.name !== routeName){
        this.$router.push({ name: routeName})
      }
    }
  }
}
</script>

<style scoped>

</style>
