<template>
    <div class="col-lg-3 col-6">
        <div class="vehicle">
            <div class="vehicle__preview">
                <img :src="vehicle.photo" alt="#" class="vehicle__image">
            </div>
            <div class="vehicle__content">
                <p class="vehicle__title">{{ vehicle.name }}</p>
                <p class="vehicle__description">{{ vehicle.description }}</p>
                <a href="#" class="vehicle__button button">Арендовать</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "VehicleItem",
    props: {
        vehicle: Object
    }
}
</script>