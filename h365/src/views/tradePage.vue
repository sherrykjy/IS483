<template>
    <div class="stickyHeader">
        <div class="pageHeader">
            <i class="uil uil-angle-left" @click="goBack"></i>
            <p> Trade </p>
        </div>

        <n-tabs v-model:value="selectedTab" type="line" class="pageTab">
            <n-tab name="allTrades">
                All
            </n-tab>
            <n-tab name="myTrades">
                My Trades
            </n-tab>
        </n-tabs>
    </div>

    <div class="pagePad">
        <div class="search-bar">
            <i class="uil uil-search"></i>
            <input type="text" v-model="searchInput" @input="searchTrades" placeholder="Search by card, set, or user" />
        </div>

        <div v-for="trade in filteredTradesData" :key="trade.trade_id">
            <div class="card">
                <div class="cardTop">
                    <div class="tradeInfo">
                        <p class="head"> Trade Request </p>
                        <p class="body"> {{ trade.name }} </p>
                    </div>
                    <div class="acceptBtn" @click="openTradePopup(trade.card_one_title, trade.card_two_title, trade.name, trade.trade_id)">
                        <p> Accept </p>
                        <i class="uil uil-thumbs-up"></i>
                    </div>
                </div>
                <div class="divider"></div>
                <div class="cardBottom">
                    <div class="offer">
                        <div class="card">
                            <p class="head"> Offering Up </p>
                            <img :src="getCardImage(trade.card_one_title, trade.card_one_type)" />
                            <p class="cardName"> {{ trade.card_one_title }} </p>
                            <p class="cardSet"> {{ trade.card_one_type }} </p>
                        </div>
                    </div>
                    <i class="uil uil-exchange"></i>
                    <div class="receive">
                        <div class="card">
                            <p class="head"> Requesting For </p>
                            <img :src="getCardImage(trade.card_two_title, trade.card_two_type)" />
                            <p class="cardName"> {{ trade.card_two_title }} </p>
                            <p class="cardSet"> {{ trade.card_two_type }} </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <Popup
            v-if="isPopupVisible"
            :visible="isPopupVisible"
            :type="popupType"
            :tradeCardName="tradeCardName"
            :receiveCardName="receiveCardName"
            :tradeWith="tradeWith"
            :tradeId="selectedTradeId"
            :errorMessage="errorMessage"
            @close="closePopup"
            @confirm="acceptTrade"
        />

    </div>

    <div class="bookNowContainer">
        <button class="bookButton"> New Trade Request </button>
    </div>

</template>

<script>
import { ref, watch, computed } from "vue";
import { useRouter } from 'vue-router';
import Popup from '@/components/popUp.vue';
import { useStore } from 'vuex';

