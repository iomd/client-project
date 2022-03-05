# script used to install libraries into system

###
echo "what type of project"
read project_type
###

###
#if audio project
  sh client/install_audio-project.sh
#if docs project
  sh client/install_docs-project.sh
#if image project
  sh client/install_image-project.sh
#if video project
  sh client/install_video-project.sh
#if web project
  sh client/install_web-project.sh

###