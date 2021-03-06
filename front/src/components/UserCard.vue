<template>
  <div class="shadow-lg rounded-md p-4 border-2">
    <!--Note-->
    <div class="mb-3">
      <div class="flex justify-between w-full mb-2">
        <label class="self-end block text-gray-500 font-bold pr-4">
          Notes
        </label>
        <div class="flex w-12 h-8">
          <colored-button color="red" v-on:click="$emit('delete')">
            <font-awesome-icon :icon="['fas', 'trash']"/>
          </colored-button>
        </div>
      </div>
      <textarea
          class="appearance-none leading-tight focus:outline-none focus:border-green-500 border-2 px-2 py-1 w-full"
          v-on:keyup="noteChange($event.target.value)"
          v-bind:value="form.note">
      </textarea>
    </div>
    <!--Account-->
    <div class="mb-3">
      <input-field label="Login"
                   v-on:keyup="loginChange($event.target.value)"
                   v-bind:value="form.username"></input-field>
      <input-field label="Pass"
                   v-on:keyup="passwordChange($event.target.value)"
                   v-bind:value="form.password"
                   type="password"></input-field>
      <div class="flex justify-start">
        <label class="block text-gray-500 font-bold md:text-right mb-1 md:mb-0 pr-2">
          Is Admin
        </label>
        <input v-on:change="isAdminChange($event.target.value)"
               v-bind:checked="this.form.isAdmin" type="checkbox"/>
      </div>
    </div>
    <!--Apps-->
    <div>
      <h3 class="text-gray-500 font-bold mb-1">Applications</h3>
      <div class="flex items-center w-full my-2" v-for="(app, index) in form.apps" v-bind:key="index">
        <input-field class="flex-grow" v-on:keyup="appsChange($event.target.value, index)" v-bind:value="app"></input-field>
        <font-awesome-icon class="cursor-pointer text-red-400 mx-2"
                           v-on:click="deleteApp(app)"
                           :icon="['fas', 'times']"/>
      </div>
      <ColoredButton v-on:click="addApp">Add app</ColoredButton>
    </div>
  </div>
</template>

<script>
import InputField from "@/components/InputField";
import ColoredButton from "@/components/ColoredButton";
import deepClone from 'lodash.clonedeep';
import {Subject} from "rxjs"
import {debounceTime} from 'rxjs/operators';

/**
 * @prop form Object{note,username,password,isAdmin,apps}
 * @event change
 * @event delete
 */
export default {
  name: "UserCard",
  components: {ColoredButton, InputField},
  props: ["user"],
  data() {
    return {
      form: {
        note: "",
        username: "",
        password: "",
        isAdmin: false,
        apps: []
      },
      emitChangeDebouch: null
    }
  },
  created() {
    this.form.note = this.user.note;
    this.form.username = this.user.username;
    this.form.password = this.user.password;
    this.form.isAdmin = this.user.isAdmin;
    this.form.apps = [...this.user.apps]
    this.changeSubject = new Subject().pipe(debounceTime(250))
    this.changeSubscription = this.changeSubject.subscribe((user) => {
      this.$emit("change",  deepClone(user))
    })
  },
  beforeDestroy() {
    if (this.changeSubscription) {
      this.changeSubscription.unsubscribe()
    }
  },
  methods: {
    noteChange(newValue) {
      this.form.note = newValue
      this.emitChange()
    },
    loginChange(newValue) {
      this.form.username = newValue
      this.emitChange()
    },
    passwordChange(newValue) {
      this.form.password = newValue
      this.emitChange()
    },
    isAdminChange(newValue) {
      this.form.isAdmin = (newValue === 'yes')
      this.emitChange()
    },
    addApp() {
      this.form.apps.push("")
    },
    appsChange(newValue, index) {
      this.form.apps[index] = newValue
      this.emitChange()
    },
    deleteApp(appToDelete){
      this.form.apps = this.form.apps.filter(app => app !== appToDelete)
      this.emitChange()
    },
    emitChange() {
      console.group("emitChange")
      console.log(!!this.form.username.length)
      console.log(!!this.form.password)
      console.groupEnd()
      if (!!this.form.username && !!this.form.password) {
        this.changeSubject.next(this.form)
      }
    }
  }
}
</script>

<style scoped>

</style>
