function drawChart(title, elementId, data) {
    var ctx = document.getElementById(elementId).getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["7:00", "7:15", "7:45", "8:00",
                "8:15", "8:30", "8:45", "9:00",
                "9:15", "9:30", "9:45", "10:00"],
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

function getDataAndDrawChart(destination, title, elementId) {
    $.ajax({
        url: '/calculate-averages',
        type: 'get',
        dataType: 'json',
        data: {
            "destination": destination
        },
        success: function(data) {
            console.log(data)
            drawChart(title, elementId, data)
        },
        error: function(jqxhr, textStatus, errorThrown) {
            console.log("Couldn't retrieve duration averages")
            console.log(jqxhr)
            console.log(textStatus)
            console.log(errorThrown)
        }
    })
}

getDataAndDrawChart("work", "Work Journey Duration", "work-chart")
getDataAndDrawChart("home", "Home Journey Duration", "home-chart")
