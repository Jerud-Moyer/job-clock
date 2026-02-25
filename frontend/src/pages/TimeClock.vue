<script setup>
import { onMounted, ref } from "vue";
import ClockForm from "../components/forms/ClockForm.vue";
import EntryList from '../components/lists/EntryList.vue';
import clockApi from '../utils/api/clock'
import { getReadableDate } from "../utils/utils";

const todaysEntries = ref([])
const totalHours = ref(null)

const getTodaysEntries = () => {
  const midnight = new Date()
  const endOfDay = new Date()
  midnight.setHours(0, 0, 0, 0)
  endOfDay.setHours(23, 59, 59, 0)
  clockApi.getEntriesByDateRange({
    start_time: midnight.toISOString(),
    end_time: endOfDay.toISOString()
  })
    .then(({ time_entries, total_hours }) => {
      todaysEntries.value = time_entries.map(entry => ({
        ...entry,
        start_time: getReadableDate(entry.start_time),
        end_time: getReadableDate(entry.end_time),
        duration: entry.duration.slice(0, String(entry.duration).indexOf('.'))
      }))
      
      totalHours.value = total_hours.slice(0, total_hours.indexOf('.'))
    })

}

onMounted(() => {
  getTodaysEntries()
})
</script>

<template>
  <div>
    <p class="text-4xl mb-4 pl-4">Time Clock</p>
    <ClockForm 
      @clocked-out="getTodaysEntries"
    />
    <EntryList
      v-if="todaysEntries.length" 
      class="mt-12" 
      :entries="todaysEntries" 
      :total-hours="totalHours"
      table-header="Today's Time Entries"
      @refresh-list="getTodaysEntries"
    />
  </div>  
</template>


<style>

</style>
