<template>
    <div v-if="isVisible" class="overlay" @click="close">
        <div class="popup" @click.stop>
            <button class="close-btn" @click="close">
                <i class="uil uil-store"> </i>
            </button>
            <h2>{{ title }}</h2>
            <p>{{ content }}</p>

            <div v-if="popupType === 'confirmUnlock'">
                <p>Are you sure you want to unlock this card?</p>
                <button @click="confirmUnlock">Unlock</button>
                <button @click="close">Cancel</button>
            </div>

            <div v-if="popupType === 'confirmTrade'">
                <p>Are you sure you want to trade this card?</p>
                <button @click="confirmTrade">Trade</button>
                <button @click="close">Cancel</button>
            </div>
            
            <div v-if="popupType === 'showCardDetails'">
                <p>{{ cardDetails }}</p>
                <button @click="close">Close</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        title: {
            type: String,
            default: 'Popup Title',
        },
        content: {
            type: String,
            default: 'This is the content of the popup!',
        },
        popupType: {
            type: String,
            default: 'default',
        },
        cardDetails: {
            type: String,
            default: '',
        },
    },
    data() {
        return {
            isVisible: false,
        };
    },
    methods: {
        show() {
            this.isVisible = true;
        },

        close() {
            this.isVisible = false;
        },

        confirmUnlock() {
            this.close();
            this.$emit('unlockConfirmed');
        },

        confirmTrade() {
            this.close();
            this.$emit('tradeConfirmed');
        },
    },
};
</script>

<style scoped>
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.popup {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}
</style>