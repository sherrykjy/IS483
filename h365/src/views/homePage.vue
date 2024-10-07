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

    <div class="pagePad">
        <div class="pageHeading">
            <img src="../assets/icons/homepage/goal.png">
            <div class="headerText">
                <p class="head"> My Weekly Progress </p>
                <p class="body"> Keep pushing towards your goals! </p>
            </div>
        </div>

        <div class="container">
            <div class="basicCard">
                <div class="barLabel">
                    <span class="updatedVar"> {{ currentWeekly }} / {{ goalWeekly }} </span>
                    <span class="updatedText"> minutes of MVPA </span>
                </div>

                <div class="bar">
                    <n-space vertical>
                        <n-progress
                            type="line"
                            :percentage="progressPercentage"
                            :height="20"
                            :border-radius="6"
                            :fill-border-radius="0"
                            :show-indicator="false"
                            color="#FFCE49"
                        />
                    </n-space>
                </div>

                <div class="updateDetails">
                    <button class="syncButton"> Sync now </button>
                </div>
            </div>

        </div>


        <div class="pageHeading">
            <img src="../assets/icons/homepage/progress.png">
            <div class="headerText">
                <p class="head"> My Daily Progress </p>
                <p class="body"> Stay focused and keep moving forward! </p>
            </div>
        </div>

        <div class="container">
            <div class="basicCard">
                <div class="barLabel" style="padding-bottom: 16px;">
                    <span class="updatedText"> You have worked out for </span>
                    <span class="updatedVar" style="color: var(--purple)"> {{ minutesToday }} </span>
                    <span class="updatedText"> minutes today! </span>
                </div>
            </div>
        </div>


        <div class="pageHeading">
            <img src="../assets/icons/homepage/glass.png">
            <div class="headerText">
                <p class="head"> My H365 Unwrapped </p>
                <p class="body"> Take a look at your progress </p>
            </div>
        </div>

        <div class="container">
            <div class="basicCard">

                <div class="pageHeading">
                    <span style="font-family: text-medium; color: var(--text-highlight); 
                    font-size: 13px; text-align: justify;"> 
                        You moved for a total of 
                        <span style="font-family: text-bold; color: var(--green)"> {{ mr_movingMinutes }} </span>
                        minutes in 
                        <span style="color: var(--orange)"> {{ lastMonth }} </span>
                    </span>
                </div>

                <router-link :to="{ name: 'monthlyReport'}">
                    <button class="syncButton"> View your {{ lastMonth }} report </button>
                </router-link>

                

            </div>
        </div>


        <div class="pageHeading">
            <img src="../assets/icons/homepage/bulb.png">
            <div class="headerText">
                <p class="head"> My next steps </p>
                <p class="body"> Personalised tips to reach your health goals </p>
            </div>
        </div>

        <div class="container">
            <div class="carousel">
                
                <!-- v-for however many events there are -->
                <div class="card drop-shadow">
                    <div class="cardImage">
                        <img src="../assets/icons/homepage/nextSteps.png">
                    </div>

                    <div class="cardText">
                        <!-- v-if few slots left -->
                        <div class="lowSlotAlert">
                            Event near you
                        </div>

                        <!-- activity name -->
                        <p class="eventName"> Bedok Walkers </p>

                        <!-- date, day, and time  -->
                        <div class="eventInfo">
                            <div class=eventDetails>
                                <p> 14 September 2024 </p>
                                <p> 10.00am - 11.00am </p>
                            </div>
                        </div>

                        <!-- location -->
                        <div class="eventInfo">
                            <div class=eventDetails>
                                <p> BEDOK, Asia Green </p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card drop-shadow">
                    <div class="cardImage">
                        <img src="../assets/icons/homepage/nextSteps.png">
                    </div>

                    <div class="cardText">
                        <!-- v-if few slots left -->
                        <div class="lowSlotAlert">
                            Event near you
                        </div>

                        <!-- activity name -->
                        <p class="eventName"> Bedok Walkers </p>

                        <!-- date, day, and time  -->
                        <div class="eventInfo">
                            <div class=eventDetails>
                                <p> 14 September 2024 </p>
                                <p> 10.00am - 11.00am </p>
                            </div>
                        </div>

                        <!-- location -->
                        <div class="eventInfo">
                            <div class=eventDetails>
                                <p> BEDOK, Asia Green </p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card drop-shadow">
                    <div class="cardImage">
                        <img src="../assets/icons/homepage/nextSteps.png">
                    </div>

                    <div class="cardText">
                        <!-- v-if few slots left -->
                        <div class="lowSlotAlert">
                            Event near you
                        </div>

                        <!-- activity name -->
                        <p class="eventName"> Bedok Walkers </p>

                        <!-- date, day, and time  -->
                        <div class="eventInfo">
                            <div class=eventDetails>
                                <p> 14 September 2024 </p>
                                <p> 10.00am - 11.00am </p>
                            </div>
                        </div>

                        <!-- location -->
                        <div class="eventInfo">
                            <div class=eventDetails>
                                <p> BEDOK, Asia Green </p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card drop-shadow">
                    <div class="cardImage">
                        <img src="../assets/icons/homepage/nextSteps.png">
                    </div>

                    <div class="cardText">
                        <!-- v-if few slots left -->
                        <div class="lowSlotAlert">
                            Event near you
                        </div>

                        <!-- activity name -->
                        <p class="eventName"> Bedok Walkers </p>

                        <!-- date, day, and time  -->
                        <div class="eventInfo">
                            <div class=eventDetails>
                                <p> 14 September 2024 </p>
                                <p> 10.00am - 11.00am </p>
                            </div>
                        </div>

                        <!-- location -->
                        <div class="eventInfo">
                            <div class=eventDetails>
                                <p> BEDOK, Asia Green </p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card drop-shadow">
                    <div class="cardImage">
                        <img src="../assets/icons/homepage/nextSteps.png">
                    </div>

                    <div class="cardText">
                        <!-- v-if few slots left -->
                        <div class="lowSlotAlert">
                            Event near you
                        </div>

                        <!-- activity name -->
                        <p class="eventName"> Bedok Walkers </p>

                        <!-- date, day, and time  -->
                        <div class="eventInfo">
                            <div class=eventDetails>
                                <p> 14 September 2024 </p>
                                <p> 10.00am - 11.00am </p>
                            </div>
                        </div>

                        <!-- location -->
                        <div class="eventInfo">
                            <div class=eventDetails>
                                <p> BEDOK, Asia Green </p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="card drop-shadow">
                    <div class="cardImage">
                        <img src="../assets/icons/homepage/nextSteps.png">
                    </div>

                    <div class="cardText">
                        <!-- v-if few slots left -->
                        <div class="lowSlotAlert">
                            Event near you
                        </div>

                        <!-- activity name -->
                        <p class="eventName"> Bedok Walkers </p>

                        <!-- date, day, and time  -->
                        <div class="eventInfo">
                            <div class=eventDetails>
                                <p> 14 September 2024 </p>
                                <p> 10.00am - 11.00am </p>
                            </div>
                        </div>

                        <!-- location -->
                        <div class="eventInfo">
                            <div class=eventDetails>
                                <p> BEDOK, Asia Green </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
        
    </div>



