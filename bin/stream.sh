#!/usr/bin/env bash
set -e
# READ ~> https://www.raspberrypi.org/documentation/raspbian/applications/camera.md

# Works ~>
# raspivid -o - -t 0 -vf -hf -w 1280 -h 720 -fps 25 -b 4000000 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554}' :demux=h264 :h264-fps=25

#  -co 10 -sa 20 -br 53

#raspivid -o - -t 0 -w 1920 -h 1080 -fps 30 -vf -hf | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554}' :demux=h264
# --awb
# raspivid -a "boto" -o - -t 0 -hf -w 640 -h 360 -fps 25 | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:31337}' :demux=h264

# cvlc v4l2:///dev/video0:width=640:height=480:fps=15 --v4l2-vflip 1 --v4l2-hflip 1 --sout="#transcode{vcodec=mp4v}:std{access=http,mux=ts,dst=:8090}"

#cvlc --no-audio v4l2:///dev/video0 \
#  --v4l2-width 1920 \
#  --v4l2-height 1080 \
#  --v4l2-chroma MJPG \
#  --v4l2-hflip 1 \
#  --v4l2-vflip 1 \
#  --sout '#standard{access=http{mime=multipart/x-mixed-replace;boundary=--7b3cc56e5f51db803f790dad720ed50a},mux=mpjpeg,dst=:8554/}' \
#  -I dummy

# codec --v4l2-chroma MJPG \
# --v4l2-chroma h264 \

# :width=640:height=480:fps=15
#cvlc --no-audio v4l2:///dev/video0 \
#--v4l2-width 480 --v4l2-height 240 --v4l2-chroma h264 \
#  --sout="#standard{access=http,mux=ts,dst=:8554}"
# mux=ts
# #transcode{vcodec=mp4v,acodec=none}:

# Broke PI! :D
#cvlc v4l2:///dev/video0 --v4l2-width 360 --v4l2-height 240 --v4l2-chroma h264 \
#  --sout '#standard{access=http,mux=ts,dst=:8554}'

#raspivid -o - -t 0 -vf -hf -w 640 -h 480 -fps 25 -b 4000000 | \
#  cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554}' :demux=h264
#:h264-fps=25

#raspivid -t 0 -w 640 -h 480 -fps 25 -b 1200000 -p 0,0,640,480 -o - | \
#  gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=0.0.0.0 port=8554

IP=192.168.64.104
PORT=5000

#raspivid -t 0 -h 720 -w 1080 -fps 48 -b 2000000 -o - | \
#  gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink port=$PORT

#raspivid -t 0 -w 1280 -h 720 -fps 25 -hf -b 2500000 -o - | \
#gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 \
## ! udpsink host=$IP port=$PORT

#raspivid -t 0 -w 1280 -h 720 -fps 25 -hf -b 2500000 -o - | \
# gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 \
# ! gdppay ! tcpserversink host=192.168.1.7 port=5000

raspivid -t 0 -w 1920 -h 1080 -fps 48 -vf -hf -b 2500000 -o - | \
gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 \
! udpsink host=$IP port=$PORT


# Client
# gst-launch-1.0 -v udpsrc port=5000 ! "application/x-rtp, payload=96" \
# ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false