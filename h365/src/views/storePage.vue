<template>
    <div class="stickyHeader">
        <div class="pageHeader">
            <p> Store </p>
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

        <div class="set">
            <p> Fruit Basket </p>
            <div class="carousel">
                <div class="card">
                    <p class="cardName"> Oliver </p>
                    <img src="../assets/icons/collection/fruit_basket/oliver_orange.png">
                    <div class="price">
                        <img src="../assets/icons/collection/coin.png">
                        <p> 200 </p>
                    </div>
                    <button class="bookEventBtn" @click="openUnlockPopup('Oliver', '200')"> Unlock </button>
                </div>

                <div class="card">
                    <p class="cardName"> Oliver </p>
                    <img src="../assets/icons/collection/fruit_basket/oliver_orange.png">
                    <div class="price">
                        <img src="../assets/icons/collection/coin.png">
                        <p> 200 </p>
                    </div>
                    <button class="bookEventBtn" @click="openUnlockPopup('Oliver', '200')"> Unlock </button>
                </div>

                <div class="card">
                    <p class="cardName"> Oliver </p>
                    <img src="../assets/icons/collection/fruit_basket/oliver_orange.png">
                    <div class="price">
                        <img src="../assets/icons/collection/coin.png">
                        <p> 200 </p>
                    </div>
                    <button class="bookEventBtn" @click="openUnlockPopup('Oliver', '200')"> Unlock </button>
                </div>

                <div class="card">
                    <p class="cardName"> Oliver </p>
                    <img src="../assets/icons/collection/fruit_basket/oliver_orange.png">
                    <div class="price">
                        <img src="../assets/icons/collection/coin.png">
                        <p> 200 </p>
                    </div>
                    <button class="bookEventBtn" @click="openUnlockPopup('Oliver', '200')"> Unlock </button>
                </div>

                <div class="card">
                    <p class="cardName"> Oliver </p>
                    <img src="../assets/icons/collection/fruit_basket/oliver_orange.png">
                    <div class="price">
                        <img src="../assets/icons/collection/coin.png">
                        <p> 200 </p>
                    </div>
                    <button class="bookEventBtn" @click="openUnlockPopup('Oliver', '200')"> Unlock </button>
                </div>
            </div>
        </div>

        <div class="set">
            <p> Fruit Basket </p>
            <div class="carousel">
                <div class="card">
                    <p class="cardName"> Oliver </p>
                    <img src="../assets/icons/collection/fruit_basket/oliver_orange.png">
                    <div class="price">
                        <img src="../assets/icons/collection/coin.png">
                        <p> 200 </p>
                    </div>
                    <button class="bookEventBtn" @click="openUnlockPopup('Oliver', '200')"> Unlock </button>
                </div>

                <div class="card">
                    <p class="cardName"> Oliver </p>
                    <img src="../assets/icons/collection/fruit_basket/oliver_orange.png">
                    <div class="price">
                        <img src="../assets/icons/collection/coin.png">
                        <p> 200 </p>
                    </div>
                    <button class="bookEventBtn" @click="openUnlockPopup('Oliver', '200')"> Unlock </button>
                </div>

                <div class="card">
                    <p class="cardName"> Oliver </p>
                    <img src="../assets/icons/collection/fruit_basket/oliver_orange.png">
                    <div class="price">
                        <img src="../assets/icons/collection/coin.png">
                        <p> 200 </p>
                    </div>
                    <button class="bookEventBtn" @click="openUnlockPopup('Oliver', '200')"> Unlock </button>
                </div>

                <div class="card">
                    <p class="cardName"> Oliver </p>
                    <img src="../assets/icons/collection/fruit_basket/oliver_orange.png">
                    <div class="price">
                        <img src="../assets/icons/collection/coin.png">
                        <p> 200 </p>
                    </div>
                    <button class="bookEventBtn" @click="openUnlockPopup('Oliver', '200')"> Unlock </button>
                </div>

                <div class="card">
                    <p class="cardName"> Oliver </p>
                    <img src="../assets/icons/collection/fruit_basket/oliver_orange.png">
                    <div class="price">
                        <img src="../assets/icons/collection/coin.png">
                        <p> 200 </p>
                    </div>
                    <button class="bookEventBtn" @click="openUnlockPopup('Oliver', '200')"> Unlock </button>
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
        @close="closePopup"
    />

</template>

<script>
import Popup from '@/components/popUp.vue';

export default {
    components: {
        Popup
    },
    data() {
        return {
            isPopupVisible: false,  // Controls popup visibility
            cardName: 'Strawberry Card',  // Example data
            cardPrice: '100',  // Example price
            popupType: ''
        };
    },
    methods: {
        openUnlockPopup(cardName, cardPrice) {
            this.cardName = cardName;
            this.cardPrice = cardPrice;
            this.popupType = 'unlock';
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
    width: 30px;
    height: 30px;
    vertical-align: middle;
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

.carousel {
    display: flex;
    overflow-x: auto; /* Enable horizontal scroll */
    gap: 16px; /* Spacing between cards */
    padding: 10px; /* Add some padding around the carousel */
    scroll-snap-type: x mandatory; /* Optional: for snap scrolling */
    scrollbar-width: thin; /* Firefox scrollbar */
}

.carousel::-webkit-scrollbar {
    height: 8px; /* Adjust height of the scrollbar */
}

.carousel::-webkit-scrollbar-thumb {
    background-color: var(--grey); /* Color of scrollbar thumb */
    border-radius: 10px;
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

</style>