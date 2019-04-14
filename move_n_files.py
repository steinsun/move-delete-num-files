from pathlib import Path
from shutil import copy2

##designed for GRID speaker id s2
def move_n_files(source_path, des_path, train_per, val_per):
    print("Start!")

    s_audio_path = Path(source_path)/ f"audio"
    s_video_path = Path(source_path) / f"video"

    d_train_path = Path(des_path) / f"grid_s2_train" / f"s2"
    d_val_path   = Path(des_path) / f"grid_s2_val" / f"s2"
    d_test_path  = Path(des_path) / f"grid_s2_test" / f"s2"

    if (d_train_path / f"audio").is_dir() is not True: (d_train_path / f"audio").mkdir(parents=True)
    if (d_train_path / f"video").is_dir() is not True: (d_train_path / f"video").mkdir(parents=True)
    if (d_val_path   / f"audio").is_dir() is not True: (d_val_path / f"audio").mkdir(parents=True)
    if (d_val_path   / f"video").is_dir() is not True: (d_val_path / f"video").mkdir(parents=True)
    if (d_test_path  / f"audio").is_dir() is not True: (d_test_path / f"audio").mkdir(parents=True)
    if (d_test_path  / f"video").is_dir() is not True: (d_test_path / f"video").mkdir(parents=True)

    audio_ind = []
    for audio in s_audio_path.iterdir():
        audio_ind.append(str(audio.stem))

    num = len(audio_ind)
    #audio_ind = [a for a in audio_path.glob("*.wav") if a.is_file()]
    #video_ind = [v for v in video_path.glob("*.mpg") if v.is_file()]

    for train in audio_ind[0:int(train_per*num)]:
        copy2(str(s_audio_path / f"{train}.wav"), str(d_train_path / f"audio"))     
        copy2(str(s_video_path / f"{train}.mpg"), str(d_train_path  / f"video")) 

    for val in audio_ind[int(train_per*num):int((train_per+val_per)*num)]:
        copy2(str(s_audio_path / f"{val}.wav"), str(d_val_path / f"audio")) 
        copy2(str(s_video_path / f"{val}.mpg"), str(d_val_path / f"video")) 

    for test in audio_ind[int((train_per+val_per)*num):]:
        copy2(str(s_audio_path / f"{test}.wav"), str(d_test_path / f"audio")) 
        copy2(str(s_video_path / f"{test}.mpg"), str(d_test_path / f"video")) 

    print("Done!")

if __name__ == "__main__":
    move_n_files("/media/datas-2/steinsun/datasets/grid/s2/", "/media/datas-2/steinsun/datasets/grid_s2/", 
        train_per=0.7, val_per=0.1)