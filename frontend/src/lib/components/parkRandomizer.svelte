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
</script>

<button
    onclick={async () => {
        const park = await getRandomPark();
        // console.log(park);
        //$inspect(park[0]); Denna throwade error ta tillbaka om jag hade fel
        flyToMarker(park[0].Id);
    }}
    class=" absolute right-4 bottom-24 md:bottom-12 size-14 bg-background-foreground border border-text-light rounded-full flex items-center justify-center brightness-100 active:brightness-95 shadow-md shadow-text-light hover:shadow-text-dark/65"
>
    <Dices size={28} strokeWidth={2.25} class="stroke-primary"></Dices>
</button>
