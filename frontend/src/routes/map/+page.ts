/*
    Page script file for fetching the park data. +page.ts files are ran on both
    the server and client, but in this case only on the client since ssr =
    false.

    Author: Adrian Damianovici
*/
import type { PageLoad } from './$types';
import { error, json } from '@sveltejs/kit';
import type { Park, DataParks } from '$lib/types';

export const ssr = false; // Disable server side rendering

export const load: PageLoad = async ({ fetch, data }) => {
    const { API_PATH, GOOGLE_MAPS_API_KEY } = data;
    
    async function raceFetch() {
        const timeoutPromise: Promise<never> = new Promise((_, reject) =>
            setTimeout(() => reject(new Error('request timed out')), 5000)
        );

        return Promise.race([
            timeoutPromise,
            fetch(API_PATH + '/api/parks').catch((err) => console.error(err)),
        ]) as Promise<Response>;
    }

    try {
        const response = await raceFetch();

        if (!response.ok) {
            console.error('ERROR: ', response.status, response);
            //return json({message: response?.json()}, {status: 400})
        }
        return {
            api: API_PATH,
            googleMapsApiKey: GOOGLE_MAPS_API_KEY,
            goToPark: data.goToPark,
            isLoggedIn: data.isLoggedIn,
            mapSelect: data.mapSelect,
            parks: (await response?.json()) ?? [],
            userId: data.userId,
        } as DataParks;
    } catch (err) {
        if (err == 'Error: request timed out') {
            //  return error(503, "Request timed out, try again later")
            return undefined;
        } else {
            return error(500, 'Unexpected Error');
        }
    }
};
