<script setup>
import { provide, ref } from 'vue';
import MainLayout from './layouts/MainLayout.vue'
import { useToast } from 'primevue';

// notifications
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

const notify = (message, severity='success') => {

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

// clocked-in
const isClockedIn = ref(false)
const jobWorking = ref('')
const openEntryId = ref(null)

const setClockedStatus = (bool) => {
  isClockedIn.value = bool
}

const setJobWorking = (jobName) => {
  jobWorking.value = jobName
}

const setOpenEntryId = (id) => {
  openEntryId.value = id
}

provide('clocked-status', {
  isClockedIn,
  setClockedStatus,
  jobWorking,
  setJobWorking,
  openEntryId,
  setOpenEntryId
})
</script>

<template>
  <MainLayout>
    <div>
      <RouterView />
      <Toast />
    </div>
  </MainLayout>
</template>

<style scoped>

</style>
