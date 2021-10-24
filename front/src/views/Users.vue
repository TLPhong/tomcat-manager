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
                 v-bind:key="createdUser.username"/>
    </div>
    <StatusCorner :is-working="isWorking" :error-message="errorMessage" :is-last-request-success="isHavingError"/>
  </div>
</template>

<script>
import UserCard from "../components/UserCard";
import ColoredButton from "../components/ColoredButton";
import InputField from "../components/InputField";
import usersService from '../services/Users';
import {finalize} from "rxjs";
import StatusCorner from "../components/StatusCorner";

export default {
  name: "UserManager",
  components: {StatusCorner, InputField, ColoredButton, UserCard},
  data() {
    return {
      isWorking: false,
      isHavingError: false,
      errorMessage: "",
      createdUsers: []
    }
  },
  created() {
    this.isWorking = true
    usersService.listUser()
        .finally(() => this.isWorking = false)
        .then(async response => {
          if (response.ok) {
            this.createdUsers = await response.json()
            this.isHavingError = false
          }
        }, reason => {
          this.isHavingError = true
          this.errorMessage = reason
        })
  },
  methods: {
    addNewUserCard() {
      this.createdUsers.unshift({
        note: "",
        username: "",
        password: "",
        isAdmin: false,
        apps: []
      })
    },
    userChanged(user) {
      this.isWorking = true
      usersService.saveUser(user)
          .pipe(finalize(() => this.isWorking = false))
          .subscribe()
    },
    deleteUser(deleteUser) {
      this.isWorking = true
      // this.createdUsers = this.createdUsers.filter(user => user !== deleteUser)
      usersService.deleteUser(deleteUser)
          .pipe(finalize(() => this.isWorking = false))
          .subscribe(() => {
            this.isHavingError = true
            this.errorMessage = this.errorMessage += "+"
          })
    }
  }
}
</script>

<style scoped>

</style>
