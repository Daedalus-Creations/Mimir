<template>
    <Card
            v-for="quote in quotes"
            :key="quote.id"
            :id="quote.id"
    ></Card>
</template>

<script lang="ts">
    import Card from '@/components/Card.vue'
    import { Component, Vue } from 'vue-property-decorator'
    import {readQuotes} from '@/store/main/getters.ts'

    @Component({
        components: {
            Card
        }
    })

    export default class Cards extends Vue {
        get quotes() {
            return readQuotes(this.$store);
        }
    }

</script>

<style scoped>

</style>