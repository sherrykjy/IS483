<template>
    <div class="basicHeader">
        <p>Log in</p>
    </div>

    <div class="image-container center">
        <img src="../assets/icons/login.png">
    </div>

    <div style="display: flex; flex-direction: column">
        <div style="width: 100%">
            <h1 class="loginHeading center">Log in to your account</h1>
        </div>

        <div class="loginForm">
            <form @submit.prevent="userLogin">
                <label for="userName" class="formLabel">Email:</label><br> <!-- need to add form handling here -->
                <input v-model="email" type="text" id="userName" class="formInput"><br><br>

                <label for="userName" class="formLabel">Password:</label><br> <!-- need to add form handling here -->
                <input v-model="password" type="password" id="userName" class="formInput"><br><br>

                <p id="loginErrorMsg" v-if="loginError"> {{ loginError }} </p> <!-- need to add v-if else here -->

                <button type="submit" class="formButton" style="color: var(--default-white); 
                background: var(--blue);"> <!-- need to add form handling here -->
                    Log in
                </button>
            </form>
        </div>

        <div class="center" style="width: 100%; display: flex; padding-bottom: 30px;">
            <p id="infoText">Don't have an account?</p>
            <a href="url" id="infoURL">Find out more</a>
        </div>

        <div class="center" style="width: 100%; display: flex; padding-bottom: 30px;">
            <img id="loginIcon1" src="../assets/icons/hpb.png">
            <img id="loginIcon2" src="../assets/icons/h365.png">
        </div>
    </div>
</template>

<style scoped>
.loginHeading {
    font-family: text-black;
    color: var(--default-text);
    font-size: 27px;
    text-align: centre;
}

.loginForm {
    padding: 20px 50px;
}

.image-container, .image-container img {
    width: 100%;
    height: auto;
    padding: 16px;
}

.image-container img {
    padding-top: 50px;
    padding-bottom: 30px;
}

#loginErrorMsg {
    width: 100%;
    padding-left: 0px;
    color: var(--red);
    font-family: text-medium;
    font-size: 13px;
    text-align: left;
}

#infoText {
    font-family: text-medium;
    font-size: 15px;
    color: var(--default-text);
    padding-right: 10px;
    margin-bottom: 0px;
}

#infoURL {
    font-family: text-medium;
    font-size: 15px;
    color: var(--blue);
}

#loginIcon1 {
    width: 25%;
}

#loginIcon2 {
    width: 15%;
}
</style>

<script>
export default {
    data() {
        return {
            email: '', // Bind to the email input
            password: '', // Bind to the password input
            loginError: '' // To store any login error message
        };
    },
    methods: {
        // Send HTTP Post for user login
        async userLogin() {
            console.log("User login attempt");
            
            try {
                const response = await this.$http.post("http://127.0.0.1:5009/user_login", {
                        email: this.email,
                        password: this.password
                })
                this.loginError = "";
                console.log("Login successful:", response.data);

                // Check for first login from user
                const userResponse = await this.$http.get("http://127.0.0.1:5001/user/" + this.email);
                console.log(userResponse);
                const userData = userResponse["data"]["data"];
                console.log(userData);

                const userId = userData["user_id"];
                const userEmail = userData["email"];

                 // Store user data in session storage
                sessionStorage.setItem('userId', userId);
                sessionStorage.setItem('userEmail', userEmail);

                // Set userId and userEmail in Vuex
                this.$store.commit('setUserId', userId);
                this.$store.commit('setUserEmail', userEmail);

                // If goal data is 0, goal has not been set yet, therefore first login
                if (userData["preferred_intensity"] == 0 || userData["target_minutes"] == 0 ) {
                    this.$router.push('/info');
                }
                // If goal data has been set, redirect to home page
                else {
                    this.$router.push('/home');
                }

            } catch (error) {
                this.loginError = "Invalid email or password.";
                console.log("Login error:", error);
            }
        }
    }
};
</script>