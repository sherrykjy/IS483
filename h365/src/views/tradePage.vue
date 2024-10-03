<template>
    <div class="stickyHeader">
        <div class="pageHeader">
            <i class="uil uil-angle-left"></i>
            <p> Trade </p>
        </div>

        <n-tabs type="line" class="pageTab">
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
            <input type="text" placeholder="Search by card, set, or user" />
        </div>

        <div class="card">
            <div class="cardTop">
                <div class="tradeInfo">
                    <p class="head"> Trade Request </p>
                    <p class="body"> Alice Tan </p>
                </div>

                <div class="acceptBtn" @click="openTradePopup('Williams', 'Selena', 'Alice Tan')">
                    <p> Accept </p>
                    <i class="uil uil-thumbs-up"></i>
                </div>
            </div>

            <div class="divider"></div>

            <div class="cardBottom">
                <div class="offer">
                    <div class="card" @click="openInfoPopup('Williams', 'Weekend Action', 'Description of Williams', '../assets/icons/collection/weekend_action/williams.png')">
                        <p class="head"> Offering Up </p>
                        <img src="../assets/icons/collection/weekend_action/williams.png">
                        <p class="cardName"> Williams </p>
                        <p class="cardSet"> Weekend Action </p>
                    </div>
                </div>

                <i class="uil uil-exchange"></i>

                <div class="receive">
                    <div class="card" @click="openInfoPopup('Selena', 'Fruit Basket', 'Description of Selena', '../assets/icons/collection/fruit_basket/selena_strawberry.png')">
                        <p class="head"> Requesting For </p>
                        <img src="../assets/icons/collection/fruit_basket/selena_strawberry.png">
                        <p class="cardName"> Selena </p>
                        <p class="cardSet"> Fruit Basket </p>
                    </div>
                </div>
            </div>
        </div>

        <div class="card">
            <div class="cardTop">
                <div class="tradeInfo">
                    <p class="head"> Trade Request </p>
                    <p class="body"> Alice Tan </p>
                </div>

                <div class="acceptBtn" @click="openTradePopup('Williams', 'Selena', 'Alice Tan')">
                    <p> Accept </p>
                    <i class="uil uil-thumbs-up"></i>
                </div>
            </div>

            <div class="divider"></div>

            <div class="cardBottom">
                <div class="offer">
                    <div class="card" @click="openInfoPopup('Williams', 'Weekend Action', 'Description of Williams', '../assets/icons/collection/weekend_action/williams.png')">
                        <p class="head"> Offering Up </p>
                        <img src="../assets/icons/collection/weekend_action/williams.png">
                        <p class="cardName"> Williams </p>
                        <p class="cardSet"> Weekend Action </p>
                    </div>
                </div>

                <i class="uil uil-exchange"></i>

                <div class="receive">
                    <div class="card" @click="openInfoPopup('Selena', 'Fruit Basket', 'Description of Selena', '../assets/icons/collection/fruit_basket/selena_strawberry.png')">
                        <p class="head"> Requesting For </p>
                        <img src="../assets/icons/collection/fruit_basket/selena_strawberry.png">
                        <p class="cardName"> Selena </p>
                        <p class="cardSet"> Fruit Basket </p>
                    </div>
                </div>
            </div>
        </div>

        <div class="card">
            <div class="cardTop">
                <div class="tradeInfo">
                    <p class="head"> Trade Request </p>
                    <p class="body"> Alice Tan </p>
                </div>

                <div class="acceptBtn" @click="openTradePopup('Williams', 'Selena', 'Alice Tan')">
                    <p> Accept </p>
                    <i class="uil uil-thumbs-up"></i>
                </div>
            </div>

            <div class="divider"></div>

            <div class="cardBottom">
                <div class="offer">
                    <div class="card" @click="openInfoPopup('Williams', 'Weekend Action', 'Description of Williams', '../assets/icons/collection/weekend_action/williams.png')">
                        <p class="head"> Offering Up </p>
                        <img src="../assets/icons/collection/weekend_action/williams.png">
                        <p class="cardName"> Williams </p>
                        <p class="cardSet"> Weekend Action </p>
                    </div>
                </div>

                <i class="uil uil-exchange"></i>

                <div class="receive">
                    <div class="card" @click="openInfoPopup('Selena', 'Fruit Basket', 'Description of Selena', '../assets/icons/collection/fruit_basket/selena_strawberry.png')">
                        <p class="head"> Requesting For </p>
                        <img src="../assets/icons/collection/fruit_basket/selena_strawberry.png">
                        <p class="cardName"> Selena </p>
                        <p class="cardSet"> Fruit Basket </p>
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
            @close="closePopup"
        />

    </div>

    <div class="bookNowContainer">
        <button class="bookButton"> New Trade Request </button>
    </div>

</template>

<script>
import Popup from '@/components/popUp.vue';

export default {
    components: {
        Popup
    },
    data() {
        return {
            isPopupVisible: false,
            tradeCardName: 'Card A',  // Example data
            receiveCardName: 'Card B',  // Example data
            tradeWith: 'User123'  // Example data
        };
    },
    methods: {
        openTradePopup(tradeCardName, receiveCardName, tradeWith) {
            this.tradeCardName = tradeCardName;
            this.receiveCardName = receiveCardName;
            this.tradeWith = tradeWith;
            this.popupType = 'trade';
            this.isPopupVisible = true;
        },
        closePopup() {
            this.isPopupVisible = false;
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