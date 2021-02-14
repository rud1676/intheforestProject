<template>
  <v-app>
    <app-header></app-header>
    <v-main>
      <router-view></router-view>
    </v-main>
</v-app>

</template>

<script>
import AppHeader from '../components/common/AppHeader';
export default {
    components:{
        AppHeader,
    }
}
</script>

<style>

</style>