<template>
    <div class="pageHeader">
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

                <!-- <div class="input drop-shadow">
                    <select v-model="selectedSchool" name="schools" id="schools" class="school-select">
                        <option value="" disabled>Select your school</option>
                        <option v-for="school in schools" :key="school.value" :value="school.value">
                            {{ school.text }}
                        </option>
                    </select>
                </div> -->

                <div class="input drop-shadow">
                    <input
                        type="text"
                        v-model="searchSchool"
                        @input="filterSchools"
                        @focus="showSchoolDropdown = true"
                        placeholder="Select your school"
                        class="region-input"
                    />

                    <ul v-show="showSchoolDropdown && filteredSchools.length > 0" class="dropdown-list">
                        <li v-for="school in filteredSchools" :key="school.value" @mousedown="selectSchool(school)">
                            {{ school.text }}
                        </li>
                    </ul>
                    <!-- {{ selectedSchool }} -->
                </div>
            </div>

            <div class="question">
                <div class="label">
                    Where do you stay
                    <div class="compulsory">*</div>
                </div>

                <div class="input drop-shadow">
                    <input
                        type="text"
                        v-model="searchTerm"
                        @input="filterRegions"
                        @focus="showDropdown = true"
                        placeholder="Select your region"
                        class="region-input"
                    />

                    <ul v-show="showDropdown && filteredRegions.length > 0" class="dropdown-list">
                        <li v-for="region in filteredRegions" :key="region.value" @mousedown="selectRegion(region)">
                            {{ region.text }}
                        </li>
                    </ul>
                    <!-- {{ selectedRegion }} -->
                </div>
            </div>

            <button class="formButton" style="color: var(--default-white); 
                background: var(--green); margin-top: 15px;"> <!-- need to add form handling here -->
                Submit
            </button>

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


.school-select {
    width: 100%;
    height: 40px;
    border: none;
    background-color: white;
    border-radius: 6px;
    padding: 0 10px;
    appearance: none;
    display: block;

    font-family: text-medium;
    font-size: 14px;
    color: var(--text-highlight);
}

.region-input, .dropdown-list {
    padding: 0 10px;
    font-family: text-medium;
    font-size: 14px;
    color: var(--text-highlight);
}

.region-input {
    width: 100%;
    height: 40px;
    border: none;
    border-radius: 6px;
    margin-bottom: 8px;
    box-sizing: border-box;
}

.dropdown-list {
    list-style-type: none;
    padding: 10px 10px 0 10px;
    margin: 0;
    position: absolute;
    width: calc(100% - 2px);
    border: 1px solid car(--text-highlight);
    border-radius: 6px;
    background-color: white;
    max-height: 400px;
    overflow-y: auto;
    z-index: 10;
    box-sizing: border-box;
}

li {
    padding-bottom: 10px;
}

ul.dropdown-list {
    width: 326px;
}

</style>

<script>
export default {
    data() {
        return {
            height: null,
            weight: null,

            searchSchool: '',
            selectedSchool: '',
            showSchoolDropdown: false,
            schools: [
                {value: 'bgss', text: 'Bedok Green Secondary School'},
                {value: 'prss', text: 'Pasir Ris Secondary School'},
                {value: 'tjc', text: 'Temasek Junior College'},
                {value: 'sp', text: 'Singapore Polytechnic'}
            ],
            filteredSchools: [],

            searchTerm: '',
            selectedRegion: '',
            showDropdown: false,
            regions: [
                { value: 'bedok', text: 'Bedok' },
                { value: 'bishan', text: 'Bishan' },
                { value: 'clementi', text: 'Clementi' },
                { value: 'jurong', text: 'Jurong' },
                { value: 'pasir_ris', text: 'Pasir Ris' },
                { value: 'serangoon', text: 'Serangoon' },
                { value: 'tampines', text: 'Tampines' },
                { value: 'woodlands', text: 'Woodlands' },
                { value: 'yishun', text: 'Yishun' }
            ],
            filteredRegions: []
        }
    },
    methods: {
        filterRegions() {
            this.filteredRegions = this.regions.filter(region =>
            region.text.toLowerCase().includes(this.searchTerm.toLowerCase())
            );
        },
        selectRegion(region) {
            this.searchTerm = region.text;
            this.selectedRegion = region.value;
            this.showDropdown = false;
        },

        filterSchools() {
            this.filteredSchools = this.schools.filter(school =>
            school.text.toLowerCase().includes(this.searchSchool.toLowerCase())
            );
        },
        selectSchool(school) {
            this.searchSchool = school.text;
            this.selectedSchool = school.value;
            this.showSchoolDropdown = false;
        }
    },
    mounted() {
        this.filteredRegions = this.regions;
        this.filteredSchools = this.schools;
    }
}
</script>