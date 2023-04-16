<template>
    <section class="section vehicles">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h2 class="section__title">Велосипеды</h2>
                </div>
            </div>
            <div class="row">
                <template v-if="bikes.length">
                    <VehicleItem
                        v-for="bike in bikes"
                        :key="bike.id"
                        :vehicle="bike"
                    />
                </template>
                <template v-else>
                    <div class="col-12">
                        <p>Список велосипедов пуст..</p>
                    </div>
                </template>
            </div>
        </div>
    </section>
</template>

<script>
import VehicleItem from "@/components/VehicleItem";
import {mapActions, mapState} from "vuex";

export default {
    name: "BikeView",
    components: { VehicleItem },
    computed: {
        ...mapState({
            bikes: state => state.bikes.bikes
        })
    },
    methods: {
        ...mapActions({
            loadingBikes: 'bikes/loadingBikes'
        })
    },
    created() {
        this.loadingBikes();
    },
    mounted() {
        document.title = 'Список велосипедов';
    }
}
</script>