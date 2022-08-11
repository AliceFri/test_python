cd /home/quanxipeng/backend
git fetch
echo '--------------- git pull ---------------'
git checkout dev
git pull
git checkout test
git pull
git checkout master
git pull
echo '--------------- git reset ---------------'
git checkout test_urgent
git reset --hard test
git checkout vehicle_v2
git reset --hard dev

# export
export port=7001 && python manage.py start-server


# ssh
#!/bin/bash
eval $(ssh-agent  -s)
ssh-add /root/.ssh/id_ed25519

cd "$BRANCH"/datahub
git pull
echo ddddddddddd- | docker login -u x docker.com --password-stdin
./deploy/deploy.py update
exit
