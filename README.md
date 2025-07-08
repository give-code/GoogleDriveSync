set up the google drive API and put your auth json file into the mirrored directory
install fswatch if not already installed
edit PARENT_FOLDER_ID in GoogleDrive.py to have the folder you want to mirror to
to run put the syncFileGoogleDrive.plist in /Users/"username"/Library/LaunchAgents
run "launchctl load ~/Library/LaunchAgents/syncFileGoogleDrive.plist"
any newly added or removed files will now be mirrored in your google drive
