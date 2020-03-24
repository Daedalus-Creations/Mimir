<template>
  <v-container>
    <v-row>
      <v-col cols="3">
        <v-navigation-drawer floating permanent>
          <v-list dense rounded>
            <v-subheader>Options</v-subheader>
            <v-list-item link>
              <v-list-item-icon>
                <v-icon>fas fa-quote-right</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>Quotes</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item link>
              <v-list-item-icon>
                <v-icon>fas fa-book</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>Titles</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item link>
              <v-list-item-icon>
                <v-icon>fas fa-user</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>Authors</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item link>
              <v-list-item-icon>
                <v-icon>fas fa-hashtag</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>Types</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item link>
              <v-list-item-icon>
                <v-icon>fas fa-tag</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>Tags</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-navigation-drawer>
      </v-col>

      <v-col cols="9" v-if="quotes.length>0">
        <v-row v-for="quote in quotes" :key="quote.id" class="mb-5">
          <Card :id="quote.id"></Card>
        </v-row>
      </v-col>
      <v-col cols="9" v-else>
        <v-row align="center" justify="center">
          <v-col>
            <div class="text-center">
              <v-icon>fas fa-quote-right</v-icon>
              <div class="subheading my-5">Add some quotes</div>
            </div>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
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
          :color="typeColor(quoteType)+' darken-1'"
          @click="createQuote(quoteType)"
        >
          <v-icon small>fas fa-{{typeIconName(quoteType)}}</v-icon>
        </v-btn>
      </v-speed-dial>
      <v-dialog v-model="newQuoteOpen" persistent max-width="960">
        <NewQuote></NewQuote>
      </v-dialog>
  </v-container>
</template>

<script lang="ts">
import Card from "@/components/Card.vue";
import NewQuote from "@/components/NewQuote.vue";
import { Component, Vue } from "vue-property-decorator";
import { readQuotes, readNewQuoteOpen, readNewQuote } from "@/store/main/getters.ts";
import { dispatchLoadQuotes } from "@/store/main/actions";
import { commitSetNewQuoteOpen, commitSetNewQuote, commitClearNewQuote } from "@/store/main/mutations"
import { typeIcon, type, typeColor, IQuoteCreate } from "@/interfaces";

@Component({
  components: {
    NewQuote,
    Card
  }
})
export default class Cards extends Vue {
  public fab: boolean = false; // floating button flag
  
  get newQuoteOpen(): boolean {
      return readNewQuoteOpen(this.$store);
  }
  set newQuoteOpen(payload: boolean) {
      commitSetNewQuoteOpen(this.$store, payload);
  }
  get newQuote(): IQuoteCreate {
      return readNewQuote(this.$store);
  }
  set newQuote(payload: IQuoteCreate) {
      commitSetNewQuote(this.$store, payload);
  }

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

  createQuote(quoteType: type) {
    commitClearNewQuote(this.$store); // reset defaults
    this.newQuote.type = quoteType; // set type
    this.newQuoteOpen = true; // open modal
  }

  created() {
    dispatchLoadQuotes(this.$store); // read quotes from server on creation
  }
}
</script>

<style scoped>
</style>
