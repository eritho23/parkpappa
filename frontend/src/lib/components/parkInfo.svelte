<script lang="ts">
    import StarRating from './starRating.svelte';
    import { Tabs, TabItem } from 'flowbite-svelte';
    import { onDestroy, onMount } from 'svelte';
    import { fly } from 'svelte/transition';
    import type { ChipTranslations, Park } from '$lib/types';
    import { X } from 'lucide-svelte';
    import InfoChips from './infoChips.svelte';
    interface Props {
        selectedPark: Park | undefined;
        startScreenSize: string;
    }
    let { selectedPark: parkData = $bindable(), startScreenSize }: Props =
        $props();
    const activeClasses =
        'text-primary p-2 lg:p-3 inline-block border-b-2 border-primary text-center text-xs lg:text-sm';
    const inactiveClasses =
        'text-text-light p-2 lg:p-3 hover:text-text-dark inline-block border-b-2 border-text-light hover:border-text-dark text-center text-xs lg:text-sm';

    const xlMediaQuery = window.matchMedia('(min-width: 1280px)');
    const lgMediaQuery = window.matchMedia('(min-width: 1024px)');
    const mdMediaQuery = window.matchMedia('(min-width: 768px)');
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
    let flyDirection = $state([-1000, 0]);
    // let displayShowBar = $state(false);
    $inspect(parkData);
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
    class="absolute top-[16.66666%] md:top-16 h-5/6 md:h-full flex flex-col bg-background-foreground w-full md:w-2/5 lg:w-[35%] overflow-y-scroll overflow-x-hidden no-scrollbar md:show-scrollbar rounded-xl md:rounded-none"
    transition:fly={{
        opacity: 100,
        x: flyDirection[0],
        y: flyDirection[1],
        duration: 800,
    }}
