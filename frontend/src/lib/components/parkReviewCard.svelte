<script lang="ts">
    import StarRating from "./starRating.svelte";
    interface Props {
        name: string,
        stars: number,
        reviewText: string,
        playgroundId: number
    };

    let {name, stars, reviewText, playgroundId}: Props = $props();
</script>

<div class="border-primary/20 border-2 rounded p-4">
    <h1 class="font-bold text-2xl">{name}</h1>
    <StarRating rating={stars * 2} ></StarRating>
    <p>{reviewText}</p>
    <a href="/map?park={playgroundId}" class="text-primary underline">Gå till park</a>
</div>