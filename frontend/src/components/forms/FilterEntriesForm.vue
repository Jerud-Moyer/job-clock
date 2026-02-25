<script setup>
import { inject, reactive } from 'vue';

const { jobOptions, clientOptions } = inject('options-store')

const emit = defineEmits(['get-filtered-entries'])

const filterSet = reactive({
    start_time: null,
    end_time: null,
    client_id: null,
    job_id: null
})

const handleEmitGetFilteredEntries = () => {
    const filterData = {}
    Object.keys(filterSet).forEach(f => {
        if(filterSet[f]) {
            const val = f === 'start_time' || f === 'end_time'
              ? new Date(filterSet[f]).toISOString()
              : filterSet[f]

            filterData[f] = val 
        }
    })

    emit('get-filtered-entries', filterData)
}

</script>

<template>
<div class="flex flex-row justify-center">
    <div class="container flex flex-col max-w-fit bg-surface-900 rounded-lg pt-6">
        <p class="text-xl text-left px-8 mb-6">Filters</p>
        <div class="flex flex-row">
            <div class="px-6">
                <FloatLabel
                    variant="on"
                    class="mb-6"
                >
                    <DatePicker
                        id="start_time"
                        v-model="filterSet.start_time"
                        show-time
                        hour-format="12"
                        fluid
                        class="min-w-[300px]"
                    />   
                    <label>Start Time</label>
                </FloatLabel>
                <FloatLabel
                    variant="on"
                    class="mb-6"
                >
                    <DatePicker
                        id="end_time"
                        v-model="filterSet.end_time"
                        show-time
                        hour-format="12"
                        fluid
                        class="min-w-[300px]"
                    />
                    <label>End Time</label>
                </FloatLabel>
            </div>
            <div class="px-6">
                <FloatLabel 
                    variant="on"
                    class="mb-6 w-full"    
                >
                    <Select 
                        v-model="filterSet.job_id"
                        :options="jobOptions"
                        optionLabel="label"
                        optionValue="value"
                        class="min-w-[300px]"
                    />
                    <label>Select a Job</label>
                </FloatLabel>
                <FloatLabel 
                    variant="on"
                    class="mb-6 w-full"    
                >
                    <Select 
                        v-model="filterSet.client_id"
                        :options="clientOptions"
                        optionLabel="label"
                        optionValue="value"
                        class="min-w-[300px]"
                    />
                    <label>Select a Client</label>
                </FloatLabel>
            </div>
        </div>
        <div class="flex flex-row justify-end p-6">
            <Button
                label="Submit"
                variant="outlined"
                severity="priimary"
                @click="handleEmitGetFilteredEntries"
            />
        </div>
    </div>
</div>
</template>