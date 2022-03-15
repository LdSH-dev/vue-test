<template>
<div class="card has-background-dark">
  <div class="card-content">
    <p class="content">
       
    </p>
    <p class="subtitle">
      Supernatural
    </p>
  </div>
  <footer class="card-footer has-background-danger">
    <p class="card-footer-item">
      <span>
          <i class="fa-solid fa-circle-play fa-2x"></i>
      </span>
    </p>
  </footer>
</div>
</template>

<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
    name: 'MovieCard'
})
</script>

<style scoped>

.card-footer{
    color: white;
    font-size: 12px;
    margin-top: 50%;
}

.card{
    color: white;
    margin: 10px auto;
    align-content: center;
    width: 200px;
    height: 200px;
    font-size: 12px;
}

.title{
    color: white;
    font-size: 10px;
}

</style>