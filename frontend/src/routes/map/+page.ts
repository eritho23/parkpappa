import type { PageLoad } from './$types';

export const ssr = false;

export const load: PageLoad = async ({fetch}) => {
    const response: Response | void = await fetch(
        'https://parkpappa.onrender.com/api/parks'
    ).catch((err) => console.log(err));

    return {
        parks: await response?.json() ?? []
    };
};
