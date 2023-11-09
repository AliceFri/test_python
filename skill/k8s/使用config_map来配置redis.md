#### 1. 创建一个配置模块为空的ConfigMap

    cat <<EOF >./example-redis-config.yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
        name: example-redis-config
    data:
        redis-config: ""
    EOF

#### 2. 应用上面创建的 ConfigMap 以及 Redis Pod 清单
    kubectl apply -f example-redis-config.yaml
    kubectl apply -f https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/config/redis-pod.yaml

#### 3. 检查创建的对象
    kubectl get pod/redis configmap/example-redis-config 

    // 查看 configmap
    kubectl describe configmap/example-redis-config

#### 4. kubectl exec 进入 pod, 进行redis-cli工具检查当前配置
    kubectl exec -it redis -- redis-cli
    CONFIG GET maxmemory
    CONFIG GET maxmemory-policy

#### 5. 向 1创建的ConfigMap添加配置， 并应用
    apiVersion: v1
    kind: ConfigMap
    metadata:
        name: example-redis-config
    data:
        redis-config: |
            maxmemory 2mb
            maxmemory-policy allkeys-lru  

    kubectl apply -f example-redis-config.yaml

#### 6. 重新创建 redis pod
    kubectl replace --force -f https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/config/redis-pod.yaml

#### 7. 重新执行 4, 验证configmap是否生效

#### 8. 删除资源
    kubectl delete pod/redis configmap/example-redis-config