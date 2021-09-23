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
    <div class="absolute top-0 right-0 text-white">
      <div class="bg-blue-300 rounded-bl-full w-10 h-10 pl-4 pt-1"
           v-if="isSaving">
        <font-awesome-icon class="animate-spin" :icon="['fas', 'cog']"/>
      </div>
      <div v-else-if="!isSaving && isLastSaveSuccess" class="bg-green-300 rounded-bl-full w-10 h-10 pl-4 pt-1">
        <font-awesome-icon :icon="['fas', 'check']"/>
      </div>
      <div v-else class="bg-red-300 rounded-bl-full w-10 h-10 pl-4 pt-1">
        <font-awesome-icon :icon="['fas', 'times']"/>
      </div>
    </div>
  </div>
</template>

<script>
import UserCard from "@/components/UserCard";
import ColoredButton from "@/components/ColoredButton";
import InputField from "@/components/InputField";
import usersService from '../services/Users';
import {finalize} from "rxjs";

export default {
  name: "UserManager",
  components: {InputField, ColoredButton, UserCard},
  data() {
    return {
      isSaving: false,
      isLastSaveSuccess: true,
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
      this.isSaving = true
      usersService.saveUser(user)
          .pipe(finalize(() => this.isSaving = false))
          .subscribe()
    },
    deleteUser(deleteUser) {
      this.isSaving = true
      this.createdUsers = this.createdUsers.filter(user => user !== deleteUser)
      usersService.deleteUser(deleteUser)
          .pipe(finalize(() => this.isSaving = false))
          .subscribe()
    }
  }
}
</script>

<style scoped>

</style>
