
  $(function() {
    "use strict";

    $('#sparklinechart1').sparkline([ 1, 4, 5, 9, 8, 10, 5, 8, 4, 1, 0, 7, 5, 7, 9, 8, 10, 5], {
            type: 'bar',
            height: '45',
            barWidth: '3',
            resize: true,
            barSpacing: '4',
            barColor: '#3b5998',
			spotColor: '#3b5998',
            minSpotColor: '#3b5998',
            maxSpotColor: '#3b5998',
            highlightSpotColor: '#3b5998',
            highlightLineColor: '#3b5998'
        });
		
		
	$("#sparklinechart2").sparkline([1,1,0,1,-1,-1,1,-1,0,0,1,-1,1,1,-1,0,0,1,1,-1,-1,1,1], {
		type: 'tristate',
		height: '30',
		zeroAxis: false
		});	
		
		
	$("#sparklinechart3").sparkline([28,48,40,19,96,27,100], {
            type: 'line',
            width: '150',
            height: '65',
            lineWidth: '2',
            lineColor: '#55acee',
            fillColor: 'transparent',
            spotColor: '#55acee',
            minSpotColor: '#55acee',
            maxSpotColor: '#55acee',
            highlightSpotColor: '#55acee',
            highlightLineColor: '#55acee'
    }); 	
		
		
	  $("#sparklinechart4").sparkline([5,6,7,9,9,5,3,2,2,4,6,7], {
		type: 'line',
		width: '180',
		height: '65',
		lineWidth: '2',
		lineColor: '#3b5998',
		fillColor: 'rgba(59, 89, 152, 0.35)',
		maxSpotColor: '#3b5998',
		highlightLineColor: '#3b5998',
		highlightSpotColor: '#3b5998'
	  });
  
  
   $('#sparklinechart5').sparkline([20, 20, 20], {
            type: 'pie',
            height: '200',
            resize: true,
            sliceColors: ['rgba(59, 89, 152, 0.85)', 'rgba(59, 89, 152, 0.65)', 'rgba(59, 89, 152, 0.45)']
        }); 


	$('#sparklinechart6').sparkline([40, 40, 40], {
		  type: 'pie',
		  height: '200',
		  resize: true,
		  sliceColors: ['rgba(85, 172, 238, 0.95)', 'rgba(85, 172, 238, 0.75)', 'rgba(85, 172, 238, 0.55)']
	  });
	  
  
  $("#sparklinechart7").sparkline([15,16,20,18,19,14,17,12,11,12,10,14,17,14,10,15], {
        type: 'bar',
        width: '100%',
        height: '200',
        barWidth: 6,
        barSpacing: 10,
        barColor: '#55acee'
    });
  


   });