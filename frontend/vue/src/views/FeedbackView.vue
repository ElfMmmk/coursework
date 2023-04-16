<template>
    <div>
        {{ feedbacks }}
    </div>
</template>

<script>
import {mapActions, mapState} from "vuex";

export default {
    name: "Feedback",
    computed: {
        ...mapState({
            feedbacks: state => state.feedbacks.feedbacks
        })
    },
    methods: {
        ...mapActions({
            loadingFeedbacks: 'feedbacks/loadingFeedbacks'
        })
    },
    created() {
        this.loadingFeedbacks();
    },
    mounted() {
        document.title = 'Список обращений';
    }
}
</script>