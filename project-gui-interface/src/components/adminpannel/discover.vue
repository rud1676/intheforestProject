<template>
  <v-container class="py-2 px-1" fluid style="height: 100vh">
    <iframe
      width="100%"
      height="100%"
      src="http://34.64.102.4:5601/goto/f1188597213aee64853a67af4f97f62c"
      @load="load"
      v-if="isLoading"
    ></iframe>
    <loading v-else></loading>
    <v-btn></v-btn>
  </v-container>
</template>

<script>
export default{
  data(){
    return{
      isLoading: false,
    }
  },
  method: { 
    load: function(){
      this.isLoading = false;
    }
  }

}
</script>
