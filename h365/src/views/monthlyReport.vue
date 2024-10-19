<template>
    <div class="stickyHeader">
        <div class="pageHeader">
            <i class="uil uil-angle-left"></i>
            <p> Your Monthly Report </p>
        </div>

        <div class="pagePad">
            <div class="colDisplay">
                <div>
                    <div class="card drop-shadow">
                        <div class="content">
                                <p class="actual"> {{ mr_topActivity }} </p>
                                <p class="label"> Top Activity </p>
                                <img src="../assets/icons/report/trophy.png" class="cardimg">
                        </div>

                    </div>
                </div>

                <div>
                    <div class="card drop-shadow">
                        <div class="content">
                                <p class="actual"> 2 </p>
                                <p class="label"> Current Streak </p>
                                <img src="../assets/icons/report/streak.png" class="cardimg">
                        </div>

                    </div>
                </div>
            </div>


            <div class="colDisplay">
                <div>
                    <div class="card drop-shadow">
                        <div class="content">
                                <p class="actual"> {{ mr_totalDistance }} KM </p>
                                <p class="label"> Total Distance </p>
                                <img src="../assets/icons/report/distance.png" class="cardimg">
                        </div>

                    </div>
                </div>

                <div>
                    <div class="card drop-shadow">
                        <div class="content">
                                <p class="actual"> {{ mr_movingMinutes }} </p>
                                <p class="label"> Moving Minutes </p>
                                <img src="../assets/icons/report/time.png" class="cardimg">
                        </div>

                    </div>
                </div>
            </div>


            <div class="card drop-shadow">
                <div class="content">
                    <p class="actual" style="font-size: 15px; margin-bottom: 5px;"> Activity Recorded </p>
                    <div class="chart">
                        <ChartComponent :chartData="chartData" style="height: 200px; width: 100%;"/>
                    </div>
                </div>
            </div>

        </div>
        
    </div>



</template>

<script>
import ChartComponent from '@/components/chartComponent.vue';
import { markRaw } from 'vue';

export default {
  components: {
    ChartComponent
  },

  data() {
    return {
        chartData: {
            labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            // labels: [],
            datasets: [
                {
                    // data: [],
                    data: [0, 0, 0, 0, 0, 0, 6001.5, 0, 0, 0, 0, 0, 0, 5708.5, 0, 0, 0, 0, 0, 0, 7104.9, 0, 0, 0, 0, 0, 0, 6006.2, 0, 0],
                    fill: false,
                    borderColor: 'rgb(28, 131, 225)',
                    tension: 0.1,
                    pointBackgroundColor: 'white',
                    pointRadius: 3
                }
            ]
        },
        streakCount: this.$route.params.streakCount || 0,
        mr_movingMinutes: this.$route.params.mr_movingMinutes || 0,
        mr_topActivity: this.$route.params.mr_topActivity || "",
        mr_totalDistance: Math.round((this.$route.params.mr_totalDistance / 1000), 2) || 0,
        mr_allActivitites: {},
        mr_month: this.$route.params.mr_month || 0,

        temp: []
    };
  },

  mounted() {
    console.log('Route params:', this.$route.params);

    if (this.$route.params.mr_allActivitites) {
        try {
            this.mr_allActivitites = JSON.parse(this.$route.params.mr_allActivitites);
            console.log('Parsed Activities:', this.mr_allActivitites);
            this.populateChartData();
        } catch (error) {
            console.error("Error parsing mr_allActivitites:", error);
        }
    } else {
        console.error("mr_allActivitites is undefined.");
    }
  },

  methods: {
    // populateChartData() {
    //     const totalDaysInMonth = new Date(2024, this.mr_month, 0).getDate();

    //     // Update labels (use Vue.set to ensure reactivity)
    //     this.$set(this.chartData, 'labels', Array.from({ length: totalDaysInMonth }, (_, i) => i + 1));
    //     console.log(this.chartData.labels);

    //     const activities = this.mr_allActivitites;
    //     this.temp = [];

    //     // Populate temp array
    //     for (let i = 1; i <= totalDaysInMonth; i++) {
    //         if (activities[i]) {
    //             this.temp.push(activities[i]);
    //         } else {
    //             this.temp.push(0);
    //         }
    //     }

    //     console.log("haha", this.temp);

    //     // Ensure reactivity for datasets[0].data
    //     this.$set(this.chartData.datasets[0], 'data', [...this.temp]);

    //     console.log("Populated Chart Data:", this.chartData.datasets[0].data);
    // }

    populateChartData() {
        const totalDaysInMonth = new Date(2024, this.mr_month, 0).getDate();

        // Create a shallow copy of chartData to avoid triggering unnecessary reactivity loops
        const newChartData = { ...this.chartData };

        // Update labels with a shallow copy
        newChartData.labels = Array.from({ length: totalDaysInMonth }, (_, i) => i + 1);
        console.log(newChartData.labels);

        const activities = this.mr_allActivitites;
        this.temp = [];

        // Populate temp array with activity data
        for (let i = 1; i <= totalDaysInMonth; i++) {
            if (activities[i]) {
                this.temp.push(activities[i]);
            } else {
                this.temp.push(0);
            }
        }

        console.log("haha", this.temp);

        // Update datasets[0].data with a shallow copy
        newChartData.datasets = [...this.chartData.datasets];
        newChartData.datasets[0] = { ...this.chartData.datasets[0], data: [...this.temp] };

        // Replace the entire chartData object with the updated copy
        // this.chartData = newChartData;

        this.chartData = markRaw(newChartData);

        console.log("Populated Chart Data:", this.chartData.datasets[0].data);
    }


    // populateChartData() {
    //     const totalDaysInMonth = new Date(2024, this.mr_month, 0).getDate();

    //     this.chartData.labels = Array.from({ length: totalDaysInMonth }, (_, i) => i + 1);
    //     console.log(this.chartData.labels);

    //     const activities = this.mr_allActivitites;
    //     this.temp = [];

    //     for (let i = 1; i <= totalDaysInMonth; i++) {
    //         if (activities[i]) {
    //             this.temp.push(activities[i]);
    //         } else {
    //             this.temp.push(0);
    //         }
    //     }

    //     console.log("haha", this.temp);
    //     // this.chartData.datasets[0].data = this.temp;
    //     this.chartData.datasets[0].data = [...this.temp];
    //     console.log("Populated Chart Data:", this.chartData.datasets[0].data);
    // }
  }
};
</script>


