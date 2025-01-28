<!--
    Component to display a button containing a map share link.
    Contains logic for three providers.

    Author: Adrian Damianovici
-->
<script lang="ts">
    import type { Park } from '$lib/types';
    import { MapPinned } from 'lucide-svelte';
    //import { mapTypes } from "$lib/types";

    // google: place?q=[Lng],[Lat]
    // apple: /?q=[Lng]%2C[Lat]
    // waze: /directions?q=[Lng]%2C[Lat]&ll=[Lng]%2C[Lat]
    interface Props {
        park: Park | undefined;
        class?: String;
        mapSelect: string;
    }

    let { park, class: className = '', mapSelect = 'google' }: Props = $props();

    let displayMapProvider: string = $derived.by(() => {
        if (mapSelect === 'google') {
            return 'Google Maps';
        } else if (mapSelect === 'apple') {
            return 'Apple Kartor';
        } else if (mapSelect === 'waze') {
            return 'Waze';
        } else {
            return '???';
        }
    })

    const mapDestination = {
        google: 'https://www.google.com/maps/place/',
        apple: 'https://beta.maps.apple.com/',
        waze: 'https://www.waze.com/sv/live-map/directions/',
    };

    const selectedMapType = mapSelect;

    function getFullPath(app: string, Lng: number, Lat: number) {
        if (app === 'google') {
            return mapDestination[app] + `?q=${Lng},${Lat}`;
        } else if (app === 'apple') {
            return mapDestination[app] + `?q=${Lng}%2C${Lat}`;
        } else if (app === 'waze') {
            return (
                mapDestination[app] + `?q=${Lng}%2C${Lat}&ll=${Lng}%2C${Lat}`
            );
        } else {
            return undefined;
        }
    }
</script>

{#if park}
    <a
        href={getFullPath(
            selectedMapType,
            park.Coordinates.x,
            park.Coordinates.y
        )}
        target="_blank"
        class={`${className} h-8 bg-primary/100 ring-primary/60 active:brightness-90 ring-1 text-white whitespace-nowrap py-2 px-2 rounded text-xs`}
    >
        <MapPinned strokeWidth="2" size="18" class="inline"></MapPinned>Öppna i {displayMapProvider}
    </a>
{/if}
