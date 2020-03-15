<template>
<div>
    <div class="section" v-if="quotes.length > 0">
    <Card
            v-for="quote in quotes"
            :key="quote.id"
            :id="quote.id"
    ></Card>
    </div>
    <section class="hero" style="height:100%" v-else>
        <div class="hero-body">
            <div class="container has-text-centered">
                <h1 class="title">
                    <b-icon icon="quote-right"></b-icon>
                </h1>
                <h2 class="subtitle">
                    Add some quotes
                </h2>
            </div>
        </div>
    </section>

    <b-button
            v-if="!newQuoteOpen"
            type="is-primary"
            size="is-large"
            rounded
            style="bottom:10vh;right:10vh;position:fixed;z-index: 9999"
            @click="newQuoteOpen=true"
    >
        <b-icon icon="plus"></b-icon>
    </b-button>
    <b-modal :active.sync="newQuoteOpen" trap-focus has-modal-card >
        <NewQuote @close="()=>{newQuoteOpen=false}" ></NewQuote>
    </b-modal>
</div>
</template>

<script lang="ts">
    import Card from '@/components/Card.vue'
    import NewQuote from '@/components/NewQuote.vue'
    import { Component, Vue } from 'vue-property-decorator'
    import {readQuotes} from '@/store/main/getters.ts'
    import {dispatchLoadQuotes} from "@/store/main/actions";

    @Component({
        components: {
            Card,
            NewQuote,
        }
    })

    export default class Cards extends Vue {
        public newQuoteOpen: boolean = false;

        get quotes() {
            return readQuotes(this.$store);
        }
        created() {
            dispatchLoadQuotes(this.$store); //read quotes from server on creation
        }
    }

</script>

<style scoped>

</style>