<script setup>

import { Toolbar } from 'primevue';

</script>

<template>
<div class="min-h-screen flex flex-col">
    <Toolbar class="toolbar w-screen">
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
    <div class="pt-[50px]">
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