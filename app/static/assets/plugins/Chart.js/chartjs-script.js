
(function(window, document, $, undefined) {
	  "use strict";
	$(function() {

		if ($('#lineChart').length) {
			
			var ctx = document.getElementById('lineChart').getContext('2d');
			var myChart = new Chart(ctx, {
				type: 'line',
				data: {
					labels: ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'],
					datasets: [{
						label: 'Facebook',
						data: [13, 20, 4, 18, 7, 4, 8],
						backgroundColor: "rgba(59, 89, 152, 0.25)",
						borderColor: "#3b5998",
						pointRadius :"0",
						borderWidth: 2
					}, {
						label: 'Twitter',
						data: [3, 30, 6, 6, 3, 4, 11],
						backgroundColor: "rgba(85, 172, 238, 0.25)",
						borderColor: "#55acee",
						pointRadius :"0",
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
				  enabled:false
				},	
			  scales: {
				  xAxes: [{
					ticks: {
						beginAtZero:true,
						fontColor: '#585757'
					},
					gridLines: {
					  display: true ,
					  color: "rgba(0, 0, 0, 0.07)"
					},
				  }],
				   yAxes: [{
					ticks: {
						beginAtZero:true,
						fontColor: '#585757'
					},
					gridLines: {
					  display: true ,
					  color: "rgba(0, 0, 0, 0.07)"
					},
				  }]
				 }

			 }
			});
			
		}


		if ($('#barChart').length) {
			var ctx = document.getElementById("barChart").getContext('2d');
			var myChart = new Chart(ctx, {
				type: 'bar',
				data: {
					labels: ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'],
					datasets: [{
						label: 'Facebook',
						data: [18, 20, 14, 18, 17, 15, 18],
						backgroundColor: "rgba(59, 89, 152, 0.25)",
						borderColor: "#3b5998",
						borderWidth: 2
					}, {
						label: 'Twitter',
						data: [8, 30, 20, 8, 13, 14, 11],
						backgroundColor: "rgba(85, 172, 238, 0.25)",
						borderColor: "#55acee",
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
				  enabled:true
				},	
			  scales: {
				  xAxes: [{
					  barPercentage: .5,
					ticks: {
						beginAtZero:true,
						fontColor: '#585757'
					},
					gridLines: {
					  display: true ,
					  color: "rgba(0, 0, 0, 0.07)"
					},
				  }],
				   yAxes: [{
					ticks: {
						beginAtZero:true,
						fontColor: '#585757'
					},
					gridLines: {
					  display: true ,
					  color: "rgba(0, 0, 0, 0.07)"
					},
				  }]
				 }

			 }
			});
		}

		if ($('#polarChart').length) {
			var ctx = document.getElementById("polarChart").getContext('2d');
			var myChart = new Chart(ctx, {
				type: 'polarArea',
				data: {
					labels: ["Lable1", "Lable2", "Lable3", "Lable4"],
					datasets: [{
						backgroundColor: [
							"rgba(59, 89, 152, 1)",
							"rgba(59, 89, 152, 0.85)",
							"rgba(59, 89, 152, 0.65)",
							"rgba(59, 89, 152, 0.45)"
						],
						data: [13, 20, 11, 18],
						borderWidth: [0, 0, 0, 0]
					}]
				},
			options: {
			   legend: {
				 position :"right",	
				 display: true,
				    labels: {
					  fontColor: '#585757',  
					  boxWidth:15
				   }
				},
			scale: {
				  gridLines: {
					   color: "rgba(0, 0, 0, 0.07)" 
					 }, 
				}
			   }
			});
		}


		if ($('#pieChart').length) {
			var ctx = document.getElementById("pieChart").getContext('2d');
			var myChart = new Chart(ctx, {
				type: 'pie',
				data: {
					labels: ["Lable1", "Lable2", "Lable3", "Lable4"],
					datasets: [{
						backgroundColor: [
							"rgba(85, 172, 238, 1)",
							"rgba(85, 172, 238, 0.85)",
							"rgba(85, 172, 238, 0.65)",
							"rgba(85, 172, 238, 0.45)"
						],
						data: [13, 120, 11, 20],
						borderWidth: [0, 0, 0, 0]
					}]
				},
			options: {
			   legend: {
				 position :"right",	
				 display: true,
				    labels: {
					  fontColor: '#585757',  
					  boxWidth:15
				   }
				}
			   }
			});
		}


		if ($('#doughnutChart').length) {
			var ctx = document.getElementById("doughnutChart").getContext('2d');
			var myChart = new Chart(ctx, {
				type: 'doughnut',
				data: {
					labels: ["Lable1", "Lable2", "Lable3", "Lable4"],
					datasets: [{
						backgroundColor: [
							"rgba(59, 89, 152, 1)",
							"rgba(59, 89, 152, 0.85)",
							"rgba(59, 89, 152, 0.65)",
							"rgba(59, 89, 152, 0.45)"
						],
						data: [13, 120, 11, 20],
						borderWidth: [0, 0, 0, 0]
					}]
				},
			options: {
			   legend: {
				 position :"right",	
				 display: true,
				    labels: {
					  fontColor: '#585757',  
					  boxWidth:15
				   }
				}
			   }
			});
		}


	});

})(window, document, window.jQuery);