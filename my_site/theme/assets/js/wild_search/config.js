import { InvenioSearchApi } from 'react-searchkit';

export const searchApi = new InvenioSearchApi({
  axios: {
      url: 'https://127.0.0.1:5000/api/records/q=NANANANA',
      withCredentials: true,
    },
  timeout: 5000,
  headers: { Accept: 'application/json' },
});
