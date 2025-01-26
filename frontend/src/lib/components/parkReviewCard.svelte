<script lang="ts">
    import StarRating from "./starRating.svelte";
    import { Trash } from "lucide-svelte";

    let {review, userId} = $props();
    let {stars, body, title, id, parkid} = review;
    let name = review.expand.user.name ?? '[Raderad]';
    let reviewUserId = review.expand.user.id ?? '';


    let userOwnsReview = $derived(userId === reviewUserId);
    $inspect('user owns rev:', userOwnsReview);

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

    async function deleteReview() {
        const res = await fetch('/api/deletereview', {
            method: 'DELETE',
            body: JSON.stringify({
                reviewId: id,
            }),
        });

        if (!res.ok) {
            console.error("req failed");
        } else {
            window.location.href = `/map?park=${parkid}`;
        }
    }
</script>

<div class="border-zinc-500 p-4 border rounded flex flex-col space-y-1">
    {#if userOwnsReview}
        <button class="flex flex-row space-x-2 text-sm hover:underline" onclick={() => deleteReview()}>
            <Trash class="size-4 "/>
            <span>Ta bort recension</span>
        </button>
    {/if}
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