<template>
  <v-card :loading="isLoading" :color="quote.color" width="100%" dark>
    <v-card-title :class="'title white--text '+headerColor">

      <v-icon left>fas fa-{{typeIconName(quote.type)}}</v-icon>

      <span v-if="!editable">{{quote.title}}</span>
      <v-text-field dense v-model="quote.title" placeholder="Title" v-else />

      <v-spacer></v-spacer>

      <v-btn small v-if="editable" @click="togglePublic" icon>
        <v-icon small v-if="quote.public">fas fa-unlock</v-icon>
        <v-icon small v-else>fas fa-lock</v-icon>
      </v-btn>

      <v-btn small v-if="editable" text class="mr-2">Custom Color</v-btn>
      <v-btn v-if="editable" color="error" small class="mr-4" @click.stop="confirmDelete=true">Delete</v-btn>
      <v-btn v-if="editable" color="success" small @click="updateQuote">Save</v-btn>
      <v-btn icon v-if="!editable" @click="editable=true" small class="my-0"> <v-icon>edit</v-icon></v-btn>

    </v-card-title>
    <v-card-text class="px-9 py-0">

      <span v-if="!editable">{{quote.text}}</span>
      <v-textarea
        dense
        rows="1"
        class="my=0"
        v-model="quote.text"
        :auto-grow="true"
        placeholder="Quote"
        v-else
      />

    </v-card-text>
    <v-card-actions class="pb-0">

      <v-list-item>
        <v-list-item-avatar small>
          <v-icon small>fas fa-user</v-icon>
        </v-list-item-avatar>
        <v-list-item-content class="subheading">
          <span v-if="!editable">{{quote.author}}</span>
          <v-text-field dense class="my-0" v-model="quote.author" placeholder="Author" v-else />
        </v-list-item-content>
      </v-list-item>

      <v-spacer></v-spacer>

      <v-btn icon><v-icon small>fas fa-sticky-note</v-icon></v-btn>

    </v-card-actions>

    <v-dialog
      v-model="confirmDelete"
      width="500"
    >

      <v-card color="error" dark>
        <v-card-title
          class="title white--text error darken-1"
          primary-title
        >
          Delete Quote
        </v-card-title>

        <v-card-text>
          Are you sure you want to delete this quote?
          </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            text
            @click="deleteQuote"
          >
            Delete
          </v-btn>
          <v-btn
            text
            @click="confirmDelete = false"
          >
            Cancel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import { readQuotes } from "@/store/main/getters.ts";
import { commitAddNotification, commitSetQuote } from "@/store/main/mutations";
import { IQuote, type, typeIcon, typeColor } from "@/interfaces";
import { dispatchDeleteQuote, dispatchLoadQuotes, dispatchUpdateQuote } from "@/store/main/actions";
const tinycolor = require("tinycolor2");

@Component({
  components: {
  }
})
export default class Card extends Vue {
  public editable = false;
  public isLoading = false;
  public confirmDelete = false;

  @Prop({ required: true }) id!: number;

  get quote(): IQuote {
    // find quote with specified id number
    return readQuotes(this.$store).find(quote => quote.id === this.id);
  }
  set quote(newquote: IQuote) {
    if (newquote) {
      commitSetQuote(this.$store, newquote);
    }
  }
  typeIconName(type): string | undefined {
    return typeIcon.get(type); // get icon name based on type enum
  }
  get type() {
    return type; // get type enum/object
  }
  get headerColor(){
        if(Array.from(typeColor.values()).includes(this.quote.color)) // if quote color is not a custom color
            return this.quote.color+' darken-2'; // use vuetify presets
        else {
            let color = tinycolor(this.quote.color);
            return color.darken(10).toString(); // compute with tinycolor
        }
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
  async updateQuote() {
    try {
      this.isLoading = true; // set loading flag
      if (this.quote) {
        await dispatchUpdateQuote(this.$store, this.quote);
      } // send request to server
      else {
        throw "quote undefined";
      }

      commitAddNotification(this.$store, {
        content: "Changes saved",
        color: "success"
      }); // send notification
      this.editable = false;
    } catch (error) {
      commitAddNotification(this.$store, {
        content: "Something went wrong",
        color: "error"
      }); // send notification
    } finally {
      this.isLoading = false; // reset loading flag
    }
  }
  async deleteQuote() {
    try {
      this.confirmDelete = false; // reset modal flag
      this.isLoading = true; // set loading flag
      if (this.quote) {
        await dispatchDeleteQuote(this.$store, this.quote.id);
      } // make api call
      else {
        throw "quote undefined";
      }
      commitAddNotification(this.$store, {
        content: "Quote Deleted",
        color: "success"
      }); // send notification
      await dispatchLoadQuotes(this.$store); // refresh
    } catch (error) {
      commitAddNotification(this.$store, {
        content: "Something went wrong",
        color: "error"
      }); // send notification
    } finally {
      this.isLoading = false; // reset loading flag
    }
  }
}
</script>

<style scoped>
/deep/ .v-card__text * {
  font-size: inherit;
  font-weight: inherit;
  line-height: inherit;
  letter-spacing: inherit;
  color: inherit;
}
/deep/ .v-messages {
  min-height: 0px;
  height: 0px;
}
/deep/ .v-text-field__details {
  min-height: 0px;
  height: 0px;
}
</style>
