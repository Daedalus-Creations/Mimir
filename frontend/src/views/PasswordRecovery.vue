<template>
  <v-content>
    <v-container class="fill-height" fluid >
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="4">
          <v-card class="elevation-12">
            <v-app-bar dark color="primary">
              <v-app-bar-title>{{appName}} - Password Recovery</v-app-bar-title>
            </v-app-bar>
            <v-card-text>
              <p class="subheading">A password recovery email will be sent to the registered account</p>
              <v-form @keyup.enter="submit" v-model="valid" ref="form" @submit.prevent="" lazy-validation>
                <v-text-field @keyup.enter="submit" label="Username" type="text" prepend-icon="person" v-model="username" v-validate="'required'" data-vv-name="username" :error-messages="errors.collect('username')" required></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click="cancel">Cancel</v-btn>
              <v-btn @click.prevent="submit" :disabled="!valid">
                Recover Password
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {appName} from '@/env';
import {dispatchPasswordRecovery} from '@/store/main/actions';

@Component
export default class Login extends Vue {
  public valid = true;
  public username: string = '';
  public appName = appName;

  public cancel() {
    this.$router.back();
  }

  public submit() {
    dispatchPasswordRecovery(this.$store, {username: this.username});
  }
}
</script>

<style>
</style>
