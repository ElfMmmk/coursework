import API from "@/utils/api";

export const drives = {
    state: () => ({
        drives: []
    }),
    mutations: {
        setDrives(state, drives) {
            state.drives = drives
        }
    },
    actions: {
        async loadingDrives({commit}) {
            try {
                commit('setDrives', [])

                const {data} = await API.get('drives/');

                commit('setDrives', data)
            } catch (e) {

            }
        }
    },
    namespaced: true
}