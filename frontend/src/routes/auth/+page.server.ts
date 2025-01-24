import { type Actions } from '@sveltejs/kit';
import { redirect } from '@sveltejs/kit';

export const load = async ({url}) => {
    const returnPark = url.searchParams.get('redirectpark') ?? '';

    return {
        returnPark
    };
}

export const actions = {
    default: async ({ request, cookies }) => {
        const form = await request.formData();
        const token = form.get('token');
        const redirectPark = form.get('redirectpark') ?? '';
        console.log(redirectPark);
        if (!token || typeof token !== 'string') {
            redirect(303, '/auth');
        }
        cookies.set('pb_auth', JSON.stringify({ token: token }), {
            path: '/',
            maxAge: 60 * 60 * 24 * 7,
        });
        if (redirectPark) {
            redirect(303, `/map?park=${redirectPark}`)
        } else {
            redirect(303, '/');
        }
    },
} satisfies Actions;
