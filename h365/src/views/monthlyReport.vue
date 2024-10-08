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
                                <p class="actual"> {{ streakCount }} </p>
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

export default {
  components: {
    ChartComponent
  },

  data() {
    return {
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
        mr_allActivitites: {}, // Empty object to be filled later
        mr_month: this.$route.params.mr_month || 0,

        temp: []
    };
  },

  mounted() {
    console.log('Route params:', this.$route.params); // Log all route parameters

    if (this.$route.params.mr_allActivitites) {
        try {
            // Parse the JSON string passed in mr_allActivitites
            this.mr_allActivitites = JSON.parse(this.$route.params.mr_allActivitites);
            console.log('Parsed Activities:', this.mr_allActivitites); // Log parsed activities

            this.populateChartData();
        } catch (error) {
            console.error("Error parsing mr_allActivitites:", error);
        }
    } else {
        console.error("mr_allActivitites is undefined.");
    }
  },

//   async mounted() {
//     try {
//         this.populateChartData();
//     } catch (error) {
//             console.log("error:", error);
//         }
//   },

//   {7: 6001.5, 14: 5708.5, 21: 7104.9, 28: 6006.2}

  methods: {
    populateChartData() {
        const totalDaysInMonth = new Date(2024, this.mr_month, 0).getDate(); // Get the total number of days in the month

        this.chartData.labels = Array.from({ length: totalDaysInMonth }, (_, i) => i + 1);
        console.log(this.chartData.labels)

        const activities = this.mr_allActivitites; // Reference the activities object
        this.temp = [];

        // Loop through all days of the month (1-based index for days)
        for (let i = 1; i <= totalDaysInMonth; i++) {
            // Check if the current day (i) exists in the activities object
            if (activities.hasOwnProperty(i)) {
                this.temp.push(activities[i]); // If it exists, add the value to the temp array
            } else {
                this.temp.push(0); // If it doesn't exist, append 0
            }
        }

        console.log("haha", this.temp)

        // Update the chartData with the populated temp array
        this.chartData.datasets[0].data = this.temp;
        
        console.log("Populated Chart Data:", this.chartData.datasets[0].data); // Log the populated chart data
    }
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