//SVG vars
var usaSvg;
var usaSvgWidth;
var usaSvgHeight;

//data var
var usaMapData;

//projection for USA map
var usaProjection;

//on page load
document.addEventListener('DOMContentLoaded', function() {   
	usaSvg = d3.select('#mapSvg')
	usaSvgWidth = usaSvg.node().clientWidth;
	usaSvgHeight = usaSvg.node().clientHeight;
	
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
			.attr('d',geoPath)
			.on('click', function(d) {
				console.log(`clicked on ${d.properties.name}`);
				drawSelectedState(d.properties.name);
		});
	});
})

//draw svg for state
function drawSelectedState(stateName) {         
	//remove existing
	usaSvg.selectAll('.selectedState').remove();

	//new glyph with class='selectedState' with a rectangle and text label
	var glyph = usaSvg.append('g')
		.classed('selectedState', true)
		.attr('transform',`translate(${usaSvgWidth/2-75},${usaSvgHeight/2-75})`);
	glyph.append('rect')
		.attr('width',150)
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
		.text(stateName);
}
