<template>
  <v-app>
    <toolbar></toolbar>
    <app-header></app-header>
    
    <v-main>
      <router-view></router-view>
    </v-main>
</v-app>

</template>

<script>
import AppHeader from '../components/common/AppHeader';
import Toolbar from '../components/common/Toolbar.vue';
export default {
    components:{
      Toolbar,
      AppHeader}
        
}
</script>

<style>

</style>