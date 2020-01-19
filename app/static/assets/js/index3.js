$(function() {
    "use strict";
	  
	  // chart 1
	 
		  var ctx = document.getElementById('add-impressions-frequency-reach').getContext('2d');
		
			var myChart = new Chart(ctx, {
				type: 'bar',
				data: {
					labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
					datasets: [{
						label: 'Impressions',
						data: [25, 23, 27, 15, 27, 23, 31, 41],
						backgroundColor: 'rgba(59, 89, 152, 0.55)',
						borderColor: "transparent",
						borderWidth: 3
					},{
						label: 'Reach',
						data: [20, 18, 21, 10, 21, 18, 26, 36],
						backgroundColor: 'rgba(54, 241, 205, 0.55)',
						borderColor: "transparent",
						borderWidth: 3
					}, {
						label: 'Frequency',
						type: 'line',
						data: [10, 8, 12, 5, 12, 8, 16, 25],
						backgroundColor: "rgba(59, 89, 152, 0.35)",
						borderColor: "#3b5998",
						pointBackgroundColor:'transparent',
                        pointHoverBackgroundColor:'transparent',
						pointBorderWidth :0,
						pointRadius :0,
						pointHoverRadius :0,
						borderWidth: 2
						
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
					  display: true ,
					  color: "rgba(0, 0, 0, 0.05)"
					},
				  }],
				   yAxes: [{
					ticks: {
						beginAtZero:true,
						fontColor: '#585757'
					},
					gridLines: {
					  display: true ,
					  color: "rgba(0, 0, 0, 0.05)"
					},
				  }]
				 }

			 }
			}); 


			// chart 4

		var ctx = document.getElementById('cpm-ctr').getContext('2d');
		
			var myChart = new Chart(ctx, {
				type: 'line',
				data: {
					labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
					datasets: [{
						label: 'CPM',
						data: [3, 3, 8, 5, 7, 4, 6, 4, 6, 3, 5, 7],
						backgroundColor: '#3b5998',
						borderColor: "transparent",
						pointRadius :"0",
						borderWidth: 3
					}, {
						label: 'CTR',
						data: [7, 5, 14, 7, 12, 6, 10, 6, 11, 5, 9, 11],
						backgroundColor: "rgba(59, 89, 152, 0.4)",
						borderColor: "transparent",
						pointRadius :"0",
						borderWidth: 1
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
					ticks: {
						beginAtZero:true,
						fontColor: '#585757'
					},
					gridLines: {
					  display: true ,
					  color: "rgba(0, 0, 0, 0.05)"
					},
				  }],
				   yAxes: [{
					ticks: {
						beginAtZero:true,
						fontColor: '#585757'
					},
					gridLines: {
					  display: true ,
					  color: "rgba(0, 0, 0, 0.05)"
					},
				  }]
				 }

			 }
			}); 



        // chart 2

 var ctx = document.getElementById("impressions-add").getContext('2d');

      var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ["Gaining Insights", "Best Dashboard Features", "Manage data flows", "Understanding data", "Data Hero Training"],
          datasets: [{
            backgroundColor: [
              'rgb(59, 89, 152)',
              'rgba(59, 89, 152, 0.80)',
              'rgba(59, 89, 152, 0.60)',
              'rgba(59, 89, 152, 0.40)',
              'rgba(59, 89, 152, 0.30)',
              'rgba(59, 89, 152, 0.20)'
            ],
            hoverBackgroundColor: [
              'rgb(59, 89, 152)',
              'rgba(59, 89, 152, 0.80)',
              'rgba(59, 89, 152, 0.60)',
              'rgba(59, 89, 152, 0.40)',
              'rgba(59, 89, 152, 0.30)',
              'rgba(59, 89, 152, 0.10)'
            ],
            data: [34178, 27641, 18874, 10687, 8947],
      borderWidth: [1, 1, 1, 1, 1]
          }]
        },
        options: {
      cutoutPercentage: 65,
            legend: {
        position: 'right',
              display: true,
        labels: {
                boxWidth:40
              }
            },
      tooltips: {
        displayColors:false,
      }
        }
      });


  // chart 3

	   var ctx = document.getElementById("freqency-add").getContext('2d');
			var myChart = new Chart(ctx, {
				type: 'bar',
				data: {
					labels: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
					datasets: [{
						label: 'Manage data flows',
						data: [39, 19, 25, 16, 31, 39, 23, 20, 23, 18, 15, 20],
						backgroundColor: "rgb(2, 166, 242)"
					},{
						label: 'Gaining Insights',
						data: [27, 12, 26, 15, 21, 27, 13, 19, 32, 22, 18, 30],
						backgroundColor: "rgba(2, 166, 242, 0.8)"
					},{
						label: 'Best Dashboard Features',
						data: [27, 12, 26, 15, 21, 27, 13, 19, 32, 22, 18, 30],
						backgroundColor: "rgba(2, 166, 242, 0.6)"
					},{
						label: 'Data Hero Training',
						data: [27, 12, 26, 15, 21, 27, 13, 19, 32, 22, 18, 30],
						backgroundColor: "rgba(2, 166, 242, 0.4)"
					},{
						label: 'Understanding data',
						data: [27, 12, 26, 15, 21, 27, 13, 19, 32, 22, 18, 30],
						backgroundColor: "rgba(2, 166, 242, 0.2)"
					}]
				},
				options: {
					legend: {
					  display: true,
					  position: 'bottom',
					  labels: {
						fontColor: '#3e3e3e',  
						boxWidth:13
					  }
					},
					tooltips: {
					  enabled:true,
					  displayColors:false,
					},	
					
					scales: {
					  xAxes: [{
					  	 stacked: true,
						  barPercentage: .5,
						display: false,
						gridLines: false
					  }],
					  yAxes: [{
					  	stacked: true,
						display: false,
						gridLines: false
					  }]
					}

			 }
			 
			});





			  });	

