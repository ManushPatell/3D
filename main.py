'''READ PLEASE:'''

'''This is a Monorepo, single repo where all files can be included
dont worry too much about the files and stuff, just git clone 
the link on github so a local version of this repo can stay on your computer
'''

'''
When you want to make a change, and commit and merge it to the main branch:

Create and checkout a new "branch" which represents your changes
git checkout -b sreyo/button
Tell git which files you changed and would like to "commit" to the repo
git add scripts/button/main.py
You could repeat this for other files if you had other changes
Create a commit which saves your work to the branch
git commit -m "Add a message about what you did"
Currently, your branch only exists on your computer. To push it to github, use
git push -u
The -u option is only needed on the first time you push a new branch. If GitHub alread "knows" about the branch, you can just run git push '''

print("hello")