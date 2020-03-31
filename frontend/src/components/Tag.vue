<template>
  <v-menu
    :close-on-content-click="false"
    bottom
    right
    transition="scale-transition"
    origin="top left"
  >
    <template v-slot:activator="{ on }">
      <v-chip v-on="on" small :color="tag.color">{{tag.title}}</v-chip>
    </template>
    <v-card width="300" dark color="white" :loading="isLoading">
      <v-card-title :style="{backgroundColor : tag.color+' !important'}" class="py-1 title"> 
        <v-text-field v-model="tag.title" dense placeholder="Title">
          <template v-slot:prepend>
            <v-btn small @click="tag.public = !tag.public" icon>
              <v-icon small v-if="tag.public">fas fa-unlock</v-icon>
              <v-icon small v-else>fas fa-lock</v-icon>
            </v-btn>
          </template>
          <template v-slot:append-outer>
            <v-btn small color="success" @click="updateTag">
              <v-icon small>fas fa-check</v-icon>
            </v-btn>
          </template>
        </v-text-field>
      </v-card-title>
      <v-card-text>
        <swatches shapes="circles" swatch-size="28" colors="text-basic" v-model="tag.color" inline></swatches>
      </v-card-text>
    </v-card>
  </v-menu>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import Swatches from "vue-swatches";
import { readTags } from "@/store/main/getters.ts";
import { commitAddNotification, commitSetTag } from "@/store/main/mutations";
import { dispatchUpdateTag } from "@/store/main/actions";
import { ITag } from "@/interfaces/index.ts"

@Component({
  components: {
    Swatches
  }
})
export default class Tag extends Vue {
    public isLoading : boolean = false;
  @Prop() id!: number;

  get tag() : ITag {
    return readTags(this.$store).find(tag => tag.id === this.id)!;
  }
  set tag(newTag) {
    commitSetTag(this.$store, newTag);
  }
  async updateTag(){
      try {
      this.isLoading = true; // set loading flag
      if (this.tag) {
        await dispatchUpdateTag(this.$store, this.tag);
      } // send request to server
      else {
        throw "quote undefined";
      }

      commitAddNotification(this.$store, {
        content: "Changes saved",
        color: "success"
      }); // send notification
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