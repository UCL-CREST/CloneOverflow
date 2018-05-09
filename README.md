# CloneOverflow
This is a repository of a study of online code clones on Stack Overflow. It contains the paper (LaTEX), related documents, and the tools used for performing the experiment.

## Structure of the repo.
* cloverflow-tse -- the paper submitted to TSE (working copy)
* cloneoverflow-fse17 -- the paper submitted to FSE'17
* cloverflow_technical_report -- the technical report regarding Stack Overflow's answerers and users survey
* UCL_Ethical_Waiver -- the document submitted to UCL for ethical waiver
* tools -- contains the tools used to process Stack Overflow snippets and the clones
* scripts -- contains scripts used to perform the experiment.

## Checking of Stack Overflow outdated code snippets in GitHub projects 
* 1) Get a list of GitHub projects filtered by no. of stars:
```bash
python src/github.py github-crawler.log 3 3
```
* 2) Create a folder to store the filtered GH projects and copy them to the folder:
```bash
mkdir github_3
./copy_github_projects.sh github-3-3.txt ../siamese_study/github github_3/
```
* 3) Run SourcererCC
```bash
```
