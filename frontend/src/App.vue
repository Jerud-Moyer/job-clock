<script setup>
import { provide, ref } from 'vue';
import MainLayout from './layouts/MainLayout.vue'
import { useToast } from 'primevue';

const toast = useToast()

const icons = {
  success: {
    key: 'successIcon',
    icon: 'pi pi-check'
  },
  error: {
    key: 'errorIcon',
    icon: 'pi pi-times'
  },
  info: {
    key: 'infoIcon',
    icon: 'pi pi-info'
  },
  warn: { 
    key: 'warnIcon',
    icon: 'pi pi-exclamation-triangle'
  }
}

const notify = (message, severity) => {

  toast.add({
    severity: severity,
    summary: 'Notification',
    detail: message,
    life: 3000,
    closable: true,
    [icons[severity]['key']]: icons[severity]['icon']
  })
}

provide('toaster', { notify })

</script>

<template>
  <MainLayout>
    <div>
      <h1>This My Timeclock!</h1>
      <RouterView />
      <Toast />
    </div>
  </MainLayout>
</template>

<style scoped>

</style>
