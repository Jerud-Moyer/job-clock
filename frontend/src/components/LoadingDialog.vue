<script setup>
import { computed } from 'vue';


const { loading } = defineProps({
    loading: {
        type: Boolean,
        required: true
    }
})

const isLoading = computed(() => {
    return loading  
        ? true
        : false
})


</script>

<template>
<Dialog
    v-model:visible="isLoading"
    :closable="false"
    modal
>
    <svg xmlns="http://www.w3.org/2000/svg" width="160" height="160" viewBox="-10 -10 980 980">
        <!-- Outer ring from original icon, mirrored to positive coords -->
        <path fill="#1db9ff" d="M480 880q-83 0-156-31.5T197 763q-54-54-85.5-127T80 480q0-83 31.5-156T197 197q54-54 127-85.5T480 80q83 0 156 31.5T763 197q54 54 85.5 127T880 480q0 83-31.5 156T763 763q-54 54-127 85.5T480 880Zm0-320q133 0 226.5-93.5T800 480q0-133-93.5-226.5T480 160q-133 0-226.5 93.5T160 480q0 133 93.5 226.5T480 560Z" opacity="0"></path>
        <!-- Redraw ring cleanly -->
        <circle cx="480" cy="480" r="390" fill="none" stroke="#1db9ff" stroke-width="55"></circle>

        <!-- Minute hand (long, thin) — points up, rotates fast -->
        <g class="min-hand">
            <rect x="456" y="130" width="48" height="360" rx="24" fill="#1db9ff"></rect>
        </g>

        <!-- Hour hand (short, thick) — offset 60° so they're visibly apart at start -->
        <g class="hour-hand" style="animation-delay: -20s">
            <rect x="448" y="230" width="64" height="240" rx="32" fill="#1db9ff"></rect>
        </g>

        <!-- Center cap -->
        <circle cx="480" cy="480" r="44" fill="#1db9ff"></circle>
        </svg>
</Dialog>
</template>

<style>
    @keyframes spin-min  { from { transform: rotate(0deg);   } to { transform: rotate(360deg); } }
    @keyframes spin-hour { from { transform: rotate(0deg);   } to { transform: rotate(360deg); } }
    .min-hand  { transform-origin: 480px 480px; animation: spin-min  1s  linear infinite; }
    .hour-hand { transform-origin: 480px 480px; animation: spin-hour 12s linear infinite; }
</style>