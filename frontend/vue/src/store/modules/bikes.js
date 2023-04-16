import API from "@/utils/api";

export const bikes = {
    state: () => ({
        bikes: []
    }),
    mutations: {
        setBikes(state, bikes) {
            state.bikes = bikes
        }
    },
    actions: {
        async loadingBikes({commit}) {
            try {
                commit('setBikes', [])

                const {data} = await API.get('bikes/');

                commit('setBikes', data)
            } catch (e) {

            }
        }
    },
    namespaced: true
}