cd C:\Users\Melody\Desktop\bs\programming\myrepo\clippycat.ca
git push -u origin main
ssh arch@clippycat.ca "cd clippycat.ca; git pull origin main --rebase; zola build -o ~/public -f"