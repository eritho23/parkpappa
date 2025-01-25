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
    }

    let { park, class: className = '' }: Props = $props();

    const mapDestination = {
        google: 'https://www.google.com/maps/place/',
        apple: 'https://beta.maps.apple.com/',
        waze: 'https://www.waze.com/sv/live-map/directions/',
    };

    const selectedMapType = 'waze';

    function getFullPath(app, Lng, Lat) {
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
        class={`${className} w-28 h-8 bg-primary/100 ring-primary/60 active:brightness-90 ring-1 text-white whitespace-nowrap py-2 px-2 rounded text-xs`}
    >
        <MapPinned strokeWidth="2" size="18" class="inline"></MapPinned> Open in
        map
    </a>
{/if}
