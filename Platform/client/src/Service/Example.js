import axios from 'axios';

import { baseUrl } from './ServiceBase';

const getExampleData = async () => {
    const response = await axios.get(baseUrl + "/Example");
    return response.data;
}

export { getExampleData };
