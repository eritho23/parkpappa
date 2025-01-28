<!--
    Page with device-specific instrucions for adding the site as a Progressive Web App (PWA).

    Author: Eric Thorburn
-->
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

<div class="content-container">
{#if isDesktop}
    {#if isMac}
        <div class="flex flex-col items-center mt-10 px-4 mb-10 max-h-screen overflow-y-auto">
            <div class="bg-white p-6 rounded-lg shadow-md w-full max-w-lg">
                <h1 class="font-bold text-3xl text-center">
                    Installera Parkpappa i Dock
                </h1>
                <ol class="list-decimal list-inside flex flex-col space-y-3 pt-4 text-lg">
                    <li>Tryck på <i>Arkiv</i> överst på skärmen</li>
                    <li>Tryck på <i>Lägg till i Dock</i></li>
                    <li>Välj namn</li>
                    <li>Tryck på <i>Lägg till</i></li>
                    <li>Klart! Nu kan du använda <span class="text-primary">Parkpappa</span> från Dock.</li>
                </ol>
                <div class="mt-6 text-center">
                    <a href="/" class="bg-primary text-white px-4 py-2 rounded">Gå tillbaka</a>
                </div>
            </div>
        </div>
    {:else if isWindows}
        <div class="flex flex-col items-center mt-10 px-4 mb-10 max-h-screen overflow-y-auto">
            <div class="bg-white p-6 rounded-lg shadow-md w-full max-w-lg">
                <h1 class="font-bold text-3xl text-center">
                    Installera Parkpappa på skrivbordet
                </h1>
                <ol class="list-decimal list-inside flex flex-col space-y-3 pt-4 text-lg">
                    <li>Kolla i adressfältet efter en installationsknapp</li>
                    <li>Tryck på <i>"Installera Parkpappa"</i> eller en ikon med nedladdningspil</li>
                    <li>Tryck på <i>Installera</i> i popupen</li>
                    <li>Klart! Nu kan du använda <span class="text-primary">Parkpappa</span> som vilken annan app som helst.</li>
                </ol>
                <div class="mt-6 text-center">
                    <a href="/" class="bg-primary text-white px-4 py-2 rounded">Gå tillbaka</a>
                </div>
            </div>
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
        <div class="flex flex-col items-center mt-10 px-4 mb-10 max-h-screen overflow-y-auto">
            <div class="bg-white p-6 rounded-lg shadow-md w-full max-w-lg">
                <h1 class="font-bold text-3xl text-center">
                    Installera Parkpappa på hemskärmen i iOS
                </h1>
                <ol class="list-decimal list-inside flex flex-col space-y-3 pt-4 text-lg">
                    <li>Öppna <i>Safari</i></li>
                    <li>Tryck på <i>Dela</i>-knappen <Share class="inline-block w-5 h-5" /></li>
                    <li>Välj <i>Lägg till på hemskärmen</i> <SquarePlus class="inline-block w-5 h-5" /></li>
                    <li>Tryck på <i>Lägg till</i></li>
                    <li>Klart! Nu kan du använda <span class="text-primary">Parkpappa</span> från hemskärmen.</li>
                </ol>
                <div class="mt-6 text-center">
                    <a href="/" class="bg-primary text-white px-4 py-2 rounded">Gå tillbaka</a>
                </div>
            </div>
        </div>
    {:else if isAndroid}
        <div class="flex flex-col items-center mt-10 px-4 mb-10 max-h-screen overflow-y-auto">
            <div class="bg-white p-6 rounded-lg shadow-md w-full max-w-lg">
                <h1 class="font-bold text-3xl text-center">
                    Installera Parkpappa på hemskärmen i Android
                </h1>
                <ol class="list-decimal list-inside flex flex-col space-y-3 pt-4 text-lg">
                    <li>Öppna <i>Chrome</i></li>
                    <li>Tryck på <i>Menyn</i> (de tre prickarna) <EllipsisVertical class="inline-block w-5 h-5" /></li>
                    <li>Välj <i>Lägg till på startskärmen</i> <SquarePlus class="inline-block w-5 h-5" /></li>
                    <li>Tryck på <i>Lägg till</i></li>
                    <li>Klart! Nu kan du använda <span class="text-primary">Parkpappa</span> från hemskärmen.</li>
                </ol>
                <div class="mt-6 text-center">
                    <a href="/" class="bg-primary text-white px-4 py-2 rounded">Gå tillbaka</a>
                </div>
            </div>
        </div>
    {/if}
{/if}
</div>