<!--
    Page with a form to create a review. Uses a form action.
    
    Author: Eric Thorburn
-->
<script lang="ts">
    import StarRating from "$lib/components/starRating.svelte";

    let stars = $state(5);

    let {data} = $props();
    let {parkId} = data;
</script>

<div class="m-auto justify-center bg-white border-2 border-primary p-4 rounded">
    <form method="post" class="flex flex-col space-y-4">
        <input type="hidden" value={parkId} name="parkid" />
        <label>
            Titel <br>
            <input type="text" name="title" placeholder="Titel" required />
        </label>
        <label>
            Recension <br>
            <textarea name="review" placeholder="Recension" required></textarea>
        </label>
        <label>
            Betyg <br>
            <input type="range" min="1" bind:value={stars} max="10" name="stars" required />
            <StarRating rating={stars}/>
        </label>
        <button class="border border-primary rounded py-2 hover:bg-primary/10" type="submit">Skicka recension</button>
    </form>
</div>