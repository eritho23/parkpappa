import { error, json } from '@sveltejs/kit';

export const GET = async ({locals, url}) => {
    const parkId = url.searchParams.get('id') ?? -1;
    if (parkId === -1) {
        return error(400, JSON.stringify({message: 'You must have a search param.'}));
    }

    const reviews = await locals.pb.collection('reviews').getFullList({filter: `parkid=${parkId}`, expand: "user"});

    return json(reviews)
}