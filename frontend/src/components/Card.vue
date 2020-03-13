<template>
    
</template>

<script lang="ts">
    import { Component, Prop, Vue } from 'vue-property-decorator'
    import {readQuotes} from '@/store/main/getters.ts'
    import {commitSetQuote} from "@/store/main/mutations";
    import {IQuote, type} from "@/interfaces";


    @Component({
        components: {}
    })
    export default class Card extends Vue {
        public isOpen=true;
        public editable=false;
        public isLoading=false;
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

        /*async updateQuote() {
            this.isLoading =true;
            await dispatchUpdateQuote(this.$store);
            this.isLoading=false;

        }*/
    }
</script>

<style scoped>

</style>