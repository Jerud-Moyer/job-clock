<script setup>
import { inject, onMounted, reactive, watch } from 'vue';
import stateOptions from '../../data/state-options';
import clientApi from '../../utils/api/clients';

const { notify } = inject('toaster')

const { clientForUpdate } = defineProps({
    clientForUpdate: {
        type: Object,
        required: false,    
        default: null,
    },
})

const emit = defineEmits(['clear-client']);

const clientState = reactive({
    first_name: '',
    last_name: '',
    email: '',
    phone: '',
    street_address: '',
    city: '',
    state: '',
    zip_code: '',
    current_rate: '',
})

const clearForm = () => {
    Object.keys(clientState).forEach(key => {
        clientState[key] = '';
    });
}

const setupForm = () => {
    if (clientForUpdate) {
        Object.keys(clientState).forEach(key => {
            clientState[key] = clientForUpdate[key] || '';
        });
    } else {
        clearForm();
        emit('clear-client');
    }
}

const handleSubmit = () => {
    if(!clientForUpdate) {
        clientApi.addClient(clientState)
            .then(json => {
                if (json.error) {
                    console.error('Error:', json.error);
                    notify(json.error, 'error');
                    return;
                } else {
                    notify('Client saved successfully!', 'success');
                    clearForm()
                    console.log('NEW CLIENT => ', json.client);
                }
            })
            .catch(err => {
                notify(err.message, 'error');
                console.error('Error saving client:', err);
            });
    } else {
        //update
        clientApi.updateClient(clientForUpdate.id, clientState)
            .then(json => {
                if (json.error) {
                    console.error('Error:', json.error);
                    notify(json.error, 'error');
                    return;
                } else {
                    notify('Client updated successfully!', 'success');
                    clearForm();
                    emit('clear-client');
                    console.log('UPDATED CLIENT => ', json.client);
                }
            })
            .catch(err => {
                notify(err.message, 'error');
                console.error('Error updating client:', err);
            });
    }
}

watch(() => clientForUpdate, (newVal) => {
    if (newVal) {
        setupForm();
    } else {
        clearForm();
    }
}, { immediate: true });

onMounted(() => {
    setupForm();
});
</script>

<template>
    <div class="flex flex-col gap-12">
        <div class="pt-8 px-4 flex flex-row gap-8 justify-around items-center">
            <div class="flex flex-col gap-4">
                <div class="relative max-w-fit">
                    <FloatLabel variant="on">
                        <InputText 
                            id="first_name"
                            name="first_name"
                            class="min-w-[250px]"
                            v-model="clientState.first_name"
                        />
                        <label>First Name</label>
                    </FloatLabel>
                </div>
                <div class="relative max-w-fit">
                    <FloatLabel variant="on">
                        <InputText 
                            id="last_name"
                            name="last_name"
                            class="min-w-[250px]"
                            v-model="clientState.last_name"
                        />
                        <label>Last Name</label>
                    </FloatLabel>
                </div>
                <div class="relative max-w-fit">
                    <FloatLabel variant="on">
                        <InputNumber 
                            id="current_rate"
                            name="current_rate"
                            mode="currency" 
                            currency="USD" 
                            locale="en-US"
                            class="min-w-[250px]"
                            v-model="clientState.current_rate"
                        />
                        <label>Current Rate</label>
                    </FloatLabel>
                </div>
            </div>
            <div class="flex flex-col gap-4">
                <div class="relative max-w-fit">
                    <FloatLabel variant="on">
                        <InputText 
                            id="email"
                            name="email"
                            class="min-w-[250px]"
                            v-model="clientState.email"
                        />
                        <label>Email</label>
                    </FloatLabel>
                </div>
                <div class="relative max-w-fit">
                    <FloatLabel variant="on">
                        <InputText 
                            id="phone"
                            name="phone"
                            class="min-w-[250px]"
                            v-model="clientState.phone"
                        />
                        <label>Phone</label>
                    </FloatLabel>
                </div>
                <div class="relative max-w-fit">
                    <FloatLabel variant="on">
                        <InputText 
                            id="street_address"
                            name="street_address"
                            class="min-w-[250px]"
                            v-model="clientState.street_address"
                        />
                        <label>Street Address</label>
                    </FloatLabel>
                </div>    
            </div>
            <div class="flex flex-col gap-4">
                <div class="relative max-w-fit">
                    <FloatLabel variant="on">
                        <InputText 
                            id="city"
                            name="city"
                            class="min-w-[250px]"
                            v-model="clientState.city"
                        />
                        <label>City</label>
                    </FloatLabel>
                </div> 
                <div class="relative max-w-fit">
                    <FloatLabel variant="on" class="">
                        <Select
                            :options="stateOptions"
                            optionLabel="label"
                            optionValue="value"
                            id="state"
                            name="state"
                            class="min-w-[250px]"
                            v-model="clientState.state"
                        />
                        <label>State</label>
                    </FloatLabel>
                </div>
                <div class="relative max-w-fit">
                    <FloatLabel variant="on">
                        <InputText 
                            id="zip_code"
                            name="zip_code"
                            class="min-w-[250px]"
                            v-model="clientState.zip_code"
                        />
                        <label>Zip Code</label>
                    </FloatLabel>
                </div> 
            </div>
        </div>
        
        <div class="flex flex-row justify-end gap-8">
            <Button 
                label="Save Client"
                severity="primary"
                variant="outlined"
                @click="handleSubmit"
            />
            <Button
                label="Clear Form"
                severity="secondary"
                @click="clearForm"
            />
        </div>
    </div>
</template>