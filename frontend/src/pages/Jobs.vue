<script setup>
import { inject, onMounted, ref } from 'vue'
import JobForm from '../components/forms/JobForm.vue';
import jobApi from '../utils/api/jobs'
import JobList from '../components/lists/JobList.vue';

const { notify } = inject('toaster')

const jobs = ref([])
const jobForUpdate = ref(null)
const tabsValue = ref('0')

const handleInitUpdate = (id) => {
    const newJobForUpdate = jobs.value.find(job => job.id == id)
    if(newJobForUpdate) {
        jobForUpdate.value= newJobForUpdate
        tabsValue.value = '2'
    } else {
        notify('Job not found', 'error')
    }
}

const handleClearJob = () => {
    jobForUpdate.value = null
}

const handleGetJobs = () => {
    jobApi.getJobs()
        .then(res => {
            jobs.value = res.jobs
        })
        .catch(err => {
            notify(`Error fetching jobs: ${err}`, error)
            console.error('Error fetching jobs: ', err)
        })
    if(tabsValue.value != '0') tabsValue.value = '0'
}

onMounted(() => {
    handleGetJobs()
})
</script>

<template>
    <div class="flex flex-col justify-start h-full">
        <p class="text-4xl text-left mb-12 pl-4">Jobs</p>
        <Tabs v-model:value="tabsValue" class="w-[900px] rounded-lg">
            <TabList>
                <Tab value="0">Job List</Tab>
                <Tab value="1">Add a Job</Tab>
                <Tab value="2">Update a Job</Tab>
            </TabList>
            <TabPanels>
                <TabPanel value="0">
                    <JobList 
                        :jobs="jobs"
                        @init-update="id => handleInitUpdate(id)"
                    />
                </TabPanel>
                <TabPanel value="1">
                    <JobForm 
                        @refresh-list="handleGetJobs"
                    />
                </TabPanel>
                <TabPanel value="2">
                    <JobForm 
                        :job-for-update="jobForUpdate"
                        @clear-job="handleClearJob"
                        @refresh-list="handleGetJobs"
                    />
                </TabPanel>
            </TabPanels>
        </Tabs>
    </div>
</template>