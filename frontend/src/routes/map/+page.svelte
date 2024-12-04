<script lang="ts">
import Map from "$lib/components/map.svelte"
export let data;
</script>
<div class="h-full w-full flex-grow flex flex-col">
    <Map {data} ></Map>
</div>
