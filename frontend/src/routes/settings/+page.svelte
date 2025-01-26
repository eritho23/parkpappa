<script lang="ts">
    import { Tabs, TabItem, Radio } from 'flowbite-svelte';

    let {data} = $props();
    let {email, mapSelect} = data;

    let emailval = $state();
    let emailsMatching = $derived(emailval === email);
</script>

<div class="h-full w-full flex-grow flex flex-col">
    <Tabs
        defaultClass="flex flex-wrap space-x-2 rtl:space-x-reverse"
        contentClass="bg-background-foreground flex-grow flex flex-col p-4 mt-0 h-full w-full border-t-[2px] border-red-500"
    >
        <TabItem
            title="Kartapplikation"
            divClass="flex-grow flex flex-col h-full w-full"
            open
        >
            <form method="post" action="?/mapProvider">
                <label>Vald kartapplikation
                    <Radio color="red" name="mapSelect" value="google" checked={mapSelect === 'google'}>Google Maps</Radio>
                    <Radio color="red" name="mapSelect" value="apple" checked={mapSelect === 'apple'}>Apple Maps</Radio>
                    <Radio color="red" name="mapSelect" value="waze" checked={mapSelect === 'waze'}>Waze</Radio>
                </label>
                <button class="border-zinc-600 rounded border-2 px-2 py-1 mt-4 hover:bg-zinc-100" type="submit">Spara</button>
            </form>
        </TabItem>
        <TabItem
            title="Ta bort konto"
            divClass="flex-grow flex flex-col h-full w-full space-y-2"
        >
            <h1 class="font-bold text-2xl">Ta bort konto</h1>
            <p>
                Du kan inte ångra kontoborttagning. Alla recensioner kommer att tas bort.
            </p>
            <form class="" method="post" action="?/deleteAccount">
                <input type="email" required bind:value={emailval} placeholder="Skriv in din e-post för att bekräfta" name="email" /> <br>
                <button type="submit" class="border-zinc-600 rounded border-2 px-2 py-1 mt-4 hover:bg-zinc-100 disabled:bg-zinc-400 text-zinc-600" title={!emailsMatching ? 'E-post matchar inte' : 'Klicka för att ta bort konto'} disabled={!emailsMatching}>Ta bort konto</button>
            </form>

        </TabItem>
    </Tabs>
</div>
