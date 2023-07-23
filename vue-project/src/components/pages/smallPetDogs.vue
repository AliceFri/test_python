<template>
  <el-row>
    <el-col v-for="(o, index) in 3" :key="o" :span="7" :offset="1">
      <el-card :body-style="{ padding: '0px' }">
        <img
          :src=getImgUrl(index)
          class="image"
        />
        <div style="padding: 10px">
          <span class="span1">{{ $t("main.newBreedPetDogs", {index: index}) }}</span>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>


<script>
export default {
  name: "smallPetDogs",
  setup() {
    const getImgUrl = (ind) => {
      return `src/assets/new/${ind}.webp`
    };
    return {
      getImgUrl,
    };
  },
};
</script>