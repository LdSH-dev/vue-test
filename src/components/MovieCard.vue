<template>
<div class="card has-background-dark">
  <div class="card-content">
    <p class="content">
       
    </p>
    <p class="subtitle">
      Flash
    </p>
  </div>
  <footer class="card-footer has-background-danger">
    <p class="card-footer-item">
      <span>
        <a href="https://www.netflix.com/watch/80057443?trackId=14170035&tctx=6%2C0%2C8615c20b-68c5-455f-a5f7-b64404602874-173999741%2Cd2bfe424-10c4-4212-af89-5f9ab370356f_26755185X19XX1647385071550%2Cd2bfe424-10c4-4212-af89-5f9ab370356f_ROOT%2C%2C%2C" class="icon-block">
          <i class="fa-solid fa-circle-play fa-2x"></i>
        </a>
          <!-- <i class="fa-solid fa-circle-play fa-2x" href="www.teste.com"></i> -->
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

i{
  color:white;
}

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