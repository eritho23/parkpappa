<script lang="ts">
    import ParkInfo from '$lib/components/parkInfo.svelte';
    import Map from '$lib/components/map.svelte';
    import type { Park, DataParks } from '$lib/types.js';
    import { Alert } from 'flowbite-svelte';
    import { RotateCcw } from 'lucide-svelte';
    import ParkRandomizer from '$lib/components/parkRandomizer.svelte';
    import { onDestroy, onMount } from 'svelte';
    import chipsData from "$lib/infoChipsTranslations.json"
    interface Props {
        data: DataParks;
        selectedPark: Park | undefined;
    }
    let { data, selectedPark = $bindable()}: Props = $props();
    let parkInfo: Park | undefined = $state(undefined);
    function showInfo(toggle: boolean = true, park?: Park | undefined) {
        selectedPark = park;
        console.log('visible? ', parkInfo);

    }
    let mapComponentRef: any = $state();

    let goToParkNumber = $derived(parseInt(data.goToPark));
    $effect(() => {
        if (data.goToPark && goToParkNumber) {
            mapComponentRef.flyToMarker(goToParkNumber)
        }
    })

    const xlMediaQuery = window.matchMedia('(min-width: 1280px)');
    const lgMediaQuery = window.matchMedia('(min-width: 1024px)');
    const mdMediaQuery = window.matchMedia('(min-width: 768px)');
    onMount(() => {
        xlMediaQuery.addEventListener('change', changeStartScreenSize);
        lgMediaQuery.addEventListener('change', changeStartScreenSize);
        mdMediaQuery.addEventListener('change', changeStartScreenSize);
        changeStartScreenSize();
    });
    onDestroy(() => {
        xlMediaQuery.removeEventListener('change', changeStartScreenSize);
        lgMediaQuery.removeEventListener('change', changeStartScreenSize);
        mdMediaQuery.removeEventListener('change', changeStartScreenSize);
    });
    let startScreenSize: string = $state("");

    function changeStartScreenSize() {
        if (xlMediaQuery.matches) {
            startScreenSize = "xl"
        } else if (lgMediaQuery.matches) {
            startScreenSize = "lg"
        } else if (mdMediaQuery.matches) {
            startScreenSize = "md"
        } else {
            startScreenSize = "sm"
        }
    }
</script>

<div class="h-full w-full flex-grow flex flex-col">
    <Map parkData={data.parks} api={String(data.api)} bind:selectedPark={selectedPark} bind:this={mapComponentRef}></Map>
    <ParkRandomizer parks={data.parks} api={data.api} flyToMarker={mapComponentRef.flyToMarker} ></ParkRandomizer>
    {#if selectedPark}
        <ParkInfo translations={data.translations} bind:selectedPark={selectedPark} api={data.api} startScreenSize={startScreenSize}></ParkInfo>
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
