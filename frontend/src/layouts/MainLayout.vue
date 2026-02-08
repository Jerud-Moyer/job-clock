<script setup>
import { ref, inject, computed } from 'vue';
import { Toolbar } from 'primevue';
import { getLocalDateTime, getReadableDate } from '../utils/utils';

const {
    startTime,
    jobWorking
} = inject('clocked-status')

const activePage = ref('a')

const timeStarted = computed(() => {
    if(startTime.value) {
        return getReadableDate(startTime.value)
    } else return null
})

const handleActivePage = (ap) => {
    activePage.value = ap
}
</script>

<template>
<div class="h-full w-full">
    <Toolbar class="toolbar w-screen px-12">
        <template #start>
            <p class="text-5xl text-primary flex">
                JobCl
                <span class="clock-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" height="32px" viewBox="0 -960 960 960" width="32px" fill="currentcolor">
                        <path stroke="currentcolor" stroke-width="18" d="m612-292 56-56-148-148v-184h-80v216l172 172ZM480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-400Zm0 320q133 0 226.5-93.5T800-480q0-133-93.5-226.5T480-800q-133 0-226.5 93.5T160-480q0 133 93.5 226.5T480-160Z"/>
                    </svg>
                </span>
                ck
            </p>
        </template>
        <template #center>
            <p v-if="jobWorking" class="text-xl">
                Working on <span class="text-bold text-primary">{{ jobWorking }}</span>
                &nbsp;&nbsp;since: <span class="text-bold text-primary">{{ timeStarted }}</span>
            </p>
        </template>
        <template #end>
            <Button
                label="Clock"
                as="router-link"
                to="/"
                severity="secondary"
                text
                :class="activePage == 'a' ? 'active' : ''"
                @click="() => handleActivePage('a')"
            /> 
            <Button
                label="Jobs"
                as="router-link"
                to="/jobs"
                severity="secondary"
                text
                :class="activePage == 'b' ? 'active' : ''"
                @click="() => handleActivePage('b')"
            />  
            <Button
                label="Clients"
                as="router-link"
                to="/clients"
                severity="secondary"
                text
                :class="activePage == 'c' ? 'active' : ''"
                @click="() => handleActivePage('c')"
            />  
        </template>
    </Toolbar>
    <div class="w-full h-full p-4 pt-16">
        <slot></slot>
    </div>
</div>
</template>

<style scoped>
.toolbar {
    position: fixed;
    top: 0;
    left: 0;

    .p-button {
        &.active {
            border-bottom: solid var(--p-sky-400) 2px;
        } 
    }

    .clock-icon {
        transform: translateY(14px);
    }
}
</style>