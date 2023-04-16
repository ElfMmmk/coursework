<template>
    <TheHeader />
    <main>
        <router-view/>
    </main>
    <TheFooter />
</template>
<script>
import TheFooter from "@/components/TheFooter";
import TheHeader from "@/components/TheHeader";
export default {
    components: { TheHeader, TheFooter }
}
</script>
