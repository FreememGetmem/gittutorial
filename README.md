Complete MLOps Bootcamp With 10+ End To End ML Projects

Create a repo by visiting your git account.

Generate ssh key:

ssh-keygen -t rsa -C "your_email@example.com"
Copy the contents of the file ~/.ssh/id_rsa.pub to your SSH keys in your GitHub account settings. Test SSH key:

ssh -T git@github.com
clone the repo:
git clone git://github.com/username/your-repository
Now cd to your git clone folder and do:

git remote set-url origin git@github.com:username/your-repository.git
Now try editing a file (try the README) and then do:

git add -A
git commit -am "my update msg"
git push -u origin master
Update: new git version seems to recommend not to have any file while new repo is created. Hence make aa blank repo.
