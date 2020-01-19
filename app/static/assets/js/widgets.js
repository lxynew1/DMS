
$(function() {
    "use strict";

// chart 1
	
	$('#widget-chart-1').sparkline([5,8,7,10,9,10,8,6,4,6,8,7,6,8], {
            type: 'bar',
            height: '35',
            barWidth: '3',
            resize: true,
            barSpacing: '3',
            barColor: '#3b5998'
        });
		
	// chart 2
	
		$('#widget-chart-2').sparkline([0,5,3,7,5,10,3,6,5,10], {
            type: 'line',
            width: '80',
            height: '40',
            lineWidth: '2',
            lineColor: '#55acee',
            fillColor: 'transparent',
            spotColor: '#55acee',
        });
		
	// chart 3	
		
		$('#widget-chart-3').sparkline([2,3,4,5,4,3,2,3,4,5,6,5,4,3,4,5], {
            type: 'discrete',
            width: '75',
            height: '40',
            lineColor: '#3b5998',
            lineHeight: 22
        });
		
		
	// chart 4

   $("#widget-chart-4").sparkline([5,6,7,9,9,5,3,2,2,4,6,7], {
      type: 'line',
      width: '100',
      height: '25',
      lineWidth: '2',
      lineColor: '#55acee',
      fillColor: 'transparent'
    });



	// easy pie chart 
	
	 $('.dash-chart').easyPieChart({
		easing: 'easeOutBounce',
		barColor : '#3b5998',
		lineWidth: 10,
		trackColor : '#f5f8ff',
		scaleColor: false,
		onStep: function(from, to, percent) {
			$(this.el).find('.easy_percent').text(Math.round(percent));
		}
	 });


    // chart 5

     var ctx = document.getElementById('widget-chart-5').getContext('2d');
              
       var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['01', '02', '03', '04', '05', '06', '07'],
          datasets: [{
            label: 'Total Revenue',
            data: [15, 8, 12, 7, 12, 10, 16],
            backgroundColor: 'rgba(59, 89, 152, 0.5)',
            borderColor: '#3b5998',
            pointBackgroundColor:'#fff',
            pointHoverBackgroundColor:'#fff',
            pointBorderColor :'#fff',
            pointHoverBorderColor :'#fff',
            pointBorderWidth :1,
            pointRadius :0,
            pointHoverRadius :4,
            borderWidth: 3
          }]
        }
        ,
        options: {
              legend: {
                position: false,
                display: true,
            },
        tooltips: {
           enabled: false
      },
     scales: {
          xAxes: [{
            display: false,
            gridLines: false
          }],
          yAxes: [{
            display: false,
            gridLines: false
          }]
        }
        }
    
      });


      // chart 6

     var ctx = document.getElementById('widget-chart-6').getContext('2d');
              
       var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['01', '02', '03', '04', '05', '06', '07'],
          datasets: [{
            label: 'Total Profit',
            data: [15, 8, 12, 7, 12, 10, 16],
            backgroundColor: 'rgba(85, 172, 238, 0.45)',
            borderColor: '#55acee',
            pointBackgroundColor:'#fff',
            pointHoverBackgroundColor:'#fff',
            pointBorderColor :'#fff',
            pointHoverBorderColor :'#fff',
            pointBorderWidth :1,
            pointRadius :0,
            pointHoverRadius :4,
            borderWidth: 3
          }]
        }
        ,
        options: {
              legend: {
                position: false,
                display: true,
            },
        tooltips: {
           enabled: false
      },
     scales: {
          xAxes: [{
            display: false,
            gridLines: false
          }],
          yAxes: [{
            display: false,
            gridLines: false
          }]
        }
        }
    
      });


     // chart 7

     var ctx = document.getElementById('widget-chart-7').getContext('2d');
              
       var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['01', '02', '03', '04', '05', '06', '07'],
          datasets: [{
            label: 'Total Shipments',
            data: [15, 8, 12, 7, 12, 10, 16],
            backgroundColor: 'rgba(59, 89, 152, 0.5)',
            borderColor: '#3b5998',
            pointBackgroundColor:'#fff',
            pointHoverBackgroundColor:'#fff',
            pointBorderColor :'#fff',
            pointHoverBorderColor :'#fff',
            pointBorderWidth :1,
            pointRadius :0,
            pointHoverRadius :4,
            borderWidth: 3
          }]
        }
        ,
        options: {
              legend: {
                position: false,
                display: true,
            },
        tooltips: {
           enabled: false
      },
     scales: {
          xAxes: [{
            display: false,
            gridLines: false
          }],
          yAxes: [{
            display: false,
            gridLines: false
          }]
        }
        }
    
      });

		
	  	
	  
});		