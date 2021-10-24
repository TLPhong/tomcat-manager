<template>
  <div class="min-h-screen h-full w-screen bg-gray-100 text-gray-800 md:pt-6">
    <div class="md:container flex bg-white rounded shadow-md pl-4 mx-auto">
      <nav-bar></nav-bar>
      <div class="w-full">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>
<script>
import NavBar from "./components/NavPanel";
export default {
  components: {NavBar}
}
</script>
