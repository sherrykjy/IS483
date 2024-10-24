<template>
    <div class="stickyHeader">
        <div class="pageHeader">
            <p> Welcome back, 
                <span> {{ userName }} </span> 
            </p>
        </div>

        <div class="displayBlock">
            <div class="blockLeft">
                <div class="blockText">
                    <p style="margin-right: 5px"> 315 </p>
                    <span> <img src="../assets/icons/homepage/coin.png"> </span>
                </div>
                <p> My Healthcoins </p>
            </div>

            <div class="blockRight">
                <div class="blockText">
                    <p> {{ streakCount }} </p>
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
                    <span class="updatedVar"> 150 / 150 </span>
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
                    <button class="syncButton" @click="stravaLogin"> Sync now </button>
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
                    <span class="updatedVar" style="color: var(--purple)"> 30 </span>
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
                    <button class="syncButton" style="width: 90%;" @click="goToMonthlyReport"> View your {{ lastMonth }} report </button>
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
                
                <div v-for="event in recommendedEvents" :key="event.event_id">
                    <router-link :to="{ name: 'viewEventPage', params: { eventId: event.event_id } }">
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
                                <p class="eventName"> {{ event.title }} </p>
                                <!-- date, day, and time  -->
                                <div class="eventInfo">
                                    <div class=eventDetails>
                                        <p> {{ formattedDate(event.start_date) }} </p>
                                        <p> {{ formattedTime(event.start_date, event.end_date) }} </p>
                                    </div>
                                </div>
                                <!-- location -->
                                <div class="eventInfo">
                                    <div class=eventDetails>
                                        <p> {{ event.location }} </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </router-link>
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
        // console.log("home page");
        const store = useStore();
        const userId = computed(() => store.state.userId);
        const userEmail = computed(() => store.state.userEmail);
        // console.log(userId.value);
        // console.log(userEmail.value);
        return {
            userId,
            userEmail
        };
    },
    data() {
        return {
            streakCount: 1,

            currentWeekly: 0,
            goalWeekly: 0,
            minutesToday: 0,

            mr_movingMinutes: 0,
            mr_topActivity: "",
            mr_totalDistance: 0,
            mr_allActivitites: {},

            lastMonth: "",
            numHealthCoins: 0,
            userName: "",
            recommendedEvents: [
                {
                    "event_id": 5,
                    "current_signups": 8,
                    "max_signups": 10,
                    "slots_left": 2,
                    "event_program": "Active Family Program",
                    "title": "Yoga Challenge",
                    "start_date": "2024-10-11T12:00:00",
                    "end_date": "2024-10-11T14:00:00",
                    "location": "Paya Lebar",
                    "tier": 2
                },
                {
                    "event_id": 6,
                    "current_signups": 5,
                    "max_signups": 10,
                    "slots_left": 5,
                    "event_program": "Active Family Program",
                    "title": "Plank Challenge",
                    "start_date": "2024-10-11T14:00:00",
                    "end_date": "2024-10-11T16:00:00",
                    "location": "Tampines",
                    "tier": 1
                }
            ]
        }
    },

    computed: {
        progressPercentage() {
            // if (this.goalWeekly > 0) {
            //     return (this.currentWeekly / this.goalWeekly) * 100;
            // }
            // return 0;
            return (150/150)*100;
        }
    },

    methods: {
        getPreviousMonth() {
            const currentDate = new Date();
            let month = currentDate.getMonth();

            if (month === 0) {
                month = 11;
            } else {
                month -= 1;
            }

            // Get the month name from the month index
            const monthNames = ["January", "February", "March", "April", "May", "June", 
                                "July", "August", "September", "October", "November", "December"];
            this.lastMonth = monthNames[month];
        },

        async fetchUserData() {
            try {
                const userReponse = await this.$http.get("http://127.0.0.1:5001/user/" + this.userEmail);
                const userData = userReponse.data.data;
                this.numHealthCoins = userData["total_point"];
                this.userName = userData["name"];
            } catch (error) {
                console.error("Error fetching user data:", error);
            }
        },
        formattedDate(dateStr) {
            const date = new Date(dateStr);

            // Get the formatted day, month, and year
            const day = date.getDate(); // 1
            const month = new Intl.DateTimeFormat('en-US', { month: 'long' }).format(date); // August
            const year = date.getFullYear(); // 2024
            const weekday = new Intl.DateTimeFormat('en-US', { weekday: 'long' }).format(date); // e.g., Wednesday

            return `${day} ${month} ${year}, ${weekday}`;
        },
        formattedTime(startDateStr, endDateStr) {
            const startDate = new Date(startDateStr);
            const endDate = new Date(endDateStr);

            const formatTime = date => {
                return new Intl.DateTimeFormat('en-US', {
                hour: 'numeric',
                minute: 'numeric',
                hour12: true
                }).format(date);
            };

            return `${formatTime(startDate)} - ${formatTime(endDate)}`;
        },

        async stravaLogin() {
            // window.open("http://localhost:5020/connect", "_blank");
            window.location.href = "http://localhost:5020/connect";
            // await this.handleStravaCallback();
            await this.syncNow();
        },

        async syncNow() {
            try {
                const goalResponse = await this.$http.get("http://127.0.0.1:5011/goals/" + this.userId)
                const goalData = goalResponse.data;
                // console.log(goalData)
                const goal_id = goalData[0].goal_id;

                const streakResponse = await this.$http.get("http://127.0.0.1:5010/streaks/" + goal_id)
                const streakData = streakResponse.data;
                // console.log(streakData)
                const streak_id = streakData[0].streak_id;

                const payload = {
                    goal_id: goal_id,
                    user_id: this.userId,
                    streak_id: streak_id,
                };

                const response = await this.$http.post('http://localhost:5030/update_streak', payload, {
                    headers: { 'Content-Type': 'application/json' }
                });

                // console.log("haha")
                // console.log(response)

                // console.log(response.data.data.streak_count)
                this.streakCount = response.data.data.streak_count;

                this.currentWeekly = response.data.data.weekly_time_lapse;
                this.goalWeekly = goalData[0].target;
                this.minutesToday = response.data.data.daily_time_lapse;

                this.mr_movingMinutes = response.data.data.monthly_time_lapse;
                this.mr_topActivity = response.data.data.monthly_top_activity;
                this.mr_totalDistance = response.data.data.monthly_distance;
                this.mr_allActivitites = response.data.data.activities_in_month;

                // console.log("haha", this.mr_allActivitites)

                if (response.status === 200) {
                    console.log('Streak update successful', response.data);
                } else {
                    console.error('Error syncing streak:', response.data);
                }
            } catch (error) {
                console.error('Sync failed:', error);
            }
        },

        // goToMonthlyReport() {
        //     this.$router.push({
        //         name: 'monthlyReport',
        //         params: {
        //             streakCount: this.streakCount,
        //             mr_movingMinutes: this.mr_movingMinutes,
        //             mr_topActivity: this.mr_topActivity,
        //             mr_totalDistance: this.mr_totalDistance,
        //             // mr_allActivitites: this.mr_allActivitites,
        //             // mr_allActivitites: Object.keys(activities).length ? JSON.stringify(activities) : '{}', // Default to empty object

                    

        //             mr_month: this.month
        //         }
        //     });

        //     this.$router.push('monthlyReport').then(() => { this.$route.params.mr_allActivitites = this.mr_allActivitites })
        // }

        goToMonthlyReport() {
            this.$router.push({
                name: 'monthlyReport',
                params: {
                    streakCount: this.streakCount,
                    mr_movingMinutes: this.mr_movingMinutes,
                    mr_topActivity: this.mr_topActivity,
                    mr_totalDistance: this.mr_totalDistance,
                    mr_allActivitites: JSON.stringify(this.mr_allActivitites), // Stringify the array before passing
                    mr_month: this.month
                }
            }).then(() => { 
                this.$route.params.mr_allActivitites = this.mr_allActivitites;
            });
        }
    },

    async mounted() {
        try {
            this.getPreviousMonth();
            this.fetchUserData();
            await this.syncNow();
        } catch (error) {
            console.log("error:", error);
        }
    },
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