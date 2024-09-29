// Initialize the map and set its view to a geographical point and zoom level
var map = L.map('map').setView([51.505, -0.09], 13); // [latitude, longitude], zoom level

// Add a tile layer (the map style) from OpenStreetMap or any tile provider
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Add a marker at the given position
var marker1 = L.marker([51.505, -0.09]).addTo(map);

// Add a popup to the marker
marker1.bindPopup("<b>Hello!</b><br>This is a marker.").openPopup();
/* Set the height and width of the map */
#map {
    height: 100vh; /* Full viewport height */
    width: 100%;   /* Full width */
}

// You can add more markers like this
var marker2 = L.marker([51.515, -0.1]).addTo(map);
marker2.bindPopup("Another marker.");

// Example of a circle marker
var circle = L.circle([51.508, -0.11], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(map);
circle.bindPopup("I am a circle.");
