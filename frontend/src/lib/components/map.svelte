<script>
   import * as L from 'leaflet';
    // If you're playing with this in the Svelte REPL, import the CSS using the
    // syntax in svelte:head instead. For normal development, this is better.
    import 'leaflet/dist/leaflet.css';
    import { onMount } from 'svelte';
    let map;  
    let markerLayers;

    function createMap(container) {
      let m = L.map(container).setView([59.609796, 16.546400], 14);
      L.tileLayer(
        'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
        {
          attribution: `&copy;<a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>,
            &copy;<a href="https://carto.com/attributions" target="_blank">CARTO</a>`,
          subdomains: 'abcd',
          maxZoom: 18,
          minZoom: 12
        }
      ).addTo(m);    
      return m;
    }

    function createMarker(loc) {
		let marker = L.marker(loc)
		.addTo(map)
		.bindPopup('popup text')
		return marker;
	}

  
    function mapAction(container) {
      map = createMap(container);
      map.setMaxBounds(L.latLngBounds(L.latLng(59.846050, 16.234630), L.latLng(59.452476, 16.965909)));
      markerLayers = L.layerGroup();
			markerLayers.addTo(map);
      return {
        destroy: () => {
          if (map) map.remove();
        },
      };
    }

    $: if (map && markerLayers) {
		try {
				const marker = createMarker(L.latLng(59.6330795581567, 16.5470303778179));
				markerLayers.addLayer(marker);
		} catch (error) {
			console.error(error);
		}
	}


    setTimeout(() => map.invalidateSize(), 0);
  </script>
  
  
  <div class="w-full h-full flex-grow" use:mapAction></div>