//SVG vars
var usaSvg;
var usaSvgWidth;
var usaSvgHeight;

//data var
var usaMapData;

//projection for USA map
var usaProjection;

//data from db
var crashData;
var aircraftData;

//states array
var states = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]


//on page load
document.addEventListener('DOMContentLoaded', function() {   
	usaSvg = d3.select('#mapSvg')
	usaSvgWidth = usaSvg.node().clientWidth;
	usaSvgHeight = usaSvg.node().clientHeight;
	
	request_data_from_flask();
	
	//load map data with promise
	Promise.all([d3.json('/static/us.geojson')])
		.then(data => {
			usaMapData = data[0];
		//projection
		usaProjection = d3.geoAlbersUsa().fitSize([usaSvgWidth,usaSvgHeight], usaMapData);
		
		//geopath
		const geoPath = d3.geoPath().projection(usaProjection);
		
		//draw map and click
		usaSvg.selectAll('.state')
			.data(usaMapData.features)
			.join('path')
			.classed('state',true)
			.style("fill", '#ffffff');
			.attr('d',geoPath)
			.on('click', function(d) {
				console.log(`clicked on ${d.properties.name}`);
				drawBox(d.properties.name);
		});
	});
})

//request Flask
async function request_data_from_flask() {

	//fetch POST request to flask server
	const url = `${window.origin}/map_function`;
	fetch(url, {
		method: 'POST'
	})
	//recieve response
	.then(response => {
		if (response.status != 200) {
			console.log("Error. Status code: ${response.status}");
			return;
		}
		response.json().then(data => {
			console.log(data);
			crashData = data;
		})
	})
}

async function get_aircraft() {

	//fetch POST request to flask server
	const url = `${window.origin}/map_get_aircraft_function`;
	fetch(url, {
		method: 'POST'
	})
	//recieve response
	.then(response => {
		if (response.status != 200) {
			console.log("Error. Status code: ${response.status}");
			return;
		}
		response.json().then(data => {
			console.log(data);
			aircraftData = data;
		})
	})
}

//draw svg for state
function drawBox(stateName) {         
	//remove existing
	usaSvg.selectAll('.selectedState').remove();

	//new glyph with class='selectedState' with a rectangle and text label
	var glyph = usaSvg.append('g')
		.classed('selectedState', true)
		//.attr('transform',`translate(${usaSvgWidth/2-75},${usaSvgHeight/2-75})`);
		.attr('transform',`translate(${0},${0})`);
	glyph.append('rect')
		.attr('width',500)
		.attr('height',150)
		.style('stroke','black')
		.style('fill','white')
		.on('click',function(d) {
			usaSvg.selectAll('.selectedState')
				.transition()
				.style('opacity',0)
				.remove();
			});
	glyph.append('text')
		.attr('dx',75)    
		.attr('dy',20)
		.style('text-anchor','middle')
		.text(stateName + " Crashes");
	
	ind = states.indexOf(stateName);
	console.log(ind);
	var dytemp = 40;
	console.log(crashData[ind]);
	console.log(crashData[ind][0]);
	console.log(crashData[ind][0][0]);
	
	
	for (var j = 0; j < 50; j++) {
		
		
		
		
		
		if (crashData[ind][j][0]==d3.select(svg_select).value){
			console.log("Match");
			
			glyph.append('text')
				.attr('dx',10)    
				.attr('dy',dytemp) 
				.style('text-anchor','left')
				.text("Match");
		}
		else {
		
			console.log("No matches");
			
			glyph.append('text')
				.attr('dx',10)    
				.attr('dy',dytemp) 
				.style('text-anchor','left')
				.text("No matches");
		}
	}
	
	/*
	if (!crashData[ind].length) {
		glyph.append('text')
			.attr('dx',10)    
			.attr('dy',dytemp) 
			.style('text-anchor','left')
			.text("No crashes");
	}
	else
	{
		for (var i=0; i<Object.keys(crashData[ind]).length; i++) {
			dytemp = dytemp + 20;
			glyph.append('text')
				.attr('dx',10)    
				.attr('dy',dytemp) 
				.style('text-anchor','left')
				.text(crashData[ind][i]);
	}
	
	
	}*/
	/*for (var i=0; i<Object.keys(crashData).length; i++) {
		if (
		console.log(crashData[i]);
		console.log(crashData[i][0][6]);
	}*/
	/*if (stateName
	var dytemp = 40;
	for (var i=0; i<Object.keys(crashData).length; i++) {
		console.log(crashData[i]);
		dytemp = dytemp + 20;
		glyph.append('text')
			.attr('dx',10)    
			.attr('dy',dytemp) 
			.style('text-anchor','left')
			.text(crashData[i]);
	}*/
}
