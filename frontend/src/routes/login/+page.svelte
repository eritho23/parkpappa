<script lang="ts">
    let {data} = $props();

    $inspect(data.providers);
</script>

<div class="mx-auto w-1/2 border">
    <form action="?/login" method="post">
        <label>
            <span>E-post</span>
            <input class="input" name="email" title="E-post" type="email" placeholder="eric@example.com" required />
        </label>
        <label>
            <span>Lösenord</span>
            <input class="input" name="password" title="Lösenord" type="password" placeholder="*******" required />
        </label>
        <button type="submit">Login</button>
        <button formaction="?/register">Register</button>
    </form>

    <!--<form method="post">
        {#each data.providers as provider}
            <button formaction="?/{provider.name}">
                    <span>{provider.displayName}</span>
            </button>
        {/each}
    </form>-->
</div>