#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", default=23165451, cast=int)
    API_HASH = config("API_HASH", default="e82ea34d8f85233fc1d257ffdd2ff9fe")
    BOT_TOKEN = config("6859201439:AAHuaFnx098y5UvH6Y79AHnx6YGO3jhjPuw")
    DEV = 1715201164
    OWNER = config("1715201164")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -map 0 -c copy -c:v libx265  -s 1920x1080  -preset ultrafast  -crf 20 -c:a aac -b:a 192k -metadata title="Sonic Otakus" -pix_fmt yuv420p -metadata:s:a title="Sonic Otakus" -metadata:s:s title="Sonic Otakus" "{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/bfc86dbdff124b65a38ca.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
