<template>
  <main>
    <BarraSuperior />

    <div id=1 class="row">
      <MovieCard />
    </div>

  </main> 
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import BarraSuperior from   '@/components/BarraSuperior.vue';
import MovieCard from '@/components/MovieCard.vue';

export default defineComponent({
  name: 'HomeView',
  components: {
    BarraSuperior,
    MovieCard
  }
});
</script>

<style>
  main{
    height: 100%;
  }
</style>