<!-- <script>
import ChartComponent from '@/components/chartComponent.vue';

export default {
  components: {
    ChartComponent
  },

  data() {
    return {
        // activities: JSON.parse(this.mr_allActivitites),
        chartData: {
            labels: [],
            datasets: [
                {
                    data: [],
                    fill: false,
                    borderColor: 'rgb(28, 131, 225)',
                    tension: 0.1,
                    pointBackgroundColor: 'white',
                    pointRadius: 3
                }
            ]
        },

        streakCount: this.$route.params.streakCount || 0,
        mr_movingMinutes: this.$route.params.mr_movingMinutes || 0,
        mr_topActivity: this.$route.params.mr_topActivity || "",
        mr_totalDistance: this.$route.params.mr_totalDistance || 0,
        mr_allActivitites: this.$route.params.mr_allActivitites || {},
        };
    },

    // props: ['streakCount', 'mr_movingMinutes', 'mr_topActivity', 'mr_totalDistance', 'mr_allActivitites', 'mr_month'],

    // props: {
    //     streakCount: {
    //         type: Number,
    //         default: 0
    //     },
    //     mr_movingMinutes: {
    //         type: Number,
    //         default: 0
    //     },
    //     mr_topActivity: {
    //         type: String,
    //         default: ""
    //     },
    //     mr_totalDistance: {
    //         type: Number,
    //         default: 0
    //     },
    //     mr_allActivitites: {
    //         type: Object,
    //         default: () => ({})
    //     },
    //     mr_month: {
    //         type: Number,
    //         default: 0
    //     }
    // },

    mounted() {
        console.log('Route params:', this.$route.params); // Log all params
        
        if (this.$route.params.mr_allActivitites) {
            console.log('Activities:', this.$route.params.mr_allActivitites); // Log mr_allActivitites
            try {
                this.mr_allActivitites = this.$route.params.mr_allActivitites;
            } catch (error) {
                console.error("Error parsing mr_allActivitites:", error);
            }
        } else {
            console.error("mr_allActivitites is undefined.");
        }
    },

    // mounted() {
    //     console.log("Streak Count:", this.streakCount);
    //     console.log("Moving Minutes:", this.mr_movingMinutes);
    //     console.log("Top Activity:", this.mr_topActivity);
    //     console.log("Total Distance:", this.mr_totalDistance);
    //     console.log("All Activities:", this.mr_allActivitites);

    //     this.currentStreak = this.streakCount;
    //     this.totalDistance = Math.round(this.mr_totalDistance / 1000);
    //     this.topActivity = this.mr_topActivity;
    //     this.allActivies = this.mr_allActivitites;
    //     this.totalTime = this.mr_movingMinutes;

    //     this.populateChartData();
    // },

    // methods: {
    //     populateChartData() {
    //         const totalDaysInMonth = new Date(2024, this.mr_month, 0).getDate();

    //         this.chartData.labels = Array.from({ length: totalDaysInMonth }, (_, i) => i + 1);

    //         this.chartData.datasets[0].data = this.chartData.labels.map(day => {
    //             return this.activities.hasOwnProperty(day) ? this.activities[day] : 0;
    //         });

    //         console.log("Populated Chart Data:", this.chartData.datasets[0].data);
    //     }
    // },
//     methods: {
//     populateChartData() {
//       const totalDaysInMonth = new Date(2024, this.mr_month, 0).getDate(); // Get the number of days in the month

//       // Generate labels for each day of the month
//       this.chartData.labels = Array.from({ length: totalDaysInMonth }, (_, i) => i + 1);

//       // Populate data for each day by referencing `mr_allActivitites`
//       this.chartData.datasets[0].data = this.chartData.labels.map(day => {
//         // Check if the day exists in `mr_allActivitites` and return the value, or return 0
//         return this.mr_allActivitites.hasOwnProperty(day) ? this.mr_allActivitites[day] : 0;
//       });

//       console.log("Chart Data:", this.chartData); // Log the final chart data for verification
//     }
//   }
};
</script> -->

<style scoped>
.pagePad {
    padding: 32px;
}

.pageHeader {
    background-color: var(--orange);
    color: var(--default-white);
}

.card {
    border: none;
}

.content {
    padding: 20px;
}

.heading {
    display: flex;
    align-items: center;
    margin-bottom: 5px;
}

.heading img {
    width: 45px;
    height: 45px;
}

.heading p {
    font-family: text-semibold;
    font-size: 14px;
    color: var(--default-text);
    margin-bottom: 0;
}

.colDisplay {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    width: 100%;
    padding-bottom: 16px;
}

.actual, .label {
    margin-bottom: 0;
    text-align: center;
}

.actual {
    font-family: text-bold;
    font-size: 20px;
    color: var(--text-highlight);
}

.label {
    font-family: text-medium;
    font-size: 14px;
    color: var(--text-highlight);
    margin-bottom: 5px;
}

.cardimg {
    width: 50px;
    height: auto;
    display: flex;
    margin: auto;
}

</style>