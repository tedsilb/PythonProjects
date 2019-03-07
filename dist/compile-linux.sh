# This script uses Pyinstaller to build a script then deletes temp files

# Get file from argument, set up command
echo Setting up...
echo
fileName=$1
rm -rf $fileName
cd ../projects
toRun="pyinstaller -F $fileName.py"

# Run command
echo Starting compilation...
echo
$toRun

# Move exe outside to dist folder
echo Compilation complete.
echo
echo Moving app to main dist folder.
echo
mkdir ../dist/$fileName
mv -f dist/$fileName ../dist/$fileName/$fileName-linux.sh

# Delete temp files
echo Deleting temporary files...
echo
rm -rf __pycache__
rm -rf build
rm -rf dist
rm -rf $fileName.spec

echo Complete.
echo