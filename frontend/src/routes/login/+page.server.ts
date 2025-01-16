import { error, fail, redirect } from '@sveltejs/kit'
import {env} from '$env/dynamic/private';
import { ClientResponseError } from 'pocketbase';

export const load = async ({locals, url}) => {
    if (locals.pb.authStore.record) {
        return redirect(303, '/reviews')
    }

    const authMethods = await locals.pb.collection('users').listAuthMethods();
    const fail = url.searchParams.get('fail') === 'true';

    return { providers: authMethods.oauth2.providers, fail}
}

export const actions = {
    register: async ({locals, request}) => {
        const data = await request.formData();
        const email = data.get('email');
        const password = data.get('password');

        if (!email || !password) {
            return fail(400, {emailRequired: email === null, passwordRequired: password === null});
        }

        data.set('passwordConfirm', password?.toString());

        try {
            await locals.pb.collection('users').create(data);
            await locals.pb.collection('users').authWithPassword(email.toString(), password.toString())

        } catch (err) {
            const error = err as ClientResponseError;
            return fail(500, {fail:true, message: error.data.message})
        }

        throw redirect(303, '/reviews')
    },
    login: async ({ locals, request }) => {
        const data = await request.formData();
        const email = data.get('email');
        const password = data.get('password');
        
        if (!email || !password) {
            return fail(400, { emailRequired: email === null, passwordRequired: password === null });
        }

        try {
            await locals.pb.collection('users').authWithPassword(email.toString(), password.toString());
        } catch (err) {
            const error = err as ClientResponseError;
            return fail(500, {fail: true, message: error.data.message});
        }

        throw redirect(303, '/reviews');
    },
    /*google: async ({locals, cookies}) => {
        const provider = (await locals.pb.collection('users').listAuthMethods()).oauth2.providers.find((p: any) => p.name === 'google') || null;
        if (!provider) throw error(500);
        cookies.set('provider', JSON.stringify(provider), {httpOnly: true, path: `/auth/callback/google`});

        throw redirect(303, provider.authURL + env.REDIRECT_URL + provider.name);
    },*/
    logout: async ({ locals }) => {
        locals.pb.authStore.clear();
        throw redirect(303, '/login');
    }
}