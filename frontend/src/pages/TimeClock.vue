<template>
  <div>
    <p class="text-4xl text-left mb-12 pl-4">Time Clock</p>
    
  </div>  
</template>

<script setup>
import { InputText } from "primevue";
import { onMounted } from "vue";
import MainLayout from "../layouts/MainLayout.vue";

onMounted(() => {
  fetch('api/say-hello')
    .then(res => res.json())
    .then(json => console.log('that work??? => ', json))
    .catch(err => console.error(err))
})
</script>

<style>

</style>
