<template>
    <n-date-picker v-model:value="selectedDate" type="date" placeholder="Filter" @update:value="updateDate" />
    <!-- <pre>{{ JSON.stringify(timestamp) }}</pre> -->
</template>

<script>
    import { defineComponent, ref, watch } from "vue";
    import { NDatePicker } from 'naive-ui'; 
    // import { format, parseISO } from 'date-fns';

    export default defineComponent({
        components: {
            NDatePicker
        },
        props: {
            modelValue: {
                type: [String, Date, null],
                default: null
            }
        },
        setup(props, { emit }) {
            const date = ref(props.modelValue ? new Date(props.modelValue) : null);

            const updateDate = (value) => {
                console.log('Date value received:', value); // Debugging log

                if (value) {
                    // The date picker returns a UTC timestamp, so adjust for Singapore's time zone (UTC+8)
                    const utcDate = new Date(value);
                    const sgDate = new Date(utcDate.getTime() - (utcDate.getTimezoneOffset() * 60000)); // Adjust to local time

                    // Format the date as 'YYYY-MM-DD' (Singapore local date)
                    const localDateString = sgDate.toISOString().split('T')[0];
                    console.log("Formatted Singapore date being emitted:", localDateString);
                    emit('update:modelValue', localDateString);
                } else {
                    emit('update:modelValue', null);
                }
            };

            return {
                date,
                updateDate
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