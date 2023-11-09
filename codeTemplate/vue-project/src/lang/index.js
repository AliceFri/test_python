import { createI18n } from "vue-i18n";
import en from "./en";
import zn from "./zn";

const i18n = createI18n({
  legacy: false,
  locale: "zn",
  messages: {
    zn: zn,
    en: en
  }
});

export default i18n;
