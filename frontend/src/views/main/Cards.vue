<template>
    <div class="section"><!--v-if="quotes.length > 0"-->
    <Card
            v-for="quote in quotes"
            :key="quote.id"
            :id="quote.id"
    ></Card>
        <b-button
                type="is-primary"
                size="is-large"
                rounded
                style="bottom:10vh;right:10vh;position:fixed;z-index: 9999"
                @click="cardModal()"
        >
            <b-icon icon="plus"></b-icon>
        </b-button>
        <!--<b-modal :active.sync="newQuoteOpen"
                 has-modal-card
                 trap-focus
                 aria-role="dialog"
                 aria-modal>
            <NewQuote></NewQuote>
        </b-modal>-->
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
        cardModal() {
            this.$buefy.modal.open({
                parent: this,
                component: NewQuote,
                hasModalCard: true,
                trapFocus: true,
                width: 1920,
            })
        }
        created() {
            dispatchLoadQuotes(this.$store);
        }
    }

</script>

<style scoped>

</style>