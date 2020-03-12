<template>
    
</template>

<script lang="ts">
    import { Component, Prop, Vue } from 'vue-property-decorator'
    import {readQuotes} from '@/store/main/getters.ts'
    import {commitSetQuote} from "@/store/main/mutations";
    import {IQuote} from "@/interfaces";


    @Component
    export default class Cards extends Vue {
        @Prop({required:true}) id!: number;

        get quote() {
            //find quote with specified id number
            return readQuotes(this.$store).find((quote) => quote.id === this.id);
        }

        set quote(newquote) {
            if (newquote) {
                commitSetQuote(this.$store, newquote);
            }
        }

        updateQuote() {

        }
    }
</script>

<style scoped>

</style>