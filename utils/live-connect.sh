#!/usr/bin/env bash
set -ex

# umount /tmp/ssh

#sshfs -oauto_cache,reconnect,allow_other,defer_permissions,negative_vncache,noappledouble,volname=BotoProjects \
#  boto-work:/home/pi/Projects /tmp/ssh

ssh -v -2 \
  -o ExitOnForwardFailure=yes \
  -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/dev/null \
  -L 9999:localhost:9999 a1 cat
