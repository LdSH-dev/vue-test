<template>
    <BarraSuperior />
    <FormLogin />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import FormLogin from   '@/components/FormLogin.vue';
import BarraSuperior from '@/components/BarraSuperior.vue';

export default defineComponent({
  name: 'HomeView',
  components: {
    FormLogin,
    BarraSuperior
  }
});
</script>

<style>
  main{
    height: 100%;
    width: 100%;
  }
</style>