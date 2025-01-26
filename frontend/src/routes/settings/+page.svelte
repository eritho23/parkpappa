<script lang="ts">
    import { Tabs, TabItem, Radio, Button } from 'flowbite-svelte';

    let {data} = $props();
    let {mapSelect} = data;
</script>

<div class="h-full w-full flex-grow flex flex-col">
    <Tabs
        defaultClass="flex flex-wrap space-x-2 rtl:space-x-reverse"
        contentClass="bg-background-foreground flex-grow flex flex-col p-4 mt-0 h-full w-full border-t-[2px] border-red-500"
    >
        <TabItem
            title="General"
            divClass="flex-grow flex flex-col h-full w-full"
            open
        >
            <form method="post">
                <label>Vald kartapplikation
                    <Radio color="red" name="mapSelect" value="google" checked={mapSelect === 'google'}>Google Maps</Radio>
                    <Radio color="red" name="mapSelect" value="apple" checked={mapSelect === 'apple'}>Apple Maps</Radio>
                    <Radio color="red" name="mapSelect" value="waze" checked={mapSelect === 'waze'}>Waze</Radio>
                </label>
                <button class="border-zinc-600 rounded border-2 px-2 py-1 mt-4 hover:bg-zinc-100" type="submit">Spara</button>
            </form>
        </TabItem>
    </Tabs>
</div>
