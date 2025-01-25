<script lang="ts">
    import { Tabs, TabItem, Radio } from 'flowbite-svelte';
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
            <div>
                <p>Vald kartapplikation</p>
                <Radio color="red" name="mapSelect" checked>Google Maps</Radio>
                <Radio color="red" name="mapSelect">Apple Maps</Radio>
                <Radio color="red" name="mapSelect">Waze</Radio>
            </div>
        </TabItem>
    </Tabs>
</div>
