#### 1. 查看各节点kubelet版本(需大于v1.4.0)
    kubectl get nodes -o=jsonpath=$'{range .items[*]}{@.metadata.name}: {@.status.nodeInfo.kubeletVersion}\n{end}'

#### 2. 检查AppArmor模块是否启动
    cat /sys/module/apparmor/parameters/enabled
    Y

#### 3. 配置文件已加载
    
    ssh gke-test-default-pool-239f5d02-gyn2 "sudo cat /sys/kernel/security/apparmor/profiles | sort"



=====================


#### 4. 保护pod
    
    向pod的metadata 添加注解
    container.apparmor.security.beta.kubernetes.io/<container_name>: <profile_ref>

...