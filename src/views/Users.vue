<template>
  <div class="relative">
    <div class=" flex justify-start w-full p-4 pb-2">
      <div class="pt-1 px-2 lg:w-1/6">
        <colored-button color="green" v-on:click="addNewUserCard">
          <font-awesome-icon :icon="['fas', 'plus']"/>
          Add user
        </colored-button>
      </div>
      <div class="w-4/6 ">
        <input-field place-holder="Search..."/>
      </div>
    </div>
    <div class="grid lg:grid-cols-3 md:grid-cols-2 gap-3 w-full py-1 px-4">
      <user-card v-for="createdUser in createdUsers"
                 v-on:change="userChanged"
                 v-on:delete="deleteUser(createdUser)"
                 v-bind:user="createdUser"
                 v-bind:key="createdUser.login"/>
    </div>
    <div class="absolute top-0 right-0">
      <div class="bg-green-400 text-white rounded-bl-full w-10 h-10 pl-4 pt-1">
        <font-awesome-icon :icon="['fas', 'check']"/>
      </div>
    </div>
  </div>
</template>

<script>
import UserCard from "@/components/UserCard";
import ColoredButton from "@/components/ColoredButton";
import InputField from "@/components/InputField";
import usersService from '../services/Users';

export default {
  name: "UserManager",
  components: {InputField, ColoredButton, UserCard},
  data() {
    return {
      isSaving: false,
      createdUsers: []
    }
  },
  created() {
    this.createdUsers = usersService.listUser()
  },
  methods: {
    addNewUserCard() {
      this.createdUsers.unshift({
        note: "",
        login: "",
        pass: "",
        isAdmin: false,
        apps: []
      })
    },
    userChanged(user) {
      usersService.saveUser(user)
    },
    deleteUser(deleteUser) {
      this.createdUsers = this.createdUsers.filter(user => user !== deleteUser)
      usersService.deleteUser(deleteUser)
    }
  }
}
</script>

<style scoped>

</style>
