import { axiosInstance } from ".";

export async function submitMatchData(data) {
    try {
        const response = await axiosInstance.post('/match', data);
        return response.data;  
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}