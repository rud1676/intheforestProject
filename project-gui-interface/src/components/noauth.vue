<template>
  <div>
    <p>죄송합니다!
    페이지를 볼 권한이 없습니다.
    자세한 내용은 관리자에게 문의하시기 바랍니다.
    </p>
    <v-btn text @click="goback()">
        뒤로가기
    </v-btn>
  </div>
</template>

<script>
export default {
    methods:{
        goback(){
            this.$router.go(-1);
        }
    }
}
</script>

<style>

</style>