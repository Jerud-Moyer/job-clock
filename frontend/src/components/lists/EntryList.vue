<script setup>
import { computed } from 'vue';


const { entries } = defineProps({
    entries: {
        type: Array,
        required: true
   }
})

const rowsNum = computed(() => entries.length)

</script>

<template>
<div>
    <DataTable
        :value="entries"
        :rows="rowsNum"
        :responsiveLayout="'scroll'"
        class="w-full"
        data-key="id"
    >
        <template #header>
            <p class="text-lg">Today's Time Entries</p>
        </template>
        <Column field="client_name" header="Client"/>
        <Column field="job_name" header="Job"/>
        <Column field="start_time" header="Started"/>
        <Column field="end_time" header="Finished"/>
        <Column field="duration" header="Duration"/>
        <Column field="notes" header="Notes"/>
        <Column field="" header=""/>
    </DataTable>
</div>
</template>

<style>

</style>