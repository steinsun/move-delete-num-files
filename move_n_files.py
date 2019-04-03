from pathlib import Path
from shutil import copy2

def move_n_files(source_path, des_path):
    s_path = Path(source_path)
    d_path = Path(des_path)

    audio_path = s_path / f"audio"
    video_path = s_path / f"video"

    audio_ind = [x for x in audio_path.glob("*.wav") if x.is_file()]
    for i in range(0,800):
        copy2(str(audio_path) / f"{audio_ind[i]}", str(d_path) / f"grid_s1_train" / f"audio") 
    for i in range(800,900):
        copy2(str(audio_path) / f"{audio_ind[i]}", str(d_path) / f"grid_s1_val" / f"audio") 
    for i in range(900,1000):
        copy2(str(audio_path) / f"{audio_ind[i]}", str(d_path) / f"grid_s1_test" / f"audio") 

    video_ind = [x for x in video_path.glob("*.wav") if x.is_file()]
    for i in range(0,800):
        copy2(str(video_path) / f"{video_ind[i]}", str(d_path) / f"grid_s1_train" / f"video") 
    for i in range(800,900):
        copy2(str(video_path) / f"{video_ind[i]}", str(d_path) / f"grid_s1_val" / f"video") 
    for i in range(900,1000):
        copy2(str(video_path) / f"{video_ind[i]}", str(d_path) / f"grid_s1_test" / f"video") 

if __name__ == "__main__":
    move_n_files("/media/datas-2/steinsun/datasets/grid/s1", "/media/datas-2/steinsun/datasets/grid_s1")