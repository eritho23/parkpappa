export const load = async ({ locals }) => {
    const isLoggedIn = locals.id !== '';
    let email = '';
    let avatarUrl = '';
    if (isLoggedIn) {
        email = locals.email ?? '';
        const avatar = await locals.pb
            .collection('users')
            .getOne(locals.id, { fields: 'avatar' });
        avatarUrl = `https://parkpappa-pb.superdator.spetsen.net/api/files/${locals.pb.authStore.record?.collectionId}/${locals.pb.authStore.record?.id}/${avatar.avatar}`;
    }

    return {
        avatarUrl,
        email,
        isLoggedIn,
    };
};
