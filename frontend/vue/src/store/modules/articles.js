import API from "@/utils/api";

export const articles = {
    state: () => ({
        articles: []
    }),
    mutations: {
        setArticles(state, articles) {
            state.articles = articles
        }
    },
    actions: {
        async loadingArticles({commit}) {
            try {
                commit('setArticles', [])

                const { data } = await API.get('articles/');

                commit('setArticles', data)
            }
            catch (e) {

            }
        }
    },
    namespaced: true
}