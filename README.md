# github_demo

# Useful commands
repo=git@github.com:ehsan4u/github_demo.git
git clone ${repo}

# Status - https://linuxhint.com/how-do-i-check-get-logs/
git status
git log
git log -p -2



# Branch
git branch
git branch -a
git branch -r
git checkout ${branch_name}

# add all files

git add -A # git add .

# Commit
message="Initializing"
git -a -m "Initializing"

# Pushing to remote 
git push