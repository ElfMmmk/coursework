import axios from "axios";
import router from "../router/index"

const API = axios.create({
    baseURL: '/api/'
})

API.interceptors.request.use(config => {
    if (localStorage.access) {
        config.headers.Authorization = `Bearer ${localStorage.access}`
    }

    return config
},error => {
    console.log(error)
})

API.interceptors.response.use(config => {
    if (localStorage.access) {
        config.headers.Authorization = `Bearer ${localStorage.access}`
    }

    return config
}, error => {
    if (error.response.data.code === 'token_not_valid') {

        axios.post('/api/token/refresh/', {refresh: localStorage.refresh}).then(response => {
            localStorage.access = response.data.access;
            error.config.headers.Authorization = `Bearer ${response.data.access}`;

            return API.request(error.config)
        })
    }

    if (error.response.status === 401) {
        router.push('/login')
    }
})

export default API