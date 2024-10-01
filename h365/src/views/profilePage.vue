<template>
    <div class="pageHeader stickyHeader">
        <p> Profile </p>
        <i class="uil uil-setting"></i>
    </div>

    <div class="greeting">
        <p style="color: var(--blue);"> Hello, </p>
        <p style="color: var(--text-highlight)"> {{ userName }} </p>
    </div>

    <div class="pagePad">
        <div class="pageHeading">
            <img src="../assets/icons/profile/goals.png">
            <p>Health Goals</p>
        </div>

        <div class="goals drop-shadow">
            <div class="lowSlotAlert">
                Physical Activity
            </div>

            <div class="goalInfo">
                <p style="color: var(--text-highlight)"> Target MVPA Minutes per Week </p>
                <p style="color: var(--default-text)"> {{ targetMinutes }} minutes / week </p>
            </div>

            <div class="goalInfo">
                <p style="color: var(--text-highlight)"> Preferred Intensity </p>
                <p style="color: var(--default-text)"> Level {{ preferredIntensity }} </p>
            </div>
        </div>

        <div class="goals drop-shadow">
            <p class="infoHead"> Primary Information </p>

            <div class="goalInfo">
                <p style="color: var(--text-highlight)"> Name </p>
                <p style="color: var(--default-text)"> {{ userName }} </p>
            </div>

            <div class="goalInfo">
                <p style="color: var(--text-highlight)"> Date of Birth </p>
                <p style="color: var(--default-text)"> {{ dateOfBirth }} </p>
            </div>

            <div class="goalInfo">
                <p style="color: var(--text-highlight)"> Sex </p>
                <p style="color: var(--default-text)"> {{ sex }} </p>
            </div>

            <div class="goalInfo">
                <p style="color: var(--text-highlight)"> School </p>
                <p style="color: var(--default-text)"> {{ school }} </p>
            </div>

            <div class="goalInfo" style="padding-bottom: 16px;">
                <p style="color: var(--text-highlight)"> Region </p>
                <p style="color: var(--default-text)"> {{ region }} </p>
            </div>
        </div>

        <div class="goals drop-shadow">
            <p class="infoHead"> Secondary Information </p>
            <p class="subhead"> Biometrics </p>

            <div class="vertical">
                <div class="goalInfo">
                    <p style="color: var(--text-highlight)"> Height (cm) </p>
                    <p style="color: var(--default-text)"> {{ height }} </p>
                </div>

                <div class="goalInfo">
                    <p style="color: var(--text-highlight)"> Weight (kg) </p>
                    <p style="color: var(--default-text)"> {{ weight }} </p>
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
        console.log("profile page");
        const store = useStore(); // Import useStore from vuex
        const userId = computed(() => store.state.userId); // Access userId from the store
        const userEmail = computed(() => store.state.userEmail) // Access userEmail from the store
        
        console.log(userEmail.value);
        
        return {
            userId,
            userEmail
        };
    },
    data() {
        return {
            userName: "", 
            targetMinutes: 0,
            preferredIntensity: 0, 
            dateOfBirth: "", 
            sex: "", 
            school: "", 
            region: "", 
            height: 0, 
            weight: 0 
        }
    },
    async mounted() {
        try {
            const response = await this.$http.get("http://127.0.0.1:5001/user/profile/" + this.userEmail);
            const userData = response["data"]["data"];

            this.userName = userData["name"];
            this.targetMinutes = userData["target_minutes"];
            this.preferredIntensity = userData["preferred_intensity"];
            this.dateOfBirth = userData["birthdate"];
            this.sex = userData["gender"];
            this.school = userData["school"];
            this.region = userData["location_group"];
            this.height = userData["height"];
            this.weight = userData["weight"];
        }
        catch (error) {
            console.log(error);
        }
    }
}
</script>

<style scoped>
.pageHeader {
    background-color: var(--grey);
}

.pageHeader i {
    font-size: 25px;
}

.greeting {
    padding-top: 30px;
}

.greeting p {
    font-family: text-bold;
    font-size: 20px;
    margin-bottom: 0px;
    text-align: center;
}

.pagePad {
    padding: 32px;
}

.pageHeading {
    padding: 0px;
    padding-bottom: 16px;
}

.pageHeading p {
    font-family: text-bold;
    font-size: 16px;
    color: var(--default-text);
}

.goals {
    background-color: var(--default-white);
    padding: 0 16px;
    border-radius: 6px;
    margin-bottom: 16px;
}

.lowSlotAlert {
    font-family: text-medium;
    font-size: 12px;
    color: var(--default-white);
    background-color: var(--yellow);
    border-radius: 6px;
    margin: 16px 0;
}

.goalInfo {
    padding-bottom: 10px;
}

.goalInfo p {
    font-family: text-semibold;
    font-size: 12px;
    margin-bottom: 0px;
}

.infoHead {
    padding-top: 16px;
    font-family: text-bold;
    font-size: 18px;
    color: var(--default-text);
    margin-bottom: 10px;
}

.subhead {
    font-family: text-semibold;
    font-size: 12px;
    color: var(--text-highlight);
    margin-bottom: 5px;
}

.vertical {
    display: flex;
}

.vertical .goalInfo {
    padding-right: 30px;
}
</style>