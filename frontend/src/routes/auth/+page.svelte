<script lang="ts">
    import PocketBase from 'pocketbase';
    
    // import { PB_PATH } from '$env/static/public';

    const pb = new PocketBase('https://parkpappa-pb.superdator.spetsen.net');

    let errorMsg: string = $state('');

    async function login(form: HTMLFormElement) {
        try {
            await pb.collection('users').authWithOAuth2({provider: 'google'})
            form.token.value = pb.authStore.token;
            form.submit();
        } catch (err) {
            errorMsg = String(err);
        }
    }
</script>


<div class="bg-white size-72 md:size-96 m-auto border-primary/40 rounded border-2 flex flex-col justify-center text-center space-y-5">
    <h1 class="text-3xl font-bold">Logga in</h1>
    {#if errorMsg}
        <div class="">
            <span class="text-primary">Fel: {errorMsg}, försök igen senare</span>
        </div>
    {/if}
    <form class="" method="post" onsubmit={(e) => {e.preventDefault(); login(e.currentTarget)}}>
        <input name="token" type="hidden" />
        <button class="p-4 border-2 border-primary rounded font-bold bg-primary/10">
            Logga in med Google
        </button>
    </form>
</div>