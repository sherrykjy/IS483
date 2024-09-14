<template>
    <div class="image-container center">
        <img src="../assets/icons/login.png">
    </div>

    <div style="display: flex; flex-direction: column">
        <div style="width: 100%">
            <h1 class="loginHeading">Log in to your account</h1>
        </div>

        <div style="width: 100%">
            <form>
                <label for="userName" class="formLabel">Email:</label><br> <!-- need to add form handling here -->
                <input type="text" id="userName" class="formInput"><br><br>

                <label for="userName" class="formLabel">Password:</label><br> <!-- need to add form handling here -->
                <input type="password" id="userName" class="formInput"><br><br>

                <p id="loginErrorMsg"> Invalid email or password. </p> <!-- need to add v-if else here -->

                <button class="formButton" style="color: var(--default-white); 
                background: var(--blue);"> <!-- need to add form handling here -->
                    Log in
                </button>
            </form>
        </div>

        <div class="center" style="width: 100%; display: flex;">
            <p id="infoText">Don't have an account?</p>
            <a href="url" id="infoURL">Find out more</a>
        </div>

        <div class="center" style="width: 100%; display: flex;">
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

.image-container, .image-container img {
    width: 100%;
    height: auto;
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
</script>