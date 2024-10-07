<template>
    <div class="stickyHeader">
        <div class="pageHeader">
            <p> Store </p>
        </div>

        <div class="displayBlock">
            <div class="blockLeft">
                <div class="blockText">
                    <p style="margin-right: 5px"> {{ numHealthCoins }} </p>
                    <span> <img src="../assets/icons/collection/coin.png"> </span>
                </div>
                <p> My Healthcoins </p>
            </div>

            <div class="blockRight">
                <div class="blockText">
                    <img src="../assets/icons/collection/lock.png" style="margin-right: 5px;">
                    <p> <span> {{ numUnlocked }} </span> / {{ numCards }} </p>
                </div>
                <p> Collectibles Unlocked </p>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="info">
            Redeem your HealthCoins for exclusive digital collectibles and showcase them on your profile.
        </div>
    </div>

    <div class="pagePad">
        <div class="search-bar">
            <i class="uil uil-search"></i>
            <input type="text" placeholder="Search by card or set" />
        </div>

        <div class="head">
            <p> Explore Sets </p>
            <router-link :to="{ name: 'tradePage'}">
                <button class="tradeButton">
                    <label> Trade </label>
                    <i class="uil uil-exchange"> </i>
                </button>
            </router-link>
        </div>

        <div v-for="(cards, cardType) in allCards" :key="cardType" class="set">
            <div class="set">
                <p> {{ cardType }} </p>
                <div class="carousel">
                    <div v-for="card in cards" :key="card.card_id">
                        <div :class="['card', { 'card-owned': userCards.includes(card.card_id) }]">
                            <p class="cardName"> {{ card.title }} </p>

                            <!-- <img v-if="card.title == 'Oliver'" src="../assets/icons/collection/fruit_basket/oliver.png">
                            <img v-else-if="card.title == 'Selena'" src="../assets/icons/collection/fruit_basket/selena.png">
                            <img v-else-if="card.title == 'Benny'" src="../assets/icons/collection/fruit_basket/benny.png">
                            <img v-else-if="card.title == 'Gracia'" src="../assets/icons/collection/fruit_basket/gracia.png">
                            <img v-else-if="card.title == 'Penny'" src="../assets/icons/collection/fruit_basket/penny.png">

                            <img v-else-if="card.title == 'LeBron'" src="../assets/icons/collection/weekend_action/lebron.png">
                            <img v-else-if="card.title == 'Williams'" src="../assets/icons/collection/weekend_action/williams.png">
                            <img v-else-if="card.title == 'Weber'" src="../assets/icons/collection/weekend_action/weber.png">
                            <img v-else-if="card.title == 'Valdez'" src="../assets/icons/collection/weekend_action/valdez.png">
                            <img v-else-if="card.title == 'Dele'" src="../assets/icons/collection/weekend_action/dele.png"> -->

                            <img :src="getCardImage(card.title, card.card_type)" />

                            <div class="price">
                                <img src="../assets/icons/collection/coin.png">
                                <p> {{ card.points_required }} </p>
                            </div>

                            <button 
                                v-if="userCards.includes(card.card_id)"
                                class="viewCardBtn" @click="openInfoPopup(card.card_id, card.description, card.recommendation)"> View 
                            </button>

                            <button 
                                v-else
                                class="bookEventBtn" @click="openUnlockPopup(card.title, card.points_required, card.card_id)"> Unlock 
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <Popup
        v-if="isPopupVisible"
        :visible="isPopupVisible"
        :type="popupType"
        :cardName="cardName"
        :cardPrice="cardPrice"
        :cardId="cardId"
        :errorMessage="errorMessage"
        :cardDescription="cardDesc"
        :cardRecommendation="cardRec"
        @close="closePopup"
        @unlock-card="unlockCard"
    />

</template>

<script>
import Popup from '@/components/popUp.vue';
import { useStore } from 'vuex';
import { computed } from 'vue';

