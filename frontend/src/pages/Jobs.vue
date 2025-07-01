<script setup>
import { inject, ref } from 'vue'
import JobForm from '../components/forms/JobForm.vue';

const { notify } = inject('toaster')

const tabsValue = ref('0')

</script>

<template>
    <div>
        <h2>Jobs Page</h2>
        <Tabs v-model:value="tabsValue" class="w-[900px]">
            <TabList>
                <Tab value="0">Job List</Tab>
                <Tab value="1">Add a Job</Tab>
                <Tab value="2">Update a Job</Tab>
            </TabList>
            <TabPanels>
                <TabPanel value="0">
                    <!-- Job List Component will go here -->
                    <JobForm />
                </TabPanel>
                <TabPanel value="1">
                    <!-- Add Job Form Component will go here -->
                    <p>Add Job Form Component Placeholder</p>
                </TabPanel>
                <TabPanel value="2">
                    <!-- Update Job Form Component will go here -->
                    <p>Update Job Form Component Placeholder</p>
                </TabPanel>
            </TabPanels>
        </Tabs>
    </div>
</template>