/*
    API Server for getting reviews.
    Defines a GET HTTP verb which returns reviews. Uses a search parameter.

    Author: Eric Thorburn
*/ 
import { error, json } from '@sveltejs/kit';

export const GET = async ({locals, url}) => {
    const parkId = url.searchParams.get('id') ?? -1;
    if (parkId === -1) {
        return error(400, JSON.stringify({message: 'You must have a search param.'}));
    }

    const reviews = await locals.pb.collection('reviews').getFullList({filter: `parkid=${parkId}`, expand: "user", sort: "-created"});

    return json(reviews)
}