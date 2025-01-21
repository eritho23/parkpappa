<script lang="ts">
    import reviews from './reviews.json';
    import ParkReviewCard from '$lib/components/parkReviewCard.svelte';
</script>

<div class="mx-auto w-3/4 flex flex-col space-y-5 overflow-auto mt-5">
    <h1 class="font-bold text-4xl">Testrecensioner från våra användare</h1>
    {#each reviews as theRev}
        <ParkReviewCard name={theRev.name} playgroundId={theRev.playgroundId} reviewText={theRev.reviewText} stars={theRev.stars} />
    {/each}
</div>