import axios from 'axios';

export const DisplayCovidData=async()=>{//combine multiple search,this will make our system scalable
    try {
        const response= axios.get(`/apidata`);

      return response;
    } catch (error) {
        
    }
}
