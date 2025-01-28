<!--
    Component displaying stars for the rating system.
    Contains logic for transforming a number into the correct number of stars / half stars

    Author: Adrian Damianovici
-->
<script lang="ts">
    import { error } from '@sveltejs/kit';
    import { Star, StarHalf } from 'lucide-svelte';
    let { rating = 0, class: className = '', size = 24 } = $props();


    let fullStars = $derived(rating <= 10 && rating > 0 ? Math.floor(rating / 2) : undefined);
    let displayHalfStar = $derived(rating <= 10 && rating > 0 ? rating % 2 === 1 : undefined);

    function range(length: number) {
        return Array.from({ length });
    }
</script>

{#if fullStars !== undefined && displayHalfStar !== undefined}
    <div class={`${className} flex`}>
        <div class="flex items-center">
            <div class=" flex">
                {#each range(5) as _}
                    <Star strokeWidth={0} fill="#ACACAC" {size} />
                {/each}
            </div>
            <div class="absolute flex">
                {#each range(fullStars) as rating}
                    <Star
                        strokeWidth={0}
                        color="gold"
                        fill="gold"
                        class="z-50"
                        {size}
                    />
                {/each}
                {#if displayHalfStar}
                    <StarHalf
                        strokeWidth={0}
                        color="gold"
                        fill="gold"
                        class="z-50"
                        {size}
                    />
                {/if}
            </div>
        </div>
    </div>
{:else}
    <p class="text-sm text-red-500">{'{Not Defined}'}</p>
    {console.error('ERROR: Rating must be between 0-10')}
{/if}
