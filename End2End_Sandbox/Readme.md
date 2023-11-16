## End2End Sand-box

-> Git is used for maitaining Code version

-> It is a version control tool

-> You have to configure your containing folder with Git

---

Initialize Code
```
git init
```

Stage the modified code files and other modifications. ('.' adds all the files, you can specify each file which you want to stage)
```
git add .
```

After the staging the files, you can commit the files for the particular version of the files. Add a comment on what changes yuo have done in them.
```
git commit -m "Comment the changes in this version"
```

After Commiting the changes to the particular version, Publish the changes in the branch you want (you can push multiple commits in single push)
[branch can be 'main' by default]
```
git push origin branch_name
```