# Synopsis
 Download malware samples from VirusShare.com

## Technical Freatures
- Download a VirusShare full torrent list
- Check for VirusShare updates
- Download torrent files
- Download zip files containing malware samples via transmission-daemon

## Usage

### Download torrent files from VirusShare.com

`python nkvs.py -u username -p password -t torrent_folder`

-u USERNAME, --username the username to login VirusShare.com

-p PASSWORD, the password to login VirusShare.com

-t TORRENTS_FOLDER, the folder to store torrent files

### Transmission-Daemon

Add aliases into .bashrc to create commands for torrent downloading.

1. Use command vsls to list all torrents

`alias vsls='transmission-remote -l'`

2. Use command vsinit to init transmission-daemon for downloading

`rm -fr ./config/transmission-daemon/torrents/*`

`alias vsinit='transmission-daemon --paused -w ./DATA -c ./DATA -e transmission.log -g ./config/transmission-daemon'`

First, clean all torrent files at transmision configration before init transmission for download.

-w --download-dir: directory to store downloaded data 

-c: directory to watch for new .torrent files to be added. 

3. Use command vsstart to start torrent downloading

`alias vsstart='transmission-remote --torrent all --stop'`

4. Use command vsstop to stop torrent downloading

`alias vsstart='transmission-remote --torrent all --start'`

5. Use command vskill to kill all transmission daemons

`alias vskill='pkill -f transmission'`

## Dependencies

`sudo apt-get install transmission-cli transmission-daemon`
