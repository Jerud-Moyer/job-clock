<script setup>
import Tab from 'primevue/tab'
import TabList from 'primevue/tablist'
import TabPanel from 'primevue/tabpanel'
import TabPanels from 'primevue/tabpanels'
import Tabs from 'primevue/tabs'
import ClientForm from '../components/forms/ClientForm.vue'

</script>

<template>
    <div>
        <Tabs value="0" class="w-[900px] mt-20">
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
                   <ClientForm />
                </TabPanel>
                <TabPanel value="1">
                    <P>HERES MY FORM!!!</P>
                </TabPanel>
                <TabPanel value="2">
                    <P>HERES MY FORM!!!</P>
                </TabPanel>
            </TabPanels>
        </Tabs>
    </div>
</template>