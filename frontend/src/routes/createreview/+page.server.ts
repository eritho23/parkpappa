import { error, redirect } from '@sveltejs/kit'

export const load = async ({locals, url}) => {
    if (!locals.pb.authStore.isValid) {
        throw redirect(303, '/auth');
    }

    const parkId = url.searchParams.get('park') ?? '';

    return {
        parkId
    }
}

export const actions = {
    default: async ({request, locals}) => {
        if (locals.pb.authStore.isValid) {
            const form = await request.formData();
            const title = form.get('title');
            const stars = form.get('stars');
            const review = form.get('review');
            const parkid = form.get('parkid');
            if (!title || !stars || !review || !parkid) {
                return error(400)
            }

            await locals.pb.collection('reviews').create({parkid, title, stars, body: review, user: locals.id});

            throw redirect(303, `/map?park=${parkid}`);
        } else {
            return error(400);
        }
    },
}