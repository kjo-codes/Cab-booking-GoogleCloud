var map;

function initMap() {
    // Specify map options
    var mapOptions = {
        center: { lat: 40.7128, lng: -74.0060 }, // New York City coordinates
        zoom: 12 // Zoom level
    };

    // Create a new map object
    map = new google.maps.Map(document.getElementById('map'), mapOptions);

    // Add event listener to the map to allow users to click and set markers
    google.maps.event.addListener(map, 'click', function (event) {
        placeMarker(event.latLng);
    });
}

function placeMarker(location) {
    // Remove existing markers
    mapMarkers.forEach(function (marker) {
        marker.setMap(null);
    });

    // Create a new marker at the clicked location
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });

    // Set the marker as the pickup or destination location based on input field
    var pickupInput = document.getElementById('pickup').value;
    var destinationInput = document.getElementById('destination').value;

    if (pickupInput === '') {
        document.getElementById('pickup').value = location.lat() + ', ' + location.lng();
    } else if (destinationInput === '') {
        document.getElementById('destination').value = location.lat() + ', ' + location.lng();
    }
}

function findLocation() {
    var pickupInput = document.getElementById('pickup').value;
    var destinationInput = document.getElementById('destination').value;

    if (pickupInput === '' || destinationInput === '') {
        alert('Please select both pickup and destination locations.');
        return;
    }

    // Perform any additional logic (e.g., initiate cab booking)
    alert('Finding route from ' + pickupInput + ' to ' + destinationInput);
}
