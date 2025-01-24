import { API_PATH } from '$env/static/private';
import { GOOGLE_MAPS_API_KEY } from '$env/static/private';

export const load = async ({params, url}) => {
    let goToPark = url.searchParams.get('park') ?? null;
    return {
        API_PATH,
        GOOGLE_MAPS_API_KEY,
        goToPark
    };
}
