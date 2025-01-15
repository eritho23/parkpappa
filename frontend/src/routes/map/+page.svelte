<script lang="ts">
    import { browser } from '$app/environment';
    import ParkInfo from '$lib/components/parkInfo.svelte';
    import Map from '$lib/components/map.svelte';
    import type { Park, DataParks } from '$lib/types.js';
    import { Alert } from 'flowbite-svelte';
    import { RotateCcw } from 'lucide-svelte';
    interface Props {
        data: DataParks;
    }
    let { data }: Props = $props();
    let selectedPark = $state();
    let parkInfoVisible = $state(false);
    function showInfo(toggle: boolean = true) {
        if (toggle) {
            parkInfoVisible = !parkInfoVisible;
        } else {
            parkInfoVisible = false;
        }
        console.log('visible? ', parkInfoVisible);
    }
</script>

<div class="h-full w-full flex-grow flex flex-col">
    <Map parkData={data.parks} {showInfo}></Map>
    {#if parkInfoVisible}
        <ParkInfo></ParkInfo>
    {/if}
    {#if !data.parks}
        <Alert
            dismissable
            color="none"
            class="bg-red-300 absolute w-full bg-opacity-75 text-red-800 top-2 sm:top-auto sm:bottom-4 border-2 border-red-800 border-opacity-75"
        >
            <span class="font-medium">Api Fetch Error</span>
            Looks like there was an error fetching data, please try again later.
            <button class="inline"><RotateCcw size="16"></RotateCcw></button>
        </Alert>
    {/if}
</div>
