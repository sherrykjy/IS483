<template>
    <n-date-picker v-model:value="timestamp" type="date" placeholder="Filter" />
    <!-- <pre>{{ JSON.stringify(timestamp) }}</pre> -->
</template>
  
<script>
    import { defineComponent, ref } from "vue";
    import { NDatePicker } from 'naive-ui';
  
    export default defineComponent({
    components: {
        NDatePicker
    },
    setup() {
        return {
        timestamp: ref(null)
        };
    }
    });
</script>  

<style>
.n-input__input {
    font-family: text-regular;
    font-size: 11px;
    color: var(--text-highlight);
}
</style>