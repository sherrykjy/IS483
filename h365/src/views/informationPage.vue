<template>
    <div class="basicHeader">
        <p>Tell us more!</p>
    </div>

    <div class="container">
        <div class="banner">
            <div class="text">
                <p class="head"> Tell us more! </p>
                <p class="body"> Help us get to know you better to personalise 
                    your health journey! </p>
            </div>

            <div class="image">
                <img src="../assets/icons/info/icon.png">
            </div>
        </div>
    </div>

    <div class="container">
        <form action="">

            <div class="question">
                <div class="label">
                    Height (in CM) 
                    <div class="compulsory">*</div>
                </div>

                <div class="input drop-shadow">
                    <input type="number" v-model="height" name="height" id="height">
                </div>
            </div>

            <div class="question">
                <div class="label">
                    Weight (in KG) 
                    <div class="compulsory">*</div>
                </div>

                <div class="input drop-shadow">
                    <input type="number" v-model="weight" name="weight" id="weight">
                </div>
            </div>

            <div class="question">
                <div class="label">
                    Which school are you from
                    <div class="compulsory">*</div>
                </div>

                <div class="input drop-shadow">
                    <select v-model="selectedSchool" name="schools" id="schools" class="school-select">
                        <option value="" disabled>Select your school</option>
                        <option v-for="school in schools" :key="school.value" :value="school.value">
                            {{ school.text }}
                        </option>
                    </select>
                </div>
            </div>

            <div class="question">
                <div class="label">
                    Where do you stay
                    <div class="compulsory">*</div>
                </div>

                <div class="input drop-shadow">
                    <select v-model="selectedRegion" name="regions" id="regions" class="school-select">
                        <option value="" disabled>Select your region</option>
                        <option v-for="region in regions" :key="region.value" :value="region.value">
                            {{ region.text }}
                        </option>
                    </select>
                </div>
            </div>
        </form>
    </div>
</template>

<style scoped>
.container {
    padding: 32px 32px 0 32px;
}

.banner {
    display: flex;
    background-color: var(--blue);
    border-radius: 6px;
}

.text {
    padding: 16px;
}

.text p {
    margin-bottom: 0;
    color: var(--default-white);
}

.head {
    font-family: text-bold;
    font-size: 18px;
}

.body {
    font-family: text-regular;
    font-size: 14px;
    text-align: justify;
}

.image img {
    width: 120px;
    height: 120px;
}

.question {
    padding-bottom: 16px;
}

.label {
    display: flex;
    margin-bottom: 10px;

    font-family: text-regular;
    font-size: 15px;
    color: var(--text-highlight);
}

.compulsory {
    color: var(--red);
    margin-left: 5px;
}

input {
    border: none;
}

.input {
    background-color: white;
    border-radius: 6px;
    width: 100%;
    height: 40px;
    border: none;
}

input {
    border: none;
    width: 100%;
    height: 40px;
    padding: 0 10px;
}

.school-select {
    width: 100%;
    height: 40px;
    border: none;
    background-color: white;
    border-radius: 6px;
    padding: 0 10px;
    appearance: none;
    font-family: text-medium;
    font-size: 14px;
    color: var(--text-highlight);
}

</style>

<script>
export default {
    data() {
        return {
            height: null,
            weight: null,
            selectedSchool: '',
            schools: [
                {value: 'bgss', text: 'Bedok Green Secondary School'},
                {value: 'prss', text: 'Pasir Ris Secondary School'},
                {value: 'tjc', text: 'Temasek Junior College'},
                {value: 'sp', text: 'Singapore Polytechnic'}
            ],
            selectedRegion: '',
            regions: [
                {value: 'bedok', text: 'Bedok'},
                {value: 'bishan', text: 'Bishan'},
                {value: 'tampines', text: 'Tampines'},
                {value: 'woodlands', text: 'Woodlands'}
            ]
        }
    }
}
</script>