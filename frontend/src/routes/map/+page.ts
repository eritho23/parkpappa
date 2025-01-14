import type { PageLoad } from './$types';
import { error, json } from '@sveltejs/kit';

export const ssr = false;

export const load: PageLoad = async ({fetch}) => {

    async function raceFetch() {
        const timeoutPromise: Promise<never> = new Promise((_, reject) => setTimeout(() => reject(new Error("request timed out")), 1000));

        return Promise.race([
            timeoutPromise,
            fetch(
                'https://parkpappa-api.cloud.spetsen.net/api/parks'
            ).catch((err) => console.log(err))
        ]) as Promise<Response>
    }

    try {
        const response = await raceFetch();

    if ( !response.ok) {
        console.log("ERROR: ", response.status, response);
        //return json({message: response?.json()}, {status: 400})
    }
    return {
        parks: await response?.json() ?? []
    };
    } catch (err) {
        if (err == "Error: request timed out") {
        //  return error(503, "Request timed out, try again later")
        return {
            parks: undefined
        }
        } else {
            return error(500, "Unexpected Error")
        }
    }
};
