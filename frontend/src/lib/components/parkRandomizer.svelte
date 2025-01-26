<script lang="ts">
    import type { DataParks, Park } from '$lib/types';
    import { error } from '@sveltejs/kit';
    import { Dices } from 'lucide-svelte';

    interface Props {
        parks: Park[];
        api: String;
        flyToMarker: (id: string) => void;
    }
    let { parks, api, flyToMarker }: Props = $props();

    async function getRandomPark() {
        try {
            const response: Response = await fetch(api + '/api/parks/random/1');

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
        //$inspect(park[0]); Denna throwade error ta tillbaka om jag hade fel
        flyToMarker(park[0].Id);
    }}
    class=" absolute right-8 bottom-20 md:bottom-12 size-14 bg-background-foreground border border-text-light rounded-full flex items-center justify-center brightness-100 active:brightness-95 shadow-md shadow-text-light hover:shadow-text-dark/65"
>
    <Dices size={28} strokeWidth={2.25} class="stroke-primary"></Dices>
</button>
