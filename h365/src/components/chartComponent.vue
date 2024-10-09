<!-- <template>
    <div>
        <canvas ref="chartCanvas"></canvas>
    </div>
</template>

<script>
import { Chart } from 'chart.js/auto';

export default {
    props: {
        chartData: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            chartInstance: null // To keep track of the chart instance
        };
    },
    mounted() {
        this.renderChart();
    },
    watch: {
        chartData: {
            handler() {
                this.updateChart(); // Call update method when chartData changes
            },
            deep: true // Watch nested changes in chartData
        }
    },
    methods: {
        renderChart() {
            const ctx = this.$refs.chartCanvas.getContext('2d');
            this.chartInstance = new Chart(ctx, {
                type: 'line',
                data: this.chartData,
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        }
                    },
                    scales: {
                        x: {
                            grid: {
                                display: false
                            },
                            ticks: {
                                font: {
                                    family: 'text-regular',
                                    size: 12
                                }
                            }
                        },
                        y: {
                            grid: {
                                display: false
                            },
                            ticks: {
                                font: {
                                    family: 'text-regular',
                                    size: 12
                                }
                            }
                        }
                    }
                }
            });
        },
        updateChart() {
            if (this.chartInstance) {
                // Update the data and re-render the chart
                this.chartInstance.data = this.chartData;
                this.chartInstance.update();
            } else {
                // If chart instance is not available, render a new chart
                this.renderChart();
            }
        }
    }
}
</script>

<style scoped>
canvas {
    width: 100%;
    height: 400px; /* Adjust height as needed */
}
</style> -->

<template>
    <div>
        <canvas ref="chartCanvas"></canvas>
    </div>
</template>

<script>
import { Chart } from 'chart.js/auto';

export default {
    props: {
        chartData: {
            type: Object,
            required: true
        }
    },
    mounted() {
        this.renderChart();
    },
    methods: {
        renderChart() {
            const ctx = this.$refs.chartCanvas.getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: this.chartData,
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        }
                    },
                    scales: {
                        x: {
                            grid: {
                                display: false
                            },
                            ticks: {
                                font: {
                                    family: 'text-regular',
                                    size: 12
                                }
                            }
                        },
                        y: {
                            grid: {
                                display: false
                            },
                            ticks: {
                                font: {
                                    family: 'text-regular',
                                    size: 12
                                }
                            }
                        }
                    }
                }
            });
        }
    }
}
</script>

<style scoped>
canvas {
    width: 100%;
    height: 400px; /* Adjust height as needed */
}
</style>