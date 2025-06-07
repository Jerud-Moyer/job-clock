<script setup>

import { Toolbar } from 'primevue';

</script>

<template>
<div class="h-full w-full">
    <Toolbar class="toolbar w-screen pr-12">
        <template #end>
            <Button
                label="Home"
                as="router-link"
                to="/"
                severity="secondary"
                text
            /> 
            <Button
                label="Clock"
                as="router-link"
                to="/time-clock"
                severity="secondary"
                text
            />  
            <Button
                label="Clients"
                as="router-link"
                to="/clients"
                severity="secondary"
                text
            />  
        </template>
    </Toolbar>
    <div class="w-full h-full p-4">
        <slot></slot>
    </div>
</div>
</template>

<style scoped>
.toolbar {
    position: fixed;
    top: 0;
    left: 0;
}
</style>