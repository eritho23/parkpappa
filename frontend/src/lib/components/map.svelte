<script lang="ts">
    import { json } from '@sveltejs/kit';
    import type { LatLng } from 'leaflet';
   import * as L from 'leaflet';
    // If you're playing with this in the Svelte REPL, import the CSS using the
    // syntax in svelte:head instead. For normal development, this is better.
    import 'leaflet/dist/leaflet.css';
    let map: L.Map;  
    let markerLayers: L.LayerGroup;

    const markerIcon = L.icon({
      iconUrl: "/marker/map-pin.svg",
      iconSize: [24, 24],

    })

    function createMap(container: HTMLDivElement) {
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

    function createMarker(loc: LatLng) {
		let marker = L.marker(loc, {icon: markerIcon})
		.addTo(map)
		.bindPopup('popup text')
		return marker;
	}

  
    function mapAction(container: HTMLDivElement) {
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
  
  
  <div class="w-full h-full flex-grow z-0" use:mapAction></div>