<template>
    <div>
        <div class="stickyHeader">
            <div class="pageHeader">
                <p>Events</p>
            </div>
            <n-tabs type="line" class="pageTab">
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
                    <datePicker v-model="dateInput" @update:modelValue="searchEvents"/>
                </div>
            </div>
            <!-- Check if there are no filtered events or eventData -->
            <div v-if="isEmpty(filteredEventsData)">
                <p class="no-events-found">No matching events found</p>
            </div>
            <!-- loop for each date -->
            <div v-for="date in sortedDates" :key="date" v-else>
                <!-- date header -->
                <div class="basicHeader">
                    <p>{{ formattedDateHeader(date) }}</p>
                </div>
                <!-- recommended events -->
                <div v-if="recommendedEvents[date] && recommendedEvents[date].length">
                    <!-- recommended header -->
                    <div class="pageHeading">
                        <img src="../assets/icons/events/star.png">
                        <p>Recommended for you</p>
                    </div>

                    <!-- recommended events cards -->
                    <div v-for="event in recommendedEvents[date]" :key="event.event_id">
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
                    </div>

                    <br>
                </div>
                
                <!-- all events header -->
                <div class="pageHeading">
                    <img src="../assets/icons/events/folder.png">
                    <p>All Events</p>
                </div>
                <!-- all events cards -->
                <div v-for="event in filteredEventsData[date]" :key="event.event_id">
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
                </div>
                
            </div>
        </div>
    </div>

</template>

<style scoped>

.stickyHeader {
    top: 0;
}

.basicHeader {
    text-align: left;
    font-family: text-bold;
    border-bottom: 1px solid rgba(123, 120, 116, 1);
}

.pageHeader {
    background-color: var(--yellow);
}

.pageTab {
    background-color: var(--grey);
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

.no-events-found {
    text-align: center;
    font-family: text-semibold;
    color: var(--text-highlight);
    font-size: 14px;
    margin-top: 20px;
}

</style>


<script>
import { defineComponent } from "vue";
import datePicker from '../components/datePicker.vue';

export default defineComponent({
    components: {
        datePicker
    },
    async mounted() {
        // to update eventData
        this.$http.get("http://127.0.0.1:5002/event/available")
        .then(response => {
            var eventDataResponse = response.data.data;
            // console.log(eventDataResponse);
            this.eventData = {};
            this.sortedDates = [];
            for (var i = 0; i < eventDataResponse.length; i++) {
                // console.log(eventDataResponse[i]);
                let event_id = eventDataResponse[i]["event_id"];
                let current_signups = eventDataResponse[i]["current_signups"];
                let max_signups = eventDataResponse[i]["max_signups"];
                let slots_left = max_signups - current_signups;
                let event_program = eventDataResponse[i]["event_program"];
                let title = eventDataResponse[i]["title"];
                let start_date = eventDataResponse[i]["start_date"];
                let end_date = eventDataResponse[i]["end_date"];
                let location = eventDataResponse[i]["location"];
                let tier = eventDataResponse[i]["tier"];

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
    data() {
        return {
            searchInput: "",
            dateInput: null,
            sortedDates: [],
            // mock data for displaying
            eventData: {
                "2024-12-01": [
                    {
                        "event_id": 1,
                        "current_signups": 6,
                        "max_signups": 10,
                        "event_program": "Active Family Program",
                        "title": "Mindfulness Week",
                        "start_date": "2024-12-01T12:00:00",
                        "end_date": "2024-12-01T14:00:00",
                        "location": "Bendemeer",
                        "tier": 2
                    },
                    {
                        "event_id": 2,
                        "current_signups": 6,
                        "max_signups": 10,
                        "event_program": "Active Family Program",
                        "title": "Gratefulness Week",
                        "start_date": "2024-12-01T12:00:00",
                        "end_date": "2024-12-01T14:00:00",
                        "location": "Bendemeer",
                        "tier": 2
                    },
                    {
                        "event_id": 3,
                        "current_signups": 6,
                        "max_signups": 10,
                        "event_program": "Active Family Program",
                        "title": "Thankfulness Week",
                        "start_date": "2024-12-01T12:00:00",
                        "end_date": "2024-12-01T14:00:00",
                        "location": "Bendemeer",
                        "tier": 2
                    }
                ] // end of 2024-12-01
            }, // end of eventData dict
            recommendedEvents: {
                "2024-10-03": [
                    {
                        "event_id": 4,
                        "current_signups": 6,
                        "max_signups": 10,
                        "event_program": "Active Family Program",
                        "title": "Mindfulness Week",
                        "start_date": "2024-10-03T19:00:00",
                        "end_date": "2024-10-03T20:00:00",
                        "location": "Bendemeer",
                        "tier": 2
                    }
                ],
                "2024-10-04": [
                    {
                        "event_id": 5,
                        "current_signups": 6,
                        "max_signups": 10,
                        "event_program": "Active Family Program",
                        "title": "Test Week",
                        "start_date": "2024-10-04T19:00:00",
                        "end_date": "2024-10-04T20:00:00",
                        "location": "Bendemeer",
                        "tier": 2
                    }
                ]
            },
            filteredEvents: null
        }
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
            try {
                const url = "http://127.0.0.1:5002/event/search";
                const params = {};

                // add search_input if provided
                if (this.searchInput) {
                    params.search_input = this.searchInput;
                }

                // add date_input if provided
                if (this.dateInput) {
                    const dateValue = this.dateInput.split("T")[0];
                    if (dateValue) {
                        params.date_input = dateValue;
                    }
                }
                
                // GET request
                const response = await this.$http.get(url, { params });
                console.log("response", response);
                console.log("response data", response.data.data);

                if (response.status === 200) {
                    console.log("testing search/filtered response");
                    var responseData = response.data.data;
                    this.filteredEvents = {};
                    this.sortedDates = [];
                    for (var i = 0; i < responseData.length; i++) {
                        let event_id = responseData[i]["event_id"];
                        let current_signups = responseData[i]["current_signups"];
                        let max_signups = responseData[i]["max_signups"];
                        let slots_left = max_signups - current_signups;
                        let event_program = responseData[i]["event_program"];
                        let title = responseData[i]["title"];
                        let start_date = responseData[i]["start_date"];
                        let end_date = responseData[i]["end_date"];
                        let location = responseData[i]["location"];
                        let tier = responseData[i]["tier"];

                        let date_key = start_date.split("T")[0];

                        if (!this.filteredEvents[date_key]) {
                            this.filteredEvents[date_key] = [];
                            this.sortedDates.push(date_key);
                        }

                        this.filteredEvents[date_key].push({
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
                }
                console.log("sorted dates:", this.sortedDates);
                console.log("filtered events:", this.filteredEvents);
            }
            catch (error) {
                console.log(error);
                this.filteredEvents = null;
                this.sortedDates = [];
            }
        },
        isEmpty(eventsData) {
            return !eventsData || Object.keys(eventsData).length === 0;
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