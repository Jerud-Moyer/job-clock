<script setup>
import { ref } from 'vue';
import FilteredEntriesForm from '../components/forms/FilterEntriesForm.vue'
import clockApi from '../utils/api/clock'
import EntryList from '../components/lists/EntryList.vue';

const entries = ref([])
const totalHours = ref(null)
const lastSearch = ref(null)

const handleGetFilteredEntries = (filterData) => {
    clockApi.getFilteredEntries(filterData)
        .then(({ time_entries, total_hours }) => {
            entries.value = time_entries
            totalHours.value = total_hours.slice(0, total_hours.indexOf('.'))
            lastSearch.value = filterData
        })
}

const refreshSearch = () => {
    if(lastSearch.value) {
        handleGetFilteredEntries(lastSearch.value)
    }
}
</script>

<template>
<div class="flex flex-col justify-center">
    <p class="text-3xl text-left px-6 mb-6">View Sheets</p>
    <FilteredEntriesForm 
        @get-filtered-entries="(payload) => handleGetFilteredEntries(payload)"
        class="mb-10"
    />
    <EntryList
        table-header="Wait Wut"
        :entries="entries"
        :total-hours="totalHours"
        @refresh-list="refreshSearch"
    />
</div>
</template>

<style>

</style>