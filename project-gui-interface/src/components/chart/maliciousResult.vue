<template>
  <v-alert
    v-if="alert"
    :value="alert"
    border="right"
    colored-border
    type="error"
    elevation="2"
  >
    <v-row align="center" no-gutters>
      <v-col class="grow">
        <v-progress-circular
          :rotate="360"
          :size="100"
          :width="15"
          :value="value"
          color="teal"
        >
          {{ positives }} / {{ total }}
        </v-progress-circular>
        검사한 사이트마다 의심되는 결과가 나온 비율
      </v-col>

      <v-btn color="info" outlined @click="close"> Close </v-btn>
    </v-row>
    <div class="my-5">검사 값: {{ url }}</div>
    <v-row no-gutters>
      <v-col>
        <v-card>
          <v-simple-table dense>
            <template v-slot:default>
              <thead>
                <tr>
                  <th>ScansCompany</th>
                  <th>Result</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in check" :key="item.scans">
                  <td>{{ item.scans }}</td>
                  <td>
                    <v-icon
                      v-if="item.clean === 'clean site' || item.clean === null"
                      color="green"
                      >mdi-check-circle-outline</v-icon
                    >
                    <v-icon v-else>mdi-help</v-icon>
                    {{ item.clean }}
                  </td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-card>
      </v-col>

      <v-col>
        <v-card>
          <v-simple-table dense>
            <template v-slot:default>
              <thead>
                <tr>
                  <th>ScansCompany</th>
                  <th>Result</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in check2" :key="item.scans">
                  <td>{{ item.scans }}</td>
                  <td>
                    <v-icon
                      v-if="item.clean === 'clean site' || item.clean === null"
                      color="green"
                      >mdi-check-circle-outline</v-icon
                    >
                    <v-icon v-else>mdi-help</v-icon>
                    {{ item.clean }}
                  </td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-card>
      </v-col>
    </v-row>
  </v-alert>
</template>
<script>
export default {
  props: {
    alert: {
      type: Boolean,
      default: false,
    },
    value: {
      type: Number,
      default: 100,
    },
    positives: {
      type: Number,
      default: 0,
    },
    total: {
      type: Number,
      default: 100,
    },
    url: {
      type: String,
      default: "",
    },
    check: {
      type: Array,
      default: () => [],
    },
    check2: {
      type: Array,
      default: () => [],
    },
  },
  methods: {
    close() {
      this.$emit("close");
    },
  },
};
</script>