import redirect, { type Actions } from '@sveltejs/kit';

export const actions = {
    default: async ({ request, cookies }) => {
        const form = await request.formData();
        const token = form.get('token');
        if (!token || typeof token !== 'string') {
            throw redirect(303, '/auth');
        }
        cookies.set('pb_auth', JSON.stringify({ token: token }), {
            path: '',
            maxAge: 60 * 60 * 24 * 7,
        });
        throw redirect(303, '/');
    },
} satisfies Actions;
