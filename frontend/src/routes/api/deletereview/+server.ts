/*
    API Server for getting reviews.
    Defines a DELETE HTTP verb which deletes reviews. Uses the request body.

    Author: Eric Thorburn
*/

import { error, json } from '@sveltejs/kit';
import { ClientResponseError } from 'pocketbase';

export const DELETE = async ({locals, request}) => {
    // Checks auth
    if (!locals.pb.authStore.isValid) {
        return error(401); // 401 Unauthorized
    }
    const body = await request.json()
    const reviewId = body.reviewId ?? null;

    let reviewUser = null;

    if (reviewId) {
        try {
            reviewUser = await locals.pb.collection('reviews').getOne(reviewId, {expand:'user'});

        } catch (err) {
            if (err instanceof ClientResponseError) {
                if (err.status === 404) {
                    return error(400, err.response.message);
                }
            }
        }

        if (reviewUser && reviewUser.expand?.user.id !== locals.id) {
            return error(401, JSON.stringify({msg:'Unauthorized'}));
        }

        try {
            await locals.pb.collection('reviews').delete(reviewId);
        } catch (err) {
            if (err instanceof ClientResponseError) {
                if (err.status === 404) {
                    return error(400, JSON.stringify({msg:err.response.message}))
                }
            } else {
                console.error('Unexpected error:', err);
                return error(500);
            }
        }
    } else {
        return error(400, JSON.stringify({msg:`Review id must be supplied (got ${reviewId})`}));
    }

    return json(200);
}