<script setup>
import { ref, onMounted, inject } from 'vue';
import clientApi from '../utils/api/clients';

const clients = ref([])

const { notify } = inject('toaster')

onMounted(() => {
    clientApi.getClients().then(response => {
        clients.value = response.clients;
        console.log('CLIENTS => ', response);
    }).catch(error => {
        notify(`Error fetching clients ${error}`, 'error');
        console.error('Error fetching clients:', error);
    });
})
</script>

<template>
    <div class="">
        <DataTable 
            :value="clients" 
            :paginator="true" 
            :rows="10" 
            :responsiveLayout="'scroll'" 
            class="w-full"
            dataKey="id"
        >
            <template #header>
                <p class="text-xl text-left">Clients</p>
            </template>
            <Column field="last_name" header="Last Name" />
            <Column field="first_name" header="First Name" />
            <Column field="email" header="Email" />
            <Column field="phone" header="Phone" />
        </DataTable>
    </div>
</template>

<style scoped>

</style>