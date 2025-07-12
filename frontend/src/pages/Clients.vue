<script setup>
import Tab from 'primevue/tab'
import TabList from 'primevue/tablist'
import TabPanel from 'primevue/tabpanel'
import TabPanels from 'primevue/tabpanels'
import Tabs from 'primevue/tabs'
import ClientForm from '../components/forms/ClientForm.vue'
import { inject, onMounted, ref } from 'vue'
import ClientList from '../components/ClientList.vue'
import clientApi from '../utils/api/clients'

const { notify } = inject('toaster')

const tabsValue = ref('0')

const clients = ref([])
const clientForUpdate = ref(null)

const handleInitUpdate = (id) => {
    const newClientForUpdate = clients.value.find(client => client.id === id);
    if (newClientForUpdate) {
        clientForUpdate.value = newClientForUpdate;
        tabsValue.value = '2'; // Switch to Update tab
    } else {
        notify('Client not found for update', 'error');
    }
} 

const handleClearCient = () => {
    clientForUpdate.value = null
}

onMounted(() => {
    clientApi.getClients()
        .then(response => {
            clients.value = response.clients;
        })
        .catch(error => {
            notify(`Error fetching clients ${error}`, 'error');
            console.error('Error fetching clients:', error);
        });
})

</script>

<template>
    <div>
        <Tabs v-model:value="tabsValue" class="w-[900px]">
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
                    <ClientList 
                        :clients="clients" 
                        @init-update="id => handleInitUpdate(id)"    
                    />
                </TabPanel>
                <TabPanel value="1">
                    <ClientForm />
                </TabPanel>
                <TabPanel value="2">
                    <ClientForm 
                        :clientForUpdate="clientForUpdate"
                        @clear-client="handleClearCient"    
                    />
                </TabPanel>
            </TabPanels>
        </Tabs>
    </div>
</template>