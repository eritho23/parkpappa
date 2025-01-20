import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ request }) => {
    const userAgent = request.headers.get('user-agent');
    console.log(userAgent);

    if (!userAgent) {
        return {
            isAndroid: false,
            isDesktop: true,
            isIOS: false,
            isMac: false,
            isMobile: false,
            isWindows: false,
            userAgent,
        };
    }

    const isMobile = /Mobi|Android/i.test(userAgent);
    const isDesktop = !isMobile;
    const isAndroid = /Android/i.test(userAgent);
    const isIOS = /iPhone|iPad|iPod/i.test(userAgent);
    const isWindows = userAgent.toLowerCase().includes('windows');
    const isMac = userAgent.toLowerCase().includes('macintosh');

    return {
        isAndroid,
        isDesktop,
        isIOS,
        isMac, 
        isMobile,
        isWindows,
        userAgent,
    };
};
