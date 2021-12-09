#!/bin/bash

if [ ! "$1" ]; then
  echo "This script requires either amd64 of arm64 as an argument"
	exit 1
elif [ "$1" = "amd64" ]; then
	PLATFORM="$1"
	DIR_NAME="skynet-blockchain-linux-x64"
else
	PLATFORM="$1"
	DIR_NAME="skynet-blockchain-linux-arm64"
fi

pip install setuptools_scm
# The environment variable SKYNET_INSTALLER_VERSION needs to be defined
# If the env variable NOTARIZE and the username and password variables are
# set, this will attempt to Notarize the signed DMG
SKYNET_INSTALLER_VERSION=$(python installer-version.py)

if [ ! "$SKYNET_INSTALLER_VERSION" ]; then
	echo "WARNING: No environment variable SKYNET_INSTALLER_VERSION set. Using 0.0.0."
	SKYNET_INSTALLER_VERSION="0.0.0"
fi
echo "Skynet Installer Version is: $SKYNET_INSTALLER_VERSION"

echo "Installing npm and electron packagers"
npm install electron-packager -g
npm install electron-installer-debian -g
npm install lerna -g

echo "Create dist/"
rm -rf dist
mkdir dist

echo "Create executables with pyinstaller"
pip install pyinstaller==4.5
SPEC_FILE=$(python -c 'import skynet; print(skynet.PYINSTALLER_SPEC_PATH)')
pyinstaller --log-level=INFO "$SPEC_FILE"
LAST_EXIT_CODE=$?
if [ "$LAST_EXIT_CODE" -ne 0 ]; then
	echo >&2 "pyinstaller failed!"
	exit $LAST_EXIT_CODE
fi

cp -r dist/daemon ../skynet-blockchain-gui/packages/gui
cd .. || exit
cd skynet-blockchain-gui || exit

echo "npm build"
lerna clean -y
npm install
# Audit fix does not currently work with Lerna. See https://github.com/lerna/lerna/issues/1663
# npm audit fix
npm run build
LAST_EXIT_CODE=$?
if [ "$LAST_EXIT_CODE" -ne 0 ]; then
	echo >&2 "npm run build failed!"
	exit $LAST_EXIT_CODE
fi

# Change to the gui package
cd packages/gui || exit

# sets the version for skynet-blockchain in package.json
cp package.json package.json.orig
jq --arg VER "$SKYNET_INSTALLER_VERSION" '.version=$VER' package.json > temp.json && mv temp.json package.json

electron-packager . skynet-blockchain --asar.unpack="**/daemon/**" --platform=linux \
--icon=src/assets/img/Skynet.icns --overwrite --app-bundle-id=net.skynet.blockchain \
--appVersion=$SKYNET_INSTALLER_VERSION --executable-name=skynet-blockchain
LAST_EXIT_CODE=$?

# reset the package.json to the original
mv package.json.orig package.json

if [ "$LAST_EXIT_CODE" -ne 0 ]; then
	echo >&2 "electron-packager failed!"
	exit $LAST_EXIT_CODE
fi

mv $DIR_NAME ../../../build_scripts/dist/
cd ../../../build_scripts || exit

echo "Create skynet-$SKYNET_INSTALLER_VERSION.deb"
rm -rf final_installer
mkdir final_installer
electron-installer-debian --src dist/$DIR_NAME/ --dest final_installer/ \
--arch "$PLATFORM" --options.version $SKYNET_INSTALLER_VERSION --options.bin skynet-blockchain --options.name skynet-blockchain
LAST_EXIT_CODE=$?
if [ "$LAST_EXIT_CODE" -ne 0 ]; then
	echo >&2 "electron-installer-debian failed!"
	exit $LAST_EXIT_CODE
fi

ls final_installer/
