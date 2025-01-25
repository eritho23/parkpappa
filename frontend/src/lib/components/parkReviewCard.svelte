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
</script>

<div class="border-primary/20 border-2 rounded p-4">
    <h1 class="font-bold text-2xl">{title}</h1>
    <span>{name}</span>
    <StarRating rating={stars * 2} ></StarRating>
    <p>{reviewText}</p>
    <a href="/map?park={playgroundId}" class="text-primary underline">Gå till park</a>
</div>