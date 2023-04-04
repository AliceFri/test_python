image -> contain -> pod(容器组) -> deployment(管理pod, 检查pod的健康状况)
将 deployment 暴露接口给公网， 会创建 service

kubectl get - 列出资源
kubectl describe - 显示有关资源的详细信息
kubectl logs - 打印 pod 和其中容器的日志
kubectl exec - 在 pod 中的容器上执行命令

    eg: kubectl describe pods 
        kubectl logs $POD_NAME
        kubectl exec -it $POD_NAME -- bash

kubectl proxy 

#### 创建 deployment
    kubectl create deployment hello-node --image=registry.k8s.io/echoserver:1.4

#### expose deployment
    kubectl expose deployment hello-node --type=LoadBalancer --port=8080
        --type=LoadBalancer 参数表明你希望将你的 Service 暴露到集群外部。
    kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080

    kubectl port-forward svc/frontend 8080:80


#### 查看信息
    kubectl version             # 查看版本
    kubectl get deployments/pods/evnets/services/rs     # 查看 Deployment/Pods/集群事件/Services/ReplicaSet
    kubectl get pod,svc,deployments -n kube-system
    kubectl get pods -o wide -a/--namespace
    kubectl config view                     # 查看 kubectl配置 ~/.kube/config

#### 清理

    kubectl delete service hello-node
    kubectl delete deployment hello-node

#### 缩放
    kubectl scale deployments/kubernetes-bootcamp --replicas=4

#### 滚动更新
    // 更新镜像
    kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2
    // 确定滚动更新
    kubectl rollout status deployments/kubernetes-bootcamp
    // 回滚滚动更新，回到之前版本
    kubectl rollout undo deployments/kubernetes-bootcamp

#### 配置
    
    kubectl create configmap sys-app-name --from-literal name=my-system
    kubectl create secret generic sys-app-credentials --from-literal username=bob --from-literal password=bobpwd

#### Deploying your chanages
    kubectl replace --force -f kubernetes.yaml

#### 安全

===============================
### 访问集群中的应用程序

#### 1. 部署和访问 k8s dashboard
    kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
    kubectl proxy # UI 只能 通过执行这条命令的机器进行访问。更多选项参见 kubectl proxy --help

#### 2. 访问集群
    1. 直接访问 REST API
        使用代理
            kubectl proxy --port=8000
        不使用代理 则需要kubectl apply等操作, 创建令牌，通过令牌访问
            ...
    2. 以编程方式访问API
        略
    


================================

## MINICUBE

    1. 打开看板 minikube dashboard
    2. 进入某个服务 minikube service hello-node       ### 牛

    3. 插件 minikube addons list
            minikube addons enable metrics-server
            minikube addons disable metrics-server
    
    4. minikube pause/unpause/stop/delete
    5. minikube ip

    # 多 node 
    6. minikube start --nodes 2 -p multinode-demo
       minikube service list -p multinode-demo 