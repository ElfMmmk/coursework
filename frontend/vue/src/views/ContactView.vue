<template>
    <section class="section contacts">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h2 class="section__title">Контакты</h2>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-4 col-6">
                    <div class="contact-info">
                        <img src="@/assets/images/contact_geo.webp" alt="Geo map" class="contact-info__image">
                        <h3 class="contact-info__title">Адрес</h3>
                        <p class="contact-info__description">Адрес: улица Пушкина, дом 34, город Москва, Россия</p>
                    </div>
                </div>
                <div class="col-lg-4 col-6">
                    <div class="contact-info">
                        <img src="@/assets/images/contact_phone.webp" alt="Geo map" class="contact-info__image">
                        <h3 class="contact-info__title">Телефон</h3>
                        <p class="contact-info__description">Телефон: +79991234567, +79991234567</p>
                    </div>
                </div>
                <div class="col-lg-4 col-6 offset-3 offset-lg-0">
                    <div class="contact-info">
                        <img src="@/assets/images/contact_email.webp" alt="Geo map" class="contact-info__image">
                        <h3 class="contact-info__title">E-mail</h3>
                        <p class="contact-info__description">Email: help@carandbike.ru</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: "ContactView",
    mounted() {
        document.title = 'Контакты';
    }
}
</script>