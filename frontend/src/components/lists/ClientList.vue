<script setup>
import { inject } from 'vue';

const { clients } = defineProps({
    clients: {
        type: Array,
        required: true,
    },
})
const emit = defineEmits(['init-update'])
const { notify } = inject('toaster')

const handleInitUpdate = (id) => {
    emit('init-update', id);
}
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
            <!-- <template #header>
                <p class="text-xl text-left">Clients</p>
            </template> -->
            <Column field="last_name" header="Last Name" />
            <Column field="first_name" header="First Name" />
            <Column field="email" header="Email" />
            <Column field="phone" header="Phone" />
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
    </div>
</template>

<style scoped>

</style>