<template>
  <div id="inspire">
    <v-system-bar app color="#AED581">
      <v-spacer></v-spacer>

      <v-icon>mdi-square</v-icon>

      <v-icon>mdi-circle</v-icon>

      <v-icon>mdi-triangle</v-icon>
    </v-system-bar>

    <v-navigation-drawer color="#9CCC65" v-model="drawer" app>
      <v-sheet color="#7CB342" class="pa-4 justify-center">
        <v-avatar class="mb-4" color="grey darken-1" size="64">
          <img src="../../assets/logo.png"
        /></v-avatar>

        <div>intheForest-Project</div>
      </v-sheet>

      <v-divider></v-divider>

      <v-list>
        <v-list-item
          v-for="[icon, text, l] in links"
          :key="l"
          link
          v-on:click="tolink(l)"
        >
          <v-list-item-icon>
            <v-icon>{{ icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  data: () => ({
    cards: ["Today", "Yesterday"],
    drawer: null,
    links: [
      ["mdi-view-dashboard", "Dashboard", "/dashboard"],
      ["mdi-magnify", "Discover", "/discover"],
      ["mdi-clock", "check", "/check"],
      ["mdi-function", "function", "/function"],
      ["mdi-alarm", "alert", "/alert"],
      ["mdi-tune", "Management", "/5444"],
    ],
  }),
  methods: {
    tolink: function (l) {
      this.$router.push({ path: l });
    },
  },
};
</script>

<style></style>
