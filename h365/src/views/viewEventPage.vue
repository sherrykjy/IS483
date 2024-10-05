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
                <p class="eventName"> Active Family Programme </p>

                <!-- activity name -->
                <p class="activityName"> Pilates </p>

                <!-- activity description -->
                <p class="activityDesc">
                    Pilates is a low-impact exercise that focuses on core strength, flexibility, 
                    and overall body control. It involves a series of controlled movements that 
                    improve posture, balance, and coordination, making it an ideal workout for 
                    the mind and body.
                </p>
            </div>
        </div>

        <div class="eventInfo">
            <div class="detailLabel">
                <i class="uil uil-schedule eventIcon"></i>
                <p> WHEN </p>
            </div>

            <div class=detailText>
                <p>2 September 2024, Monday</p>
                <p>6.15pm - 7.15pm</p>
            </div>

            <div class="splitRow">
                <div class="splitStack">
                    <div class="detailLabel">
                        <i class="uil uil-map-pin eventIcon"></i>
                        <p> WHERE </p>
                    </div>
                
                    <div class=detailText>
                        <p>PAYA LEBAR, Paya Lebar Precinct (Paya Lebar Quarter Mall)</p>
                    </div>
                </div>

                <div class="detailLabel intensity">
                    <p>Intensity: </p>
                    <img src="../assets/icons/events/intensity1.png">
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
            <p class="eventName" style="margin-bottom: 10px;">Exer-Fit Consultancy Services</p>

            <div class="organiserContact">
                <i class="uil uil-phone-volume"></i>
                <p>91234567</p>
            </div>

            <div class="organiserContact">
                <i class="uil uil-envelope"></i>
                <p>enquiries@exer-fit.com.sg</p>
            </div>
        </div>

        <div class="bookNowContainer">
            <button class="bookButton" @click="openCodePopup('Pilates')"> Book Now </button>
        </div>
    </div>

    <Popup
        v-if="isPopupVisible"
        :visible="isPopupVisible"
        :type="popupType"
        :eventName="eventName"
        @close="closePopup"
    />

</template>

<script>
import Popup from '@/components/popUp.vue';

export default ({
    components: {
        Popup
    },

    data() {
        return {
            isPopupVisible: false,
            eventName: '',
            popupType: 'event-code'
        };
    },
    methods: {
        openCodePopup(eventName) {
            this.eventName = eventName;
            this.isPopupVisible = true;
        },
        closePopup() {
            this.isPopupVisible = false;
        }
    }
});

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