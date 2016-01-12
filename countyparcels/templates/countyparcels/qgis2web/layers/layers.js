var baseLayer = new ol.layer.Group({'title': 'Base maps',layers: []});
var format_counties = new ol.format.GeoJSON();
var features_counties = format_counties.readFeatures(geojson_counties);
var jsonSource_counties = new ol.source.Vector();
jsonSource_counties.addFeatures(features_counties);
var lyr_counties = new ol.layer.Vector({
                source: jsonSource_counties, 
                style: style_counties,
                title: "counties"
            });


var layersList = [baseLayer,lyr_counties];
