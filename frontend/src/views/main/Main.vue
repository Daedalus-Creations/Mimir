<template>
  <div>
    <!--<v-navigation-drawer
      v-model="showDrawer"
      fixed
      width="25%"
      :clipped="$vuetify.breakpoint.lgAndUp"
      app
    >
      <v-list subheader dense>
        <v-subheader>Main menu</v-subheader>
        <v-list-item to="/main/dashboard">
          <v-list-item-action>
            <v-icon>web</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item to="/main/profile/view">
          <v-list-item-action>
            <v-icon>person</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Profile</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item to="/main/profile/edit">
          <v-list-item-action>
            <v-icon>edit</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Edit Profile</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item to="/main/profile/password">
          <v-list-item-action>
            <v-icon>vpn_key</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Change Password</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list subheader v-show="hasAdminAccess" dense>
        <v-subheader>Admin</v-subheader>
        <v-list-item to="/main/admin/users/all">
          <v-list-item-action>
            <v-icon>group</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Manage Users</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item to="/main/admin/users/create">
          <v-list-item-action>
            <v-icon>person_add</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Create User</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>-->
<v-card class="overflow-hidden">
    <v-navigation-drawer v-model="showDrawer" color="blue darken-3" temporary fixed dark>
      <v-list dense nav class="py-0">
        <v-list-item two-line>
          <v-list-item-avatar>
            <img src="https://randomuser.me/api/portraits/men/81.jpg" />
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>Application</v-list-item-title>
            <v-list-item-subtitle>Subtext</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-divider></v-divider>

        <v-list-item link to="/main/dashboard">
          <v-list-item-action>
            <v-icon>web</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to="/main/profile/view">
          <v-list-item-action>
            <v-icon>person</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Profile</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to="/main/profile/edit">
          <v-list-item-action>
            <v-icon>edit</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Edit Profile</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to="/main/profile/password">
          <v-list-item-action>
            <v-icon>vpn_key</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Change Password</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-list subheader v-show="hasAdminAccess" dense>
        <v-divider></v-divider>
        <v-subheader>Admin</v-subheader>
        <v-list-item link to="/main/admin/users/all">
          <v-list-item-action>
            <v-icon>group</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Manage Users</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to="/main/admin/users/create">
          <v-list-item-action>
            <v-icon>person_add</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Create User</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
</v-card>
    <v-app-bar :clipped-left="$vuetify.breakpoint.lgAndUp" app color="blue darken-3" dark>
      <v-app-bar-nav-icon @click.stop="switchShowDrawer" />
      <v-toolbar-title style="width: 300px" class="ml-0 pl-4">
        <span class="hidden-sm-and-down">{{appName}}</span>
      </v-toolbar-title>
      <v-autocomplete
        flat
        solo-inverted
        :items="items"
        :loading="isLoading"
        :search-input.sync="search"
        hide-details
        hide-no-data
        prepend-inner-icon="search"
        append-icon=""
        label="Search quotes"
        class="hidden-sm-and-down"
        hide-selected
        item-text="Description"
        item-value="API"
      />
      <v-spacer />
      <v-btn @click="logout">Log Out</v-btn>

      <template v-slot:extension>
        <v-tabs align-with-title>
          <v-tab to="/main/dashboard">Your Quotes</v-tab>
          <v-tab to="#">Vocab List</v-tab>
          <v-tab to='#'>Browse</v-tab>
          <v-tab to='/main/profile'>Settings</v-tab>
        </v-tabs>
        <v-spacer></v-spacer>
        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-btn text v-on="on">Sort</v-btn>
          </template>
          <v-list>
            <v-list-item @click="sortBy('author')"><v-list-item-title>By Author</v-list-item-title></v-list-item>
            <v-list-item @click="sortBy('title')"><v-list-item-title>By Title</v-list-item-title></v-list-item>
            <v-list-item @click="sortBy('type')"><v-list-item-title>By Type</v-list-item-title></v-list-item>
            <v-list-item @click="sortBy('color')"><v-list-item-title>By Color</v-list-item-title></v-list-item>
          </v-list>
        </v-menu>
        <v-btn icon>
          <v-icon>fas fa-filter</v-icon>
        </v-btn>
        <v-spacer></v-spacer>
      </template>
    </v-app-bar>
    <v-content>
      <router-view></router-view>
    </v-content>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

import { appName } from "@/env";
import {
  readDashboardMiniDrawer,
  readDashboardShowDrawer,
  readHasAdminAccess,
  readQuotes
} from "@/store/main/getters";
import {
  commitSetDashboardShowDrawer,
  commitSetDashboardMiniDrawer,
  commitSetQuotes,
} from "@/store/main/mutations";
import { dispatchUserLogOut } from "@/store/main/actions";
import {IQuote} from "@/interfaces/index.ts"

const routeGuardMain = async (to, from, next) => {
  if (to.path === "/main") {
    next("/main/dashboard");
  } else {
    next();
  }
};

@Component
export default class Main extends Vue {
  public appName = appName;

  get quotes() : IQuote[] {
    return readQuotes(this.$store); // read quotes to display from store
  }
  set quotes(newQuotes : IQuote[]) {
    commitSetQuotes(this.$store, newQuotes); // read quotes to display from store
  }

  public sortBy(attr : string): void{
    this.quotes = this.quotes.sort((a,b) => a[attr].localeCompare(b[attr])) //sort list of quotes by selected attribute
  }
  public beforeRouteEnter(to, from, next) {
    routeGuardMain(to, from, next);
  }

  public beforeRouteUpdate(to, from, next) {
    routeGuardMain(to, from, next);
  }

  get miniDrawer() {
    return readDashboardMiniDrawer(this.$store);
  }

  get showDrawer() {
    return readDashboardShowDrawer(this.$store);
  }

  set showDrawer(value) {
    commitSetDashboardShowDrawer(this.$store, value);
  }

  public switchShowDrawer() {
    commitSetDashboardShowDrawer(
      this.$store,
      !readDashboardShowDrawer(this.$store)
    );
  }

  public switchMiniDrawer() {
    commitSetDashboardMiniDrawer(
      this.$store,
      !readDashboardMiniDrawer(this.$store)
    );
  }

  public get hasAdminAccess() {
    return readHasAdminAccess(this.$store);
  }

  public async logout() {
    await dispatchUserLogOut(this.$store);
  }
}
</script>
