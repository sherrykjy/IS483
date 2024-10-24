<template>
    <div class="pageHeader">
        <p> Set Your Fitness Goals </p>
    </div>

    <div class="container" style="padding: 32px 40px 0 40px; display: flex; align-items: center;">
        <div class="image">
            <img src="../assets/icons/goal/goal1.png" style="width: 90px; height: auto;">
        </div>

        <div class="vertical">
            <p class="head"> Whether you're just starting or pushing your limits, setting the right goals can keep you motivated and on track. </p>
            <p class="body"> Note: You can change your mind! </p>
            <p class="body"> Revisit your goals anytime via the in-app profile. </p>
        </div>

    </div>

    <div class="container">
        <div class="banner">
            <div class="text">
                <p class="body"> Youths aged 13-17 should aim for at least 150 minutes
                    of moderate to high intensity physical activity every week </p>
            </div>

            <div class="image">
                <img src="../assets/icons/goal/goal2.png">
            </div>
        </div>
    </div>

    <div class="container">
        <form @submit.prevent="submitGoal" novalidate>
            <div class="question">
                <div class="label">
                    What is your target number of MVPA minutes per week?
                    <span class="compulsory">*</span>
                </div>

                <div class="input drop-shadow">
                    <input type="number" v-model="goal" name="goal" 
                    id="goal" placeholder="Input your weekly target" step="1">
                </div>

                <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
            </div>

            <div class="question">
                <div class="label">
                    What is the intensity of physical activity you are comfortable with?
                    <span class="compulsory"> * </span>
                </div>

                <div class="radio-buttons">
                    <div class="selection">
                        <label class="radio-button" :class="{ selected: selectedIntensity === '1' }">
                            <input type="radio" v-model="selectedIntensity" value="1" />
                            1
                        </label>
                        <p> Low </p>
                    </div>

                    <div class="selection">
                        <label class="radio-button" :class="{ selected: selectedIntensity === '2' }">
                            <input type="radio" v-model="selectedIntensity" value="2" />
                            2
                        </label>
                        <p> Moderate </p>
                    </div>

                    <div class="selection">
                        <label class="radio-button" :class="{ selected: selectedIntensity === '3' }">
                            <input type="radio" v-model="selectedIntensity" value="3" />
                            3
                        </label>
                        <p> High </p>
                    </div>
                </div>

                <div class="info">
                    <p>
                        <span> Light: </span>
                        Gentle activities eg. walking, yoga
                    </p>

                    <p>
                        <span> Moderate: </span>
                        Activities that increase heart rate, eg. cycling swimming
                    </p>

                    <p>
                        <span> High: </span>
                        Intense activities eg. running, HIIT workouts
                    </p>
                </div>

            </div>

            <button class="formButton" style="color: var(--default-white); 
                background: var(--green); margin-top: 15px;">
                Submit
            </button>
        </form>

    </div>

</template>

<script>
import { useStore } from 'vuex';
import { computed } from 'vue';

export default {
    setup() {
        console.log("goal setting page");
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
            selectedIntensity: '',
            goal: '',
            errorMessage: ''
        }
    },
    methods: {
        async submitGoal() {
            this.errorMessage = '';

            // validate goal input
            if (this.goal < 150) {
                console.log("error in goal input");
                this.errorMessage = "Please enter a valid weekly target of at least 150 minutes.";
                return;
            } else if (!Number.isInteger(Number(this.goal))) {
                console.log("invalid numeric input");
                this.errorMessage = "Please enter a valid whole number of at least 150.";
                return;
            }
            
            try {
                console.log("Submit goal attempt");
                console.log("User email:", this.userEmail);
                const userResponse = await this.$http.patch("http://127.0.0.1:5001/user/" + this.userEmail, {
                        target_minutes: this.goal,
                        preferred_intensity: this.selectedIntensity,
                        goal_date: new Date().toISOString().split('T')[0]
                })
                console.log(userResponse);

                const goalResponse = await this.$http.post("http://127.0.0.1:5011/goal", {
                    user_id: this.userId,
                    goal_description: "Hit MVPA goal",
                    tier: 1,
                    completed: false,
                    target: this.goal
                })
                console.log(goalResponse);

                this.$router.push('/home');
            }
            catch (error) {
                console.log(error);
            }
        }
    }
}
</script>

<style scoped>
.container {
    padding: 32px 32px 0 32px;
    /* display: flex; */
    justify-content: center;
}

.banner {
    display: flex;
    background-color: var(--orange);
    border-radius: 6px;
    align-items: center;
    justify-content: space-between;
}

.text {
    padding: 16px;
}

.text p {
    margin-bottom: 0;
    color: var(--default-white);
}

.vertical {
    flex-direction: column;
}

.vertical p {
    margin-bottom: 0;
}

.vertical .head {
    font-family: text-semibold;
    font-size: 12px;
    color: var(--default-text);
    text-align: justify;
    margin-bottom: 5px;
}

.vertical .body {
    font-family: text-medium;
    font-size: 10px;
    color: var(--text-highlight);
    font-style: italic;
}

.body {
    font-family: text-regular;
    font-size: 12px;
    text-align: justify;
}

.image img {
    width: 120px;
    padding-right: 10px;
}

.question {
    padding-bottom: 16px;
    width: 100%;
}

.label {
    font-family: text-regular;
    font-size: 15px;
    color: var(--text-highlight);
    margin-bottom: 16px;
}

.compulsory {
    color: var(--red);
    margin-left: 5px;
}

input {
    border: none;
    width: 100%;
    height: 40px;
    padding: 0 10px;
    font-family: text-medium;
    font-size: 14px;
    color: var(--text-highlight);
}

.input {
    background-color: white;
    border-radius: 6px;
    height: 40px;
}

.selection {
    text-align: center;
    font-family: text-regular;
    color: var(--text-highlight);
}

.radio-buttons {
    display: flex;
    gap: 10px;
    font-size: 13px;
}

.radio-button {
    display: inline-block;
    padding: 10px 20px;
    border: 2px solid #ccc;
    border-radius: 6px;
    cursor: pointer;
    text-align: center;
    width: 100px;
    transition: background-color 0.3s, border-color 0.3s;
    margin-bottom: 5px;
}

.radio-button input[type="radio"] {
  display: none;
}

.radio-button.selected {
  background-color: var(--text-highlight);
  color: white;
  border-color: var(--text-highlight);
}

.info {
    font-size: 10px;
    font-style: italic;
    color: var(--text-highlight);
}

.info p{
    margin-bottom: 0;
    font-family: text-medium;
}

.info span {
    font-family: text-bold;
}

.error-message {
    color: var(--red);
    font-size: 12px;
    margin-top: 5px;
}

</style>