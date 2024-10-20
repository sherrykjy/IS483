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

            <!-- Display error message -->
            <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>

            <div class="buttonBlock">
                <button style="background-color: var(--text-highlight);" @click="closePopup"> Cancel </button>
                <button style="background-color: var(--blue);" @click="confirmUnlock"> Confirm </button>
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

            <!-- Display error message -->
            <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>

            <div class="buttonBlock">
                <button style="background-color: var(--text-highlight);" @click="closePopup"> Cancel </button>
                <button style="background-color: var(--blue);" @click="confirmTrade"> Confirm </button>
            </div>
        </div>



        <!-- Info Popup -->
        <div v-if="type === 'info'">
            <div class="head">
                <img src="../assets/icons/collection/lightbulb.png">
                <p> Did you know </p>
            </div>

            <p class="cbody">
                {{ cardDescription }}
            </p>

            <div class="head">
                <img src="../assets/icons/collection/recommendation.png">
                <p> Recommendation </p>
            </div>

            <p class="cbody">
               {{ cardRecommendation }}
            </p>

            <div class="coolButton">
                <button style="background-color: var(--blue);" @click="closePopup"> Cool! </button>
            </div>
        </div>



        <!-- event code pop up -->
        <div v-if="type === 'event-code'">

            <div class="head-event" style="margin-bottom: 7px">
                <p> Event Entry Code </p>
                <div class="close-button" @click="closePopup">
                    <i class="uil uil-times"></i>
                </div>
            </div>

            <p class="code"> 
                This event requires a special entry code. Check with your admin 
                to get your access code and join the fun! 
            </p>

            <label for="eventCode" class="formLabel code" style="margin-bottom: 0px;"> 
                Please enter code 
            </label><br>

            <input type="text" id="eventCode" class="formInput" v-model="userEntryCode"><br><br>

            <!-- Display error message -->
            <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>

            <button class="formButton" style="color: var(--default-white); background: var(--blue); width: 100%;" @click="submitEventCode">
                Enter
            </button>
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
        type: String,  // 'unlock', 'trade', 'info' or 'event-code'
        default: ''
    },
    cardName: {
        type: String,
        default: ''
    },
    cardId: {
        type: [String, Number],
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
    },
    cardRecommendation: {
        type: String, // Used for info popup
        default: ''
    },
    eventName: {
        type: String,
        default: ''
    },
    errorMessage: { 
        type: String, default: '' 
    },
    tradeId: {
        type: [String, Number], 
        default: ''
    }
},
data() {
    return {
      userEntryCode: ''  // This is where the user's event code will be stored
    };
},
methods: {
    closePopup() {
        this.$emit('close');
    },
    confirmTrade() {
        this.$emit('confirm', this.tradeId);
    },
    submitEventCode() {
        // Emit the event code input by the user to the parent
        this.$emit('validate-code', this.userEntryCode);
    },
    confirmUnlock() {
        this.$emit('unlock-card', this.cardId);
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

.head-event {
    font-family: text-bold;
    font-size: 17px;
    color: var(--default-text);
    margin-bottom: 0;
    display: flex;
    align-items: center;
    justify-content: space-between
}

.head-event p {
    margin: 0;
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

.popupContent {
    text-align: justify;
}

.code {
    font-family: text-medium;
    font-style: italic;
    font-size: 11px;
    color: var(--text-highlight);
    margin-bottom: 10px;
}

.error-message {
    width: 100%;
    padding-left: 0px;
    color: var(--red);
    font-family: text-medium;
    font-size: 13px;
    text-align: left;
}

</style>  