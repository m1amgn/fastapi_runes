<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

const dataUrl = 'http://127.0.0.1:8000/api_runes/';

export default {
  name: 'DataFetch',
  data() {
    return {
      msg: 'Not yet',
    };
  },
  methods: {
    getMessage() {
      // debugger;
      axios.get(dataUrl)
        .then((response) => {
          console.log(response);
          this.msg = response.data;
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
