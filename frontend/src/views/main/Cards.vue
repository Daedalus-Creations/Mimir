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

    <v-speed-dial
                v-model="fab"
                bottom right fixed direction="left"               
                transition="slide-x-reverse-transition"
        >
            <template slot="activator">
                <v-btn
                        v-model="fab"
                        color="blue darken-2"
                        dark
                        fab
                >
                    <v-icon v-if="!fab">fas fa-plus</v-icon>
                    <v-icon v-else>fas fa-times</v-icon>
                </v-btn>
            </template>
            <v-btn  v-for="quoteType in type"
                    fab
                    dark
                    small
                    :key="quoteType"
                    :color="typeColor(quoteType)+' darken-2'"
                    @click="newQuoteOpen=true"
            >
                <v-icon>fas fa-{{typeIconName(quoteType)}}</v-icon>
            </v-btn>
        </v-speed-dial>
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
    import {typeIcon, type, typeColor} from "@/interfaces";

    @Component({
        components: {
            NewQuote,
            Card
        }
    })

    export default class Cards extends Vue {
        public fab : boolean = false;
        public newQuoteOpen : boolean = false;

        typeIconName(type) : string | undefined {
            return typeIcon.get(type); //get icon name based on type enum
        }
        typeColor(type) : string | undefined {
            return typeColor.get(type);
        }
        get type() {
            return type; //get type enum/object
        }

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