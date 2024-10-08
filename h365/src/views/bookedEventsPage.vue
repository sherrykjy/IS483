<template>
    <div class="stickyHeader">
        <div class="pageHeader">
            <p>Events</p>
        </div>

        <n-tabs v-model:value="selectedTab" type="line" class="pageTab">
            <n-tab name="allEvents">
                All
            </n-tab>
            <n-tab name="bookedEvents">
                Booked
            </n-tab>
        </n-tabs>
    </div>

    <div class="pagePad">
        <div class="searchAndFilter">
            <div class="search-bar">
                <i class="uil uil-search"></i>
                <input type="text" v-model="searchInput" @input="searchEvents" placeholder="Search by event or location" />
            </div>

            <div class="filterButton">
                <datePicker v-model="dateInput" @update:modelValue="searchEvents" />
            </div>
        </div>        

        <!-- loop for each date -->
        <div v-for="date in sortedDates" :key="date">
            <div v-if="filteredEventsData[date] && filteredEventsData[date].length">
                <!-- date header -->
                <div class="basicHeader">
                    <p>{{ formattedDateHeader(date) }}</p>
                </div>

                <div class="divider"></div>

                <div v-for="event in filteredEventsData[date]" :key="event.event_id">
                    <router-link :to="{ name: 'viewEventPage', params: { eventId: event.event_id } }">
                        <div class="basicCard">
                            <div class="cardImage">
                                <img src="../assets/icons/events/event1.png">
                            </div>
                            <div class="cardText">
                                <!-- v-if few slots left -->
                                <div class="lowSlotAlert" v-if="event.slots_left <= 5">
                                    Few Slots Left
                                </div>
                                <!-- programme name -->
                                <p class="programmeName" v-if="event.event_program != 'Null'">{{ event.event_program }}</p>
                                <!-- activity name -->
                                <p class="eventName">{{ event.title }}</p>
                                <!-- date, day, and time  -->
                                <div class="eventInfo">
                                    <i class="uil uil-schedule eventIcon"></i>
                                    <div class=eventDetails>
                                        <p>{{ formattedDate(event.start_date) }}</p>
                                        <p>{{ formattedTime(event.start_date, event.end_date) }}</p>
                                    </div>
                                </div>
                                <!-- location -->
                                <div class="eventInfo">
                                    <i class="uil uil-map-pin eventIcon"></i>
                                    <div class=eventDetails>
                                        <p>{{ event.location }}</p>
                                    </div>
                                </div>
                                <div class="eventBtnIntensity">
                                    <form action="">
                                        <button class="bookEventBtn">Book Now</button>
                                    </form>
                                    <!-- intensity -->
                                    <div class="intensity">
                                        <p>Intensity: </p>
                                        <img v-if="event.tier === 1" src="../assets/icons/events/intensity1.png">
                                        <img v-else-if="event.tier === 2" src="../assets/icons/events/intensity2.png">
                                        <img v-else-if="event.tier === 3" src="../assets/icons/events/intensity3.png">
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
import { defineComponent, ref, computed, watch } from "vue";
import datePicker from '../components/datePicker.vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

