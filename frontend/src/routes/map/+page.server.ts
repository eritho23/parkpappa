import { API_PATH } from '$env/static/private';
import { GOOGLE_MAPS_API_KEY } from '$env/static/private';

export const load = async ({ params, url, locals }) => {
    let goToPark = url.searchParams.get('park') ?? null;
    const isLoggedIn = locals.pb.authStore.isValid;
    return {
        API_PATH,
        GOOGLE_MAPS_API_KEY,
        goToPark,
        isLoggedIn,
    };
};
