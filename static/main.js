function drawChart(title, elementId, labels, data) {
    var ctx = document.getElementById(elementId).getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Average Journey Time in Minutes Per Day',
                data: data,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            title: {
                display: true,
                text: title
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

function getDataAndDrawChart(destination, title, elementId, labels) {
    $.ajax({
        url: '/calculate-averages',
        type: 'get',
        dataType: 'json',
        data: {
            "destination": destination
        },
        success: function(data) {
            console.log(data)
            drawChart(title, elementId, labels, data)
        },
        error: function(jqxhr, textStatus, errorThrown) {
            console.log("Couldn't retrieve duration averages")
            console.log(jqxhr)
            console.log(textStatus)
            console.log(errorThrown)
        }
    })
}
morning_times = ["7:00", "7:15", "7:45", "8:00", "8:15", "8:30", "8:45", "9:00", "9:15", "9:30", "9:45", "10:00"]
evening_times = ["17:00", "17:15", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45",
    "20:00"]
getDataAndDrawChart("work", "Work Journey Duration", "work-chart", morning_times)
getDataAndDrawChart("home", "Home Journey Duration", "home-chart", evening_times)
