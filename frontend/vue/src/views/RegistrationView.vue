<template>
    <section class="section login">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h1 class="login__title">Добро пожаловать!</h1>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-6 col-12 offset-lg-3">
                    <form @submit.prevent="registration" class="login__form form" method="POST">
                        <div class="form__field form__field--login">
                            <label for="email" class="form__label" hidden>Email</label>
                            <input required v-model="email" type="text" name="email" id="email" class="form__input form__input--login" placeholder="E-mail">
                        </div>
                        <div class="form__field form__field--login">
                            <label for="username" class="form__label" hidden>Имя</label>
                            <input required v-model="username" type="text" name="username" id="username" class="form__input form__input--login" placeholder="Имя пользователя">
                        </div>
                        <div class="form__field form__field--login">
                            <label for="password" class="form__label" hidden>Пароль</label>
                            <input required v-model="password" type="password" name="password" id="password" class="form__input form__input--login" placeholder="Пароль">
                        </div>
                        <div class="form__field form__field--login">
                            <label for="password2" class="form__label" hidden>Повторите пароль</label>
                            <input required v-model="password2" type="password" name="password2" id="password2" class="form__input form__input--login" placeholder="Повторите пароль">
                        </div>
                        <button class="form__button form__button--login button">Зарегистрироваться</button>
                        <p class="form__helper">Уже есть аккаунт? <router-link to="/login">Войти</router-link></p>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: "RegistrationView",
    data() {
        return {
            email: '',
            username: '',
            password: '',
            password2: ''
        }
    },
    methods: {
        async registration(evt) {
            const userData = {
                username: this.username,
                password: this.password,
                email: this.email,
                password2: this.password2
            }

            const isRegistration = await this.$store.dispatch('auth/registration', userData);
            if (isRegistration) this.$router.push('/login');
        },
    },
    mounted() {
        document.title = 'Регистрация нового пользователя';
    }
}
</script>