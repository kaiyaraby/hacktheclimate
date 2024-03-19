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
const getAccessibilityAnalysis = async (region) => {
    if (region.length > 2) {
        const response = await axios.post(baseUrl + "/Analysis/accessibilityAnalysis", region);
        return response.data;
    }
    return {};
};

const getTurbineAnalysis = async (region) => {
    if (region.length > 2)
    {
        const response = await axios.post(baseUrl + "/Analysis/turbineAnalysis", region);
        return response.data;
    }
    return {};
}

export { getAccessibilityAnalysis, getTurbineAnalysis };
