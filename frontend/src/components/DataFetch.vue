<template>
  <div>
    <p>{{ msg }}</p>
  </div>
  <div class="container mt-5">
    <form @submit.prevent="submitForm" class="bg-light p-4 rounded shadow-sm">
      <div class="mb-3">
        <label for="firstName" class="form-label">
          <input type="text" id="firstName" v-model="firstName" class="form-control" required />
          First Name:
        </label>
      </div>
      <div class="mb-3">
        <label for="middleName" class="form-label">
          <input type="text" id="middleName" v-model="middleName" class="form-control" />
          Middle Name:
        </label>
      </div>
      <div class="mb-3">
        <label for="lastName" class="form-label">
          <input type="text" id="lastName" v-model="lastName" class="form-control" required />
          Last Name:
        </label>
      </div>
      <div class="mb-3">
        <label for="dob" class="form-label">
          <input type="date" id="dob" v-model="dob" class="form-control" required />
          Date of Birth:
        </label>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>

    <div v-if="apiResponse" class="mt-4 bg-light p-4 rounded shadow-sm">
      <h3>API Response:</h3>
      <p v-for="(value, key) in apiResponse" :key="key"><strong>{{ key }}:</strong> {{ value }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      firstName: '',
      middleName: '',
      lastName: '',
      dob: '',
      apiResponse: null,
    };
  },
  methods: {
    async submitForm() {
      const [year, month, day] = this.dob.split('-');
      const monthWithoutLeadingZero = month.startsWith('0') ? month.substring(1) : month;

      const payload = {
        birthday: day,
        birthmonth: monthWithoutLeadingZero,
        birthyear: year,
        firstname: this.firstName,
        fathername: this.middleName,
        secondname: this.lastName,

      };

      console.log('Sending payload:', payload);

      try {
        const response = await axios.post('http://127.0.0.1:8000/api_runes/', payload);
        this.apiResponse = response.data;
      } catch (error) {
        console.error('Error sending the data to the API:', error);
      }
    },
    getMessage() {
      axios.get('http://127.0.0.1:8000/api_runes/')
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

<style scoped>
/* Add any custom styles here */
</style>
