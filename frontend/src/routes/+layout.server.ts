/*
    Load file for the navigation bar and some application-wide properties.

    Author: Eric Thorburn
*/
import {PB_PATH} from '$env/static/private';

export const load = async ({ locals }) => {
    const isLoggedIn = locals.id !== '';
    let email = '';
    let avatarUrl = '';
    if (isLoggedIn) {
        email = locals.email ?? '';
        const avatar = await locals.pb
            .collection('users')
            .getOne(locals.id, { fields: 'avatar' });
        // builds the avatar image src url
        avatarUrl = `${PB_PATH}/api/files/${locals.pb.authStore.record?.collectionId}/${locals.pb.authStore.record?.id}/${avatar.avatar}`;
    }

    return {
        avatarUrl,
        email,
        isLoggedIn,
    };
};
