<template xmlns="http://www.w3.org/1999/html">
<div>
  <div class="page_content">
      <div class="flex">
    <div class="input_box">
    <el-input
      v-model="keyWord"
      placeholder="message search"
      class="input-with-select"
    >
      <template #append>
        <el-button @click="searchList">
          <el-icon><Search /></el-icon>
        </el-button>
      </template>
    </el-input>
      </div>
    <el-button type="primary" @click="leaveMessage">{{ $t("main.newMessage") }}</el-button>
      </div>
          <el-table :data="showMessages" style="width: 100%">
    <el-table-column prop="id" label="ID" width="100" />
    <el-table-column prop="name" :label="$t('main.name')" width="180" />
            <el-table-column prop="date" :label="$t('main.date')" width="180"/>
            <el-table-column prop="email" :label="$t('main.email')" width="180"/>
    <el-table-column prop="message" :label="$t('main.message')" />
            <el-table-column  :label="$t('main.operator')">
              <template #default="scope">
                <el-button type="warning" @click="deleteRow(scope.row)">
                 {{ $t("main.deleteMessage") }}
                </el-button>
              </template>
            </el-table-column>
  </el-table>
  </div>

  <el-dialog v-model="dialogFormVisible" :title="$t('main.newMessage')">
    <el-form ref="messageForm" :model="formData" :rules="rules">
      <el-form-item :label="$t('main.name')" prop="name">
        <el-input v-model="formData.name" />
      </el-form-item>
      <el-form-item :label="$t('main.email')" prop="email">
        <el-input v-model="formData.email" />
      </el-form-item>
      <el-form-item :label="$t('main.message')" prop="message">
        <el-input v-model="formData.message" />
      </el-form-item>
    </el-form>
    <template #footer>
      <div class="flex">
        <el-button @click="cancelForm">取消</el-button>
        <el-button type="primary" @click="submitForm(messageForm)">提交</el-button>
      </div>
    </template>
  </el-dialog>
</div>
</template>


<script>
import {Search} from "@element-plus/icons-vue";
import {toRefs, reactive, ref} from "vue";
export default {
  name: "leaveMessage",
  components: {Search},
  setup() {
    const data = reactive({
      keyWord: "",
      idFlag: 3,
      messages: [
        {id: 1, name: 'bob', email: 'bob@xxx.edu', message: 'have a good time!', date: '2023-05-01'},
        {id: 2, name: 'alice', email: 'alice@xxx.edu', message: 'have a good time!', date: '2023-05-01'},
        {id: 3, name: 'linda', email: 'alice@xxx.edu', message: 'have a good time!', date: '2023-05-01'},
      ],
      showMessages: [
        {id: 1, name: 'bob', email: 'bob@xxx.edu', message: 'have a good time!', date: '2023-05-01'},
        {id: 2, name: 'alice', email: 'alice@xxx.edu', message: 'have a good time!', date: '2023-05-01'},
        {id: 3, name: 'linda', email: 'alice@xxx.edu', message: 'have a good time!', date: '2023-05-01'},
      ],
      dialogFormVisible: false,
      formData: {
        name: '',
        email: '',
        message: ''
      },
      rules: {
        name: [
          {
            required: true,
            trigger: "blur",
          }
        ],
        email: [
          {
            required: true,
            trigger: "blur",
          }
        ],
         message: [
          {
            required: true,
            trigger: "blur",
          }
        ]
      },
    })
    const leaveMessage=()=>{
      data.formData = {
        name: '',
        email: '',
        message: ''
      };
      data.dialogFormVisible = true;
    };
    const searchList=()=>{
      data.showMessages = data.messages.filter(
          (item) => item.message.includes(data.keyWord)
      )
    };
    const submitForm=(formEl)=>{
      if (!formEl) return;
      formEl.validate((valid, fields) => {
      if (valid) {
        data.idFlag += 1;
        data.messages.push({
          id: data.idFlag,
          name: data.formData.name,
          email: data.formData.email,
          message: data.formData.message,
          date: new Date().toISOString().split('T')[0]
        });
        data.showMessages = data.messages;
        data.keyWord = '';
        data.dialogFormVisible = false;
      } else {
        console.log('error submit!', fields)
      }
  })
    }
    const cancelForm=()=>{

      data.dialogFormVisible = false;
    }
    const deleteRow=row=>{
        data.messages = data.messages.filter(
            item=>item.id!==row.id
        );
        data.showMessages = data.messages;
        data.keyWord = '';
    }
    const messageForm=ref();
    return {
      ...toRefs(data),
      searchList,
      leaveMessage,
      messageForm,
      submitForm,
      cancelForm,
      deleteRow,
    }
  }
};
</script>

<style scoped>
.input_box{
  width: 300px;
  margin-right: 15px;
}

</style>