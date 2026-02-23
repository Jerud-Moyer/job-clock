<script setup>
import { computed, inject, ref } from 'vue';
import EntryForm from '../forms/EntryForm.vue';
import clockApi from '../../utils/api/clock';


const { entries } = defineProps({
    entries: {
        type: Array,
        required: true
   },
   tableHeader: {
        type: String,
        default: ''
   }
})

const emit = defineEmits(['refresh-list'])

const { notify } = inject('toaster')
const showEntryForm = ref(false)
const selectedEntry = ref({})
const rowsNum = computed(() => entries.length)

const handleRefreshList = () => {
    showEntryForm.value = false
    emit('refresh-list')
}

const handleInitUpdate = (id) => {
    clockApi.getEntryById(id)
        .then(res => {
            const entry = res.time_entry
            if (entry) {
                selectedEntry.value = entry    
                showEntryForm.value = true
            }
        })
        .catch(err => notify(String(err), 'error'))
}

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
            <p class="text-lg">{{ tableHeader }}</p>
        </template>
        <Column field="client_name" header="Client"/>
        <Column field="job_name" header="Job"/>
        <Column field="start_time" header="Started"/>
        <Column field="end_time" header="Finished"/>
        <Column field="duration" header="Duration"/>
        <Column field="notes" header="Notes"/>
        <Column header="Update" class="text-center">
            <template #body="slotProps">
                <Button 
                    severity="primary" 
                    text 
                    rounded
                    icon="pi pi-pencil"
                    @click="handleInitUpdate(slotProps.data.id)"
                />
            </template>
        </Column>
    </DataTable>
    <Dialog
        v-model:visible="showEntryForm"
        header="Update Time Entry"
        modal
        close-on-escape
    >
        <EntryForm 
            :entry="selectedEntry"
            @action-canceled="() => showEntryForm = false"
            @action-succeeded="handleRefreshList"  
        />
    </Dialog>
</div>
</template>

<style>

</style>