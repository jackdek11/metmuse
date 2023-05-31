import axios from 'axios';


export default class photosMixin {
    static async getPhotos(page = 1) {
        try{
            let response = await axios.get(
                `http://127.0.0.1:8000/api/v1/images?page=${page}`,
            );
            return response;
        } catch (e){
            return {}
        }
        
    }
    static searchPhoto(id) {
        return axios.get(`http://127.0.0.1:8000/${id}/`);
    }
}