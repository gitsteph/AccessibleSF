var geolocation = require("./geolocation");

geolocation();

var map;

window.initMap = function () {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 8
  });
}