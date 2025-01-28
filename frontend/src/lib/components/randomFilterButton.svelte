<!--
    The random filter menu logic and component.
    Ensures the filters are valid when applied.

    Author: Adrian Damianovici
-->
<script lang="ts">
    import { SlidersHorizontal } from 'lucide-svelte';
    import { Modal, MultiSelect } from 'flowbite-svelte';
    import categories from '$lib/filterCategories.json';
    import { userFilterPrefrences } from './filterSettings.svelte';
    let modalOpen = $state(false);

    let include = $state([]);
    let exclude = $state([]);
    $inspect(include);

    function onSubmit() {
        let includeSet = new Set(include);
        let excludeSet = new Set(exclude);
        if (includeSet.intersection(excludeSet).size > 0) {
            console.log('Cannot include and exclude same property!');
        } else {
            // console.log("Worked");
            userFilterPrefrences.include = include;
            userFilterPrefrences.exclude = exclude;
            console.log(userFilterPrefrences, 'settings');
            modalOpen = false;
        }
    }
</script>

<button
    onclick={() => (modalOpen = !modalOpen)}
    class=" absolute right-4 bottom-40 md:bottom-28 size-14 bg-primary border-primary/60 rounded-full flex items-center justify-center brightness-100 active:brightness-95 shadow-md shadow-text-light hover:shadow-text-dark/65"
>
    <SlidersHorizontal
        size={28}
        strokeWidth={2.25}
        class="stroke-background-foreground"
    ></SlidersHorizontal>
</button>
<Modal
    title="Justera Slumparen"
    bind:open={modalOpen}
    outsideclose
    autoclose={false}
>
    <p>Inkludera taggar</p>
    <MultiSelect items={categories} bind:value={include}></MultiSelect>

    <p>Exkludera taggar</p>
    <MultiSelect items={categories} bind:value={exclude}></MultiSelect>

    <div class="">
        <button
            onclick={() => onSubmit()}
            class="h-8 bg-primary/100 ring-primary/60 active:brightness-90 ring-1 text-white whitespace-nowrap py-2 px-2 rounded text-xs"
            >Tillämpa</button
        >
        <button
            onclick={() => (modalOpen = false)}
            class="h-8 ring-primary/100 active:brightness-90 ring-2 text-primary/100 whitespace-nowrap py-2 px-2 rounded text-xs"
            >Avbryt</button
        >
    </div>
</Modal>
