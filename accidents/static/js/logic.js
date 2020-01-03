
d3.json("/mapkey").then( configResponse => {

  let api_key = configResponse.apikey;
  // var newYorkCoords = [40.73, -74.0059];
  // var mapZoomLevel = 12;

  // Create the tile layer that will be the background of our map
  var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: api_key
  });
  var layers = {
    // COMING_SOON: new L.LayerGroup(),
    // EMPTY: new L.LayerGroup(),
    // LOW: new L.LayerGroup(),
    // NORMAL: new L.LayerGroup(),
    // OUT_OF_ORDER: new L.LayerGroup()
    ALL: new L.LayerGroup()
  };

  // Create the map with our layers
  var map = L.map("map-id", {
    center: [40.73, -74.0059],
    zoom: 12,
    layers: [
      lightmap,
      layers.ALL
    ]
  });
  // Create the createMap function
  // Create the tile layer that will be the background of our map
  // Create a baseMaps object to hold the lightmap layer
  // Create an overlayMaps object to hold the accidentaccidents layer
  // Create the map object with options
  // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map

  d3.csv("/data/US_Accidents_May19_2018_2019.csv").then(response => {
    console.log(response.data);
  //d3.json('https://data.ny.gov/api/views/e8ky-4vqe/rows.json?accessType=DOWNLOAD').then(response => {
    //console.log(response.data);

    // Create the createMarkers function
    // console.log(accidents);

    // Pull the "accidents" property off of response.data
    let columns = response.data.columns
    // Initialize an array to hold accident markers
    let accidentMarkers = [];
    // Loop through the accidents array
    columns.forEach(columns => {

      // For each accident, create a marker and bind a popup with the accident's name
      accidentMarkers.push(L.marker([column.StartLat, column.StartLng], {

      }));
      // Add the marker to the accidentMarkers array
      accidentMarkers[accidentMarkers.length - 1].addTo(layers['ALL']);
    });
    // Create a layer group made from the accident markers array, pass it into the createMap function
  });
  // NO NEED: Perform an API call to the accident API to get accident information. Call createMarkers when complete
})

