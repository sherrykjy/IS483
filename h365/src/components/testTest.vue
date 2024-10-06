<!-- CODE ON HOW TO CALL ALL 3 POP UPS -->

<!-- <template>
    <div class="stickyHeader">
        <div class="pageHeader">
            <p> My Collectibles </p>
        </div>

        <div class="displayBlock">
            <div class="blockLeft">
                <div class="blockText">
                    <p> 1080 </p>
                    <span> <img src="../assets/icons/collection/coin.png"> </span>
                </div>
                <p> My Healthcoins </p>
            </div>

            <div class="blockRight">
                <div class="blockText">
                    <img src="../assets/icons/collection/lock.png" style="width: 25px; height: auto; margin-right: 3px;">
                    <p> <span> 2 </span> / 108 </p>
                </div>
                <p> Collectibles Unlocked </p>
            </div>
        </div>

        <div class="buttonGroup">
            <button class="storeButton">
                <label> Store </label>
                <i class="uil uil-store"> </i>
            </button>

            <button class="tradeButton">
                <label> Trade </label>
                <i class="uil uil-exchange"> </i>
            </button>
        </div>
    </div>

    <div class="pagePad">
        <div class="search-bar">
            <i class="uil uil-search"></i>
            <input type="text" placeholder="Search by card or set" />
        </div>

        <div class="colDisplay">
            <div class="card" @click="openInfoPopup('Selena', 'Fruit Basket', 'Description of Selena', '../assets/icons/collection/fruit_basket/selena_strawberry.png')">
                <img src="../assets/icons/collection/fruit_basket/selena_strawberry.png">
                <p class="cardName"> Selena </p>
                <p class="cardSet"> Fruit Basket </p>
            </div> -->

            <!-- <div class="card" @click="openTradePopup('Williams', 'Selena', 'Alice Tan')">
                <img src="../assets/icons/collection/fruit_basket/gracia_grape.png">
                <p class="cardName"> Gracia </p>
                <p class="cardSet"> Fruit Basket </p>
            </div> -->

            <!-- <div class="card" @click="openUnlockPopup('Sweet Squad', '200')">
                <img src="../assets/icons/collection/wellness_wonders/sweat_squad.png">
                <p class="cardName"> Sweet Squad </p>
                <p class="cardSet"> Wellness Wonders </p>
            </div> -->

            <!-- <div class="card" @click="openInfoPopup('Hydration Hero', 'Wellness Wonders', 'Description of Hydration Hero', '../assets/icons/collection/wellness_wonders/hydration_hero.png')">
                <img src="../assets/icons/collection/wellness_wonders/hydration_hero.png">
                <p class="cardName"> Hydration Hero </p>
                <p class="cardSet"> Wellness Wonders </p>
            </div>

            <div class="card" @click="openInfoPopup('Cardio Champ', 'Wellness Wonders', 'Description of Cardio Champ', '../assets/icons/collection/wellness_wonders/cardio_champ.png')">
                <img src="../assets/icons/collection/wellness_wonders/cardio_champ.png">
                <p class="cardName"> Cardio Champ </p>
                <p class="cardSet"> Wellness Wonders </p>
            </div> -->

        <!-- </div> -->
        
        <!-- info pop up -->
        <!-- <Popup
            ref="popup"
            :visible="isPopupVisible"
            :type="popupType"
            :cardName="selectedCardName"
            :cardPrice="selectedCardPrice"
            :tradeCardName="tradeCardName"
            :receiveCardName="receiveCardName"
            :tradeWith="tradeWith"
            :cardImage="selectedCardImage"
            :cardSet="selectedCardSet"
            :cardDescription="selectedCardDescription"
            @close="closePopup"
            @confirm="handleConfirm"
        /> -->

        <!-- unlock pop up -->
        <!-- <Popup
            v-if="isPopupVisible"
            :visible="isPopupVisible"
            :type="popupType"
            :cardName="cardName"
            :cardPrice="cardPrice"
            @close="closePopup"
        /> -->

        <!-- trade pop up -->
        <!-- <Popup
            v-if="isPopupVisible"
            :visible="isPopupVisible"
            :type="popupType"
            :tradeCardName="tradeCardName"
            :receiveCardName="receiveCardName"
            :tradeWith="tradeWith"
            @close="closePopup"
        /> -->

    <!-- </div>
    
</template> -->

<!-- <script>
import Popup from '@/components/popUp.vue';

