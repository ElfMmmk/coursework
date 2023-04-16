<template>
    <section class="section blog">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h2 class="section__title">Новости</h2>
                </div>
            </div>
            <div class="row">
                <ArticleItem
                    v-for="article in articles"
                    :key="article.id"
                    :article="article"
                />
            </div>
        </div>
    </section>
</template>

<script>
import ArticleItem from "@/components/ArticleItem";
import {mapActions, mapState} from "vuex";

export default {
    name: "ArticleView",
    components: { ArticleItem },
    computed: {
        ...mapState({
            articles: state => state.articles.articles
        })
    },
    methods: {
        ...mapActions({
            loadingArticles: 'articles/loadingArticles'
        })
    },
    created() {
        this.loadingArticles();
    },
    mounted() {
        document.title = 'Новости';
    }
}
</script>
