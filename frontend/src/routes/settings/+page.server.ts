import { redirect } from '@sveltejs/kit';

export const load = async ({locals}) => {
    if (!locals.pb.authStore.isValid) {
        throw redirect(303, '/auth');
    }

    const mapSelect = locals.pb.authStore.record?.preferedMapShare ?? '';

    return {
        mapSelect
    };
}

export const actions = {
    default: async ({locals, request}) => {
        const form = await request.formData();
        const mapSelect = form.get('mapSelect');
        if (mapSelect === 'apple' || mapSelect === 'google' || mapSelect === 'waze') {
            await locals.pb.collection('users').update(locals.id, { preferedMapShare: mapSelect })
        }
    },
}