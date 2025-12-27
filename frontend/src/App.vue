<script setup>
import { onMounted, provide, ref } from 'vue';
import MainLayout from './layouts/MainLayout.vue'
import { useToast } from 'primevue';
import clockApi from './utils/api/clock'

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
const startTime = ref(null)

const setClockedStatus = (bool) => {
  isClockedIn.value = bool
}

const setJobWorking = (jobName) => {
  jobWorking.value = jobName
}

const setOpenEntryId = (id) => {
  openEntryId.value = id
}

const setStartTime = (date) => {
  startTime.value = date
}

provide('clocked-status', {
  isClockedIn,
  setClockedStatus,
  jobWorking,
  setJobWorking,
  openEntryId,
  setOpenEntryId,
  startTime,
  setStartTime
})

onMounted(() => {
  clockApi.checkForOpenEntry()
    .then(res => {
      if(res.time_entry) {
        const tm = res.time_entry
        setJobWorking(tm.job_name)
        setOpenEntryId(tm.id)
        setStartTime(tm.start_time)
        setClockedStatus(true)
      }
    })
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
