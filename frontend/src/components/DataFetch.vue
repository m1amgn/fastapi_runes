<template>
  <div class="bg-white p-4 rounded shadow-sm">
    <h3
      style="margin: 1%;">
      Расчет Индивидуального Рунического Кода
    </h3>
  </div>
  <div class="container mt-5">
    <form @submit.prevent="submitForm" class="bg-light p-4 rounded shadow-sm">
      <div class="mb-3">
        <label for="firstName" class="form-label">
          Имя
          <input
            type="text"
            id="firstName"
            v-model="firstName"
            @input="checkCyrillic('firstName')"
            class="form-control"
            required />
        </label>
      </div>
      <div class="mb-3">
        <label for="middleName" class="form-label">
          Отчество
          <input
            type="text"
            id="middleName"
            v-model="middleName"
            @input="checkCyrillic('middleName')"
            class="form-control"
            required />
        </label>
      </div>
      <div class="mb-3">
        <label for="lastName" class="form-label">
          Фамилия
          <input
            type="text"
            id="lastName"
            v-model="lastName"
            @input="checkCyrillic('lastName')"
            class="form-control"
            required />
        </label>
      </div>
      <div class="mb-3">
        <label for="dob" class="form-label">
          Дата рождения
          <input type="date" id="dob" v-model="dob" class="form-control" required />
        </label>
      </div>
      <button type="submit" class="btn btn-primary" :disabled="submitButtonDisabled">
        Отправить
      </button>
    </form>
    <div v-if="error" class="alert alert-danger mt-3" role="alert">
      {{ error }}
    </div>
    <div v-if="apiData" ref="scrollTarget" class="mt-4 bg-white p-4 rounded shadow-sm">
      <div class="images-row">
        <div v-for="(value, key) in apiData" :key="key" class="mt-4 bg-white p-4 rounded shadow-sm">
          <img :src="getImagePath(value)" :alt="value" class="img-fluid mt-3" />
        </div>
      </div>
      <div style="text-align: left; padding: 5%;" class="mt-4 bg-white p-4 rounded shadow-sm">
        <div class="description">
          <p>{{ fateDescription }}</p>
          <p><strong>{{ fateRune }}</strong></p>
        </div>
        <div class="description">
          <p>{{ personalityDescription }}</p>
          <p><strong>{{ personalityRune }}</strong></p>
        </div>
        <div>
          <p>{{ goldDescription }}</p>
          <p><strong>{{ goldRune }}</strong></p>
        </div>
      </div>
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
      apiData: null,
      jsonData: null,
      error: '',
      fateRune: '',
      personalityRune: '',
      goldRune: '',
      fateDescription: '',
      personalityDescription: '',
      goldDescription: '',
    };
  },
  computed: {
    submitButtonDisabled() {
      return !!this.error;
    },
  },
  methods: {
    async submitForm() {
      const payload = this.getPayload();
      try {
        const apiResponse = await axios.post('http://127.0.0.1:8000/api_runes', payload);
        const jsonResponse = await axios.get('/assets/runes_description.json');
        this.apiData = apiResponse.data;
        this.jsonData = jsonResponse.data;
        this.fateRune = this.jsonData.faterune[this.apiData.faterune];
        this.personalityRune = this.jsonData.personalityrune[this.apiData.personalityrune];
        this.goldRune = this.jsonData.goldrune[this.apiData.goldrune];
        this.fateDescription = this.jsonData.faterune.description;
        this.personalityDescription = this.jsonData.personalityrune.description;
        this.goldDescription = this.jsonData.goldrune.description;
        this.scrollToApiData();
        this.resetForm();
      } catch (error) {
        console.error('Error sending the data to the API or getting JSON:', error);
      }
    },
    getPayload() {
      const [year, month, day] = this.dob.split('-');
      const monthWithoutLeadingZero = month.startsWith('0') ? month.substring(1) : month;
      return {
        birthday: day,
        birthmonth: monthWithoutLeadingZero,
        birthyear: year,
        firstname: this.firstName,
        fathername: this.middleName,
        secondname: this.lastName,
      };
    },
    getImagePath(imageName) {
      return `/assets/${imageName}.jpg`;
    },
    checkCyrillic(fieldName) {
      const fieldValue = this[fieldName];
      const cyrillicRegex = /^[а-яА-ЯЁё]+$/;
      if (!cyrillicRegex.test(fieldValue)) {
        this.error = `Please enter only Cyrillic characters for ${fieldName}`;
      } else {
        this.error = '';
      }
    },
    scrollToApiData() {
      this.$nextTick(() => {
        const element = this.$refs.scrollTarget;
        if (element) {
          element.scrollIntoView({ behavior: 'smooth' });
        }
      });
    },
    resetForm() {
      this.firstName = '';
      this.middleName = '';
      this.lastName = '';
      this.dob = '';
      this.error = '';
    },
  },
};
</script>

<style scoped>
.images-row {
  display: flex;
  flex-wrap: wrap;
  gap: 1em;
}

.images-row > div {
  flex: 1 1 auto;
  min-width: 100px;
}

.images-row img {
  max-width: 200px;
  max-height: 200px;
  object-fit: cover;
}

.description {
  padding-bottom: 3%;
}
</style>
