<template>
    <div class="notification" :style="colorStyle">
        <b-loading :active.sync="isLoading" :is-full-page="false" :can-cancel="true"></b-loading>
        <div class="level is-mobile">
            <div class="level-left">
                <div class="level-item">
                    <h1 class="title is-5">
                        <b-icon icon="book"></b-icon>
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
                    <b-dropdown aria-role="list">
                        <b-button inverted rounded outlined size="is-small" type="is-info" slot="trigger">Type</b-button>
                        <b-dropdown-item value="uncategorized" aria-role="listitem">
                            <div class="media">
                                <div class="media-left">
                                    <b-icon icon="quote-right"></b-icon>
                                </div>
                                <div class="media-content">
                                    <h3>Uncategorized</h3>
                                </div>
                            </div>
                        </b-dropdown-item>
                        <b-dropdown-item value="book" aria-role="listitem">
                            <div class="media">
                                <div class="media-left">
                                    <b-icon icon="book"></b-icon>
                                </div>
                                <div class="media-content">
                                    <h3>Book</h3>
                                </div>
                            </div>
                        </b-dropdown-item>
                        <b-dropdown-item value="movie" aria-role="listitem">
                            <div class="media">
                                <div class="media-left">
                                    <b-icon icon="film"></b-icon>
                                </div>
                                <div class="media-content">
                                    <h3>Film</h3>
                                </div>
                            </div>
                        </b-dropdown-item>
                        <b-dropdown-item value="poem" aria-role="listitem">
                            <div class="media">
                                <div class="media-left">
                                    <b-icon icon="feather"></b-icon>
                                </div>
                                <div class="media-content">
                                    <h3>Poem</h3>
                                </div>
                            </div>
                        </b-dropdown-item>
                        <b-dropdown-item value="speech" aria-role="listitem">
                            <div class="media">
                                <div class="media-left">
                                    <b-icon icon="comment"></b-icon>
                                </div>
                                <div class="media-content">
                                    <h3>Speech</h3>
                                </div>
                            </div>
                        </b-dropdown-item>
                        <b-dropdown-item value="lyrics" aria-role="listitem">
                            <div class="media">
                                <div class="media-left">
                                    <b-icon icon="music"></b-icon>
                                </div>
                                <div class="media-content">
                                    <h3>Lyrics</h3>
                                </div>
                            </div>
                        </b-dropdown-item>
                        <b-dropdown-item value="other" aria-role="listitem">
                            <div class="media">
                                <div class="media-left">
                                    <b-icon icon="ellipsis-h"></b-icon>
                                </div>
                                <div class="media-content">
                                    <h3>Other</h3>
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
                                @click="submit"
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
    import { Component, Vue } from 'vue-property-decorator'
    import {IQuoteCreate, defaultQuote} from "@/interfaces";

    var tinycolor = require("tinycolor2");

    export default class NewQuote extends Vue {
        public quote : IQuoteCreate = defaultQuote;

        get colorStyle() {
            const background = tinycolor(this.quote.color); //get background color
            const textColor = background.isLight() ? '#000' : "#fff"; //invert to get text color
            const outline = background.isLight() ? tinycolor(this.quote.color)
                .darken()
                .toHexString() : tinycolor(this.quote.color)
                .brighten()
                .toHexString(); //lighten

            const accent = textColor;
            return {
                background: background.toHexString(),
                color: textColor,
                "--placeholder-color": outline,
                "--accent-color": accent,
                "--button-color": textColor,
            };
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
        color: var(--placeholder-color); /*#c8e7ff;*/
        opacity: 70%;
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