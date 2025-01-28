/*
    Provide form actions for the settings page as well as information regarding
    the current settings.

    Author: Eric Thorburn
*/

import { redirect } from '@sveltejs/kit';

export const load = async ({locals}) => {
    if (!locals.pb.authStore.isValid) {
        throw redirect(307, '/auth');
    }

    const mapSelect = locals.pb.authStore.record?.preferedMapShare ?? '';

    const email = locals.email;

    return {
        email,
        mapSelect,
    };
}

export const actions = {
    deleteAccount: async ({locals, request, cookies }) => {
        const form = await request.formData();
        const email = form.get('email');

        if (email !== locals.email) {
            return { success: false, msg: 'E-mail does not match', action: 'deleteAccount' }
        } else {
            await locals.pb.collection('users').delete(locals.id);
            cookies.delete('pb_data', {path: '/'});
            return redirect(303, '/auth');
        }
    },
    mapProvider: async ({locals, request}) => {
        const form = await request.formData();
        const mapSelect = form.get('mapSelect');
        if (mapSelect === 'apple' || mapSelect === 'google' || mapSelect === 'waze') {
            try {
                await locals.pb.collection('users').update(locals.id, { preferedMapShare: mapSelect })
            } catch {
                return {success: false, action: 'mapProvider'}
            }
        }
        
    },
}