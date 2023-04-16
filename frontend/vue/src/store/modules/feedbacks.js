import API from "@/utils/api";

export const feedbacks = {
    state: () => ({
        feedbacks: []
    }),
    mutations: {
        setFeedbacks(state, feedbacks) {
            state.feedbacks = feedbacks
        }
    },
    actions: {
        async loadingFeedbacks({commit}) {
            try {
                commit('setFeedbacks', [])

                const {data} = await API.get('http://django.std-1813.ist.mospolytech.ru/api/feedbacks');

                commit('setFeedbacks', data)
            } catch (e) {

            }
        }
    },
    namespaced: true
}