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

{#if errorMsg}
    <span>{errorMsg}</span>
{/if}

<form method="post" onsubmit={(e) => {e.preventDefault(); login(e.currentTarget)}}>
    <input name="token" type="hidden" />
    <button class="p-4 border rounded font-bold">
        Login using Google
    </button>
</form>