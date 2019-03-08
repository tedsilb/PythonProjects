# This script uses Pyinstaller to build an app then deletes temp files
# Run this from a terminal, using the name of the file as the argument (no extension)
# Example: ./compile-mac.sh CoinFlip

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
mv -f dist/$fileName.app/ ../dist/$fileName/$fileName.app
mv -f dist/$fileName ../dist/$fileName/$fileName-mac.sh

# Delete temp files
echo Deleting temporary files...
echo
rm -rf __pycache__
rm -rf build
rm -rf dist
rm -rf $fileName.spec

echo Complete.
echo