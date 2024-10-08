<template>
    <div class="stickyHeader">
        <div class="pageHeader">
            <p> Your Monthly Report </p>
        </div>

        <div class="pagePad">
            <div class="colDisplay">
                <div>
                    <div class="card drop-shadow">
                        <div class="content">
                                <p class="actual"> {{ topActivity }} </p>
                                <p class="label"> Top Activity </p>
                                <img src="../assets/icons/report/trophy.png" class="cardimg">
                        </div>

                    </div>
                </div>

                <div>
                    <div class="card drop-shadow">
                        <div class="content">
                                <p class="actual"> {{ currentStreak }} </p>
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
                                <p class="actual"> {{ totalDistance }} KM </p>
                                <p class="label"> Total Distance </p>
                                <img src="../assets/icons/report/distance.png" class="cardimg">
                        </div>

                    </div>
                </div>

                <div>
                    <div class="card drop-shadow">
                        <div class="content">
                                <p class="actual"> {{ totalTime }} </p>
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
        labels: [1, 2, 3, 4, 5, 31],
        datasets: [
          {
            data: [65, 59, 80, 81, 56, 55, 40],
            fill: false,
            borderColor: 'rgb(28, 131, 225)',
            tension: 0.1,
            pointBackgroundColor: 'white',
            pointRadius: 3
          }
        ]
      },
      totalDistance: 100,
      totalTime: 1000,
      topActivity: 'Running',
      currentStreak: 14,
    };
  }
};
</script>

<style scoped>
.pagePad {
    padding: 32px;
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