const znLargePetDogs = [
        "金毛犬",
        "拉布拉多",
        "阿拉斯加",
        "大白熊",
        "鬥牛犬",
        "高加索犬",
        "德牧",
        "蘇牧",
        "邊牧",
        "斑點狗"
      ]

const znMiduimuAndSmallPetDogs = [
      "哈士奇",
      "貴賓犬",
      "泰迪犬",
      "博美",
      "吉娃娃",
      "比熊犬",
      "雪納瑞",
      "蝴蝶犬",
      "柯基犬",
      "京巴",
      "臘腸犬"
    ]

const znNewBreedPetDogs = ["比特犬", "小鹿犬", "阿富汗獵犬"]

export default {
  main: {
    webTitle: "寵物狗小屋",
    switchLanguage: "切換語言",
    webIntroduction: "網站簡介",
    petDogs: "寵物狗",
    petDogNews: "寵物狗新聞",
    largeSized: "大型",
    smallAndMediumSized: "中小型",
    newBreed: "新加種類",
    leaveMessage: "網站留言",

    largePetDogs:  ({named}) => znLargePetDogs[named('index')],
    miduimuAndSmallPetDogs:  ({named}) => znMiduimuAndSmallPetDogs[named('index')],
    newBreedPetDogs: ({named}) => znNewBreedPetDogs[named('index')],

    messageSearch: "内容查询",
    newMessage: "新建留言",
    deleteMessage: "删除",
    name: "姓名",
    date: "日期",
    message: "留言",
    operator: "操作",
    email: "邮箱",



    title1: "宠物狗介绍",
    content1: "你好，很开心你能够访问我们的宠物网站，目前我们正专注于宠物狗的信息收集，为想要养宠物狗的朋友提供一个咨询交流的平台。希望喜欢宠物狗的朋友能一起建设本站。",
    content2: "狗是一种有灵性的动物，已被人类驯化了几千年，其嗅觉灵敏，动作敏捷，善解人意，忠于主人。在很多国家，各种体形优美的狗早已成为最受喜爱的家庭宠物。",
    content3: "对于一些子女在外，家里没有人相伴的孤单老人，可以喂养宠物狗狗，因为这样可以使你的生活更加的充实，解除生活的孤寂感。让自己的小孩子饲养动物，可以培养他的责任感、和要对动物有爱心。当自家的宠物狗狗与你有了很多年感情之后，你会把它当做亲人看待，舍不得它，宠物狗狗可以促进人与人之间更好的交流与沟通。",

    title2: "本站介绍",
    content4: "本站包含宠物狗种类的介绍，图文并茂。本站也支持中英文语言切换。如果您有任务想法或建议，可以通过网站留言给我们。",
    content5: "本站计划中后陆续开发的功能有：讨论功能，宠物狗交易功能等",
    content6: "本站前端使用Vue 3.0进行开发， Vue是一套流行的用于构建用户界面的渐进式框架。本站组件使用的是ElementPlus, 这是一套为开发者、设计师和产品经理准备的基于Vue 3.0 的组件库，提供了配套设计资源，帮助你的网站快速成型。",

    title3: "本站口号",
    content7: "动物是人类的朋友,请爱护它吧～!",
    content8: "儿童的好玩伴, 成年人的好帮手, 老年人的安慰",
    content9: "爱护动物, 让人类不孤单",

    title4: "其他",
    content10: "如果你也爱宠物狗，那我们就是朋友",



  }
};
