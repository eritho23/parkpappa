import { API_PATH } from '$env/static/private';
import { env } from '$env/dynamic/private';
const {GOOGLE_MAPS_API_KEY} = env;

export const load = async ({ url, locals }) => {
    let goToPark = url.searchParams.get('park') ?? null;
    const isLoggedIn = locals.pb.authStore.isValid;
    const userId = locals.id;
    return {
        API_PATH,
        GOOGLE_MAPS_API_KEY,
        goToPark,
        isLoggedIn,
        userId,
    };
};
