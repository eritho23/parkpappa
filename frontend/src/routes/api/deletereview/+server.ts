import { error, json } from '@sveltejs/kit';
import Client, { ClientResponseError } from 'pocketbase';

export const DELETE = async ({locals, request}) => {
    if (!locals.pb.authStore.isValid) {
        return error(401);
    }
    const body = await request.json()
    const reviewId = body.reviewId ?? null;

    if (reviewId) {
        try {
            const reviewUser = await locals.pb.collection('reviews').getOne(reviewId, {expand:'user'});

            if (reviewUser.expand?.user.id !== locals.id) {
                return error(401, JSON.stringify({msg:'Unauthorized'}));
            }
        } catch (err) {
            if (err instanceof ClientResponseError) {
                if (err.status === 404) {
                    return error(400, err.response.message);
                }
            }
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