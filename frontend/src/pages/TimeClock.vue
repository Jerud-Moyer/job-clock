<template>
  <div>
    <p class="text-4xl mb-12 pl-4">Time Clock</p>
    <ClockForm />
  </div>  
</template>

<script setup>
import { InputText } from "primevue";
import { onMounted } from "vue";
import MainLayout from "../layouts/MainLayout.vue";
import ClockForm from "../components/forms/ClockForm.vue";

onMounted(() => {
  
})
</script>

<style>

</style>
