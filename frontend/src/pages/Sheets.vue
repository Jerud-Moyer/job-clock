<script setup>
import { ref } from 'vue';
import FilteredEntriesForm from '../components/forms/FilterEntriesForm.vue'
import clockApi from '../utils/api/clock'
import EntryList from '../components/lists/EntryList.vue';

const entries = ref([])

const handleGetFilteredEntries = (filterData) => {
    clockApi.getFilteredEntries(filterData)
        .then(json => entries.value = json.time_entries)
}
</script>

<template>
<div>
    <p class="text-3xl text-left mb-6">View Sheets</p>
    <FilteredEntriesForm 
        @get-filtered-entries="(payload) => handleGetFilteredEntries(payload)"
    />
    <EntryList
        table-header="Wait Wut"
        :entries="entries"
    />
</div>
</template>

<style>

</style>