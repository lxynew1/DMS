$(function() {
    "use strict";


        // chart 1

       var ctx = document.getElementById('total-actions').getContext('2d');
              
       var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['01', '02', '03', '04', '05', '06', '07'],
          datasets: [{
            label: 'Total Actions',
            data: [15, 8, 12, 5, 12, 8, 16],
            backgroundColor: 'rgba(20, 171, 239, 0.24)',
            borderColor: '#14abef',
            pointBackgroundColor:'#fff',
            pointHoverBackgroundColor:'#fff',
            pointBorderColor :'#14abef',
            pointHoverBorderColor :'#14abef',
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
      }
        }
      });

      
      // chart 2

       var ctx = document.getElementById('page-views').getContext('2d');
              
       var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['01', '02', '03', '04', '05', '06', '07'],
          datasets: [{
            label: 'Page Views',
            data: [5, 8, 12, 5, 12, 8, 16],
            backgroundColor: 'rgba(59, 89, 152, 0.24)',
            borderColor: '#3b5998',
            pointBackgroundColor:'#fff',
            pointHoverBackgroundColor:'#fff',
            pointBorderColor :'#3b5998',
            pointHoverBorderColor :'#3b5998',
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
      }
        }
      });


     // chart 3

       var ctx = document.getElementById('audience-growth').getContext('2d');
              
       var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['01', '02', '03', '04', '05', '06', '07'],
          datasets: [{
            label: 'Audience Growth',
            data: [15, 10, 12, 8, 10, 8, 10],
            backgroundColor: 'rgba(20, 171, 239, 0.24)',
            borderColor: '#14abef',
            pointBackgroundColor:'#fff',
            pointHoverBackgroundColor:'#fff',
            pointBorderColor :'#14abef',
            pointHoverBorderColor :'#14abef',
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
      }
        }
      });


  // easy pie chart 
	
	 $('.women-easy-chart').easyPieChart({
		easing: 'easeOutBounce',
		barColor : '#3b5998',
		lineWidth: 12,
		trackColor : 'rgba(0, 0, 0, 0.08)',
		scaleColor: false,
		onStep: function(from, to, percent) {
			$(this.el).find('.w_percent').text(Math.round(percent));
		}
	 });	


	 $('.men-easy-chart').easyPieChart({
		easing: 'easeOutBounce',
		barColor : '#55acee',
		lineWidth: 12,
		trackColor : 'rgba(0, 0, 0, 0.08)',
		scaleColor: false,
		onStep: function(from, to, percent) {
			$(this.el).find('.w_percent').text(Math.round(percent));
		}
	 });



    // chart 4

       var ctx = document.getElementById('gender-ratio').getContext('2d');

      var gradient1 = ctx.createLinearGradient(0, 0, 0, 300);
          gradient1.addColorStop(0, 'rgba(85, 172, 238, 0.3)');
          gradient1.addColorStop(1, 'rgba(255,255,255,.2)');

      var gradient2 = ctx.createLinearGradient(0, 0, 0, 500);
          gradient2.addColorStop(0, 'rgba(59, 89, 152, 0.3)');
          gradient2.addColorStop(1, 'rgba(255,255,255,0)');
              
       var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
          datasets: [{
            label: 'Women',
            data: [600, 620, 530, 610 , 540, 770, 700, 800],
            backgroundColor: gradient1,
            borderColor: '#14abef',
            pointBackgroundColor:'#fff',
            pointHoverBackgroundColor:'#fff',
            pointBorderColor :'#14abef',
            pointHoverBorderColor :'#14abef',
            pointBorderWidth :2,
            pointRadius :4,
            pointHoverRadius :4,
            borderWidth: 3,
          },{
            label: 'Men',
            data: [600, 800, 670, 930, 790 , 1100, 800, 920],
            backgroundColor: gradient2,
            borderColor: '#3b5998',
            pointBackgroundColor:'#fff',
            pointHoverBackgroundColor:'#fff',
            pointBorderColor :'#3b5998',
            pointHoverBorderColor :'#3b5998',
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
      }
        }
      });




// worl map

jQuery('#dashboard-map').vectorMap(
{
    map: 'world_mill_en',
    backgroundColor: 'transparent',
    borderColor: '#818181',
    borderOpacity: 0.25,
    borderWidth: 1,
    zoomOnScroll: false,
    color: '#009efb',
    regionStyle : {
        initial : {
          fill : '#14abef'
        }
      },
    markerStyle: {
      initial: {
        r: 9,
        'fill': '#fff',
        'fill-opacity':1,
        'stroke': '#000',
        'stroke-width' : 5,
        'stroke-opacity': 0.4
                },
                },
    enableZoom: true,
    hoverColor: '#009efb',
    markers : [{
        latLng : [21.00, 78.00],
        name : 'Lorem Ipsum Dollar'
      
      }],
    hoverOpacity: null,
    normalizeFunction: 'linear',
    scaleColors: ['#b6d6ff', '#005ace'],
    selectedColor: '#c9dfaf',
    selectedRegions: [],
    showTooltip: true,
});










    });	