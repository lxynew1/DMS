!function($) {
    "use strict";

    var EasyPieChart = function() {};

    EasyPieChart.prototype.init = function() {
    	//initializing various types of easy pie charts
		
    	$('.easy-pie-chart-1').easyPieChart({
			easing: 'easeOutBounce',
			barColor : '#3b5998',
			lineWidth: 10,
			animate: 1000,
            lineCap: 'rgba(0, 0, 0, 0.05)',
            trackColor : 'rgba(0, 0, 0, 0.05)',
			onStep: function(from, to, percent) {
				$(this.el).find('.percent').text(Math.round(percent));
			}
		});

		$('.easy-pie-chart-2').easyPieChart({
			easing: 'easeOutBounce',
			barColor : '#55acee',
			lineWidth: 10,
			lineCap: 'rgba(0, 0, 0, 0.05)',
            trackColor : 'rgba(0, 0, 0, 0.05)',
			onStep: function(from, to, percent) {
				$(this.el).find('.percent').text(Math.round(percent));
			}
		});

		$('.easy-pie-chart-3').easyPieChart({
			easing: 'easeOutBounce',
			barColor : '#3b5998',
			lineWidth: 10,
			lineCap: 'rgba(0, 0, 0, 0.05)',
            trackColor : 'rgba(0, 0, 0, 0.05)',
			onStep: function(from, to, percent) {
				$(this.el).find('.percent').text(Math.round(percent));
			}
		});

		$('.easy-pie-chart-4').easyPieChart({
			easing: 'easeOutBounce',
			barColor : '#55acee',
			lineWidth: 10,
			lineCap: 'rgba(0, 0, 0, 0.05)',
            trackColor : 'rgba(0, 0, 0, 0.05)',
			onStep: function(from, to, percent) {
				$(this.el).find('.percent').text(Math.round(percent));
			}
		});

		$('.easy-pie-chart-5').easyPieChart({
			easing: 'easeOutBounce',
			barColor : '#3b5998',
			lineWidth: 10,
			trackColor : 'rgba(0, 0, 0, 0.05)',
			scaleColor: false,
			onStep: function(from, to, percent) {
				$(this.el).find('.percent').text(Math.round(percent));
			}
		});

		$('.easy-pie-chart-6').easyPieChart({
			easing: 'easeOutBounce',
			barColor : '#55acee',
			lineWidth: 10,
			trackColor : 'rgba(0, 0, 0, 0.05)',
			scaleColor: false,
			onStep: function(from, to, percent) {
				$(this.el).find('.percent').text(Math.round(percent));
			}
		});


		$('.easy-pie-chart-7').easyPieChart({
			easing: 'easeOutBounce',
			barColor : '#3b5998',
			lineWidth: 10,
			trackColor : 'rgba(0, 0, 0, 0.05)',
			scaleColor: false,
			onStep: function(from, to, percent) {
				$(this.el).find('.percent').text(Math.round(percent));
			}
		});


		$('.easy-pie-chart-8').easyPieChart({
			easing: 'easeOutBounce',
			barColor : '#55acee',
			lineWidth: 10,
			trackColor : 'rgba(0, 0, 0, 0.05)',
			scaleColor: false,
			onStep: function(from, to, percent) {
				$(this.el).find('.percent').text(Math.round(percent));
			}
		});


    },
    //init
    $.EasyPieChart = new EasyPieChart, $.EasyPieChart.Constructor = EasyPieChart
}(window.jQuery),

//initializing
function($) {
    "use strict";
    $.EasyPieChart.init()
}(window.jQuery);