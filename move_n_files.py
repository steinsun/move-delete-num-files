from pathlib import Path
from shutil import copy2

def move_n_files(source_path, des_path, train_per, val_per):
    print("Start!")

    s_audio_path = Path(source_path)/ f"audio"
    s_video_path = Path(source_path) / f"video"

    d_train_path = Path(des_path) / f"grid_s2_train" 
    d_val_path = Path(des_path) / f"grid_s2_val" 
    d_test_path = Path(des_path) / f"grid_s2_test" 

    if d_train_path.is_dir() == False:
        d_train_path.mkdir()
    if d_val_path.is_dir() == False:
        d_val_path.mkdir()
    if d_test_path.is_dir() == False:
        d_test_path.mkdir()

    audio_ind = []
    for audio in s_audio_path.iterdir():
        audio_ind.append(str(audio.stem))

    num = len(audio_ind)
    #audio_ind = [a for a in audio_path.glob("*.wav") if a.is_file()]
    #video_ind = [v for v in video_path.glob("*.mpg") if v.is_file()]

    for name in audio_ind[0:int(train_per*num)]:
        if (d_train_path / f"audio").is_dir() == False:
            (d_train_path / f"audio").mkdir()
        copy2(str(s_audio_path / f"{name}.wav"), str(d_train_path / f"audio")) 
        if (d_train_path / f"video").is_dir() == False:
            d_train_path.mkdir("video")
        copy2(str(s_video_path / f"{name}.mpg"), str(d_train_path  / f"video")) 
    for name in audio_ind[int(train_per*num):int((train_per+val_per)*num)]:
        if (d_val_path / f"audio").is_dir() == False:
            d_val_path.mkdir("audio")
        copy2(str(s_audio_path / f"{name}.wav"), str(d_val_path / f"audio")) 
        if (d_val_path / f"video").is_dir() == False:
            d_val_path.mkdir("video")
        copy2(str(s_video_path / f"{name}.mpg"), str(d_val_path / f"video")) 
    for name in audio_ind[int((train_per+val_per))*num:num]:
        if (d_test_path / f"audio").is_dir() == False:
            d_test_path.mkdir("audio")
        copy2(str(s_audio_path / f"{name}.wav"), str(d_test_path / f"audio")) 
        if (d_test_path / f"video").is_dir() == False:
            d_test_path.mkdir("video")
        copy2(str(s_video_path / f"{name}.mpg"), str(d_test_path / f"video")) 

    print("Done!")

if __name__ == "__main__":
    move_n_files("/media/datas-2/steinsun/datasets/grid/s2/", "/media/datas-2/steinsun/datasets/grid_s2/s2/", 
        train_per=0.7, val_per=0.1)