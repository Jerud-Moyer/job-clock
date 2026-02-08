<script setup>
import { inject, onMounted, ref } from 'vue';
import { useConfirm } from "primevue/useconfirm";
import { getLocalDateTime } from '../../utils/utils';
import jobApi from '../../utils/api/jobs';
import clockApi from '../../utils/api/clock';

const { entry } = defineProps({
    entry: {
        type: Object,
        default: {
            start_time: null,
            end_time: null
        }
    }
})

const { notify } = inject('toaster')
const confirm = useConfirm()

const emit = defineEmits(['action-canceled', 'action-succeeded'])

const jobOptions = ref([]) 
const selectedJob = ref(null)
const startTime = ref(null)
const endTime = ref(null)

const clearForm = () => {
    selectedJob.value = null
    startTime.value = null
    endTime.value = null
}

const handleCancel = () => {
    clearForm()
    emit('action-canceled')
}

const handleUpdateEntry = () => {
    const updatedEntry = {
        id: entry.id,
        job_id: selectedJob.value,
        start_time: new Date(startTime.value).toISOString(),
        end_time: new Date(endTime.value).toISOString()
    }

    clockApi.updateEntry(updatedEntry)
        .then(json => {
            if(json.time_entry) {
                emit('action-succeeded')

                return notify(`Entry ${json.time_entry.id} updated successfully`, 'success')
            } else if(json.error) {
                console.error('Error:', json.error);
                return notify(json.error, 'error');
            }
        })
        .catch(err => {
            console.error('API Error:', err);
            notify('Failed to save job.', 'error');
        });
}

const handleDeleteEntry = (e) => {
    console.log('ummmmmmmm ', e.currentTarget)
    confirm.require({
        target: e.currentTarget,
        message: 'Are you sure you want to delete this entry?',
        icon: 'pi pi-exclamation-triangle',
        rejectProps: {
            label: 'Cancel',
            severity: 'warn',
            outlined: true,
            class: 'mr-4'
        },
        acceptProps: {
            label: 'Delete',
            severity: 'danger',
            outlined: true
        },
        accept: () => {
            clockApi.deleteEntry(entry.id)
                .then(json => {
                    if(json.error) {
                        console.error('Clock API error: ', json.error)
                        notify(json.error, 'error')
                    } else {
                        notify(`Entry #${entry.id} deleted.`, 'success')
                        emit('action-succeeded')
                    }
                })
                .catch(err => {
                    console.error(err)
                    notify('There was a problem deleting that entry', 'error')
                })
        },
    });
}

onMounted(() => {
    jobApi.getJobOptions()
        .then(res => {
            jobOptions.value = res.options
            selectedJob.value = res.options?.find(opt => (
                opt.value == entry.job_id
            )).value
        })

    startTime.value = getLocalDateTime(entry.start_time)
    endTime.value = getLocalDateTime(entry.end_time)
})

</script>

<template>
<div class="flex flex-col p-4">
    <FloatLabel 
        variant="on"
        class="mb-6 w-full"    
    >
        <Select 
            v-model="selectedJob"
            :options="jobOptions"
            optionLabel="label"
            optionValue="value"
            class="min-w-[300px]"
        />
        <label>Select a Job</label>
    </FloatLabel>
    <FloatLabel 
        variant="on"
        class="mb-6"    
    >
        <DatePicker 
            id="start_time" 
            v-model="startTime" 
            showTime 
            hourFormat="12" 
            fluid  
            class="min-w-[300px]"
        />
        <Label>Start Time</Label>
    </FloatLabel>
    <FloatLabel 
        variant="on"
        class="mb-6"    
    >
        <DatePicker 
            id="end_time" 
            v-model="endTime" 
            showTime 
            hourFormat="12" 
            fluid  
            class="min-w-[300px]"
        />
        <Label>End Time</Label>
    </FloatLabel>
    <div class="flex flex-row justify-between gap-4">
        <Button
            label="Submit"
            severity="primary"
            variant="outlined"
            @click="handleUpdateEntry"
        />
        <Button
            label="Cancel"
            severity="warn"
            variant="outlined"
            @click="handleCancel"
        />
        <Button
            label='Delete'
            severity="danger"
            variant="outlined"
            @click="handleDeleteEntry($event)"
        />
        <ConfirmPopup />
    </div>
</div>
</template>

<style>

</style>