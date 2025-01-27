<script>
    import {
        Check,
        Map,
        SquarePlus,
        ShieldCheck,
        MapPinCheckInside,
    } from 'lucide-svelte';
</script>

<div class="flex flex-col overflow-y-scroll h-screen">
    <div
        class="text-center w-full h-full px-auto justify-center bg-white border-b border-grey/90 flex flex-col space-y-8 py-12"
    >
        <h1 class="text-4xl font-bold">Parkpappa</h1>
        <p class="lg:p-0 p-4">Hitta dina favoritlekparker i Västerås med en interaktiv karta!</p>
        <div class="flex flex-col space-y-3 mx-auto">
            <div class="flex flex-row space-x-2">
                <Check />
                <span>Enkel användning</span>
            </div>
            <div class="flex flex-row space-x-2">
                <MapPinCheckInside />
                <span>Data från Västerås stad</span>
            </div>
            <div class="flex flex-row space-x-2">
                <ShieldCheck />
                <span>Recensioner och rekommendationer</span>
            </div>
        </div>
        <div class="flex flex-col md:flex-row mx-auto">
            <div class="flex flex-row md:mr-5 mb-5 md:mb-0">
                <a
                    class="bg-primary/100 hover:underline text-white w-max whitespace-nowrap py-2 px-4 rounded"
                    href="/map"><Map class="inline" /> Till kartan</a
                >
            </div>
            <div class="flex flex-row">
                <a
                    class="bg-primary/10 hover:underline border-primary border-2 text-black w-max whitespace-nowrap py-2 px-4 rounded"
                    href="/addtohomescreen"
                    ><SquarePlus class="inline" /> Lägg till på hemskärmen</a
                >
            </div>
        </div>
    </div>
    <div class="md:w-1/3 px-4 md:px-0 mx-auto py-12">
        <h1 class="font-bold text-center text-xl mb-3">
            Allt du behöver veta för ett smidigt parkbesök
        </h1>
        <p>
            Parkpappa är den perfekta sidan för föräldrar med leksugna barn! Vår
            karta visar inte bara alla lekparker i Västerås, utan ger även
            möjlighet att filtrera parkerna för minnesvärda och varierade besök.
        </p>
    </div>
    <div class="h-24 text-center justify-center w-full">
        <h1 class="font-bold text-xl">
            Skapad av Adrian, David och Eric på <a href="https://vasteras.hitachigymnasiet.se/utbildning-teknikprogrammet/teknikspets" class="text-primary hover:underline">spetsen</a>
        </h1>
    </div>
    <div
        class="flex lg:flex-row flex-col px-4 md:px-0 md:w-2/3 pt-3 pb-12 mb-16 justify-center mx-auto mt-12"
    >
        <img
            class="rounded-full size-48 lg:size-72 mx-auto mb-12"
            src="/img/jocke.jpg"
            alt="Joakim Flink"
        />
        <div class="hidden lg:visible border-r-2 border-zinc-800"></div>
        <div class="w-4/5 lg:w-1/3 flex flex-col my-auto mx-auto space-y-4">
            <h1 class="font-bold text-2xl">Parkpionjären Joakim Flink</h1>
            <p class="">
                Parkpappa började 2020, då Joakim Flink startade instagramkontot <a
                    href="https://www.instagram.com/park_pappa"
                    class="text-primary hover:underline">@park_pappa</a
                >. Under sin föräldraledighet besökte han alla lekparker i
                Västerås och recenserade dem på instagramkontot. År 2025
                lanseras denna webbsida med målet att göra varierade, givande
                parkbesök tillgängliga för småbarnsföräldrar. Joakim tycker inte
                att Västerås stad har någon bra lösning för att visa upp parker.
            </p>
        </div>
    </div>
</div>
