# boto-mon


## Install notes

```bash
pip install --user virtualenvwrapper
sudo apt-get install build-essential libc6-dev \
  libncurses5-dev libncursesw5-dev libreadline6-dev \
  libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev \
  libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev -q -y
mkdir Python && cd Python
./configure
make -j4
sudo make install
mkvirtualenv --python=`which python3.5`  boto-mon
```

### Remote SSH volume to Pi

Mount remote project files,...
```bash
sshfs -oauto_cache,reconnect,allow_other,defer_permissions,negative_vncache,noappledouble,volname=BotoProjects boto:/home/pi/Projects /tmp/ssh
umount /tmp/ssh
```

Map connection to localhost so that direct connection to interpreter is possible.
```bash
ssh -L 9999:localhost:9999 a1
```
