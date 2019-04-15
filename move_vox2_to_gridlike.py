from pathlib import Path
from shutil import copy2

def move_audio(src_path,dst_path) :
    audio_dir = []
    for speaker in src_path.iterdir():
        Path(dst_path/speaker.stem).mkdir(exist_ok=True)
        Path(dst_path/speaker.stem/f"audio").mkdir(exist_ok=True)
        for youtubeid in speaker.iterdir():
            audio_dir = list(youtubeid.glob("*.m4a"))
            print(str(youtubeid))
            for audio in audio_dir:
                
                extension_tmp = audio.suffix
                extension = extension_tmp.replace(".","")
                try:
                    track = AudioSegment.from_file(str(audio), extension)
                    wav_filename = f"{audio.stem}.wav"
                    wav_path = dst_path / speaker.stem / f"audio" / wav_filename
                    print('CONVERTING: ' + str(audio))
                    #file_handle = track.export(str(wav_path), format='wav')
                    print(str(wav_path))
                    #print(str(file_handle))
                except:
                    print("ERROR CONVERTING " + str(audio))


                print(f"from {audio} to {str(dst_path)}/audio/{audio.stem}{audio.suffix}")

                #copy2(str(audio), str(dst_path/speaker.stem /f"audio"))

def move_video(src_path,dst_path) :
    video_dir = []
    for speaker in src_path.iterdir():
        Path(dst_path/speaker.stem).mkdir(exist_ok=True)
        Path(dst_path/speaker.stem/f"video").mkdir(exist_ok=True)
        for youtubeid in speaker.iterdir():
            video_dir = list(youtubeid.glob("*.mp4"))
            print(str(youtubeid))
            for video in video_dir:
                print(f"from {video} to {str(dst_path)}/video/{video.stem}{video.suffix}")
                copy2(str(video), str(dst_path/speaker.stem /f"video"))

if __name__ == "__main__" :
    #speaker_audio_dir_path = Path("/home/szb/datasets/vox2tmp/audio")
    #speaker_video_dir_path = Path("/home/szb/datasets/vox2tmp/video")
    #dst_dir_path = Path("/home/szb/datasets/vox2")
    speaker_audio_dir_path = Path("/media/datas/steinsun/datasets/voxceleb2/audio/vox2_aac/dev/aac")
    speaker_video_dir_path = Path("/media/datas/steinsun/datasets/voxceleb2/video/vox2_mp4/dev/mp4")
    dst_dir_path = Path("/media/datas/steinsun/datasets/vox2")
    move_audio(speaker_audio_dir_path, dst_dir_path)
    move_video(speaker_video_dir_path, dst_dir_path)