export default {
    components: {
        Popup
    },
    setup() {
        console.log("all trades page");
        const selectedTab = ref('allTrades');
        const router = useRouter();
        const store = useStore(); // Import useStore from vuex
        const userId = computed(() => store.state.userId); // Access userId from the store
        const userEmail = computed(() => store.state.userEmail) // Access userEmail from the store

        watch(selectedTab, (newTab) => {
            if (newTab === 'allTrades') {
                router.push({ path: '/trade' });
            } else if (newTab === 'myTrades') {
                router.push({ path: '/mytrades' });
            }
        });

        return {
            selectedTab,
            userId,
            userEmail
        };
    },
    data() {
        return {
            isPopupVisible: false,
            tradeCardName: 'Card A',  // Example data
            receiveCardName: 'Card B',  // Example data
            tradeWith: 'User123',  // Example data
            selectedTradeId: '',
            trades: [],
            searchInput: '',
            searchResults: [],
            errorMessage: '',
            concurrentTradeFound: false,
            errorFound: false,
            selectedTradeData: null,
            userCards: null,
            userActiveTrade: null
        };
    },
    methods: {
        openInfoPopup(cardDescription, cardRecommendation) {
            this.selectedCardDescription = cardDescription;
            this.selectedCardRecommendation = cardRecommendation;
            this.popupType = 'info';
            this.isPopupVisible = true;
        },
        async openTradePopup(tradeCardName, receiveCardName, tradeWith, tradeId) {
            this.tradeCardName = tradeCardName;
            this.receiveCardName = receiveCardName;
            this.tradeWith = tradeWith;
            this.selectedTradeId = tradeId;
            this.popupType = 'trade';
            this.isPopupVisible = true;

            try {
                // FETCH REQUIRED INFORMATION
                // fetch trade information
                const tradeResponse = await this.$http.get("http://127.0.0.1:5013/trade/" + tradeId);
                this.selectedTradeData = tradeResponse.data;
                console.log(this.selectedTradeData);

                // fetch user's active trade requests
                const userTradeResponse = await this.$http.get("http://127.0.0.1:5013/trade/user/" + this.userId);
                this.userActiveTrade = userTradeResponse.data.data[0];
                console.log("trade for signed-in user:", this.userActiveTrade);

                // fetch user's card information
                const userTwoResponse = await this.$http.get("http://127.0.0.1:5006/usercard/user/" + this.userId);
                this.userCards = userTwoResponse.data.data.cards;

                // START OF VALIDATION & ERROR HANDLING
                // validate against card involved in trade
                if (this.userActiveTrade.card_one_id == this.selectedTradeData.card_two_id) {
                    this.errorMessage = "Warning: You have a concurrent listing that will be deleted. Please click Confirm to proceed.";
                    this.concurrentTradeFound = true;
                }

                // error handling: when trade request selected is user's own request
                if (this.selectedTradeData.user_id == this.userId) {
                    this.errorMessage = "Unable to accept trade request with yourself. Please select a different trade request.";
                    this.errorFound = true;
                    return;
                }

                // validate cards in trade
                const userTwoRequestedCard = this.userCards.find(card => card.card_id == this.selectedTradeData.card_one_id);
                const userTwoTargetCard = this.userCards.find(card => card.card_id == this.selectedTradeData.card_two_id);

                // error handling: user two already owns the card being offered
                if (userTwoRequestedCard) {
                    this.errorMessage = "You already own the offered collectible. Please select a different trade request.";
                    this.errorFound = true;
                    return;
                }

                // error handling: user two does not have the card being requested
                if (userTwoTargetCard === undefined) {
                    this.errorMessage = "You do not have the requested collectible in your collection."
                    this.errorFound = true;
                    return;
                }

            } catch (error) {
                console.log("error in popup");
            }
        },
        closePopup() {
            this.isPopupVisible = false;
            this.errorMessage = '';
            this.concurrentTradeFound = false;
            this.errorFound = false;
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
        goBack() {
            this.$router.go(-1);
        },
        async fetchAllTrades() {
            try {
                const response = await this.$http.get("http://127.0.0.1:5013/active_trades");
                console.log(response.data.data);
                this.trades = response.data.data;
            } catch (error) {
                console.log("Error fetching trades:" + error);
            }
        },
        async searchTrades() {
            console.log("checking search input:", this.searchInput);
            try {
                const url = "http://127.0.0.1:5013/trade/search";
                const params = {};
                params.search_input = this.searchInput;

                const response = await this.$http.get(url, { params });
                console.log("response:", response);

                if (response.status === 200) {
                    console.log("returning search results");
                    console.log(response.data.data);
                    this.searchResults = response.data.data;
                }
            } catch (error) {
                console.log("Error in searching for trades:" + error);
            }
        },
        async acceptTrade(tradeId) {
            console.log("trade id accepted:", tradeId);
            try {
                // no errors above, proceed with processing trade & swapping of cards
                if (!this.errorFound) {
                    // user one card information
                    const userOneResponse = await this.$http.get("http://127.0.0.1:5006/usercard/user/" + this.selectedTradeData.user_id);
                    const userOneCards = userOneResponse.data.data.cards;
                    console.log(userOneCards);
                    const userOneTargetCard = userOneCards.find(card => card.card_id == this.selectedTradeData.card_one_id);

                    // error handling: other user does not have the card they are offering
                    if (userOneTargetCard === undefined) {
                        this.errorMessage = "There is an error in processing this trade. Please try again later.";
                        console.log("user one does not have offered card");
                        return;
                    }
                    const user_card_id_one = userOneTargetCard.user_card_id;

                    // user two card information
                    const userTwoTargetCard = this.userCards.find(card => card.card_id == this.selectedTradeData.card_two_id);
                    const user_card_id_two = userTwoTargetCard.user_card_id;

                    // console.log(user_card_id_one);
                    // console.log(user_card_id_two);

                    // process trade & swap cards
                    const processTradeResponse = await this.$http.post("http://127.0.0.1:5015/trade_card", {
                        trade_id: tradeId,
                        user_card_id_one: user_card_id_one,
                        user_id_one: this.selectedTradeData.user_id,
                        card_id_one: this.selectedTradeData.card_one_id,
                        user_card_id_two: user_card_id_two,
                        user_id_two: this.userId,
                        card_id_two: this.selectedTradeData.card_two_id
                    });
                    console.log(processTradeResponse);

                    // delete if concurrent trade found
                    if (this.concurrentTradeFound) {
                        console.log("perform deletion of concurrent trade");
                        const tradeToDelete = this.userActiveTrade.trade_id;
                        const deleteTradeResponse = await this.$http.delete("http://127.0.0.1:5013/trade/" + tradeToDelete)
                        console.log(deleteTradeResponse);
                    }

                    await this.fetchAllTrades();
                    this.isPopupVisible = false;
                    this.$router.push('/collection');

                } else {
                    console.log("errors found, skipping swapping of cards");
                }

            } catch (error) {
                // error handling: in db changes while processing trade
                console.log("Error in processing trade:" + error);
            }

        }
    },
    mounted() {
        this.fetchAllTrades();
    },
    computed: {
        filteredTradesData() {
            if (this.searchInput) {
                console.log("returning filtered data");
                console.log("filtered trades:", this.searchResults);
                return this.searchResults || [];
            } else {
                return this.trades;
            }
        }
    }
};
</script>

<style scoped>
.pageHeader {
    background-color: var(--purple);
    color: var(--default-white);
}

.stickyHeader {
    background-color: var(--grey);
}

div .search-bar {
    width: 100%;
    display: flex;
    justify-content: center;
}

.pagePad {
    padding: 0 32px 100px 32px;
}

.card {
    border: none;
    padding: 16px;
    margin-top: 16px;
    border-radius: 6px;
}

.card .cardTop {
    border-radius: 6px 6px 0 0;
    background-color: var(--default-white);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.tradeInfo .head {
    font-family: text-bold;
    font-size: 15px;
    color: var(--default-text);
    margin: 0;
}

.cardBottom .head {
    font-family: text-bold;
    font-size: 13px;
    color: var(--default-text);
    margin: 0;
}

.tradeInfo .body {
    font-family: text-bold;
    font-size: 12px;
    color: var(--text-highlight);
    margin: 0;
}

.acceptBtn {
    display: flex;
    gap: 5px;
    font-family: text-medium;
    color: var(--grey);
    font-size: 10px;
    background-color: var(--green);
    border-radius: 5px;
    border: none;
    padding: 5px 10px;
}

.acceptBtn p {
    margin: 0;
}

.divider {
    width: 100%;
    height: 1px;
    background-color: var(--grey);
    margin: 10px 0;
}

.offer .card, .receive .card {
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

.cardBottom .cardName {
    font-family: text-bold;
    font-size: 12px;
    color: var(--default-text);
    text-align: center;
    line-height: 17px;
    margin: 0;
}

.cardBottom .cardSet {
    font-family: text-bold;
    font-size: 12px;
    color: var(--orange);
    margin: 0;
}

.cardBottom i {
    font-size: 30px;
}

.cardBottom {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.offer, .receive {
    flex: 1;
    display: flex;
    justify-content: center;
}

.offer .card, .receive .card {
    margin: 0;
}

.cardBottom .card {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 8px;
    padding: 10px;
}

.cardBottom .card img {
    width: 100%;
    max-width: 150px;
    height: auto;
}


.bookButton {
    background: linear-gradient(180deg, #D28269, #DB4B1E);
    /* background-color: var(--red); */
    color: var(--grey);
    font-family: text-medium;
    font-size: 13px;
    border: none;
    width: 100%;
    padding: 16px 0px;
    position: fixed;
    bottom: 81.75px;
}

.bookNowContainer {
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.25);
    z-index: 10;
}

</style>