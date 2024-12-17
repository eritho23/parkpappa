<script lang="ts">
    import { browser } from "$app/environment";
    import Map from "$lib/components/map.svelte"
    import { Alert } from "flowbite-svelte";
export let data;
</script>


<div class="h-full w-full flex-grow flex flex-col">
    <Map {data} ></Map>
    {#if !data.parks}
    <Alert dismissable color="none" class="bg-red-300 absolute w-full bg-opacity-75 text-red-900 top-2 sm:top-auto sm:bottom-4">
        <span class="font-medium">Api Fetch Error</span>
        Looks like there was an error fetching data, please try again later.
      </Alert>
    {/if}
</div>
