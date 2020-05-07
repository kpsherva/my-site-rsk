import { InvenioSearchApi } from 'react-searchkit';

function searchApi () {
    const config = new InvenioSearchApi({
        axios: {
            url: 'https://127.0.0.1:5000/api/records/?q="My Thesis"',
            withCredentials: true,
        },
        timeout: 5000,
        headers: { Accept: 'application/json' },
    });
    return config;
}

export default searchApi;

window.searchApi = searchApi
