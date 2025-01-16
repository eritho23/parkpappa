import PocketBase from 'pocketbase';
import { env } from '$env/dynamic/private';
import { error, type Handle } from '@sveltejs/kit';
import { sequence } from '@sveltejs/kit/hooks';

export const authentication: Handle = async ({event, resolve}) => {
    event.locals.pb = new PocketBase(env.PB_URL);

    event.locals.pb.authStore.loadFromCookie(event.request.headers.get('cookie') || '');

    try {
        event.locals.pb.authStore.isValid && await event.locals.pb.collection('users').authRefresh();
    } catch(_) {
        event.locals.pb.authStore.clear();
    }

    const response = await resolve(event);

    response.headers.append('set-cookie', event.locals.pb.authStore.exportToCookie());

    return response;
}

export const authorization: Handle = async ({event, resolve}) => {

    if (event.url.pathname.startsWith('/api')) {
        const loggedIn = event.locals.pb.authStore;
        if (!loggedIn) {
            throw error(401, JSON.stringify({message: 'authenticate first'}));
        }
    }

    const response = await resolve(event);
    return response;
}

export const handle = sequence(authentication, authorization);