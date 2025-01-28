/*
    Authentication logic for the authentication page. Form handling and
    redirecting to the correct park.

    Author: Eric Thorburn
*/
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
        // console.log(redirectPark);
        if (!token || typeof token !== 'string') {
            redirect(303, '/auth');
        }
        cookies.set('pb_auth', JSON.stringify({ token: token }), {
            path: '/',
            maxAge: 60 * 60 * 24 * 7, // one week in seconds
        });
        if (redirectPark) {
            redirect(303, `/map?park=${redirectPark}`); // redirect to the park the user was at
        } else {
            redirect(303, '/');
        }
    },
} satisfies Actions;
