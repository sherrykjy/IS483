<template>
    <div class="pageContainer">
        <div class="pageHeader">
            <i class="uil uil-angle-left"></i>
            <p>Event details</p>
        </div>

        <div class="eventDetails">
            <div class="eventImage">
                <img src="../assets/icons/events/event1.png">
            </div>

            <div class="eventText">
                <!-- programme name -->
                <p class="eventName"> {{ programName }} </p>

                <!-- activity name -->
                <p class="activityName"> {{ eventTitle }} </p>

                <!-- activity description -->
                <p class="activityDesc">
                    {{ eventDescription }}
                </p>
            </div>
        </div>

        <div class="eventInfo">
            <div class="detailLabel">
                <i class="uil uil-schedule eventIcon"></i>
                <p> WHEN </p>
            </div>

            <div class=detailText>
                <p>{{ formattedDate(eventStartDate) }}</p>
                <p>{{ formattedTime(eventStartDate, eventEndDate) }}</p>
            </div>

            <div class="splitRow">
                <div class="splitStack">
                    <div class="detailLabel">
                        <i class="uil uil-map-pin eventIcon"></i>
                        <p> WHERE </p>
                    </div>
                
                    <div class=detailText>
                        <p>{{ eventLocation }}</p>
                    </div>
                </div>

                <div class="detailLabel intensity">
                    <p>Intensity: </p>
                    <img v-if="eventTier === 1" src="../assets/icons/events/intensity1.png">
                    <img v-else-if="eventTier === 2" src="../assets/icons/events/intensity2.png">
                    <img v-else-if="eventTier === 3" src="../assets/icons/events/intensity3.png">
                </div>
            </div>
        </div>

        <div class="reminder">
            <p>Please arrive early for the session as latecomers who miss the pre-activity 
                safety and well-being checks will not be allowed to participate.
            </p>
        </div>


        <div class="eventInfo">
            <p class="activityName" style="margin-bottom: 0;">Organiser</p>

            <!-- organiser name -->
            <p class="eventName" style="margin-bottom: 10px;">{{ eventOrganiserName }}</p>

            <div class="organiserContact">
                <i class="uil uil-phone-volume"></i>
                <p>{{ eventOrganiserPhone }}</p>
            </div>

            <div class="organiserContact">
                <i class="uil uil-envelope"></i>
                <p>{{ eventOrganiserEmail }}</p>
            </div>
        </div>

        <div class="bookNowContainer">
            <button class="bookButton" @click="openCodePopup"> Book Now </button>
        </div>
    </div>

    <Popup
        v-if="isPopupVisible"
        :visible="isPopupVisible"
        :type="popupType"
        :eventName="eventName"
        :errorMessage="errorMessage"
        @close="closePopup"
        @validate-code="validateCode"
    />

</template>

<script>
import Popup from '@/components/popUp.vue';
import { useStore } from 'vuex';
import { computed } from 'vue';

