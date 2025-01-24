import { Loader } from '@googlemaps/js-api-loader';

export interface GoogleMapsOptions {
	apiKey: string;
	version?: string;
	libraries?: string[];
}

export async function loadGoogleMaps({ apiKey, version = 'weekly', libraries = [] }: GoogleMapsOptions): Promise<void> {
	const loader = new Loader({
		apiKey,
		version,
		libraries,
	});
	await loader.load();
}
