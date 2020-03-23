<template>
  <v-card :loading="isLoading" :color="quote.color" dark>
    <template v-slot:progress>
      <v-progress-linear absolute color="green lighten-3" height="4" indeterminate></v-progress-linear>
    </template>
    <v-card-title :class="'headline '+quote.color+' darken-2'">
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn text v-on="on">
            <v-icon left>fas fa-{{typeIconName(quote.type)}}</v-icon>
            {{quote.type}}
          </v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="quoteType in type"
            :key="quoteType"
            @click="()=>{quote.type = quoteType; quote.color = typeColor(quoteType);}"
          >
            <v-list-item-action>
              <v-icon :color="typeColor(quoteType)+' darken-2'">fas fa-{{typeIconName(quoteType)}}</v-icon>
            </v-list-item-action>
            <v-list-item-content>{{quoteType}}</v-list-item-content>
          </v-list-item>
        </v-list>
      </v-menu>
      <v-spacer></v-spacer>

      <v-btn @click="togglePublic" icon>
        <v-icon v-if="quote.public">fas fa-unlock</v-icon>
        <v-icon v-else>fas fa-lock</v-icon>
      </v-btn>
      <v-btn text>Custom Color</v-btn>
    </v-card-title>
    <v-card-text class="pb-0">
      <v-form>
        <v-container class="pb-0">
          <v-row>
            <v-col >
              <v-text-field v-model="quote.title" label="Title"></v-text-field>
            </v-col>
            <v-col>
              <v-text-field v-model="quote.author" label="Author"></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-textarea v-model="quote.text" label="Quote" rows="2" filled :auto-grow="true" />
            </v-col>
          </v-row>
          <v-row>
            <v-col class="py-0">
              <v-textarea label="Tags" filled rounded dense rows="1" :auto-grow="true" />
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-btn text @click="submit">Create</v-btn>
      <v-btn text @click="close">Cancel</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import { Component, Emit, Vue, Prop, Watch } from "vue-property-decorator";
import {
  IQuoteCreate,
  defaultQuote,
  typeIcon,
  type,
  typeColor
} from "@/interfaces";
import { dispatchCreateQuote, dispatchLoadQuotes } from "@/store/main/actions";
import Swatches from "vue-swatches";
import "vue-swatches/dist/vue-swatches.min.css";
import { commitAddNotification, commitSetNewQuote, commitSetNewQuoteOpen } from "@/store/main/mutations";
import { readNewQuote, readNewQuoteOpen } from "../store/main/getters";

@Component({
  components: {
    Swatches
  }
})
export default class NewQuote extends Vue {
  public isLoading: boolean = false; // Loading flag

  get quote() : IQuoteCreate {
    return readNewQuote(this.$store);
  }
  set quote(payload: IQuoteCreate) {
    commitSetNewQuote(this.$store, payload);
  }
  get newQuoteOpen(): boolean {
    return readNewQuoteOpen(this.$store);
  }
  set newQuoteOpen(payload: boolean){
    commitSetNewQuoteOpen(this.$store, payload);
  }

  get type(): type {
    return type; // get type enum/object
  }
  get customColor(): boolean {
    return Array.from(typeColor.values()).includes(this.quote.color); // check whether a custom color is set
  }
  typeColor(type): string | undefined {
    return typeColor.get(type); // get color name based on type
  }
  typeIconName(type): string | undefined {
    return typeIcon.get(type); // get icon name based on type enum
  }
  togglePublic(): void {
    this.quote.public = !this.quote.public; // toggle public setting
    if (this.quote.public) {
      commitAddNotification(this.$store, {
        content: "Warning: This quote will be publicly viewable",
        color: "warning"
      });
    } // if public, issue warning
    else {
      commitAddNotification(this.$store, {
        content: "This quote will be private",
        color: "warning"
      });
    } // if public, issue warning
  }

  async submit() {
    try {
      this.isLoading = true; // set loading flag
      await dispatchCreateQuote(this.$store, this.quote); // push quote to server
      commitAddNotification(this.$store, {
        content: "Quote Created",
        color: "success"
      }); // send notification
    } catch (error) {
      commitAddNotification(this.$store, {
        content: "Something went wrong",
        color: "error"
      }); // send notification
    } finally {
      this.isLoading = false; // reset loading flag
      this.close(); // close modal
      await dispatchLoadQuotes(this.$store); // refresh
    }
  }
  close(): void {
    this.newQuoteOpen = false;
  }

}
</script>
