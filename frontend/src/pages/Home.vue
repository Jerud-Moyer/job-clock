<template>
  <div>
    <h2>Home Page</h2>
    <router-link to="/time-clock">
      <Button severity="primary" rounded>Clock Page</Button>
    </router-link>
  </div>
</template>

<script setup> 
import { onMounted } from 'vue';


onMounted(() => {
  console.log('this thing on?')
  fetch('/api/clients/say-hello')
    .then(response => response.json())
    .then(data => {
      console.log('Response from server:', data);
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
});

</script>

<style>

</style>
