# Synopsis
 Download malware samples from virusshare.com

## Technical Freatures
- Download a VirusShare full torrent list
- Check for VirusShare updates
- Download torrent files
- Download zip files containing malware samples via transmission-daemon
- Unzip malware samples
- Move malware samples based on SHA256 

## Usage

### Transmission-Daemon control

- Kill all transmission daemons
`pkill -f transmission`

List all torrents
`transmission-remote -l`

Start all torrents
`transmission-remote --torrent all --start`

Stop all torrents
`transmission-remote --torrent all --stop`

Stop a specific torrent
`transmission-remote -t [ID] -S`

Start a specific torrent
`transmission-remote -t [ID] -s`

## Dependencies

`sudo apt-get install transmission-cli transmission-daemon`

