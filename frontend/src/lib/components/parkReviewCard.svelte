<script lang="ts">
    import StarRating from "./starRating.svelte";

    let {review} = $props();
    let {stars, body, playgroundId, title} = review;
    let name = review.expand.user.name;

    const THRESHOLD = 300;

    let longText = $derived(body.length > THRESHOLD);
    let showMore = $state(false);
    let shownText = $derived.by(() => {
        if (!longText) {
            return body;
        } else {
            if (!showMore) {
                return body.substring(0, THRESHOLD) + '...';
            } else {
                return body;
            }
        }
    })
</script>

<div class="border-zinc-500 p-4 border rounded flex flex-col space-y-1">
    <h1 class="font-bold text-xl">{title}</h1>
    <span>{name}</span>
    <StarRating rating={stars} ></StarRating>
    <p class="text-sm">{shownText}</p>
    <div class="flex flex-row space-x-4">
        {#if longText}
            <button class="hover:underline" type="button" onclick={() => {showMore = !showMore}}>{showMore ? 'Visa mindre' : 'Visa mer'}</button>
        {/if}
    </div>
</div>