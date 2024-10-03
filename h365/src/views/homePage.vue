<template>
    <div class="stickyHeader">
        <div class="pageHeader">
            <p> Welcome back, 
                <span> Sherry </span> 
            </p>
        </div>

        <div class="displayBlock">
            <div class="blockLeft">
                <div class="blockText">
                    <p style="margin-right: 5px"> 1080 </p>
                    <span> <img src="../assets/icons/homepage/coin.png"> </span>
                </div>
                <p> My Healthcoins </p>
            </div>

            <div class="blockRight">
                <div class="blockText">
                    <p> {{ streakCount }} day </p>
                    <img src="../assets/icons/homepage/streak.png" style="width: 25px; height: auto; margin-right: 3px;">
                </div>

                <div style="display: flex; align-items: center;">
                    <p style="margin-right: 3px"> Activity Streak </p>
                    <i class="uil uil-info-circle" style="display: flex; align-items: center;"></i>
                </div>
            </div>
        </div>
    </div>

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
</template>

<script>
export default {
    data() {
        return {
            streakCount: 5
        }
    }
}
</script>

<style scoped>
.pageHeader {
    background-color: var(--blue);
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
</style>