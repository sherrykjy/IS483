<template>
    <div v-if="visible" class="popupOverlay">
      <div class="popupContent">
        <i class="uil uil-times popupClose" @click="closePopup"></i>
  
        <!-- Unlock Popup -->
        <div v-if="type === 'unlock'">
            <p class="head">
                Confirm Unlock
            </p>

            <p class="body">
                You are unlocking 
                <span> {{ cardName }} </span>
                for 
                <span> {{ cardPrice }} </span>
                HealthCoins 
            </p>

            <div class="buttonBlock">
                <button style="background-color: var(--text-highlight);" @click="closePopup"> Cancel </button>
                <button style="background-color: var(--blue);" @click="confirmAction"> Confirm </button>
            </div>
        </div>
  
        <!-- Trade Popup -->
        <div v-if="type === 'trade'">
            <p class="head">
                Confirm Trade
            </p>

            <p class="body">
                You are trading 
                <span> {{ tradeCardName }} </span>
                for 
                <span> {{ receiveCardName }} </span>
                with 
                <span> {{ tradeWith }} </span>
            </p>

            <div class="buttonBlock">
                <button style="background-color: var(--text-highlight);" @click="closePopup"> Cancel </button>
                <button style="background-color: var(--blue);" @click="confirmAction"> Confirm </button>
            </div>
        </div>
  
        <!-- Info Popup -->
        <div v-if="type === 'info'">
            <div class="head">
                <img src="../assets/icons/collection/lightbulb.png">
                <p> Did you know </p>
            </div>

            <p class="cbody">
                Strawberries aren’t true berries by botanical definition. 
                They are part of the rose family!
            </p>

            <div class="head">
                <img src="../assets/icons/collection/recommendation.png">
                <p> Recommendation </p>
            </div>

            <p class="cbody">
                The daily fruit intake recommendation is 1.5-2 cups of fruit 
                per day. Munch on 12-16 strawberries as part of your healthy 
                diet with this rich source of vitamin C, fibre, and antioxidants.
            </p>

            <div class="coolButton">
                <button style="background-color: var(--blue);" @click="closePopup"> Cool! </button>
            </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
props: {
    visible: {
        type: Boolean,
        default: false
    },
    type: {
        type: String,  // 'unlock', 'trade', or 'info'
        default: ''
    },
    cardName: {
        type: String,
        default: ''
    },
    cardPrice: {
        type: Number, // Used for unlock popup
        default: 0
    },
    tradeCardName: {
        type: String, // Used for trade popup (card to trade)
        default: ''
    },
    receiveCardName: {
        type: String, // Used for trade popup (card to receive)
        default: ''
    },
    tradeWith: {
        type: String, // Used for trade popup (person trading with)
        default: ''
    },
    cardImage: {
        type: String, // Used for info popup
        default: ''
    },
    cardSet: {
        type: String, // Used for info popup
        default: ''
    },
    cardDescription: {
        type: String, // Used for info popup
        default: ''
    }
},
methods: {
    closePopup() {
        this.$emit('close');
    },
    confirmAction() {
        this.$emit('confirm');
    }
}
}
</script>

<style scoped>
.popupOverlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 20000;
    display: flex;
    justify-content: center;
    align-items: center;
}

.popupContent {
    background: white;
    padding: 20px;
    border-radius: 8px;
    width: 300px;
    text-align: center;
}

.popupClose {
    position: absolute;
    top: 15px;
    right: 15px;
    font-size: 32px; /* Increase the size */
    color: white; /* Make it white */
    cursor: pointer;
}

.confirmButton {
    background-color: #4caf50;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

.cardImagePopup {
    width: 100px;
    height: auto;
    margin: 10px 0;
}

.card {
    width: 70%;
    display: flex;
    margin: auto;
}
.container {
    padding: 16px;
}

.head {
    font-family: text-bold;
    font-size: 17px;
    color: var(--default-text);
    margin-bottom: 0;
    display: flex;
}

.head img {
    width: 25px;
    height: 25px;
    margin-right: 5px;
}

.container .head p {
    margin-bottom: 5px;
}

.cbody {
    font-family: text-medium;
    font-size: 14px;
    color: var(--default-text);
    padding: 0 8px;
    line-height: 15px;
    text-align: justify;
}

.body {
    font-family: text-medium;
    font-size: 14px;
    color: var(--default-text);
    text-align: justify;
}

.body span {
    font-family: text-bold;
}

button {
    font-family: text-medium;
    color: var(--grey);
    font-size: 10px;
    background-color: var(--blue);
    border-radius: 5px;
    border: none;
    padding: 5px 10px;
    width: 60px;
}

.buttonBlock {
    display: flex;
    justify-content: flex-end;
    gap: 5px;
    margin-top: 16px;
}

.coolButton {
    display: flex;
    justify-content: center;
}

</style>  