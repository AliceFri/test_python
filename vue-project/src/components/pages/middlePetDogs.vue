<template>
  <el-row>
    <el-col v-for="(o, index) in 11" :key="o" :span="7" :offset="1">
      <el-card :body-style="{ padding: '0px' }">
        <img
          :src=getImgUrl(index)
          class="image"
        />
        <div style="padding: 10px">
          <span class="span1">{{ $t("main.miduimuAndSmallPetDogs", {index: index}) }}</span>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: "middlePetDogs",
      setup() {
    const getImgUrl = (ind) => {
      return `src/assets/miduleSmall/${ind}.webp`
    };
    return {
      getImgUrl,
    };
  },
};
</script>