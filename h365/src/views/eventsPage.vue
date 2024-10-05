<template>
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
                <input type="text" placeholder="Search by event or location" />
            </div>

            <div class="filterButton">
                <datePicker />
            </div>
        </div>

        <div class="basicHeader">
            <p>2 September 2024</p>    
        </div>

        <div class="pageHeading">
            <img src="../assets/icons/events/star.png">
            <p>Recommended for you</p>
        </div>



        <!-- v-for however many events there are -->
        <router-link :to="{ name: 'viewEventPage'}">
                                    
            <div class="basicCard">
                <div class="cardImage">
                    <img src="../assets/icons/events/event1.png">
                </div>

                <div class="cardText">
                    <!-- v-if few slots left -->
                    <div class="lowSlotAlert">
                        Few Slots Left
                    </div>

                    <!-- programme name -->
                    <p class="programmeName">Active Family Programme</p>

                    <!-- activity name -->
                    <p class="eventName">Pilates</p>

                    <!-- date, day, and time  -->
                    <div class="eventInfo">
                        <i class="uil uil-schedule eventIcon"></i>
                        <div class=eventDetails>
                            <p>2 September 2024, Monday</p>
                            <p>6.15pm - 7.15pm</p>
                        </div>
                    </div>

                    <!-- location -->
                    <div class="eventInfo">
                        <i class="uil uil-map-pin eventIcon"></i>
                        <div class=eventDetails>
                            <p>PAYA LEBAR, Paya Lebar Precinct (Paya Lebar Quarter Mall)</p>
                        </div>
                    </div>

                    <div class="eventBtnIntensity">
                        <form action="">
                            <button class="bookEventBtn">Book Now</button>
                        </form>

                        <!-- intensity -->
                        <div class="intensity">
                            <p>Intensity: </p>
                            <img src="../assets/icons/events/intensity1.png">
                        </div>
                    </div>
                </div>
            </div>
        </router-link>

        <div class="basicCard">
            <div class="cardImage">
                <img src="../assets/icons/events/event1.png">
            </div>

            <div class="cardText">
                <!-- v-if few slots left -->
                <div class="lowSlotAlert">
                    Few Slots Left
                </div>

                <!-- programme name -->
                <p class="programmeName">Active Family Programme</p>

                <!-- activity name -->
                <p class="eventName">Pilates</p>

                <!-- date, day, and time  -->
                <div class="eventInfo">
                    <i class="uil uil-schedule eventIcon"></i>
                    <div class=eventDetails>
                        <p>2 September 2024, Monday</p>
                        <p>6.15pm - 7.15pm</p>
                    </div>
                </div>

                <!-- location -->
                <div class="eventInfo">
                    <i class="uil uil-map-pin eventIcon"></i>
                    <div class=eventDetails>
                        <p>PAYA LEBAR, Paya Lebar Precinct (Paya Lebar Quarter Mall)</p>
                    </div>
                </div>

                <div class="eventBtnIntensity">
                    <form action="">
                        <button class="bookEventBtn">Book Now</button>
                    </form>

                    <!-- intensity -->
                    <div class="intensity">
                        <p>Intensity: </p>
                        <img src="../assets/icons/events/intensity1.png">
                    </div>
                </div>
            </div>
        </div>

        <div class="basicCard">
            <div class="cardImage">
                <img src="../assets/icons/events/event1.png">
            </div>

            <div class="cardText">
                <!-- v-if few slots left -->
                <div class="lowSlotAlert">
                    Few Slots Left
                </div>

                <!-- programme name -->
                <p class="programmeName">Active Family Programme</p>

                <!-- activity name -->
                <p class="eventName">Pilates</p>

                <!-- date, day, and time  -->
                <div class="eventInfo">
                    <i class="uil uil-schedule eventIcon"></i>
                    <div class=eventDetails>
                        <p>2 September 2024, Monday</p>
                        <p>6.15pm - 7.15pm</p>
                    </div>
                </div>

                <!-- location -->
                <div class="eventInfo">
                    <i class="uil uil-map-pin eventIcon"></i>
                    <div class=eventDetails>
                        <p>PAYA LEBAR, Paya Lebar Precinct (Paya Lebar Quarter Mall)</p>
                    </div>
                </div>

                <div class="eventBtnIntensity">
                    <form action="">
                        <button class="bookEventBtn">Book Now</button>
                    </form>

                    <!-- intensity -->
                    <div class="intensity">
                        <p>Intensity: </p>
                        <img src="../assets/icons/events/intensity1.png">
                    </div>
                </div>
            </div>
        </div>

        <br>

        <div class="pageHeading">
            <img src="../assets/icons/events/folder.png">
            <p>All Events</p>
        </div>



        <!-- v-for however many events there are -->
        <div class="basicCard">
            <div class="cardImage">
                <img src="../assets/icons/events/event2.png">
            </div>

            <div class="cardText">
                <!-- v-if few slots left -->
                <div class="lowSlotAlert">
                    Few Slots Left
                </div>

                <!-- programme name -->
                <p class="programmeName">Active Family Programme</p>

                <!-- activity name -->
                <p class="eventName">Cardio Dance Fitness</p>

                <!-- date, day, and time  -->
                <div class="eventInfo">
                    <i class="uil uil-schedule eventIcon"></i>
                    <div class=eventDetails>
                        <p>2 September 2024, Monday</p>
                        <p>10.00am - 11.00am</p>
                    </div>
                </div>

                <!-- location -->
                <div class="eventInfo">
                    <i class="uil uil-map-pin eventIcon"></i>
                    <div class=eventDetails>
                        <p>TAMPINES, Asia Green</p>
                    </div>
                </div>

                <div class="eventBtnIntensity">
                    <form action="">
                        <button class="bookEventBtn">Book Now</button>
                    </form>

                    <!-- intensity -->
                    <div class="intensity">
                        <p>Intensity: </p>
                        <img src="../assets/icons/events/intensity3.png">
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

</style>


<script>
import { defineComponent } from "vue";
import datePicker from '../components/datePicker.vue';

export default defineComponent({
    components: {
        datePicker
    }
});
</script>