<template>
    <footer class="footer">
        <div class="footer__shape">
            <svg xmlns="http://www.w3.org/2000/svg" height="150px" width="160%" preserveAspectRatio="none" viewBox="0 0 1200 120">
                <path fill="#fff" d="M985.66,92.83C906.67,72,823.78,31,743.84,14.19c-82.26-17.34-168.06-16.33-250.45.39-57.84,11.73-114,31.07-172,41.86A600.21,600.21,0,0,1,0,27.35V120H1200V95.8C1132.19,118.92,1055.71,111.31,985.66,92.83Z"></path>
            </svg>
        </div>
        <div class="footer__wrapper">
            <div class="container">
                <div class="row">
                    <div class="footer__column col-lg-3 col-6">
                        <p class="footer__logo logo">
                            <span class="logo__first">car</span>
                            &
                            <span class="logo__second--light">bike</span>
                        </p>
                        <p class="footer__text">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptas fugit nostrum ea eius placeat dolores culpa repellendus deserunt commodi qui dolorum itaque nobis maiores veniam ipsum, voluptate id hic ut.</p>
                    </div>
                    <div class="footer__column col-lg-3 col-6">
                        <p class="footer__subtitle">Полезные ссылки</p>
                        <nav class="footer__nav">
                            <ul class="footer__menu">
                                <li class="footer__item">
                                    <router-link to="/" class="footer__link">Главная</router-link>
                                </li>
                                <li class="footer__item">
                                    <router-link to="/vehicles" class="footer__link">Автомобили</router-link>
                                </li>
                                <li class="footer__item">
                                    <router-link to="/bikes" class="footer__link">Велосипеды</router-link>
                                </li>
                                <li class="footer__item">
                                    <router-link to="/articles" class="footer__link">Новости</router-link>
                                </li>
                                <li class="footer__item">
                                    <router-link to="/contacts" class="footer__link">Контакты</router-link>
                                </li>
                            </ul>
                        </nav>
                    </div>
                    <div class="footer__column col-lg-3 col-6">
                        <p class="footer__subtitle">Связаться с нами</p>
                        <div class="footer__address">
                            <p>15 Street No, Ox Building, Near Station, 1356.</p>
                            <p>Phone number: (+1) 123 4567 890</p>
                            <p>Email Address: Carrgo@gmail.com</p>
                        </div>
                    </div>
                    <div class="footer__column col-lg-3 col-6">
                        <p class="footer__subtitle">Обратная связь</p>
                        <div class="footer__feedback">
                            <form action="#" class="form">
                                <div class="form__field">
                                    <label for="e-mail" class="form__label" hidden>E-mail</label>
                                    <input type="text" id="e-mail" name="e-mail" class="form__input" placeholder="Email">
                                </div>
                                <div class="form__field">
                                    <label for="subject" class="form__label" hidden>Subject</label>
                                    <input type="text" id="subject" name="subject" class="form__input" placeholder="Сообщение">
                                </div>
                                <button class="form__button button button--light">Отправить</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>
    <div class="footer-line">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <p class="footer-line__copyright">© Copyright 2022 by Tortoiz. All Right Reserved.</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "TheFooter"
}
</script>