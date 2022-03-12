<template>
  <main class="columns is-gapless is-multiline"> 
    <div class="columns is-one-quarter">
      <BarraLateral />
    </div>
    <div class="column is-two-quarter">
      <FormLogin />
    </div>
  </main> 
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import BarraLateral from '@/components/BarraLateral.vue';
import FormLogin from   '@/components/FormLogin.vue';

export default defineComponent({
  name: 'HomeView',
  components: {
    BarraLateral,
    FormLogin
  }
});
</script>
