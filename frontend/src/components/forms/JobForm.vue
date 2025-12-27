<script setup>
import { inject, onMounted, reactive, ref, watch } from 'vue';
import jobApi from '../../utils/api/jobs';
import clientApi from '../../utils/api/clients'
import { Checkbox } from 'primevue';

const { notify } = inject('toaster')

const { jobForUpdate } = defineProps({
    jobForUpdate: {
        type: Object,
        required: false,
        default: null,
    },
})

const emit = defineEmits(['clear-job', 'refresh-list']);

const jobState = reactive({
    title: '',
    description: '',
    client_id: null,
    active: true,
});

const clientOptions = ref([])

const clearForm = () => {
    Object.keys(jobState).forEach(key => {
        if(key === 'active') {
            jobState[key] = true;
        } else if (key === 'client_id') {
            jobState[key] = null;
        } else {
            jobState[key] = '';
        }
    });

    emit('clear-job')
}

const setupForm = () => {
    if (jobForUpdate) {
        Object.keys(jobState).forEach(key => {
            if(jobForUpdate[key]) {
                if(key == 'client') {
                    console.log('THIS MY CLIENT ID? ', jobForUpdate[key].id)
                    jobstate[key] = jobForUpdate[key].id
                } else {
                    jobState[key] = jobForUpdate[key]
                }
            }
        });
    } else {
        clearForm();
        emit('clear-job');
    }
}

const handleSubmit = () => {
    if(!jobForUpdate) {
        jobApi.addJob(jobState)
            .then(json => {
                if (json.error) {
                    console.error('Error:', json.error);
                    notify(json.error, 'error');
                    return;
                } else {
                    notify('Job saved successfully!', 'success');
                    clearForm();
                    emit('refresh-list')
                    console.log('NEW JOB => ', json.job);
                }
            })
            .catch(err => {
                console.error('API Error:', err);
                notify('Failed to save job.', 'error');
            });
    } else {
        jobApi.updateJob(jobForUpdate.id, jobState)
            .then(json => {
                if (json.error) {
                    console.error('Error:', json.error);
                    notify(json.error, 'error');
                    return;
                } else {
                    notify('Job updated successfully!', 'success');
                    clearForm();
                    emit('refresh-list')
                }
            })
            .catch(err => {
                console.error('API Error:', err);
                notify('Failed to update job.', 'error');
            });
    }
}

watch(() => jobForUpdate, (newVal) => {
    setupForm();
}, { immediate: true });

onMounted(() => {
    setupForm();
    clientApi.getClientOptions()
        .then(res => clientOptions.value = res.options)
        .catch(err => notify(`There has been a problem: ${err}`, 'error'))
});

</script>

<template>
<div class="flex-flex-col gap-12">
    <div class="pt-8 px-4 flex flex-row gap-8 justify-around items-start">
        <div class="flex flex-col gap-4">
            <div class="relative max-w-fit">
                <FloatLabel variant="on">
                    <InputText
                        id="title"
                        name="title"
                        class="min-w-[300px]"
                        v-model="jobState.title"
                    />
                    <label>Title</label>
                </FloatLabel>
            </div>
            <FloatLabel variant="on">
                <Select
                    id="client"
                    name="client"
                    class="min-w-[300px]"
                    v-model="jobState.client_id"
                    :options="clientOptions"
                    optionLabel="label"
                    optionValue="value"
                />
                <label>Client</label>
            </FloatLabel>
            <div class="flex flex-row justify-start gap-6">
                <Checkbox
                    id="active"
                    name="active"
                    size="large"
                    binary
                    v-model="jobState.active"
                />
                <label>Active</label>
            </div>
        </div>
        <div class="flex flex-col gap-8 justify-between">
            <div class="relative max-w-fit">
                <FloatLabel variant="on">
                    <Textarea
                        id="description"
                        name="description"
                        class="min-w-[300px]"
                        :rows="5"
                        v-model="jobState.description"
                    />
                    <label>Description</label>
                </FloatLabel>
            </div>
        </div> 
    </div>
    <div class="flex flex-row justify-end gap-6 mt-12">
        <Button
            :label="jobForUpdate ? 'Update Job' : 'Add Job'"
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