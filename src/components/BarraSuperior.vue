<template>
    <header>
<nav class="navbar is-danger" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
        <a class="navbar-item teste" href="/">
            <!-- <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28"> -->
            <span> Cross - Streaming API </span>
        </a>
    </div>

    <div id="navbar" class="navbar-menu">
    <div class="navbar-start">
        
      <a class="navbar-item">
        Documentation
      </a>

      <div class="navbar-item has-dropdown is-hoverable has-text-dark">
        <a class="navbar-link">
          Account
        </a>

        <div class="navbar-dropdown">
          <a class="navbar-item">
            Profile
          </a>
          <a class="navbar-item">
            Linked Streaming Sources
          </a>
          <hr class="navbar-divider">
          <a class="navbar-item">
            Logout
          </a>
        </div>
      </div>

      <a class="navbar-item">
        Documentation
      </a>
      <a class="navbar-item has-text-warning">
        Report an issue
      </a>
      
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <a class="button is-primary has-background-dark" href="/login">
            <strong>Log in</strong>
          </a>
          <a class="button is-light">
            Sign up
          </a>
        </div>
      </div>
    </div>
    </div>

</nav>
    </header>    
</template>

<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
    name: 'BarraSuperior'
})
</script>

<style scoped>

header{
    color: white;
    width: 100%;
}

.teste{
    background: hsl(0, 0%, 21%);
    color: 	#ffe08a !important ;
    border: 2px solid	#ffe08a !important;
    margin-top: 8px;
    margin-right: 10px;
    height: 40px;
    text-align: center;
    align-content: center;
}

</style>