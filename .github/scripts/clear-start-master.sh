projectPath="/var/www/github/telegram-bot-master"
cd $projectPath
docker build . --file Dockerfile --tag telegram-bot:master &&
docker-compose -f .github/docker-compose.github-master.yml up -d
if [ $? -eq 1 ]; then
	exit 1
fi
if [[ $(docker images -f dangling=true -q) ]]; then
  docker rmi $(docker images -f dangling=true -q)
fi

# path="/var/www/nginx"
# if [ -e $path ]; then
#   available="/available"
#   conf="/conf.d"
#   nginx="docker exec nginx nginx"
#   mkdir -p $path$available
#   mkdir -p $path$conf
#   cp etc/nginx/electrostation-gh-master.conf $path$available
#   ln -sf ..$available/electrostation-gh-master.conf $path$conf
#
#   $nginx -t
#   if [ $? -eq 0 ]; then
#     $nginx -s reload
#   fi
# fi

cd
