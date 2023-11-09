<template>
  <el-row>
    <el-col :span="7" :offset="1">
      <el-card :body-style="{ padding: '0px' }">
        <img
          src="../../assets/big/0.webp"
          class="image"
        />
        <div style="padding: 10px">
          <span class="span1">{{ $t("main.largePetDogs", {index: 0}) }}</span>
        </div>
      </el-card>
    </el-col>
    <el-col :span="7" :offset="1">
      <el-card :body-style="{ padding: '0px' }">
        <img
          src="../../assets/big/1.webp"
          class="image"
        />
        <div style="padding: 10px">
          <span class="span1">{{ $t("main.largePetDogs", {index: 1}) }}</span>
        </div>
      </el-card>
    </el-col>
    <el-col :span="7" :offset="1">
      <el-card :body-style="{ padding: '0px' }">
        <img
          src="../../assets/big/2.webp"
          class="image"
        />
        <div style="padding: 10px">
          <span class="span1">{{ $t("main.largePetDogs", {index: 2}) }}</span>
        </div>
      </el-card>
    </el-col>
    <el-col :span="7" :offset="1">
      <el-card :body-style="{ padding: '0px' }">
        <img
          src="../../assets/big/3.webp"
          class="image"
        />
        <div style="padding: 10px">
          <span class="span1">{{ $t("main.largePetDogs", {index: 3}) }}</span>
        </div>
      </el-card>
    </el-col>
    <el-col :span="7" :offset="1">
      <el-card :body-style="{ padding: '0px' }">
        <img
          src="../../assets/big/4.webp"
          class="image"
        />
        <div style="padding: 10px">
          <span class="span1">{{ $t("main.largePetDogs", {index: 4}) }}</span>
        </div>
      </el-card>
    </el-col>
    <el-col :span="7" :offset="1">
      <el-card :body-style="{ padding: '0px' }">
        <img
          src="../../assets/big/5.webp"
          class="image"
        />
        <div style="padding: 10px">
          <span class="span1">{{ $t("main.largePetDogs", {index: 5}) }}</span>
        </div>
      </el-card>
    </el-col>
    <el-col :span="7" :offset="1">
      <el-card :body-style="{ padding: '0px' }">
        <img
          src="../../assets/big/6.webp"
          class="image"
        />
        <div style="padding: 10px">
          <span class="span1">{{ $t("main.largePetDogs", {index: 6}) }}</span>
        </div>
      </el-card>
    </el-col>
    <el-col :span="7" :offset="1">
      <el-card :body-style="{ padding: '0px' }">
        <img
          src="../../assets/big/7.webp"
          class="image"
        />
        <div style="padding: 10px">
          <span class="span1">{{ $t("main.largePetDogs", {index: 7}) }}</span>
        </div>
      </el-card>
    </el-col>
    <el-col :span="7" :offset="1">
      <el-card :body-style="{ padding: '0px' }">
        <img
          src="../../assets/big/8.webp"
          class="image"
        />
        <div style="padding: 10px">
          <span class="span1">{{ $t("main.largePetDogs", {index: 8}) }}</span>
        </div>
      </el-card>
    </el-col>
    <el-col :span="7" :offset="1">
      <el-card :body-style="{ padding: '0px' }">
        <img
          src="../../assets/big/9.webp"
          class="image"
        />
        <div style="padding: 10px">
          <span class="span1">{{ $t("main.largePetDogs", {index: 9}) }}</span>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
import {reactive, toRefs} from "vue";

export default {
  name: "bigPetDogs",
    setup() {
    const getImgUrl = (ind) => {
      return `src/assets/big/${ind}.webp`
    };
    return {
      getImgUrl,
    };
  },
}
</script>