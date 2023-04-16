<template>
    <section class="section vehicles">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h2 class="section__title">Автомобили</h2>
                </div>
            </div>
            <div class="row">
                <template v-if="vehicles.length">
                    <VehicleItem
                        v-for="vehicle in vehicles"
                        :key="vehicle.id"
                        :vehicle="vehicle"
                    />
                </template>
                <template v-else>
                    <div class="col-12">
                        <p>Список автомобилей пуст..</p>
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
    name: "VehicleView",
    components: { VehicleItem },
    computed: {
        ...mapState({
            vehicles: state => state.vehicles.vehicles
        })
    },
    methods: {
        ...mapActions({
            loadingVehicles: 'vehicles/loadingVehicles'
        })
    },
    created() {
        this.loadingVehicles();
    },
    mounted() {
        document.title = 'Список автомобилей';
    }
}
</script>