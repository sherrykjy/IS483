<template>
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
            <div class="card" @click="openPopup">
                <img src="../assets/icons/collection/fruit_basket/selena_strawberry.png">
                <p class="cardName"> Selena </p>
                <p class="cardSet"> Fruit Basket </p>
            </div>

            <div class="card" @click="openPopup">
                <img src="../assets/icons/collection/fruit_basket/gracia_grape.png">
                <p class="cardName"> Gracia </p>
                <p class="cardSet"> Fruit Basket </p>
            </div>

            <div class="card" @click="openPopup">
                <img src="../assets/icons/collection/wellness_wonders/sweat_squad.png">
                <p class="cardName"> Sweet Squad </p>
                <p class="cardSet"> Wellness Wonders </p>
            </div>

            <div class="card" @click="openPopup">
                <img src="../assets/icons/collection/wellness_wonders/hydration_hero.png">
                <p class="cardName"> Hydration Hero </p>
                <p class="cardSet"> Wellness Wonders </p>
            </div>

            <div class="card" @click="openPopup">
                <img src="../assets/icons/collection/wellness_wonders/cardio_champ.png">
                <p class="cardName"> Cardio Champ </p>
                <p class="cardSet"> Wellness Wonders </p>
            </div>

        </div>
        <Popup ref="popup" />

    </div>
    
</template>

<script>
import Popup from '@/components/popUp.vue';

export default {
    components: {
        Popup,
    },
    methods: {
        openPopup() {
            this.$refs.popup.show();
        },
    },
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

.blockText img {
    width: 30px;
    height: auto;
    vertical-align: middle;
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
    display: grid; /* Use CSS Grid for layout */
    grid-template-columns: repeat(2, 1fr); /* Create 2 equal columns */
    gap: 16px; /* Space between the cards */
    width: 100%; /* Optional: set the width of the container */
    padding-top: 16px;
}

</style>