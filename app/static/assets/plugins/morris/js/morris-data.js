
$(function () {
    "use strict";
    
	// Use Morris.Bar
	Morris.Bar({
	  element: 'bar-chart',
	  data: [
		{x: '2011 Q1', y: 3, z: 2, a: 1},
		{x: '2011 Q2', y: 2, z: 3, a: 1},
		{x: '2011 Q3', y: 1, z: 2, a: 4},
		{x: '2011 Q4', y: 2, z: 4, a: 3}
	  ],
	  xkey: 'x',
	  ykeys: ['y', 'z', 'a'],
	  labels: ['Y', 'Z', 'A'],
	  barColors: ['#3b5998', '#55acee', '#fba540'],
	  gridTextColor : "#585757",
	  resize: true
	});
	
	
	Morris.Donut({
	  element: 'donut-chart',
	  data: [
		{value: 50, label: 'data1'},
		{value: 15, label: 'data2'},
		{value: 10, label: 'data3'},
		{value: 5, label: 'data4'}
	  ],
	  colors: [
			'rgba(59, 89, 152, 1)',
			'rgba(59, 89, 152, 0.85)',
			'rgba(59, 89, 152, 0.65)',
			'rgba(59, 89, 152, 0.45)'
		],
		resize: true,
		labelColor: "#000",
	  formatter: function (x) { return x + "%"}
	});
	
	
	// Use Morris.Area instead of Morris.Line
		Morris.Area({
		  element: 'line-chart',
		  behaveLikeLine: true,
		  data: [
			{x: '2011 Q1', y: 1, z: 0},
			{x: '2011 Q2', y: 6, z: 2},
			{x: '2011 Q3', y: 2, z: 6},
			{x: '2011 Q4', y: 8, z: 1}
		  ],
		  xkey: 'x',
		  ykeys: ['y', 'z'],
		  labels: ['Y', 'Z'],
		  lineColors: ['#3b5998', '#55acee'],
		  resize: true,
		  gridTextColor : "#585757",
		  fillOpacity: 0.1,
		});
	
	
	
	// Use Morris.Area instead of Morris.Line
	Morris.Area({
	  element: 'area-chart',
	  data: [
		{x: '2010 Q4', y: 0, z: 1},
		{x: '2011 Q1', y: 5, z: 4},
		{x: '2011 Q2', y: 2, z: 1},
		{x: '2011 Q3', y: 2, z: 5},
		{x: '2011 Q4', y: 8, z: 2},
		{x: '2012 Q1', y: 4, z: 5}
	  ],
	  xkey: 'x',
	  ykeys: ['y', 'z'],
	  labels: ['Y', 'Z'],
	  lineColors: ['#3b5998', '#55acee'],
	  gridTextColor : "#585757",
	  resize: true
	});
	
	
	
 });    