export default 
    defineComponent({
        components: {
            datePicker
        },
        setup() {
            console.log("booked events page");
            const selectedTab = ref('bookedEvents');
            const store = useStore(); // Import useStore from vuex
            const router = useRouter();
            const userId = computed(() => store.state.userId); // Access userId from the store
            const userEmail = computed(() => store.state.userEmail) // Access userEmail from the store

            watch(selectedTab, (newTab) => {
                if (newTab === 'allEvents') {
                    // Navigate to /events route
                    router.push({ path: '/events' });
                } else if (newTab === 'bookedEvents') {
                    // Navigate to /booked route
                    router.push({ path: '/booked' });
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
                sortedDates: [],
                eventData: {},
                searchInput: '',
                dateInput: null,
                filteredEvents: {}
            }
        },
        async mounted() {
            this.$http.get("http://127.0.0.1:5007/userevent/active/" + this.userId)
            .then(response => {
                var eventDataResponse = response.data;
                console.log(eventDataResponse);
                this.eventData = {};
                this.sortedDates = [];
                for (var i = 0; i < eventDataResponse.length; i++) {
                    // console.log(eventDataResponse[i]);
                    let data = eventDataResponse[i].data;
                    // console.log(data);
                    let event_id = data["event_id"];
                    let current_signups = data["current_signups"];
                    let max_signups = data["max_signups"];
                    let slots_left = max_signups - current_signups;
                    let event_program = data["event_program"];
                    let title = data["title"];
                    let start_date = data["start_date"];
                    let end_date = data["end_date"];
                    let location = data["location"];
                    let tier = data["tier"];

                    let date_key = start_date.split("T")[0];

                    if (!this.eventData[date_key]) {
                        this.eventData[date_key] = [];
                        this.sortedDates.push(date_key);
                    }

                    this.eventData[date_key].push({
                        "event_id": event_id,
                        "current_signups": current_signups,
                        "max_signups": max_signups,
                        "slots_left": slots_left,
                        "event_program": event_program,
                        "title": title,
                        "start_date": start_date,
                        "end_date": end_date,
                        "location": location,
                        "tier": tier
                    })

                }
                this.sortedDates.sort();
                console.log("event data:", this.eventData);
                console.log("sorted dates:", this.sortedDates);
            })
            .catch(error => {
                console.log("error:", error);
            });
        },
        methods: {
            // Format date as '2 September 2024, Monday'
            formattedDate(dateStr) {
                const date = new Date(dateStr);

                // Get the formatted day, month, and year
                const day = date.getDate(); // 1
                const month = new Intl.DateTimeFormat('en-US', { month: 'long' }).format(date); // August
                const year = date.getFullYear(); // 2024
                const weekday = new Intl.DateTimeFormat('en-US', { weekday: 'long' }).format(date); // e.g., Wednesday

                return `${day} ${month} ${year}, ${weekday}`;
            },
            formattedDateHeader(dateStr) {
                const date = new Date(dateStr);
                return date.toLocaleDateString('en-GB', {
                    day: 'numeric',
                    month: 'long',
                    year: 'numeric'
                })
            },
            // Format time as '10.00am - 11.00am'
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
            async searchEvents() {
                console.log("checking search input:", this.searchInput);
                console.log("checking date input:", this.dateInput);

                this.filteredEvents = {};

                for (const date of this.sortedDates) {
                    const eventsForDate = this.eventData[date].filter(event => {
                        const matchesSearchInput = event.title.toLowerCase().includes(this.searchInput.toLowerCase()) || 
                                                    event.location.toLowerCase().includes(this.searchInput.toLowerCase());
                        
                        const matchesDate = !this.dateInput || date === this.dateInput;

                        return matchesSearchInput && matchesDate;
                    });

                    if (eventsForDate.length) {
                        this.filteredEvents[date] = eventsForDate;
                    }
                }
            }
        },
        computed: {
            filteredEventsData() {
                if (this.searchInput || this.dateInput) {
                    console.log("returning filtered data");
                    console.log("filtered events:", this.filteredEvents);
                    return this.filteredEvents || {};
                } else {
                    return this.eventData;
                }
            }
        }
    });
</script>

<style scoped>
.stickyHeader {
    top: 0;
}

.basicHeader {
    text-align: left;
    font-family: text-bold;
    border: 0;
}

.pageHeader {
    background-color: var(--yellow);
}

.pageTab {
    background-color: var(--grey);
}

.divider {
    width: 90%;
    height: 1px;
    background-color: var(--text-highlight);
    margin: auto;
    display: flex;
    margin-bottom: 20px;
}

.basicCard {
    width: 90%;
    display: flex;
    background-color: var(--default-white);
    margin: 0 auto;
    margin-bottom: 20px;
}

.basicCard .cardImage, .basicCard .cardText {
    flex: 1;
}

.basicCard .cardImage {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    padding: 0px;
}

.basicCard .cardImage img {
    height: 100%;
    width: 100%;
    object-fit: contain;
    margin: 0px;
}

.basicCard .cardText {
    padding: 16px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.lowSlotAlert {
    font-family: text-medium;
    font-size: 8px;
    color: var(--default-white);
    background-color: var(--red);
}

.programmeName {
    font-family: text-medium;
    font-size: 10px;
    color: var(--text-highlight);
    margin-bottom: 0px;
}

.eventName {
    font-family: text-bold;
    font-size: 16px;
    color: var(--default-text);
    margin-bottom: 0px;
    line-height: 16px;
}

.eventIcon {
    color: var(--text-highlight);
}

.eventInfo {
    display: flex;
    padding: 0px;
    align-items: center;
    justify-content: flex-start;
}

.eventDetails {
    font-family: text-semibold;
    color: var(--text-highlight);
    font-size: 9px;
    padding-left: 10px;
}

.eventDetails p {
    margin-bottom: 0px;
}

.bookEventBtn {
    font-family: text-medium;
    color: var(--grey);
    font-size: 10px;
    background-color: var(--blue);
    border-radius: 5px;
    border: none;
    padding-top: 2px 10px;
}

.eventBtnIntensity {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.eventBtnIntensity .intensity {
    display: flex;
    align-items: center;
}

.eventBtnIntensity .intensity img {
    margin-left: 3px;
}

.intensity p {
    font-family: text-semibold;
    font-size: 10px;
    color: var(--text-highlight);
    margin: 5px 5px 0 0;
}
</style>