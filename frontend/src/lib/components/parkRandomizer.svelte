<!--
    A component related to getting a random park.
    This component handles user preferences and fetching of the random park.

    Author: Adrian Damianovici
-->

<script lang="ts">
    import type { DataParks, Park } from '$lib/types';
    import { error, json } from '@sveltejs/kit';
    import { Dices } from 'lucide-svelte';
    import { userFilterPrefrences } from './filterSettings.svelte';
    import { fade } from 'svelte/transition';

    interface Props {
        parks: Park[];
        api: String;
        flyToMarker: (id: string) => void;
    }
    let { parks, api, flyToMarker }: Props = $props();

    const mapArrayToObject = (array: string[]): Record<string, boolean> => {
        return array.reduce((acc: Record<string, boolean>, str: string) => {
            acc[str] = true;
            return acc;
        }, {});
    };

    async function getRandomPark() {
        try {
            const body = JSON.stringify({
                include: mapArrayToObject(userFilterPrefrences.include),
                exclude: mapArrayToObject(userFilterPrefrences.exclude),
            });
            let response: Response;
            if (
                userFilterPrefrences.exclude.length > 0 ||
                userFilterPrefrences.include.length > 0
            ) {
                response = await fetch(api + '/api/parks/random_filtered', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: body,
                });
            } else {
                response = await fetch(api + '/api/parks/random/1');
            }

            if (!response.ok) {
                console.error('ERROR: ', response.status, response);
                //return json({message: response?.json()}, {status: 400})
            }
            return (await response?.json()) ?? [];
        } catch (err) {
            if (err == 'Error: request timed out') {
                return error(503, 'Request timed out, try again later');
            } else {
                return error(500, 'Unexpected Error');
            }
        }
    }

    let noParksError = $state(false);

    function displayErrorMessage() {
        noParksError = true;
        setTimeout(() => {
            noParksError = false;
        }, 3000); // Adjust the time as needed
    }
</script>

<button
    onclick={async () => {
        const park = await getRandomPark();
        if (park.length === 0) {
            displayErrorMessage();
        } else {
            flyToMarker(park[0].Id);
        }
    }}
    class=" absolute right-4 bottom-24 md:bottom-12 size-14 bg-background-foreground border border-text-light rounded-full flex items-center justify-center brightness-100 active:brightness-95 shadow-md shadow-text-light hover:shadow-text-dark/65"
>
    <Dices size={28} strokeWidth={2.25} class="stroke-primary"></Dices>
</button>

{#if noParksError}
    <div class="absolute right-20 bottom-36 md:bottom-24 bg-primary text-white p-2 rounded w-3/4 md:w-1/2 lg:w-1/3" transition:fade={{ duration: 100 }}>
        Inga parker hittades, uppdatera filter
    </div>
{/if}