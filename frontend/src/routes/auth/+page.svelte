<!--
    Authentication page with 'Sign in with Google' flow
-->
<script lang="ts">
    import PocketBase from 'pocketbase';
    import GoogleButton from '$lib/components/GoogleButton.svelte';
    import {PB_PATH} from '$env/static/private';
    const pb = new PocketBase(PB_PATH);

    let {data} = $props();

    let errorMsg: string = $state('');

    async function login(form: HTMLFormElement) {
        try {
            await pb.collection('users').authWithOAuth2({provider: 'google', createData: {preferedMapShare: 'google'}})
            form.token.value = pb.authStore.token;
            form.redirectpark.value = data.returnPark;
            form.submit();
        } catch (err) {
            errorMsg = String(err);
        }
    }
</script>


<div class="bg-white size-72 md:size-96 m-auto border-primary/40 rounded border-2 flex flex-col text-center space-y-5 p-6 h-96">
    <div class="spacer h-5"></div>
    <!-- Centered content -->
    <div class="flex flex-col justify-center items-center flex-grow">
        <h1 class="text-3xl font-bold">Logga in</h1>
        <div class="spacer h-5"></div>
        <form class="" method="post" onsubmit={(e) => {e.preventDefault(); login(e.currentTarget)}}>
            <input name="token" type="hidden" />
            <input name="redirectpark" type="hidden" />
            <GoogleButton />
        </form>
    </div>
    
    <!-- Separate content not affecting centering -->
    <div class="text-left mt-10 text-xs mx-10 pb-4">
        <ul class="list-disc list-inside text-gray-500">
            <li>Synkronisera dina inställningar på alla dina enheter</li>
            <li>Lämna recensioner på parker du besöker</li>
        </ul>
    </div>
</div>

