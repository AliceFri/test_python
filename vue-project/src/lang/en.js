
const enLargePetDogs = [
        "Golden haired",
        "Labrador",
        "Alaska",
        "Great pyrenees",
        "Bulldog",
        "Caucasian shepherd",
        "German shepherd",
        "Su shepherd dog",
        "Border collie",
        "Spotted dog"
      ]

const enMiduimuAndSmallPetDogs = [
      "Siberian husky",
      "Poodle",
      "Teddy dog",
      "Pomeranian",
      "Chihuahua",
      "Bichons frises",
      "Schnauzer",
      "Papillon dog",
      "Corgi",
      "Pekingese",
      "Dachshund"
    ]

const enNewBreedPetDogs = ["Pit bull", "Little deer dog", "Afghan hound"]

export default {
  main: {
    webTitle: "Pet Dog's House",
    switchLanguage: "switch language",
    webIntroduction: "introduction",
    petDogs: "pet dogs",
    petDogNews: "pet dogs news",
    largeSized: "large sized",
    smallAndMediumSized: "midium&small sized",
    newBreed: "new breed",
    leaveMessage: "leave message",

    largePetDogs:  ({named}) => enLargePetDogs[named('index')],
    miduimuAndSmallPetDogs:  ({named}) => enMiduimuAndSmallPetDogs[named('index')],
    newBreedPetDogs: ({named}) => enNewBreedPetDogs[named('index')],

    messageSearch: "message search",
    newMessage: "new message",
    deleteMessage: "Delete",
    name: "Name",
    date: "Date",
    message: "Message",
    operator: "Operator",
    email: "Email",

    title1: "Pet Dog Introduction",
    content1: "Hello, I am very glad that you can visit our pet website. At present, we are focusing on the information collection of pet dogs, and provide a platform for consultation and exchange for friends who want to raise pet dogs. I hope friends who like pet dogs can build this site together.",
    content2: "Dog is a kind of spiritual animal, which has been domesticated by human beings for thousands of years. It has a keen sense of smell, quick movement, empathy and loyalty to its master. Dogs of all shapes and sizes have long been favorite household pets in many countries.",
    content3: "For some lonely old people whose children are away and have no one to accompany them at home, they can feed pet dogs, because this can make your life more fulfilling and relieve the loneliness of life. Letting your child raise animals can cultivate his sense of responsibility and love for animals. When your pet dog has been in love with you for many years, you will treat it as a relative and be reluctant to bear it. Pet dogs can promote better communication and communication between people",

    title2: "The Web Introduction",
    content4: "This site contains an introduction to the types of pet dogs, with both pictures and texts. This site also supports Chinese and English language switching. If you have task ideas or suggestions, you can leave a message to us through the website.",
    content5: "The functions that will be developed successively in the plan of this site include: discussion function, pet dog trading function, etc.",
    content6: "The front end of this site is developed using Vue 3.0, a popular progressive framework for building user interfaces. The components of this site use ElementPlus, which is a set of Vue 3.0-based component libraries for developers, designers and product managers. It provides supporting design resources to help your website quickly prototype.",

    title3: "Slogan Of This Web",
    content7: "Animals are friends of human beings, please love them~!",
    content8: "A good playmate for children, a good helper for adults, and comfort for the elderly",
    content9: "Love animals, so that human beings are not alone",

    title4: "Other",
    content10: "If you also love pet dogs, then we are friends",

  }
};
