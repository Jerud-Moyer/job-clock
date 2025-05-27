<template>
  <div>
    <h2>Time Clock</h2>
      <router-link to="/">
        <button>Home Page</button>
      </router-link>
      <div class="flex justify-between w-[900px] border-2">
        <Button severity="info" variant="outlined">WAIT</Button>
        <InputText placeholder="WUT..." />
      </div>
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
