<template>
  <div class="common-layout">
    <el-container>
      <el-header class="common-header flex-float">
        <div class="flex">
          <img class="logo" :src=getImgUrl() />
          <h1 class="title">{{ $t("main.webTitle") }}</h1>
        </div>
        <el-button mb-2 @click="changeLang">{{
          $t("main.switchLanguage")
        }}</el-button>
      </el-header>
      <el-container>
        <el-aside class="common-aside" width="200px">
          <el-menu
            active-text-color="#ffd04b"
            background-color="#545c64"
            class="el-menu-vertical-demo"
            default-active="2"
            text-color="#fff"
            :router="true"
          >
            <el-menu-item index="/introduction" class="el1">
              <el-icon><document /></el-icon>
              <span>{{$t("main.webIntroduction")}}</span>
            </el-menu-item>
            <el-sub-menu index="2">
              <template #title>
                <el-icon><location /></el-icon>
                <span>{{$t("main.petDogs")}}</span>
              </template>
              <el-menu-item-group>
                <el-menu-item class="el1" index="/bigPetDogs"
                  >{{$t("main.largeSized")}}</el-menu-item
                >
                <el-menu-item class="el1" index="/middlePetDogs"
                  >{{$t("main.smallAndMediumSized")}}</el-menu-item
                >
                <el-menu-item class="el1" index="/smallPetDogs"
                  >{{$t("main.newBreed")}}</el-menu-item
                >
              </el-menu-item-group>
            </el-sub-menu>
<!--            <el-menu-item class="el1" index="/news">-->
<!--              <el-icon><document /></el-icon>-->
<!--              <span>{{$t("main.petDogNews")}}</span>-->
<!--            </el-menu-item>-->
            <el-menu-item class="el1" index="/leaveMessage">
              <el-icon><setting /></el-icon>
              <span>{{$t("main.leaveMessage")}}</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>


<script>
import { useI18n } from "vue-i18n";
export default {
  name: "layout",
  setup() {
    const { locale } = useI18n();
    const changeLang = () => {
      if (locale.value === "zn") {
        locale.value = "en";
      } else {
        locale.value = "zn";
      }
    };
    const getImgUrl=()=>{
      const i = 0;
      return `src/assets/pic/${i}.jpg`
    };
    return { changeLang, getImgUrl };
  },
};
</script>

<style scoped>
.el-container {
  height: 100vh;
  overflow: hidden;
}
.common-header {
  height: 90px;
  /*background: rgb(39, 45, 53);*/
  background: #000;
}
.common-aside {
  background: rgb(48, 55, 65);
}
.logo {
  width: 80px;
  background: rgb(39, 45, 53);
}
.title {
  color: #fff;
}
.el1{
  height: 100px;
}
.el-main{
  background: #efefef;
}
</style>