export default {
    name: 'viewEventPage',
    components: {
        Popup
    },
    setup() {
        console.log("view event page");
        const store = useStore(); // Import useStore from vuex
        const userId = computed(() => store.state.userId); // Access userId from the store
        const userEmail = computed(() => store.state.userEmail) // Access userEmail from the store
                
        return {
            userId,
            userEmail
        };
    },
    data() {
        return {
            eventId: null,
            programName: "",
            eventTitle: "",
            eventDescription: "",
            eventStartDate: null,
            eventEndDate: null,
            eventLocation: "",
            eventTier: "",
            eventOrganiserName: "",
            eventOrganiserEmail: "",
            eventOrganiserPhone: "",
            entryCode: "",
            isPopupVisible: false,
            eventName: '',
            popupType: 'event-code',
            userEntryCode: "",
            errorMessage: '' 
        }
    },
    async mounted() {
        const eventId = this.$route.params.eventId;
        console.log("eventID:", eventId);

        try {
            const response = await this.$http.get("http://127.0.0.1:5002/event/" + eventId);
            const eventData = response.data.data;
            console.log(eventData);

            this.eventId = eventId;
            this.programName = eventData["event_program"];
            this.eventTitle = eventData["title"];
            this.eventDescription = eventData["description"];
            this.eventStartDate = eventData["start_date"];
            this.eventEndDate = eventData["end_date"];
            this.eventLocation = eventData["location"];
            this.eventTier = eventData["tier"];
            this.eventOrganiserName = eventData["organiser"];
            this.eventOrganiserEmail = eventData["organiser_email"];
            this.eventOrganiserPhone = eventData["organiser_phone"];
            this.entryCode = eventData["entry_code"];

        }
        catch (error) {
            console.log("error:", error);
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
        async joinEvent() {
            console.log("join event attempt");

            try {
                const response = await this.$http.post("http://127.0.0.1:5007/userevent/enrol", {
                    user_id: this.userId,
                    event_id: this.eventId,
                    entry_code: this.entryCode
                })
                console.log(response);
                console.log("Join event successful");

                this.$router.push('/booked');
            }
            catch (error) {
                console.log("Join Event:", error);
                var responseError = error.response.data.error;
                console.log(responseError);
                if (responseError == "User is already registered for this event") {
                    this.errorMessage = "User is already registered for this event.";
                    alert("User is already registered for this event.")
                }
                else {
                    this.errorMessage = "Failed to join the event. Please try again.";
                }   
            }
        },
        openCodePopup() {
            if (this.entryCode != "Null") {
                this.isPopupVisible = true;
            }
            else {
                // calling joinEvent method for event with no entry code
                this.joinEvent();
            }
        },
        closePopup() {
            this.isPopupVisible = false;
            this.errorMessage = ''; 
        },
        validateCode(userEntryCode) {
            // Compare the user input with the event's entry code
            if (userEntryCode === this.entryCode) {
                console.log("Correct entry code entered");
                this.joinEvent(); // Call the joinEvent method if the code is correct
            } else {
                console.log("Invalid entry code");
                this.errorMessage = "Invalid event code. Please try again.";
            }
        },
    }
}
</script>

<style scoped>
.pageContainer {
    padding-bottom: 100px;
}

.pageHeader {
    background-color: var(--yellow);
}

.eventDetails {
    display: flex;
    padding: 16px;
}

.eventImage, .eventText {
    padding: 16px;
}

.eventName, .activityDesc {
    font-family: text-medium;
    font-size: 12px;
    color: var(--default-text);

    margin-bottom: 0px;
}

.activityName {
    font-family: text-bold;
    font-size: 17px;
    color: var(--default-text);

    margin-bottom: 10px;
}

.activityDesc {
    text-align: justify;
}

.eventInfo {
    padding: 16px;
    border-radius: 6px;
    background-color: var(--default-white);
    margin: 0 32px;
}

.detailLabel {
    display: flex;
    font-family: text-semibold;
    font-size: 11px;
    color: var(--text-highlight);
}

.detailLabel i {
    margin-right: 5px;
}

.detailLabel p {
    margin-bottom: 0px;
    margin-right: 10px;
}

.detailText {
    display: flex;
    flex-direction: column;
    margin-bottom: 16px;

    font-family: text-medium;
    font-size: 11px;
    color: var(--default-text);
}

.detailText p {
    margin-bottom: 0px;
}

.splitStack {
    display: flex;
    flex-direction: column;
    margin-right: 10px;
}

.splitStack .detailText {
    margin: 0;
    padding: 0;
}

.splitRow {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}

.splitRow .detailLabel {
    display: flex;
    align-items: center;
}

.splitRow .detailLabel img {
    width: 15px;
}

.detailLabel.intensity {
    align-self: flex-end;
}

.reminder {
    padding: 16px 32px;
    font-family: text-medium;
    font-size: 10px;
    color: var(--text-highlight);
    font-style: italic;
    text-align: justify;
    margin-bottom: 10px;
}

.reminder p {
    margin-bottom: 0px;
}

.organiser {
    padding: 0 32px;
    background-color: var(--default-white);
}

.organiserContact {
    display: flex;
    align-items: center;
    color: var(--blue);
}

.organiserContact i {
    margin-right: 10px;
}

.organiserContact p {
    font-family: text-bold;
    font-size: 12px;
    margin-bottom: 0;
}

.bookButton {
    background-color: var(--blue);
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