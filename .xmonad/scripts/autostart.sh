#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

(sleep 2; run $HOME/.config/polybar/launch.sh) &

#cursor active at boot
xsetroot -cursor_name left_ptr &

#starting utility applications at boot time
run variety &
run nm-applet &
run xfce4-power-manager &
#run volumeicon &
numlockx on &
picom --config $HOME/.xmonad/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
#wpg -rs 'LA2.jpeg' 'LA2.jpeg'

#starting user applications at boot time
#nitrogen --restore &

