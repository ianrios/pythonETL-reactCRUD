import axios from 'axios'
import { API_URL } from '../constants.js'

export const axiosHelper = ({
    method = 'get',
    url = '',
    data = {},
    // token = '',
    successMethod = r => console.log(r),
    failureMethod = e => console.log(e)
}) => {

    const finalData = JSON.parse(JSON.stringify(data))

    return axios({
        method,
        url: `${API_URL}/${url}`,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
        data: finalData
    })
        .then(successMethod)
        .catch(failureMethod)
}