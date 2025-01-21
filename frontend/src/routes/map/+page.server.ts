import { API_PATH } from '$env/static/private';

export const load = async ({params, url}) => {
    let goToPark = url.searchParams.get('park') ?? null;
    return {
        API_PATH,
        goToPark
    };
}
