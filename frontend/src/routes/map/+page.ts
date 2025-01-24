import type { PageLoad } from './$types';
import { error, json } from '@sveltejs/kit';
import type { Park, DataParks } from '$lib/types';

export const ssr = false;

export const load: PageLoad = async ({ fetch, data }) => {
    const { API_PATH } = data;
    async function raceFetch() {
        const timeoutPromise: Promise<never> = new Promise((_, reject) =>
            setTimeout(() => reject(new Error('request timed out')), 5000)
        );

        return Promise.race([
            timeoutPromise,
            fetch(API_PATH + '/api/parks').catch((err) => console.log(err)),
        ]) as Promise<Response>;
    }

    try {
        const response = await raceFetch();

        if (!response.ok) {
            console.log('ERROR: ', response.status, response);
            //return json({message: response?.json()}, {status: 400})
        }
        return {
            parks: (await response?.json()) ?? [],
            api: API_PATH,
            goToPark: data.goToPark,
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
