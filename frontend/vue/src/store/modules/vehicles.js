import API from "@/utils/api";

export const vehicles = {
    state: () => ({
        vehicles: []
    }),
    mutations: {
        setVehicles(state, vehicles) {
            state.vehicles = vehicles
        }
    },
    actions: {
        async loadingVehicles({commit}) {
            try {
                commit('setVehicles', [])

                const { data } = await API.get('vehicles/');

                commit('setVehicles', data)
            }
            catch (e) {

            }
        },
        async loadingVehicle({commit}, id) {
            try {
                const { data } = await API.get('vehicles/' + id);
                return data;
            }
            catch (e) {

            }
        }
    },
    namespaced: true
}