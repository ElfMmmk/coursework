<template>
    <section class="section login">
        <div class="container">
            <div class="row">
                <div class="col-12">
                   <h1 class="login__title">Пожалуйста, авторизуйтесь</h1>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-6 col-12 offset-lg-3">
                    <form @submit.prevent="login" class="login__form form" method="POST">
                        <div class="form__field form__field--login">
                            <label for="username" class="form__label" hidden>Имя пользователя</label>
                            <input required v-model="username" type="text" name="username" id="username" class="form__input form__input--login" placeholder="Имя пользователя">
                        </div>
                        <div class="form__field form__field--login">
                            <label for="password" class="form__label" hidden>Пароль</label>
                            <input required v-model="password" type="password" name="password" id="password" class="form__input form__input--login" placeholder="Пароль">
                        </div>
                        <button class="form__button form__button--login button">Войти</button>
                        <p class="form__helper">Нет аккаунта? <router-link to="/registration">Зарегистрироваться</router-link></p>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<script>

export default {
    name: "LoginView",
    data() {
        return {
            username: '',
            password: ''
        }
    },
    methods: {
        async login(evt) {
            const userAuthData = {
                username: this.username,
                password: this.password
            }

            const isAuthenticated = await this.$store.dispatch('auth/login', userAuthData);
            if (isAuthenticated) this.$router.push('/account');
        },
    },
    mounted() {
        document.title = 'Авторизация в систему';
    }
}
</script>