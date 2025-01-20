<script lang="ts">
    import {EllipsisVertical, Smartphone, Share, SquarePlus} from 'lucide-svelte';

    let { data } = $props();
    let {
        isAndroid,
        isDesktop,
        isIOS,
        isMac, 
        isMobile,
        isWindows,
        userAgent
    } = data;
</script>

{#if isDesktop}
    {#if isMac}
        <div>
            <h1 class="flex flex-row mt-10 px-4 font-bold text-2xl">
                Installera Parkpappa i Dock
            </h1>
            <ol class="list-decimal list-inside flex flex-col space-y-3 px-4 pt-4">
                <li>Tryck på <i>Arkiv</i> överst på skärmen</li>
                <li>Tryck på <i>Lägg till i Dock</i></li>
                <li>Välj namn</li>
                <li>Tryck på <i>Lägg till</i></li>
                <li>Klart! Nu kan du använda <span class="text-primary">Parkpappa</span> från Dock.</li>
            </ol>
        </div>
    {:else if isWindows}
        <div>
            <h1 class="flex flex-row mt-10 px-4 font-bold text-2xl">
                Installera Parkpappa på skrivbordet
            </h1>
            <ol class="list-decimal list-inside flex flex-col space-y-3 px-4 pt-4">
                <li>Kolla i adressfältet efter en installationsknapp</li>
                <li>Tryck på <i>"Installera Parkpappa"</i> eller en ikon med nedladdningspil</li>
                <li>Tryck på <i>Installera</i> i popupen</li>
                <li>Klart! Nu kan du använda <span class="text-primary">Parkpappa</span> som vilken annan app som helst.</li>
            </ol>
        </div>
    {:else}
        <div>
            <h1 class="flex flex-row mt-10 px-4 font-bold text-2xl">
                Din plattform kunde inte detekteras. Du kan använda Parkpappa i din webbläsare.
            </h1>
        </div>
    {/if}
{:else if isMobile}
    {#if isIOS}
        <div>
            <h1 class="flex flex-row mt-10 px-4 font-bold text-2xl">
                Installera Parkpappa som en webapp på hemskärmen i iOS
            </h1>
            <ol class="list-decimal list-inside flex flex-col space-y-3 px-4 pt-4">
                <li>Tryck på <i>"Dela"</i>-knappen <Share /> </li>
                <li>Tryck på <i>Lägg till på hemskärmen</i><SquarePlus /></li>
                <li>Välj namn på bokmärket</li>
                <li>Tryck på <i>Lägg till</i></li>
                <li>Klart! Nu kan du använda <span class="text-primary">Parkpappa</span> som vilken annan app som helst.</li>
            </ol>
        </div>
    {:else if isAndroid}
        <div>
            <h1 class="flex flex-row mt-10 px-4 font-bold text-2xl">
                Installera Parkpappa på startskärmen på Android
            </h1>
            <ol class="list-decimal list-inside flex flex-col space-y-3 px-4 pt-4">
                <li>Tryck på tre prickar uppe till höger i webbläsaren <EllipsisVertical /></li>
                <li>Tryck på <i>Lägg till på startskärmen</i><Smartphone /></li>
                <li>Tryck på <i>Installera</i> och vänta lite</li>
                <li>Klart! Nu kan du använda <span class="text-primary">Parkpappa</span> som vilken annan app som helst.</li>
            </ol>
        </div>
    {:else}
        <div>
            <h1 class="flex flex-row mt-10 px-4 font-bold text-2xl">
                Din plattform kunde inte detekteras. Du kan använda Parkpappa i din webbläsare.
            </h1>
        </div>
    {/if}
{:else}
    <div>
        <h1 class="flex flex-row mt-10 px-4 font-bold text-2xl">
            Din plattform kunde inte detekteras. Du kan använda Parkpappa i din webbläsare.
        </h1>
    </div>
{/if}