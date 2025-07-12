<script setup>
const { jobs } = defineProps({
    jobs: {
        type: Array,
        required: true
    }
})

const emit = defineEmits(['init-update'])

const handleInitUpdate = (id) => {
    emit('init-update', id)
}
</script>

<template>
    <div class="">
        <DataTable 
            :value="jobs" 
            :paginator="true" 
            :rows="10" 
            :responsiveLayout="'scroll'" 
            class="w-full"
            dataKey="id"
        >
            <template #header>
                <p class="text-xl text-left">Jobs</p>
            </template>
            <Column field="title" header="Title" />
            <Column field="client.client_name" header="Client" />
            <Column field="description" header="Description" />
            <Column field="last_clocked" header="Last Clocked" />
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