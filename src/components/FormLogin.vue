<template>
  <form class="box has-background-danger">
  <div class="field">
    <label class="label">Mail</label>
    <div class="control has-icons-left">
      <span class="icon is-small is-left">
        <i class="fa-solid fa-envelope"></i> 
      </span>
      <input class="input has-background-dark has-text-primary-light" type="email" placeholder="e.g. alex@example.com">
    </div>
  </div>

  <div class="field">
    <label class="label">Password</label>
    <div class="control has-icons-left">
      <span class="icon is-small is-left">
        <i class="fa-solid fa-lock"></i> 
      </span>
      <input class="input has-background-dark has-text-primary-light" type="password" placeholder="********">
    </div>
  </div>

  <button class="button is-primary has-background-dark">Log In</button>
</form>
</template>

<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
    name: 'FormLogin'
})
</script>

<style scoped>

.box{
  margin-top: 8%;
  margin-left:30%;
  width: 40%;
}

</style>
