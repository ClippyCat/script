# Sync loco repo on windows to vps.
# My simple salution to replace rcync.


cd C:\Users\Melody\Desktop\bs\programming\clippycat.ca
git push -u origin main
ssh debian@clippycat.ca "cd /var/www/html; git pull origin main --rebase"