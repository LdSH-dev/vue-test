<template>
  <form class="box has-background-danger">
  <div class="field">
    <label class="label">Email</label>
    <div class="control">
      <input class="input has-background-dark has-text-primary-light" type="email" placeholder="e.g. alex@example.com">
    </div>
  </div>

  <div class="field">
    <label class="label">Senha</label>
    <div class="control">
      <input class="input has-background-dark has-text-primary-light" type="password" placeholder="********">
    </div>
  </div>

  <button class="button is-primary has-background-dark">Entrar</button>
</form>
</template>

<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
    name: 'FormLogin'
})
</script>
