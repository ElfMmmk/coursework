<template>
    <div class="col-lg-4 col-6">
        <div class="post">
            <div class="post__preview">
                <img :src="article.preview" alt="#" class="post__image">
            </div>
            <div class="post__info">
                <h3 class="post__title">
                    <a href="#" class="post__link">{{ article.title }}</a>
                </h3>
                <p class="post__description">{{ article.excerpt }}</p>
                <p class="post__created-info">
                    {{ article.created_at }}, by<span class="post__author">{{ article.author }}</span>
                </p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ArticleItem",
    props: {
        article: Object
    }
}
</script>