// info pop up
export default {
  components: {
    Popup
  },
  data() {
    return {
      isPopupVisible: false,
      popupType: '', // 'unlock', 'trade', 'info'
      selectedCardName: '',
      selectedCardPrice: 0,
      tradeCardName: '',
      receiveCardName: '',
      tradeWith: '',
      selectedCardImage: '',
      selectedCardSet: '',
      selectedCardDescription: ''
    };
  },
  methods: {
    openInfoPopup(cardName, cardSet, cardDescription, cardImage) {
      this.selectedCardName = cardName;
      this.selectedCardSet = cardSet;
      this.selectedCardDescription = cardDescription;
      this.selectedCardImage = cardImage;
      this.popupType = 'info';
      this.isPopupVisible = true;
    },
    closePopup() {
      this.isPopupVisible = false;
    },
    handleConfirm() {
      console.log('Action confirmed');
      this.isPopupVisible = false;
    }
  }
}; -->


<!-- // unlock pop up
// export default {
//     components: {
//         Popup
//     },
//     data() {
//         return {
//             isPopupVisible: false,  // Controls popup visibility
//             cardName: 'Strawberry Card',  // Example data
//             cardPrice: '100',  // Example price
//             popupType: ''
//         };
//     },
//     methods: {
//         openUnlockPopup(cardName, cardPrice) {
//             this.cardName = cardName;
//             this.cardPrice = cardPrice;
//             this.popupType = 'unlock';
//             this.isPopupVisible = true;
//         },
//         closePopup() {
//             this.isPopupVisible = false;
//         }
//     }
// };


// trade pop up
// export default {
//   components: {
//     Popup
//   },
//   data() {
//     return {
//       isPopupVisible: false,
//       tradeCardName: 'Card A',  // Example data
//       receiveCardName: 'Card B',  // Example data
//       tradeWith: 'User123'  // Example data
//     };
//   },
//   methods: {
//     openTradePopup(tradeCardName, receiveCardName, tradeWith) {
//       this.tradeCardName = tradeCardName;
//       this.receiveCardName = receiveCardName;
//       this.tradeWith = tradeWith;
//       this.popupType = 'trade';
//       this.isPopupVisible = true;
//     },
//     closePopup() {
//       this.isPopupVisible = false;
//     }
//   }
// };
// </script> -->










<!-- POP-UPS GOOD CODE -->

<template>
    <div class="card">
        <div class="container">
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
                <button style="background-color: var(--text-highlight);"> Cancel </button>
                <button style="background-color: var(--blue);"> Confirm </button>
            </div>
        </div>
    </div>

    <div class="card">
        <div class="container">
            <p class="head">
                Confirm Trade
            </p>

            <p class="body">
                You are trading 
                <span> {{ giveCard }} </span>
                for 
                <span> {{ receiveCard }} </span>
                with 
                <span> {{ tradeUser }} </span>
            </p>

            <div class="buttonBlock">
                <button style="background-color: var(--text-highlight);"> Cancel </button>
                <button style="background-color: var(--blue);"> Confirm </button>
            </div>
        </div>
    </div>

    <div class="card">
        <div class="container">
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
                <button style="background-color: var(--blue);"> Cool! </button>
            </div>
        </div>
    </div>

    <div class="card">
        <div class="container">
            <div class="close-button" @click="closePopup">
                <i class="uil uil-times"></i>
            </div>

            <div class="head" style="margin-bottom: 7px">
                <p> Event Entry Code </p>
            </div>

            <p class="code"> This event requires a special entry code. Check with your admin 
                to get your access code and join the fun! </p>

            <label for="eventCode" class="formLabel code" style="margin-bottom: 0px;"> Please enter code </label><br>
            <input type="text" id="eventCode" class="formInput"><br><br>

            <button class="formButton" style="color: var(--default-white); 
                background: var(--blue); width: 100%;">
                Enter
            </button>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        cardName: {
            type: String,
            required: true,
        },
        cardPrice: {
            type: Number,
            required: true,
        },
        giveCard: {
            type: String,
            required: true,
        },
        receiveCard: {
            type: String,
            required: true,
        },
        tradeUser: {
            type: String,
            required: true,
        }
    },
};

</script>

<style scoped>
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
}

.body {
    font-family: text-medium;
    font-size: 14px;
    color: var(--default-text);
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




.code {
    font-family: text-medium;
    font-style: italic;
    font-size: 11px;
    color: var(--text-highlight);
    text-align: justify;
    margin-bottom: 10px;
}

.close-button {
    position: absolute;
    top: 10px;
    right: 10px;
    cursor: pointer;
    font-size: 1.5em;
    color: var(--text-highlight);
}

</style>