export default {
    components: {
        Popup
    },
    data() {
        return {
            isPopupVisible: false,  // Controls popup visibility
            cardName: 'Strawberry Card',  // Example data
            cardPrice: 100,  // Example price
            cardId: '',
            cardDesc: '',
            cardRec: '',
            popupType: '',
            numHealthCoins: 0,
            numUnlocked: 0,
            numCards: 0,
            allCards: {},
            userCards: [],
            errorMessage: ''
        };
    },
    methods: {
        openUnlockPopup(cardName, cardPrice, cardId) {
            this.cardName = cardName;
            this.cardPrice = cardPrice;
            this.cardId = cardId;
            this.popupType = 'unlock';
            this.isPopupVisible = true;
        },
        closePopup() {
            this.isPopupVisible = false;
            this.errorMessage = ''; 
        },
        openInfoPopup(cardId, cardDesc, cardRec) {
            this.cardId = cardId;
            this.cardDesc = cardDesc;
            this.cardRec = cardRec;
            this.popupType = 'info';
            this.isPopupVisible = true;
        },
        async unlockCard(cardId) {
            console.log("unlocking card with ID:", cardId);

            try {
                const response = await this.$http.post("http://127.0.0.1:5006/usercard/buy", {
                    user_id: this.userId,
                    card_id: cardId
                })
                console.log(response);
                console.log("unlock card successful");

                // refresh user cards and points
                await this.fetchUserData();
                await this.fetchUserCards();

                this.isPopupVisible = false;
            }
            catch (error) {
                console.log("Unlock Card:", error);
                let responseError = error.response.data.error;
                console.log(responseError);
                if (responseError == "Insufficient HealthCoins to buy this card") {
                    this.errorMessage = "Insufficient HealthCoins to buy this card";
                }
                else {
                    this.errorMessage = "Failed to join the event. Please try again.";
                }  
            }
        },
        // Fetch user data
        async fetchUserData() {
            try {
                const userReponse = await this.$http.get("http://127.0.0.1:5001/user/" + this.userEmail);
                const userData = userReponse.data.data;
                this.numHealthCoins = userData["total_point"];
            } catch (error) {
                console.error("Error fetching user data:", error);
            }
        },
        // Fetch user cards
        async fetchUserCards() {
            try {
                const userCardResponse = await this.$http.get("http://127.0.0.1:5006/usercard/user/" + this.userId);
                const userCardData = userCardResponse.data.data;
                
                this.userCards = userCardData["cards"].map(card => card["card_id"]);
                this.numUnlocked = userCardData["count_redeemed"];
            } catch (error) {
                console.error("Error fetching user cards:", error);
            }
        },
        async fetchAllCards() {
            const cardReponse = await this.$http.get("http://127.0.0.1:5003/cards");
            const cardData = cardReponse.data;
            for (let i = 0; i < cardData.length; i++) {
                let card_type = cardData[i]["card_type"];
                if (!this.allCards[card_type]) {
                    this.allCards[card_type] = [];
                }
                this.allCards[card_type].push(cardData[i]);
            }
            this.numCards = cardData.length;
        },
        getCardImage(card_title, card_set) {
            if (!card_title || !card_set) {
                console.error("Invalid card_title or card_set:", card_title, card_set);
                return ;
            }

            const formattedTitle = card_title.toLowerCase().replace(/\s+/g, "_");
            // console.log(formattedTitle);
            const formattedSetName = card_set.toLowerCase().replace(/\s+/g, "_");
            return require(`@/assets/icons/collection/${formattedSetName}/${formattedTitle}.png`);
        },
    },
    setup() {
        console.log("store page");
        const store = useStore(); // Import useStore from vuex
        const userId = computed(() => store.state.userId); // Access userId from the store
        const userEmail = computed(() => store.state.userEmail) // Access userEmail from the store
        
        console.log(userEmail.value);
        
        return {
            userId,
            userEmail
        };
    },
    async mounted() {
        try {
            this.fetchUserData();
            this.fetchAllCards();
            this.fetchUserCards(); 
        }
        catch (error) {
            console.log("error:", error);

            this.numUnlocked = 0;
            
        }
    }
};
</script>

<style scoped>
.pageHeader {
    background-color: var(--orange);
    color: var(--default-white)
}

.stickyHeader {
    background-color: var(--grey);
    padding-bottom: 1px;
}

.stickyHeader .displayBlock {
    align-items: center;
    justify-content: center;
}

.displayBlock {
    display: flex;
    width: 80%;
    margin: auto;
    padding-top: 16px;
}

.blockLeft, .blockRight {
    flex: 1;
    display: flex;
    flex-direction: column;
    background-color: var(--default-white);
    align-items: center;
    text-align: center;
    padding: 10px;
    min-height: 70px;
}

.blockLeft {
    border-right: 1px solid var(--grey-highlight);
    border-radius: 6px 0 0 6px;
}

.blockRight {
    border-radius: 0 6px 6px 0;
}

.blockLeft p, .blockRight p {
    font-family: text-medium;
    font-size: 13px;
    color: var(--default-text);
    margin: 0;
}

.blockText {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
}

.blockText p, .blockText span {
    font-family: text-bold;
    font-size: 17px;
    color: var(--default-text);
    margin: 0;
}

.blockText img, .card .price img {
    width: 20px;
    height: 20px;
    display: flex;
    align-items: center;
}

.info {
    font-family: text-regular;
    font-size: 13px;
    color: var(--default-text);
    text-align: center;
    padding: 16px 0 20px 0;
}

div .search-bar {
    width: 100%;
    display: flex;
    justify-content: center;
}

.pagePad {
    padding: 0 32px;
    padding-bottom: 60px;
}

.head {
    display: flex;
    justify-content: space-between;
    padding: 30px 0 0 0;
}

.head p, .set p {
    margin: 0;
    font-family: text-bold;
    font-size: 16px;
    color: var(--default-text);
}

.set p {
    color: var(--text-highlight);
}

.set {
    padding-bottom: 16px;
}

button {
    all: unset;
    padding: 11px 24px;
    border-radius: 6px;
    color: var(--default-white);
}

button label {
    margin-right: 5px;
}

.tradeButton {
    background: linear-gradient(180deg, #814FF0, #462D7F);
}

.card {
    display: flex;
    flex: 0 0 auto;
    align-items: center;
    padding: 16px 0;
    border-radius: 10px;
    border: none;
    width: 130px;
}

.cardName {
    font-family: text-bold;
    font-size: 12px;
    color: var(--default-text);
    text-align: center;
    margin-bottom: 0;
}

.card img {
    width: 65px;
    height: auto;
    margin: 5px 0 0 0;
}

.price {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 5px 0;
}

.price img {
    margin: 0;
}

.price p {
    font-family: text-bold;
    font-size: 12px;
    color: var(--text-highlight);
    margin-bottom: 0;
}

.card .bookEventBtn {
    font-family: text-medium;
    color: var(--grey);
    font-size: 10px;
    background-color: var(--green);
    border-radius: 5px;
    border: none;
    padding: 5px 10px;
    width: 85px;
    text-align: center;
}

.card .viewCardBtn {
    font-family: text-medium;
    color: var(--grey);
    font-size: 10px;
    background-color: var(--blue);
    border-radius: 5px;
    border: none;
    padding: 5px 10px;
    width: 85px;
    text-align: center;
}

.card-owned {
    background-color: #D8D8D5;
}

</style>