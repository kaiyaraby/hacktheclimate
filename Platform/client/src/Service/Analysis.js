import axios from 'axios';

import { baseUrl } from './ServiceBase';

/*
 * give this [
 *  {
*       "latitude":
*       "longitude":
 *  },
 * ]
 */
const getAnalysis = async (region) => {
    if (region.length > 2) {
        const response = await axios.post(baseUrl + "/Analysis", region);
        return response.data;
    }
    return {};
};

export { getAnalysis };
