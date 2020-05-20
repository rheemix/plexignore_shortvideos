# .plexignore for Short Videos
 Create .plexignore files for all short videos including live photos


## Descriptions
-  Creates .plexignore files at each directory with list of videos that are less than 5 seconds long
  - Searches MOV, AVI and MP4 files
  - Video duration limit can be changed using `duration_limit`
  - Live photos are generally less than 3 seconds, so they will be included in the list
  - Video duration is determined using `ffprobe`

## Requirements
- Python 3 OR Windows Executable also included
- [ffmpeg](https://ffmpeg.zeranoe.com/builds/) downloaded and \bin directory included in path