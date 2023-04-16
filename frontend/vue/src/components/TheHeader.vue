<template>
    <header class="header">
        <div class="header__top">
            <div class="container">
                <div class="row">
                    <div class="col-12 col-lg-6">
                        <div class="header__left">
                            <router-link to="/" class="header__logo logo">
                                <span class="logo__first">car</span>
                                &
                                <span class="logo__second">bike</span>
                            </router-link>
                            <div class="header__search">
                                <form action="#" class="form">
                                    <label for="search" class="form__label" hidden></label>
                                    <input type="text" name="search" id="search" class="form__input" placeholder="Поиск автомобиля или велосипеда">
                                    <button class="button button--search">
                                        <svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="30px">
                                            <path fill="currentColor" d="M21.78,12.53l-3.94,4c-0.15,0.15-0.34,0.22-0.53,0.22s-0.38-0.07-0.53-0.22c-0.3-0.29-0.3-0.76-0.01-1.06
                                                    l2.69-2.72H2.75C2.34,12.75,2,12.41,2,12c0-0.41,0.34-0.75,0.75-0.75h16.71l-2.69-2.72c-0.29-0.3-0.29-0.77,0.01-1.06
                                                    c0.29-0.3,0.77-0.29,1.06,0l3.94,4C22.07,11.77,22.07,12.23,21.78,12.53z"/>
                                        </svg>
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="col-12 col-lg-6">
                        <div class="header__right">
                            <router-link to="/account" class="header__button button button--light">Личный кабинет</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="header__bottom">
            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <nav class="header__nav">
                            <ul class="header__menu menu">
                                <li class="menu__item">
                                    <router-link to="/" class="menu__link">Главная</router-link>
                                </li>
                                <li class="menu__item">
                                    <router-link to="/vehicles" class="menu__link">Автомобили</router-link>
                                </li>
                                <li class="menu__item">
                                    <router-link to="/bikes" class="menu__link">Велосипеды</router-link>
                                </li>
                                <li class="menu__item">
                                    <router-link to="/articles" class="menu__link">Новости</router-link>
                                </li>
                                <li class="menu__item">
                                    <router-link to="/contacts" class="menu__link">Контакты</router-link>
                                </li>
                            </ul>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    </header>
</template>

<script>
export default {
    name: "TheHeader"
}
</script>