>
    <!-- {#if displayShowBar}
        <div
        class="h-2 w-20 top-1 absolute self-center"
        >
            <div
                class="h-1 w-16 bg-primary/50 rounded-full"
            ></div>
        </div>
    {/if} -->
    <div
        class="absolute flex right-3 top-2 size-8 items-center justify-center rounded-full"
    >
        <button onclick={() => (parkData = undefined)}
            ><X class="drop-shadow-lg stroke-text-dark"></X></button
        >
    </div>
    <img
        class="w-full h-52 lg:h-72 object-cover"
        src="./placeholders/playground.jpg"
        alt="Playground"
    />
    <div class="ml-2 pb-4">
        <div>
            <h1 class="md:text-xl lg:text-2xl">{parkData?.Name}</h1>
            <div class="flex items-center">
                <p class="md:text-sm lg:text-lg">3.9</p>
                <StarRating rating={7} size={topicReviewSize}></StarRating>
            </div>
            <InfoChips park={parkData}></InfoChips>
        </div>
        <Tabs {activeClasses} {inactiveClasses}>
            <TabItem title="Officiell" open>
                <div class="bg-background-foreground -mt-4">
                    <p class="md:text-sm lg:text-md xl:text-lg">
                        Park Pappans Recension
                    </p>
                    <div class="flex w-full">
                        <div class="flex flex-col w-max">
                            <div class="flex justify-end -mb-1 lg:mb-0">
                                <p class="mr-1">Nöje:</p>
                                <StarRating rating={3} size={topicReviewSize}
                                ></StarRating>
                            </div>
                            <div class="flex justify-end -mb-1 lg:mb-0">
                                <p class="mr-1">Fräschet:</p>
                                <StarRating rating={3} size={topicReviewSize}
                                ></StarRating>
                            </div>
                            <div class="flex justify-end -mb-1 lg:mb-0">
                                <p class="mr-1">Miljö:</p>
                                <StarRating rating={3} size={topicReviewSize}
                                ></StarRating>
                            </div>
                        </div>
                        <div class="justify-end w-full">
                            <div class="flex flex-col">
                                <h1
                                    class=" text-3xl md:text-2xl lg:text-4xl xl:text-5xl text-center font-thin"
                                >
                                    3.8
                                </h1>
                                <StarRating
                                    rating={8}
                                    size={totalReviewSize}
                                    class="justify-center"
                                ></StarRating>
                            </div>
                        </div>
                    </div>
                    <div class="mb-2">
                        <a
                            class="flex items-center text-blue-500"
                            href="https://www.instagram.com/park_pappa?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
                            target="_blank"
                        >
                            <svg
                                role="img"
                                class="mr-1 fill-blue-500"
                                viewBox="0 0 24 24"
                                xmlns="http://www.w3.org/2000/svg"
                                width="16"
                                height="16"
                                ><title>Instagram</title><path
                                    d="M7.0301.084c-1.2768.0602-2.1487.264-2.911.5634-.7888.3075-1.4575.72-2.1228 1.3877-.6652.6677-1.075 1.3368-1.3802 2.127-.2954.7638-.4956 1.6365-.552 2.914-.0564 1.2775-.0689 1.6882-.0626 4.947.0062 3.2586.0206 3.6671.0825 4.9473.061 1.2765.264 2.1482.5635 2.9107.308.7889.72 1.4573 1.388 2.1228.6679.6655 1.3365 1.0743 2.1285 1.38.7632.295 1.6361.4961 2.9134.552 1.2773.056 1.6884.069 4.9462.0627 3.2578-.0062 3.668-.0207 4.9478-.0814 1.28-.0607 2.147-.2652 2.9098-.5633.7889-.3086 1.4578-.72 2.1228-1.3881.665-.6682 1.0745-1.3378 1.3795-2.1284.2957-.7632.4966-1.636.552-2.9124.056-1.2809.0692-1.6898.063-4.948-.0063-3.2583-.021-3.6668-.0817-4.9465-.0607-1.2797-.264-2.1487-.5633-2.9117-.3084-.7889-.72-1.4568-1.3876-2.1228C21.2982 1.33 20.628.9208 19.8378.6165 19.074.321 18.2017.1197 16.9244.0645 15.6471.0093 15.236-.005 11.977.0014 8.718.0076 8.31.0215 7.0301.0839m.1402 21.6932c-1.17-.0509-1.8053-.2453-2.2287-.408-.5606-.216-.96-.4771-1.3819-.895-.422-.4178-.6811-.8186-.9-1.378-.1644-.4234-.3624-1.058-.4171-2.228-.0595-1.2645-.072-1.6442-.079-4.848-.007-3.2037.0053-3.583.0607-4.848.05-1.169.2456-1.805.408-2.2282.216-.5613.4762-.96.895-1.3816.4188-.4217.8184-.6814 1.3783-.9003.423-.1651 1.0575-.3614 2.227-.4171 1.2655-.06 1.6447-.072 4.848-.079 3.2033-.007 3.5835.005 4.8495.0608 1.169.0508 1.8053.2445 2.228.408.5608.216.96.4754 1.3816.895.4217.4194.6816.8176.9005 1.3787.1653.4217.3617 1.056.4169 2.2263.0602 1.2655.0739 1.645.0796 4.848.0058 3.203-.0055 3.5834-.061 4.848-.051 1.17-.245 1.8055-.408 2.2294-.216.5604-.4763.96-.8954 1.3814-.419.4215-.8181.6811-1.3783.9-.4224.1649-1.0577.3617-2.2262.4174-1.2656.0595-1.6448.072-4.8493.079-3.2045.007-3.5825-.006-4.848-.0608M16.953 5.5864A1.44 1.44 0 1 0 18.39 4.144a1.44 1.44 0 0 0-1.437 1.4424M5.8385 12.012c.0067 3.4032 2.7706 6.1557 6.173 6.1493 3.4026-.0065 6.157-2.7701 6.1506-6.1733-.0065-3.4032-2.771-6.1565-6.174-6.1498-3.403.0067-6.156 2.771-6.1496 6.1738M8 12.0077a4 4 0 1 1 4.008 3.9921A3.9996 3.9996 0 0 1 8 12.0077"
                                /></svg
                            >
                            <p>Upptäck mer av Park_pappa!</p>
                        </a>
                        <div class="w-full h-12"></div>
                        <!--Ända anledningen för denhära diven är för att få overlfow scroll att funka-->
                    </div>
                </div>
            </TabItem>
            <TabItem title="Community">
                <div class="w-full h-12"></div>
                <!--Ända anledningen för denhära diven är för att få overlfow scroll att funka-->
            </TabItem>
        </Tabs>
    </div>
</div>
