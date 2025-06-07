<script setup>
import Tab from 'primevue/tab'
import TabList from 'primevue/tablist'
import TabPanel from 'primevue/tabpanel'
import TabPanels from 'primevue/tabpanels'
import Tabs from 'primevue/tabs'
import ClientForm from '../components/forms/ClientForm.vue'
import { inject } from 'vue'
import ClientList from '../components/ClientList.vue'

const { notify } = inject('toaster')

</script>

<template>
    <div>
        <Tabs value="0" class="w-[900px]">
            <TabList>
                <Tab value="0" >
                   Client List
                </Tab>
                <Tab value="1" >
                    Add a Client
                </Tab>
                <Tab value="2" >
                    Update a Client
                </Tab>
            </TabList>
            <TabPanels class="">
                <TabPanel value="0">
                    <ClientList />
                </TabPanel>
                <TabPanel value="1">
                    <ClientForm />
                </TabPanel>
                <TabPanel value="2">
                    <ClientForm />
                </TabPanel>
            </TabPanels>
        </Tabs>
    </div>
</template>