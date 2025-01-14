import { Config } from 'tailwindcss/types/config';
import flowbitePlugin from 'flowbite/plugin';

/** @type {import('tailwindcss').Config} */
export default {
    content: [
        './src/**/*.{html,js,svelte,ts}',
        './node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}',
    ],
    darkMode: 'selector',
    theme: {
        extend: {
            colors: {
                primary: {
                    DEFAULT: '#E5102C',
                },
                text: {
                    DEFAULT: '#000000',
                    light: '#ACACAC',
                    dark: '#595858',
                },
                background: {
                    DEFAULT: '#ECECEC',
                    foreground: '#FFFFFF',
                },
                ring: {
                    DEFAULT: '#DFDFDF',
                },
                gold: {
                    DEFAULT: 'F2C00E',
                },
            },
            fontWeight: {
                thin: '100',
                normal: '400',
                medium: '500',
                semibold: '600',
            },
        },
        fontFamily: {
            primary: ['Lexend'],
        },
    },
    plugins: [flowbitePlugin],
} as Config;
