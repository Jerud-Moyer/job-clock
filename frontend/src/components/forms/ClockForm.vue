<script setup>
import { computed, inject, onMounted, ref } from 'vue';
import jobApi from '../../utils/api/jobs'
import clockApi from '../../utils/api/clock'

const { notify } = inject('toaster')

const { 
    isClockedIn, 
    setClockedStatus,
    jobWorking,
    setJobWorking,
    openEntryId,
    setOpenEntryId,
    setStartTime
} = inject('clocked-status')

const jobOptions = ref([])
const filteredJobOptions = ref([])
const selectedJob = ref(null)
const notes = ref('')

const searchJobOptions = (event) => {
    setTimeout(() => {
        if (!event.query.trim().length) {
            filteredJobOptions.value = [...jobOptions.value];
        } else {
            filteredJobOptions.value = jobOptions.value.filter((option) => {
                return option.label.toLowerCase().startsWith(event.query.toLowerCase());
            });
        }
    }, 250);
}

const handleClockIn = () => {
    if(selectedJob.value) {
        // setJobWorking(selectedJob.value.label)
        // setClockedStatus(true)

        const dateTime = new Date()

        const entry = {
            start_time: dateTime.toISOString(),
            job_id: selectedJob.value.value,
            notes: notes.value
        }

        clockApi.addEntry(entry)
            .then(res => {
                console.log('we got entry! ', res)
                if(res.time_entry) {
                    notify(`Clocked into ${jobWorking.value}`)
                    setJobWorking(selectedJob.value.label)
                    setClockedStatus(true)
                    setOpenEntryId(res.time_entry.id)
                    setStartTime(res.time_entry.start_time)
                }
            }) 
            .catch(err => {
                console.error(err)
                notify('There was a problem clocking in: ', 'error')
            })
    } else {
        notify('Select a Job to Clock-in!', 'error')
    }
}

const handleClockOut = () => {
    const entryId = openEntryId.value
    clockApi.clockOut(entryId)
        .then(res => {
            if(res.time_entry) {
                console.log('clocked out successfully: ', res.entry)
                notify(`Clocked out of ${jobWorking.value}`)
                setClockedStatus(false)
                setJobWorking(null)
            }
        })
        .catch(err => {
            console.error(err)
            notify('There was a problem clocking you out', 'error')
        })

}

onMounted(() => {
    jobApi.getJobOptions()
        .then(res => {
            jobOptions.value = res.options
        })
        .catch(err => console.error(err))
})
</script>

<template>
<div class="h-full">    
    <div
        v-if="!isClockedIn" 
        class="flex flex-col h-full justify-center items-center"
    >
        <div class="mt-12">
            <FloatLabel variant="on">
                <AutoComplete 
                    v-model="selectedJob"
                    optionLabel="label" 
                    :suggestions="filteredJobOptions" 
                    @complete="searchJobOptions"
                    dropdown
                />
                <label>Select a Job</label>
            </FloatLabel>
        </div>
        <div class="mt-6">
            <FloatLabel variant="on">
                <Textarea
                    v-model="notes"
                    rows="5"
                    cols="25"
                />
                <label>Notes</label>
            </FloatLabel>
        </div>
        <div class="mt-6">
            <Button
                icon="pi pi-clock"
                label="Clock In"
                rounded
                @click="handleClockIn"
            />
        </div>
    </div>
    <div 
        v-if="isClockedIn"
        class="flex flex-col h-full justify-center items-center"
    >
        <p class="text-3xl mb-6">Working on <span class="font-bold text-color-emphasis">{{ jobWorking }}</span></p>
        <div class="mt-6">
            <FloatLabel variant="on">
                <Textarea
                    v-model="notes"
                    rows="5"
                />
                <label>Notes</label>
            </FloatLabel>
        </div>
        <div class="mt-6">
            <Button
                severity="warn"
                icon="pi pi-clock"
                label="Clock Out"
                rounded
                @click="handleClockOut"
            />
        </div>
    </div>
</div>
</template>

<style scoped>

</style>