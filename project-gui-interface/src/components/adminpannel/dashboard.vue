<template>
  <router-view></router-view>
</template>

<script>
export default {
  data: () => ({
    overlay: false,
    zIndex: 0,
    users: [],
  }),
};
</script>
