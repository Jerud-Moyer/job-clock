<template>
<div>
  <h2>Time Clock</h2>
    <router-link to="/">
      <button>Home Page</button>
    </router-link>
</div>  
</template>

<script setup>
import { onMounted } from "vue";

onMounted(() => {
  fetch('api/say-hello')
    .then(res => res.json())
    .then(json => console.log('that work??? => ', json))
    .catch(err => console.error(err))
})
</script>

<style>

</style>
