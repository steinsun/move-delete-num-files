from pathlib import Path
from shutil import copy2

def move_audio(source_path,des_path) :
    audio_dir = []
    for speaker in speaker_audio_dir_path.iterdir():
        Path(des_dir_path/speaker.stem).mkdir(exist_ok=True)
        Path(des_dir_path/speaker.stem/f"audio").mkdir(exist_ok=True)
        for youtubeid in speaker.iterdir():
            audio_dir = list(youtubeid.glob("*.wav"))
            print(str(youtubeid))
            for audio in audio_dir:
                print(f"from {audio} to {str(speaker)}/audio/{audio.stem}{audio.suffix}")
                copy2(str(audio), str(des_dir_path/speaker.stem /f"audio"))

def move_video(source_path,des_path) :
    video_dir = []
    for speaker in speaker_video_dir_path.iterdir():
        Path(des_dir_path/speaker.stem).mkdir(exist_ok=True)
        Path(des_dir_path/speaker.stem/f"video").mkdir(exist_ok=True)
        for youtubeid in speaker.iterdir():
            video_dir = list(youtubeid.glob("*.mpg"))
            print(str(youtubeid))
            for video in video_dir:
                print(f"from {video} to {str(speaker)}/video/{video.stem}{video.suffix}")
                copy2(str(video), str(des_dir_path/speaker.stem /f"video"))

if __name__ == "__main__" :
    #speaker_audio_dir_path = Path("/home/szb/datasets/vox2tmp/audio")
    #speaker_video_dir_path = Path("/home/szb/datasets/vox2tmp/video")
    #des_dir_path = Path("/home/szb/datasets/vox2")
    speaker_audio_dir_path = Path("/media/datas/steinsun/datasets/voxceleb2/audio/vox2_aac/dev/aac")
    speaker_video_dir_path = Path("/media/datas/steinsun/datasets/voxceleb2/video/vox2_mp4/dev/mp4")
    des_dir_path = Path("/media/datas/steinsun/datasets/vox2")
    move_audio(speaker_audio_dir_path, des_dir_path)
    move_video(speaker_video_dir_path, des_dir_path)

