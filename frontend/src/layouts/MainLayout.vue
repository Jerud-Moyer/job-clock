<script setup>
import { ref } from 'vue';
import { Toolbar } from 'primevue';

const activePage = ref('a')

const handleActivePage = (ap) => {
    activePage.value = ap
}
</script>

<template>
<div class="h-full w-full">
    <Toolbar class="toolbar w-screen pr-12">
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
}
</style>