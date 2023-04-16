<template>
    <tr>
        <DriveItemVehicle :vehicleID="drive.vehicle" />
        <td>{{ drive.total }} руб</td>
        <td>{{ tariff }}</td>
        <td>{{ date }}</td>
        <td>{{ drive.duration }}</td>
    </tr>
</template>

<script>
import DriveItemVehicle from "../components/DriveItemVehicle";
export default {
    name: "DriveItem",
    components: {
        DriveItemVehicle
    },
    props: {
        drive: Object
    },
    computed: {
        date() {
            return new Date(this.drive.date).toLocaleDateString('ru')
        },
        tariff() {
            return ['Поминутный', 'Почасовой', 'Суточный', 'Специальный'][this.drive.tariff - 1];
        }
    }
}
</script>