import axios from "axios";

const API_URL = 'https://justcors.com/tl_21b1f06/http://django.std-1813.ist.mospolytech.ru/api/';

export class AuthService {
    static login({username, password}) {
        return axios.post(API_URL + 'token/', {
            username: username,
            password: password
        }).then(response => {
            if (response.data.refresh) {
                localStorage.setItem('access', response.data.access);
                localStorage.setItem('refresh', response.data.refresh);
            }

            return response.data.access;
        });
    }

    static async verify(token) {
        try {
            const response = await axios.post(API_URL + 'token/verify/', {
                token: token
            });

            return true;
        }
        catch (except) {
            if (except.response.data.code === 'token_not_valid') {
                token = await AuthService.refresh();
                if (token) return true;
            }
        }

        return false;
    }

    static async refresh() {
        try {
            const response = await axios.post(API_URL + 'token/refresh/', {
                refresh: localStorage.refresh
            })

            if (response.data.access) {
                localStorage.setItem('access', response.data.access);
                return response.data.access;
            }

            return response.data;
        }
        catch (e) {
            console.log(e)
        }
    }

    static logout() {
        localStorage.setItem('access', '');
    }

    static register({email, username, password, password2}) {
        return axios.post(API_URL + 'registration/', {
            email: email,
            username: username,
            password: password,
            password2: password2
        });
    }
}