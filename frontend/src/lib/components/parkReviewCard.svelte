<script lang="ts">
    import StarRating from "./starRating.svelte";
    interface Props {
        name: string,
        stars: number,
        reviewText: string,
        playgroundId: number,
        title: string
    };

    let {name, stars, reviewText, playgroundId, title}: Props = $props();

    let longText = $derived(reviewText.length > 400);
    let showMore = $state(false);
    let shownText = $derived.by(() => {
        if (!longText) {
            return reviewText;
        } else {
            if (!showMore) {
                return reviewText.substring(0, 400) + '...';
            } else {
                return reviewText;
            }
        }
    })
</script>

<div class="border-primary/20 border-2 rounded p-4">
    <h1 class="font-bold text-2xl">{title}</h1>
    <span>{name}</span>
    <StarRating rating={stars * 2} ></StarRating>
    <p>{shownText}</p>
    {#if longText}
        <button class="hover:underline" type="button" onclick={() => {showMore = !showMore}}>{showMore ? 'Visa mindre' : 'Visa mer'}</button>
    {/if}
    <a href="/map?park={playgroundId}" class="text-primary underline">Gå till park</a>
</div>