<!--
    Component for the map.
    This file contains a Svelte component for the interactive map. It contains
    most of the logic required for Leaflet, the JS map library.

    Author: Adrian Damianovici
-->
<script lang="ts">
    import { json } from '@sveltejs/kit';
    import type { LatLng } from 'leaflet';
    import * as L from 'leaflet';
    import 'leaflet/dist/leaflet.css';
    import type { Park } from '$lib/types';
    let map: L.Map;
    let markerLayers: L.LayerGroup;
    interface Props {
        parkData: Park[];
        api: string;
        selectedPark: Park | undefined;
    }
    let {parkData, api, selectedPark = $bindable() }: Props = $props();

    const markerIcon = L.icon({
        iconUrl: '/marker/map-pin.svg',
        iconSize: [24, 24],
    });
    const markerIconNoId = L.icon({
        iconUrl: '/marker/map-pin-noid.svg',
        iconSize: [24, 24],
    });

    function getParkFromId(id: number) {
        // console.log(id);
        let park = parkData.find((park) => park.Id === id);
        //$inspect(park); Denna throwade error ta tillbaka om jag hade fel

        return park as Park;
    }
    export function flyToMarker(markerID: number) {
        //console.log('funcion called');
        map.eachLayer((layer) => {
            // @ts-expect-error
            if (layer.options.id === markerID) {
                // @ts-expect-error
                map.flyTo(layer.getLatLng(), 17);
                selectedPark = getParkFromId(markerID);
                SetEmbed(selectedPark);
                return;
            }
        });
    }
    async function SetEmbed(park?: Park | undefined) {
        if (park) {
            if (!park.Embed) {
                try {
                    const controller = new AbortController(); // Create a controller for timeout handling
                    const timeoutId = setTimeout(() => controller.abort(), 5000); // 5-second timeout
                    const response: Response = await fetch(
                        api + `/api/parks/${park.Id}/embed`,
                        { signal: controller.signal } // Pass the signal for timeout control
                    );
                    clearTimeout(timeoutId); // Clear the timeout once the request completes

                    if (response.ok) {
                        const embed = await response.text(); // Get the embed HTML as text
                        park.Embed = embed; // Attach the embed to the park object
                    } else {
                        console.error(`ERROR: Failed to fetch embed for park ${park.Id}, status: ${response.status}`);
                    }
                } catch (err) {
                    console.error('Unexpected error while fetching embed:', err);
                }
            }
        }
        
        
    }
    function createMap(container: HTMLDivElement) {
        let m = L.map(container)
            .setView([59.609796, 16.5464], 14)
            .on('click', () => {
                console.log('Map Clicked');
                selectedPark = undefined;
            });
        L.tileLayer(
            'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
            {
                attribution: `&copy;<a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>,
            &copy;<a href="https://carto.com/attributions" target="_blank">CARTO</a>`,
                subdomains: 'abcd',
                maxZoom: 18,
                minZoom: 12,
            }
        ).addTo(m);
        return m;
    }

    function createMarker(loc: LatLng, id?: number) {
        let marker: L.Marker;
        if (id !== undefined) {
            // @ts-expect-error
            marker = L.marker(loc, { icon: markerIcon, id: id })
                .addTo(map)
                .bindTooltip(getParkFromId(id).Name, {
                    direction: 'bottom',
                    offset: L.point(0, 15),
                });
        } else {
            marker = L.marker(loc, { icon: markerIconNoId })
                .addTo(map)
                .bindPopup('popup text');
        }

        return marker;
    }

    function mapAction(container: HTMLDivElement) {
        map = createMap(container);
        map.setMaxBounds(
            L.latLngBounds(
                L.latLng(59.84605, 16.23463),
                L.latLng(59.452476, 16.965909)
            )
        );
        markerLayers = L.layerGroup();
        markerLayers.addTo(map);
        return {
            destroy: () => {
                if (map) map.remove();
            },
        };
    }

    $effect(() => {
        if (map && markerLayers && parkData) {
            try {
                // const marker = createMarker(L.latLng(59.6330795581567, 16.5470303778179));
                // console.log(parkData, parkData[0]);
                for (let i = 0; i < parkData.length; i++) {
                    const currentPark = parkData[i];
                    // console.log(currentPark);
                    // console.log(
                    //     currentPark.Coordinates.x,
                    //     currentPark.Coordinates.y
                    // );
                    const marker = createMarker(
                        L.latLng(
                            currentPark.Coordinates.x,
                            currentPark.Coordinates.y
                        ),
                        currentPark.Id
                    ).on('click', (e) => {
                        getParkFromId(e.target.options.id);
                        selectedPark = getParkFromId(e.target.options.id);
                        SetEmbed(selectedPark); //Inte smart att sätta embed här men det funkar
                        //flyToMarker(e.target.options.id);
                    });
                    markerLayers.addLayer(marker);
                }
            } catch (error) {
                console.error(error);
            }
        }
    });
    setTimeout(() => map.invalidateSize(), 0);
</script>

<div class="w-full h-full flex-grow z-0" use:mapAction></div>
