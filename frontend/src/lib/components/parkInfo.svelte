<script lang="ts">
    import StarRating from './starRating.svelte';
    import { Tabs, TabItem } from 'flowbite-svelte';
    import { onDestroy, onMount } from 'svelte';
    import { fly } from 'svelte/transition';
    import type { Park } from '$lib/types';
    import type { Park } from '$lib/types';
    import { X } from 'lucide-svelte';
    import InfoChips from './infoChips.svelte';
    import ShareToMap from './shareToMap.svelte';
    import ParkReviewCard from './parkReviewCard.svelte';

    let streetViewUrl = $state('');
    let mapElement: HTMLElement | null = null;
    interface Props {
        googleMapsApiKey: string;
        isLoggedIn: boolean;
        selectedPark: Park | undefined;
        startScreenSize: string;
        userId: string;
        mapSelect: string;
    }
    let { selectedPark: parkData = $bindable(), startScreenSize, googleMapsApiKey = $bindable(), isLoggedIn, userId, mapSelect }: Props = $props();
    const activeClasses =
        'text-primary p-2 lg:p-3 inline-block border-b-2 border-primary text-center text-xs lg:text-sm';
    const inactiveClasses =
        'text-text-light p-2 lg:p-3 hover:text-text-dark inline-block border-b-2 border-text-light hover:border-text-dark text-center text-xs lg:text-sm';

    const xlMediaQuery = window.matchMedia('(min-width: 1280px)');
    const lgMediaQuery = window.matchMedia('(min-width: 1024px)');
    const mdMediaQuery = window.matchMedia('(min-width: 768px)');
    let isBlacklisted = $state(false);

    // Fetch the blacklist and check if the parkData.Id is in the blacklist
    async function checkBlacklist() {
        const response = await fetch('/blacklist/streetviewblacklist.json');
        const data = await response.json();
        const blacklist = data.blacklisted_park_ids;
        if (parkData && blacklist.includes(parkData.Id.toString())) {
            isBlacklisted = true;
        } else {
            isBlacklisted = false;
        }
    }

    // Reactive statement to update streetViewUrl whenever parkData changes
    $effect(() => {
        if (parkData && googleMapsApiKey) {
            const lat = parkData.Coordinates.x;
            const lng = parkData.Coordinates.y;
            streetViewUrl = `https://www.google.com/maps/embed/v1/streetview?key=${googleMapsApiKey}&location=${lat},${lng}&heading=210&pitch=10&fov=35`;
            checkBlacklist();
        }
    });
    onMount(() => {
        xlMediaQuery.addEventListener('change', screenResize);
        lgMediaQuery.addEventListener('change', screenResize);
        mdMediaQuery.addEventListener('change', screenResize);
        screenResize(startScreenSize);
    });
    
    onDestroy(() => {
        xlMediaQuery.removeEventListener('change', screenResize);
        lgMediaQuery.removeEventListener('change', screenResize);
        mdMediaQuery.removeEventListener('change', screenResize);
    });
    let totalReviewSize = $state(16);
    let topicReviewSize = $state(24);
    let flyDirection = $state(
        startScreenSize === 'sm' ? [0, 1000] : [-1000, 0]
    );
    // let displayShowBar = $state(false);
    $inspect(parkData?.Id);

    let reviews: [] | null = $state(null)
    $inspect(reviews);

    $effect(() => {
        if (!parkData) {
            clearParks();
        } else {
            if (parkData.Id) {
                refetchReviews()
            }
        }
    })

    function clearParks() {
        reviews = null;
    }

    async function refetchReviews() {
        const res = await fetch(`/api/getreview?id=${parkData?.Id}`);
        if (res.ok) {
            try {
                reviews = await res.json();
            } catch (_) {
                reviews = null
            }
        }
    }

    onMount(async () => {
        await refetchReviews();
    });

    $inspect(reviews);

    let reviewAvg = $derived.by(() => {
        if (reviews) {
            console.log(reviews)
            let res = 0;
            let total = 0;
            for (let i = 0; i < reviews.length; i++) {
                console.log(reviews[i]);
                res += reviews[i].stars;
                total += 1;
            }
            console.log(res, total)
            return Math.floor(res / total)
        } else {
            return null;
        }
    });

    $inspect(reviewAvg);

    function screenResize(startSize?: MediaQueryListEvent | String) {
        console.log(startSize);
        if (typeof startSize !== 'string') {
            console.log('not first', typeof startSize);
            if (xlMediaQuery.matches) {
                totalReviewSize = 24;
                topicReviewSize = 28;
                flyDirection = [-1000, 0];
                console.log(flyDirection);
                // displayShowBar = false;
            } else if (lgMediaQuery.matches) {
                totalReviewSize = 16;
                topicReviewSize = 20;
                flyDirection = [-1000, 0];
                console.log(flyDirection);
                // displayShowBar = false;
            } else if (mdMediaQuery.matches) {
                totalReviewSize = 12;
                topicReviewSize = 16;
                flyDirection = [-1000, 0];
                console.log(flyDirection);
                // displayShowBar = false;
            } else {
                totalReviewSize = 14;
                topicReviewSize = 24;
                flyDirection = [0, 1000];
                console.log(flyDirection);
                // displayShowBar = true;
            }
        } else {
            if (startSize === 'sm') {
                flyDirection = [0, 1000];
                $inspect(flyDirection);
            } else {
                flyDirection = [-1000, 0];
                $inspect(flyDirection);
            }
        }
    }
