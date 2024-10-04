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

        <div class="pagePad">
            <div class="pageHeading">
                <img src="../assets/icons/homepage/goal.png">
                <div class="headerText">
                    <p class="head"> My next steps </p>
                    <p class="body"> {{ currentProgress }} minutes / {{ goalProgress }} minutes </p>
                </div>
            </div>

            <div class="pagePad">
                <div class="card">
                    <n-space vertical>
                        <n-progress
                            type="line"
                            :percentage="progressPercentage"
                            :height="20"
                            :border-radius="6"
                            :fill-border-radius="0"
                            :show-indicator="false"
                        />
                    </n-space>
                </div>
            </div>



            <div class="pageHeading">
                <img src="../assets/icons/homepage/progress.png">
                <p> My Daily Progress </p>
            </div>



            <div class="pageHeading">
                <img src="../assets/icons/homepage/glass.png">
                <div class="headerText">
                    <p class="head"> My H365 Unwrapped </p>
                    <p class="body"> Take a look at your progress in {{ lastMonth }} </p>
                </div>
            </div>



            <div class="pageHeading">
                <img src="../assets/icons/homepage/bulb.png">
                <div class="headerText">
                    <p class="head"> My next steps </p>
                    <p class="body"> Personalised tips to reach your health goals </p>
                </div>
            </div>

        </div>
        
    </div>



</template>

<script>
export default {
    data() {
        return {
            streakCount: 5,
            currentProgress: 75,
            goalProgress: 150,
            lastMonth: "August"
        }
    },

    computed: {
        progressPercentage() {
            if (this.goalProgress > 0) {
                return (this.currentProgress / this.goalProgress) * 100;
            }
            return 0;
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


.pageHeading {
    display: flex;
    align-items: center;
}

.pageHeading img {
    width: 40px;
    height: 40px;
}

.pageHeading p, .headerText .head {
    font-family: text-semibold;
    font-size: 16px;
    color: var(--default-text);
}

.headerText .body {
    font-family: text-medium;
    font-size: 13px;
    color: var(--text-highlight);
}

</style>