<template>
    <div class="notification" :style="colorStyle" >
        <b-loading :active.sync="isLoading" :is-full-page="false" :can-cancel="true"></b-loading>
        <div class="level is-mobile">
            <div class="level-left">
                <div class="level-item">
                    <h1 class="title is-5">
                        <b-icon :icon="typeIconName(quote.type)"></b-icon>
                    </h1>
                </div>
                <div class="level-item">
                    <input
                            class="nostyle title is-5 editable"
                            placeholder="Book Title"
                            v-model="quote.title"
                    />
                </div>
            </div>
            <div class="level-right">
                <div class="level-item">
                    <b-dropdown aria-role="list" v-model="quote.type">
                        <b-button inverted rounded outlined size="is-small" type="is-info" slot="trigger">Type</b-button>
                        <b-dropdown-item v-for="quoteType in type" :value="quoteType" aria-role="listitem">
                            <div class="media">
                                <div class="media-left">
                                    <b-icon :icon="typeIconName(quoteType)"></b-icon>
                                </div>
                                <div class="media-content">
                                    <h3>{{quoteType}}</h3>
                                </div>
                            </div>
                        </b-dropdown-item>
                    </b-dropdown>
                </div>
                <div class="level-item">
                    <swatches
                            v-model="quote.color"
                            shapes="circles"
                            show-fallback
                            popover-to="left"
                    >
                        <b-button slot="trigger" type="is-info" size="is-small" rounded inverted outlined>color</b-button>
                    </swatches>
                </div>
                <div class="level-item">
                        <b-button
                                type="is-success"
                                size="is-small"
                                rounded
                                @click="submit()"
                        >
                            <b-icon icon="check"></b-icon>
                        </b-button>
                    </div>
                </div>
            </div>
        <div class="container">
      <textarea
              placeholder="Quote"
              class=" nostyle autosize subtitle is-6 editable"
              spellcheck="false"
              v-model="quote.text"
              ></textarea>
        </div>
            <!--<div class="level">
                <div class="level-left">
                    <div class="level-item">
                        <vue-tags-input
                                class="nostyle"
                                :class="editable ? 'editable' : ''"
                                v-model="tagInput"
                                :tags="quote.tags"
                                :disabled="!editable"
                                @tags-changed="newTags => tags = newTags"
                        />
                    </div>
                </div>
            </div>-->
            <div class="level is-mobile">
                <div class="level-left">
                    <div class="level-item">
                        <h1 class="title is-6">
                            <b-icon icon="user"></b-icon>
                        </h1>
                    </div>
                    <div class="level-item">
                        <input class="nostyle title is-6 editable"
                                placeholder="Author"
                                v-model="quote.author"></input>
                    </div>
                </div>

            </div>

    </div>
</template>

<script lang="ts">
    import {Component, Emit, Vue} from 'vue-property-decorator';
    import {IQuoteCreate, defaultQuote, typeIcon, type} from "@/interfaces";
    import {dispatchCreateQuote, dispatchLoadQuotes} from "@/store/main/actions";
    import Swatches from "vue-swatches";
    import "vue-swatches/dist/vue-swatches.min.css";

    var tinycolor = require("tinycolor2");

    @Component({
        components: {
            Swatches
        }
    })
    export default class NewQuote extends Vue {
        public quote : IQuoteCreate = Object.assign({}, defaultQuote); // copy defaults to initialize
        public isLoading: boolean = false; // Loading flag

        typeIconName(type) : string | undefined {
            return typeIcon.get(type); //get icon name based on type enum
        }
        get type() {
            return type; //get type enum/object
        }

        get colorStyle() {
            const background = tinycolor(this.quote.color); //get background color
            const textColor = background.isLight() ? '#000' : "#fff"; //invert to get text color
            const outline = background.isLight() ? tinycolor(this.quote.color)
                .darken()
                .toHexString() : tinycolor(this.quote.color)
                .brighten()
                .toHexString(); //lighten or darken background color to get outline/placeholder color

            const accent = textColor;
            return {
                background: background.toHexString(),
                color: textColor,
                "--placeholder-color": outline,
                "--accent-color": accent,
                "--button-color": textColor,
            };
        }

        async submit() {
            try {
                this.isLoading = true; //set loading flag
                await dispatchCreateQuote(this.$store, this.quote); // push quote to server
                this.$buefy.toast.open({
                    message: 'Quote Created',
                    type: 'is-success'
                })
            }
            catch(error){
                this.$buefy.toast.open({
                    message: 'Something went wrong',
                    type: 'is-danger'
                })
            }
            finally {
                this.isLoading = false; //reset loading flag
                this.quote = Object.assign({}, defaultQuote); //reset content
                this.$emit('close'); //close modal
                await dispatchLoadQuotes(this.$store); //refresh
            }
        }
    }
</script>

<style scoped>
    :root {
        --placeholder-color: #fff;
        --accent-color: #000;
        --button-color: #fff;
    }
    /deep/ ::placeholder {
        color: var(--placeholder-color);
    }
    /*
    /deep/ button{
      border-color: var(--button-color) !important;
      color: var(--button-color) ;
      background: var(--button-color) !important;
    }*/
    /deep/ .ti-input {
        border: None;
    }
    /deep/ .ti-new-tag-input {
        background: transparent;
        color: var(--accent-color);
    }
    .nostyle {
        width: 100%;
        outline: None;
        border: None;
        overflow: hidden;
        background-color: transparent;
        -webkit-box-shadow: none;
        -moz-box-shadow: none;
        box-shadow: none;
        resize: none;
    }
    .editable {
        box-shadow: 0 -2px inset var(--placeholder-color); /*#1e1e1f;*/
    }
    .editable:focus {
        box-shadow: 0 -2px inset var(--accent-color);
    }
    .editable:focus-within {
        box-shadow: 0 -2px inset var(--accent-color);
    }
</style>