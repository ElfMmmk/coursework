import { AuthService } from "@/services/AuthService";

export const auth = {
    state: () => ({
        token: localStorage.access || '',
        refresh: localStorage.refresh || ''
    }),
    getters: {
        isAuthenticated: state => !!state.token
    },
    mutations: {
        setToken(state, token) {
            state.token = token;
        }
    },
    actions: {
        login({commit}, userAuthData) {
            return AuthService.login(userAuthData).then(token => {
                commit('setToken', token);
                return true;
            }).catch(except => {
                return false;
            })
        },
        async verify({state}) {
            return await AuthService.verify(state.token);
        },
        refresh({state, commit}) {
            AuthService.refresh(state.refresh).then(token => {
                commit('setToken', token);
            })
        },
        logout({commit}) {
            AuthService.logout();
            commit('setToken', '');
        }
    },
    namespaced: true
}