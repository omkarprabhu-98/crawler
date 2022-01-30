
videos = ['big_buck_bunny_1080p24.y4m', 'tearsofsteel-4k.y4m']
resolutions = ['1920:1080', '1280:720', '720:480']
encoders = ['libvpx-vp9', 'libx264']
crf = ['21', '31']
target_rate = ['250k', '750k', '2000k']

"ffmpeg -i -c:v [encoders] -vf scale=[resolution] -b:v [target_rate] -pass [1|2] <output>"


for video in videos:
    for resolution in resolutions:
        for r in crf 
            file_name = video_resolution_encoder_crf_r
            "ffmpeg -i -c:v libvpx-vp9 -vf scale=[resolution] -crf [r] -b:v 0"
        for r in target_rate 
            file_name = video_resolution_encoder_twopass_r
            "ffmpeg -i input.mp4 -c:v libvpx-vp9 -vf scale=[resolution] -b:v [r] -pass 1 -an -f null /dev/null && \"
            "ffmpeg -i input.mp4 -c:v libvpx-vp9 -vf scale=[resolution] -b:v [r] -pass 2 -c:a libopus output.webm"
        for r in crf 
            file_name =  
            "ffmpeg -i -c:v libx264 -vf scale=[resolution] -crf [r]"
        for r in target_rate 
            file_name = video_resolution_encoder_twopass_r
            "ffmpeg -i input.mp4 -c:v libx264 -vf scale=[resolution] -b:v [r] -pass 1 -an -f null /dev/null && \"
            "ffmpeg -i input.mp4 -c:v libx264 -vf scale=[resolution] -b:v [r] -pass 2 -c:a libopus output.webm"