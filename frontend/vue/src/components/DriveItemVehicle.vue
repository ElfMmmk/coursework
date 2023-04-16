<template>
    <th scope="row">{{ vehicle.name }} <small>“{{ vehicle.number }}”</small></th>
</template>
<script>
import {mapActions} from "vuex";

export default {
    data() {
        return {
            vehicle: {}
        }
    },
    props: {
        vehicleID: Number
    },
    methods: {
        ...mapActions({
            loadingVehicle: 'vehicles/loadingVehicle'
        })
    },
    async created() {
        this.vehicle = await this.loadingVehicle(this.vehicleID);
    }
}
</script>