<script lang="ts">

    const stats = {
         "BalancingPlay": true,
         "ToddlerPlay": true,
         "WaterPlay": true,
         "SpinningPlay": false
    }
    const colorMatch = {
      "BalancingPlay": "blue",
      "CarPlay": "red",
      "HopscotchArea": "gray",
      "PlayCircuit": "purple",
      "RockingPlay": "yellow",
      "RolePlay": "orange",
      "SlidePlay": "green",
      "SoundPlay": "lime",
      "SpinningPlay": "pink",
      "ToddlerPlay": "violet",
      "WaterPlay": "cyan"
    }

    function objectToTrueArray(plays) {
        
    }

</script>

<div class="flex flex-row gap-1">
    {#each stats as stat}
        <div class="px-2 py-1 bg-red-400/50 rounded-lg text-sm mt-1 bg-">{stat}</div>
    {/each}
</div>