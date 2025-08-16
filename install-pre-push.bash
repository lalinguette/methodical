# automatically run unit tests when pushing
GIT_DIR=$(git rev-parse --git-dir)
ln -s -f ../../pre-push.bash $GIT_DIR/hooks/pre-push
