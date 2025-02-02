<!--
    Component for displaying park attributes.
    This component is part of ParkInfo.

    Author: Adrian Damianovici
-->
<script lang="ts">
    import type { Park } from '$lib/types';
    interface Props {
        park: Park | undefined;
    }
    let { park }: Props = $props();

    const translations = {
        equipment: {
            BBQArea: 'Grillplats',
            ClimbingFrame: 'Klätterställning',
            RainShelter: 'Regnskydd',
            RunningTrack: 'Löpbana',
            SandPlayArea: 'Sandlåda',
            SleddingHill: 'Pulkabacke',
            SwingSet: 'Gungor',
            WaterAvailability: 'Vattentillgänglighet',
            WindShelter: 'Vindskydd',
        },
        typesofplay: {
            BalancingPlay: 'Balansgång',
            CarPlay: 'Billek',
            HopscotchArea: 'Haghoppning',
            PlayCircuit: 'Hinderbana',
            RockingPlay: 'Vagglek',
            RolePlay: 'Rollspel',
            SlidePlay: 'Rutschkana',
            SoundPlay: 'Ljudlek',
            SpinningPlay: 'Snurrställning',
            ToddlerPlay: 'Småbarnsvänligt',
            WaterPlay: 'Vattenlek',
        },
    };

    const playTypes = {
        BalancingPlay: true,
        CarPlay: true,
        HopscotchArea: true,
        PlayCircuit: true,
        RockingPlay: true,
        RolePlay: true,
        SlidePlay: true,
        SoundPlay: true,
        SpinningPlay: true,
        ToddlerPlay: true,
        WaterPlay: true,
    };

    const equipment = {
        BBQArea: false,
        ClimbingFrame: false,
        RainShelter: false,
        RunningTrack: false,
        SandPlayArea: true,
        SleddingHill: false,
        SwingSet: true,
        WaterAvailability: false,
        WindShelter: false,
    };

    const colorMatch = {
        BalancingPlay: 'bg-blue-400/50',
        CarPlay: 'bg-red-400/50',
        HopscotchArea: 'bg-gray-400/50',
        PlayCircuit: 'bg-purple-400/50',
        RockingPlay: 'bg-yellow-400/50',
        RolePlay: 'bg-orange-400/50',
        SlidePlay: 'bg-green-400/50',
        SoundPlay: 'bg-lime-400/50',
        SpinningPlay: 'bg-pink-400/50',
        ToddlerPlay: 'bg-violet-400/50',
        WaterPlay: 'bg-cyan-400/50',

        BBQArea: 'bg-red-400/50',
        ClimbingFrame: 'bg-green-400/50',
        RainShelter: 'bg-blue-400/50',
        RunningTrack: 'bg-orange-400/50',
        SandPlayArea: 'bg-yellow-400/50',
        SleddingHill: 'bg-gray-400/50',
        SwingSet: 'bg-pink-400/50',
        WaterAvailability: 'bg-cyan-400/50',
        WindShelter: 'bg-slate-400/50',
    };

    function objectToTrueArray(
        plays: Park['TypesOfPlay'] | Park['Equipment'] | undefined
    ): string[] {
        if (!plays) {
            return [];
        }
        return Object.entries(plays)
            .filter(([_, value]) => value)
            .map(([key]) => key);
    }

    function getColorFromName(name: string) {
        return Object.entries(colorMatch).find(([key, _]) => key === name)?.[1];
    }
</script>


{#if objectToTrueArray(park?.TypesOfPlay).length > 0}
<p class="text-md text-text-dark mt-1">Lekredskap</p>
<div
    class="flex flex-row gap-1 overflow-x-scroll overflow-y-clip mb-2 no-scrollbar"
>
    {#each objectToTrueArray(park?.TypesOfPlay) as play}
        <div
            class={`px-2 py-1 rounded-md text-sm mt-2 mb-1 ${getColorFromName(play)}`}
        >
            {translations.typesofplay[
                play as keyof typeof translations.typesofplay
            ]}
        </div>
    {/each}
</div>
{/if}

{#if objectToTrueArray(park?.Equipment).length > 0}
<p class="text-md text-text-dark">Utrustning</p>
<div class="flex flex-row gap-1 overflow-x-scroll overflow-y-clip no-scrollbar">
    {#each objectToTrueArray(park?.Equipment) as play}
        <div
            class={`px-2 py-1 rounded-md text-sm mt-1 mb-1 ${getColorFromName(play)}`}
        >
            {translations.equipment[
                play as keyof typeof translations.equipment
            ]}
        </div>
    {/each}
</div>
{/if}