</script>

<div
    class="absolute top-[16.66666%] md:top-16 h-[83.33333vh] md:h-[calc(100vh-4rem)] flex flex-col bg-background-foreground w-full md:w-2/5 lg:w-[35%] overflow-y-scroll overflow-x-hidden no-scrollbar md:show-scrollbar rounded-xl md:rounded-none"
    transition:fly={{
        opacity: 100,
        x: flyDirection[0],
        y: flyDirection[1],
        duration: 800,
    }}
>   {#if isBlacklisted}
    <div class="absolute flex right-3 top-2 size-8 items-center justify-center rounded-full">
        <button onclick={() => parkData = undefined}>
            <X class="drop-shadow-lg stroke-text-dark"></X>
        </button>
    </div>    
    {/if}
    {#if parkData}
        {#if !isBlacklisted}
            <div class="w-full h-52 lg:h-72 min-h-52 lg:min-h-72">
                <iframe title="Street View"
                    width="100%"
                    height="100%"
                    frameborder="0"
                    style="border:0"
                    src={streetViewUrl}
                    allowfullscreen
                ></iframe>
            </div>
        {:else}
            <div class="ml-2 pb-4"></div>
        {/if}
    {/if}
    
    <div class="ml-2 pb-4">
        {#if !isBlacklisted}
        <div class="relative">
            <div class="absolute flex right-3 top-2 size-8 items-center justify-center rounded-full">
            <button onclick={() => parkData = undefined}>
                <X class="drop-shadow-lg stroke-text-dark"></X>
            </button>
            </div>
        </div>
        {/if}
        <div>
            <h1 class="md:text-xl lg:text-2xl">{parkData?.Name}</h1>
            <div class="flex items-center">
                {#if reviewAvg}
                    <p class="md:text-sm lg:text-lg">{Math.round(reviewAvg) / 2}</p>
                    <StarRating rating={reviewAvg} size={topicReviewSize}></StarRating>
                {/if}
                <ShareToMap class="ml-4" park={parkData} {mapSelect}></ShareToMap>
            </div>
            <InfoChips park={parkData}></InfoChips>
        </div>
        <Tabs {activeClasses} {inactiveClasses}>
            {#if parkData?.Embed}
                <TabItem title="Instagram" open>
                    <div class="w-full" style="overflow: hidden;">
                        <iframe
                            srcdoc={parkData.Embed}
                            class="w-full"
                            title="Instagram Embed"
                            scrolling="no"
                            style="width: 100%; height: 1000px; transform: scale(0.9); transform-origin: 0 0;"
                            onload="{(event) => {
                                const iframe = event.target as HTMLIFrameElement;
                                if (iframe && iframe.contentWindow) {
                                    iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
                                }
                            }}"
                        ></iframe>
                    </div>
                    <div class="w-full h-12"></div>
                </TabItem>
            {/if}
            <TabItem title="Community" open={!parkData?.Embed}>
                {#if !isLoggedIn}
                    <a class="p-2 rounded border-2 hover:bg-primary/10 border-primary" href={`/auth?redirectpark=${String(parkData?.Id)}`}>Logga in för att skriva en recension</a>
                {:else}
                    <a class="p-2 rounded border-2 hover:bg-primary/10 border-primary" href={"/createreview?park=" + String(parkData?.Id)}>Skapa recension</a>
                {/if}
                <div class="h-6"></div>
                {#if reviews}
                    <div class="flex flex-col space-y-4">
                        {#each reviews as review}
                            <ParkReviewCard {review} {userId} />
                        {/each}
                    </div>
                {/if}
            </TabItem>
        </Tabs>
    </div>
</div>