</template>

<script>
import { useStore } from 'vuex';
import { computed } from 'vue';

export default {
    setup() {
        console.log("home page");
        const store = useStore(); // Import useStore from vuex
        const userId = computed(() => store.state.userId); // Access userId from the store
        const userEmail = computed(() => store.state.userEmail) // Access userEmail from the store
        console.log(userId.value);
        console.log(userEmail.value);
        return {
            userId,
            userEmail
        };
    },
    data() {
        return {
            streakCount: 5,
            currentWeekly: 75,
            goalWeekly: 150,
            minutesToday: 30,
            mr_movingMinutes: 180,
            lastMonth: "August"
        }
    },

    computed: {
        progressPercentage() {
            if (this.goalWeekly > 0) {
                return (this.currentWeekly / this.goalWeekly) * 100;
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
    padding-bottom: 20px;
}

.stickyHeader .displayBlock {
    align-items: center;
    justify-content: center;
}

.container {
    padding: 0 16px 10px 16px;
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

.updateDetails {
    display: flex;
    justify-content: flex-end;
}

.syncButton {
    font-family: text-medium;
    color: var(--blue);
    font-size: 10px;
    background-color: #E9F3FD;
    border-radius: 5px;
    border: none;
    padding: 8px 10px;
    margin: 0 16px 16px 16px;
}

.basicCard {
    background-color: var(--default-white);
    flex-direction: column;
}

.barLabel {
    padding: 16px 16px 5px 16px;
    color: var(--text-highlight);
    font-size: 13px;
}

.updatedVar {
    font-family: text-bold;
}

.updatedText {
    font-family: text-medium;
}

.bar {
    width: 100%;
    height: auto;
    padding: 5px 16px 16px 16px;
}


.card {
    display: flex;
    flex: 0 0 auto;
    border-radius: 6px;
    border: none;
    width: 165px;
}

.cardImage img {
    width: 165px;
    height: 65px;
    border-radius: 6px 6px 0 0;
}


.lowSlotAlert {
    font-family: text-medium;
    font-size: 8px;
    color: var(--default-white);
    background-color: var(--green);
    border-radius: 5px;
    margin-bottom: 5px;
}

.cardText {
    padding: 16px;
}

.eventName {
    font-family: text-semibold;
    font-size: 12px;
    color: var(--default-text);
    margin: 0;
}

.eventDetails p {
    font-family: text-medium;
    font-size: 10px;
    color: var(--text-highlight);
    margin: 0;
}


</style>