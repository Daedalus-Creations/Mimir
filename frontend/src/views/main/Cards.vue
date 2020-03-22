<template>
  <div>
    <div class="section" v-if="quotes.length > 0">
      <Card v-for="quote in quotes" :key="quote.id" :id="quote.id"></Card>
    </div>
    <v-container class="fill-height" v-else>
      <v-row align="center" justify="center">
        <v-col>
          <div class="text-center">
            <v-icon>fas fa-quote-right</v-icon>
            <div class="subheading my-5">Add some quotes</div>
          </div>
        </v-col>
      </v-row>
    </v-container>

    <v-speed-dial
      v-model="fab"
      bottom
      right
      fixed
      direction="left"
      transition="slide-x-reverse-transition"
    >
      <template v-slot:activator>
        <v-btn v-model="fab" color="blue darken-2" dark fab>
          <v-icon v-if="!fab">fas fa-plus</v-icon>
          <v-icon v-else>fas fa-times</v-icon>
        </v-btn>
      </template>
      <v-btn
        v-for="quoteType in type"
        fab
        dark
        small
        :key="quoteType"
        :color="typeColor(quoteType)+' darken-2'"
        @click="newQuote(quoteType)"
      >
        <v-icon small>fas fa-{{typeIconName(quoteType)}}</v-icon>
      </v-btn>
    </v-speed-dial>
    <v-dialog v-model="newQuoteOpen" persistent max-width="960">
      <NewQuote @close="()=>{newQuoteOpen=false}" :key="newQuoteKey" :initType="newQuoteType"></NewQuote>
    </v-dialog>
  </div>
</template>

<script lang="ts">
import Card from "@/components/Card.vue";
import NewQuote from "@/components/NewQuote.vue";
import { Component, Vue } from "vue-property-decorator";
import { readQuotes } from "@/store/main/getters.ts";
import { dispatchLoadQuotes } from "@/store/main/actions";
import { typeIcon, type, typeColor } from "@/interfaces";

@Component({
  components: {
    NewQuote,
    Card
  }
})
export default class Cards extends Vue {
  public fab: boolean = false; // floating button flag
  public newQuoteOpen: boolean = false; // modal open
  public newQuoteType: type = type.UNCATEGORIZED;
  public newQuoteKey: number = 0;

  typeIconName(type): string | undefined {
    return typeIcon.get(type); // get icon name based on type enum
  }
  typeColor(type): string | undefined {
    return typeColor.get(type); // get color based on type
  }
  get type() {
    return type; // get type enum/object
  }

  get quotes() {
    return readQuotes(this.$store); // read quotes to display from store
  }

  newQuote(quoteType: type) {
    this.newQuoteKey++; // increment key to reset component
    this.newQuoteType = quoteType; // set new quote type
    this.newQuoteOpen = true; // set quote type
  }

  created() {
    dispatchLoadQuotes(this.$store); // read quotes from server on creation
  }
}
</script>

<style scoped>
</style>
