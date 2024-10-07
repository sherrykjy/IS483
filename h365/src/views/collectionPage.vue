<template>
    <div class="stickyHeader">
        <div class="pageHeader">
            <p> My Collectibles </p>
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
                    <p> <span> {{ userCards.length }} </span> / {{ numCards }} </p>
                </div>
                <p> Collectibles Unlocked </p>
            </div>
        </div>

        <div class="buttonGroup">
            <router-link :to="{ name: 'storePage'}">
                <button class="storeButton">
                    <label> Store </label>
                    <i class="uil uil-store"> </i>
                </button>
            </router-link>

            <router-link :to="{ name: 'tradePage'}">
                <button class="tradeButton">
                    <label> Trade </label>
                    <i class="uil uil-exchange"> </i>
                </button>
            </router-link>
        </div>
    </div>

    <div class="pagePad">
        <div class="search-bar">
            <i class="uil uil-search"></i>
            <input type="text" placeholder="Search by card or set" />
        </div>

        <div class="colDisplay">
            <div v-for="card in userCards" 
                :key="card.card_id"
                class="card"
                @click="openInfoPopup(card.description, card.recommendation)"
            >
                <img :src="getCardImage(card.title, card.card_type)" />
                <p class="cardName"> {{ card.title }} </p>
                <p class="cardSet"> {{ card.card_type }} </p>
            </div>

        </div>
        
        <!-- info pop up -->
        <Popup
            ref="popup"
            :visible="isPopupVisible"
            :type="popupType"
            :cardDescription="selectedCardDescription"
            :cardRecommendation="selectedCardRecommendation"
            @close="closePopup"
        />
    </div>
    
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
            isPopupVisible: false,
            popupType: '', // 'unlock', 'trade', 'info', 'event-code'
            selectedCardName: '',
            selectedCardImage: '',
            selectedCardSet: '',
            selectedCardDescription: '',
            selectedCardRecommendation: '',
            userCards: [],
            numCards: 0,
            numHealthCoins: 0
        };
    },
    methods: {
        async fetchUserCards() {
            try {
                const response = await fetch("http://127.0.0.1:5006/usercard/user/" + this.userId);
                const data = await response.json();
                // console.log(data);

                if (data && data.data && data.data.cards) {
                    this.userCards = data.data.cards;
                    console.log(this.userCards);
                } else {
                    console.log("No cards found for this user.")
                }
            } catch (error) {
                console.error("Error fetching user cards:" + error);
            }
        },
        async fetchAllCards() {
            try {
                const cardReponse = await this.$http.get("http://127.0.0.1:5003/cards");
                const cardData = cardReponse.data;
                this.numCards = cardData.length;
            } catch (error) {
                console.error("Error fetching all cards:" + error);
            }
        },
        async fetchUserData() {
            try {
                const userReponse = await this.$http.get("http://127.0.0.1:5001/user/" + this.userEmail);
                const userData = userReponse.data.data;
                this.numHealthCoins = userData["total_point"];
            } catch (error) {
                console.log("Error fetching user data:" + error);
            }
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
        openInfoPopup(cardDescription, cardRecommendation) {
            this.selectedCardDescription = cardDescription;
            this.selectedCardRecommendation = cardRecommendation;
            this.popupType = 'info';
            this.isPopupVisible = true;
        },
        closePopup() {
            this.isPopupVisible = false;
        }
    },
    mounted() {
        this.fetchUserCards();
        this.fetchAllCards();
        this.fetchUserData();
    },
    setup() {
        console.log("collection page");
        const store = useStore(); // Import useStore from vuex
        const userId = computed(() => store.state.userId); // Access userId from the store
        const userEmail = computed(() => store.state.userEmail) // Access userEmail from the store
        
        console.log(userEmail.value);
        
        return {
            userId,
            userEmail
        };
    }
};
</script>

<style scoped>
.pageHeader {
    background-color: var(--green);
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

.buttonGroup {
    color: var(--default-white);
    font-family: text-bold;
    font-size: 15px;
    display: flex;
    justify-content: center;
    margin: 16px 0 20px 0;
    gap: 15px;
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

.storeButton {
    background: linear-gradient(180deg, #1C83E1, #0F4E87);
}

.tradeButton {
    background: linear-gradient(180deg, #814FF0, #462D7F);
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

.card {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 16px;
    border: none;
}

.card img {
    width: 130px;
}

.card p {
    margin-bottom: 2px;
}

.cardName {
    font-family: text-bold;
    font-size: 17px;
    color: var(--default-text);
    text-align: center;
    line-height: 17px;
}

.cardSet {
    font-family: text-bold;
    font-size: 13px;
    color: var(--orange);
}

.colDisplay {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    width: 100%;
    padding-top: 16px;
}

</style>