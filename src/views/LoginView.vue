<template>
    <FormLogin />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import FormLogin from   '@/components/FormLogin.vue';

export default defineComponent({
  name: 'HomeView',
  components: {
    FormLogin
  }
});
</script>

<style>
  main{
    height: 100%;
  }
</style>