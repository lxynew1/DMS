$(function() {
    "use strict";


    // chart 1

       var ctx = document.getElementById('imp-per-post').getContext('2d');

      var gradient1 = ctx.createLinearGradient(0, 0, 0, 500);
          gradient1.addColorStop(0, 'rgba(59, 89, 152, 0.3)');
          gradient1.addColorStop(1, 'rgba(255,255,255,0)');
              
       var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
          datasets: [{
            label: 'Impressions per Post',
            data: [800, 800, 670, 930, 790 , 1100, 800, 920],
            backgroundColor: 'transparent',
            borderColor: '#3b5998',
            pointBackgroundColor:'#fff',
            pointHoverBackgroundColor:'#fff',
            pointBorderColor :'#3b5998',
            pointHoverBorderColor :'#3b5998',
            lineTension :'0',
            pointBorderWidth :2,
            pointRadius :4,
            pointHoverRadius :4,
            borderWidth: 3,
          }]
        }
        ,
        options: {
            legend: {
        position: false,
              display: true,
            },
      tooltips: {
        displayColors:false,
      },  
        scales: {
          xAxes: [{
          barPercentage: .4,
          ticks: {
            beginAtZero:true,
            fontColor: '#585757'
          },
          gridLines: {
            display: false ,
            color: "rgba(0, 0, 0, 0.05)"
          },
          }],
           yAxes: [{
          ticks: {
            beginAtZero:true,
            fontColor: '#585757'
          },
          gridLines: {
            display: false ,
            color: "rgba(0, 0, 0, 0.05)"
          },
          }]
         }
        }
      });




       // chart 2

       var ctx = document.getElementById('reach-per-post').getContext('2d');

      var gradient2 = ctx.createLinearGradient(0, 0, 0, 300);
          gradient2.addColorStop(0, 'rgba(85, 172, 238, 0.3)');
          gradient2.addColorStop(1, 'rgba(255,255,255,.2)');
              
       var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
          datasets: [{
            label: 'Avg Reach Per Post',
            data: [600, 620, 530, 610 , 540, 770, 700, 800],
            backgroundColor: 'transparent',
            borderColor: '#14abef',
            pointBackgroundColor:'#fff',
            pointHoverBackgroundColor:'#fff',
            pointBorderColor :'#14abef',
            pointHoverBorderColor :'#14abef',
            lineTension :'0',
            pointBorderWidth :2,
            pointRadius :4,
            pointHoverRadius :4,
            borderWidth: 3,
          }]
        }
        ,
        options: {
            legend: {
        position: false,
              display: true,
            },
      tooltips: {
        displayColors:false,
      },  
        scales: {
          xAxes: [{
          barPercentage: .4,
          ticks: {
            beginAtZero:true,
            fontColor: '#585757'
          },
          gridLines: {
            display: false ,
            color: "rgba(0, 0, 0, 0.05)"
          },
          }],
           yAxes: [{
          ticks: {
            beginAtZero:true,
            fontColor: '#585757'
          },
          gridLines: {
            display: false ,
            color: "rgba(0, 0, 0, 0.05)"
          },
          }]
         }
        }
      });



// chart 2
   
      var ctx = document.getElementById('post-reaction').getContext('2d');
    
      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
          datasets: [{
            label: 'Reactions',
            data: [15, 8, 12, 5, 12, 8, 16, 25, 15, 10, 20, 10, 0],
            backgroundColor: "transparent",
            borderColor: "#3b5998",
            pointBackgroundColor:'#fff',
            pointHoverBackgroundColor:'#fff',
            lineTension :'0',
            pointBorderWidth :2,
            pointRadius :4,
            pointHoverRadius :4,
            borderWidth: 3,
          }]
        },
      options: {
        legend: {
          display: true,
          labels: {
          fontColor: '#585757',  
          boxWidth:40
          }
        },
        tooltips: {
          displayColors:false
        },  
        scales: {
          xAxes: [{
          barPercentage: .4,
          ticks: {
            beginAtZero:true,
            fontColor: '#585757'
          },
          gridLines: {
            display: false ,
            color: "rgba(0, 0, 0, 0.05)"
          },
          }],
           yAxes: [{
          ticks: {
            beginAtZero:true,
            fontColor: '#585757'
          },
          gridLines: {
            display: false ,
            color: "rgba(0, 0, 0, 0.05)"
          },
          }]
         }

       }
      }); 







    });	