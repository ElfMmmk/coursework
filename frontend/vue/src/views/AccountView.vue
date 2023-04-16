<template>
    <section class="section account">
        <div class="container">
            <div class="row">
                <div class="panel">
                    <div class="col-12">
                        <p class="panel__title">Персональная информация</p>
                    </div>
                    <div class="panel__wrapper">
                        <form class="row form">
                            <div class="col-6 panel__field">
                                <label for="username" class="form__label">Имя пользователя</label>
                                <input required readonly v-model="username" type="text" name="username" id="username" class="form__input form__input--login" placeholder="Имя пользователя">
                            </div>
                            <div class="col-6 panel__field">
                                <label for="email" class="form__label">E-mail</label>
                                <input required readonly v-model="email" type="text" name="email" id="email" class="form__input form__input--login" placeholder="E-mail">
                            </div>
                            <div class="col-6 panel__field">
                                <label for="password" class="form__label">Пароль</label>
                                <input required v-model="password" type="text" name="password" id="password" class="form__input form__input--login" placeholder="Введите новый пароль">
                            </div>
                            <div class="col-6 panel__field">
                                <label for="role" class="form__label">Статус</label>
                                <input required readonly v-model="role" type="text" name="role" id="role" class="form__input form__input--login" placeholder="Статус">
                            </div>
                            <div class="col-12">
                                <button class="form__button form__button--login button">Изменить</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="panel">
                    <div class="col-12">
                        <form @submit.prevent="logout" class="form">
                            <button class="form__button form__button--login button">Выйти из аккаунта</button>
                        </form>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="panel">
                    <div class="col-12">
                        <p class="panel__title">Поездки</p>
                    </div>
                    <div class="col-12">
                        <div class="panel__table">
                            <table class="table">
                                <thead>
                                    <tr>
                                        <th scope="col">Транспортное средство</th>
                                        <th scope="col">Сумма поездки</th>
                                        <th scope="col">Тариф</th>
                                        <th scope="col">Дата</th>
                                        <th scope="col">Длительность</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <DriveItem
                                        v-for="drive in drives"
                                        :key="drive.id"
                                        :drive="drive"
                                    />
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import {mapActions, mapState} from "vuex";
import DriveItem from "../components/DriveItem";

export default {
    name: "AccountView",
    components: { DriveItem },
    data() {
        return {
            role: 'Администратор',
            password: '',
            email: 'admin@carandbike.ru',
            username: 'Admin'
        }
    },
    computed: {
        ...mapState({
            drives: state => state.drives.drives
        })
    },
    methods: {
        ...mapActions({
            loadingDrives: 'drives/loadingDrives',
            logoutUser: 'auth/logout'
        }),
        logout() {
            this.logoutUser();
            this.$router.push('/login');
        }
    },
    created() {
        this.loadingDrives();
    },
    mounted() {
        document.title = 'Личный кабинет';
    }
}
</script>