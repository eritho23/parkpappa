/*
    The SvelteKit hooks file.
    This file handles authentication and runs on every request. It handles
    authentication state and auth cookies for the client.

    Author: Eric Thorburn
*/

import { redirect } from '@sveltejs/kit';
import { type Handle } from '@sveltejs/kit';
import PocketBase from 'pocketbase';
import { building } from '$app/environment';
import {PB_PATH} from '$env/static/private';

export const handle: Handle = async ({ event, resolve }) => {
    event.locals.id = '';
    event.locals.email = '';
    event.locals.pb = new PocketBase(PB_PATH);

    const isAuth: boolean = event.url.pathname === '/auth';
    if (isAuth || building) {
        event.cookies.set('pb_auth', '', { path: '/', maxAge: 1 });
        return await resolve(event);
    }

    const pb_auth = event.request.headers.get('cookie') ?? '';
    event.locals.pb.authStore.loadFromCookie(pb_auth);

    if (!event.locals.pb.authStore.isValid) {
        event.cookies.set('pb_auth', '', { path: '/', maxAge: 1 });
        return await resolve(event);
    }

    try {
        const auth = await event.locals.pb
            .collection('users')
            .authRefresh<{ id: string; email: string }>();
        event.locals.id = auth.record.id;
        event.locals.email = auth.record.email;
    } catch (_) {
        throw redirect(307, '/');
    }

    const response = await resolve(event);
    const cookie = event.locals.pb.authStore.exportToCookie({
        sameSite: 'lax',
    });
    response.headers.append('set-cookie', cookie);
    return response;
};
