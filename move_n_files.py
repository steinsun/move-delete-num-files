from pathlib import Path
from shutil import copy2

def move_n_files(source_path, des_path):
    print("Start!")
    s_path = Path(source_path)
    d_path = Path(des_path)

    audio_path = s_path / f"audio"
    video_path = s_path / f"video"

    audio_ind = []
    for audio in audio_path.iterdir():
        audio_ind.append(str(audio.stem))
    
    #audio_ind = [a for a in audio_path.glob("*.wav") if a.is_file()]
    #video_ind = [v for v in video_path.glob("*.mpg") if v.is_file()]

    for name in audio_ind[0:700]:
        copy2(str(f"{name}.wav"), str(d_path / f"grid_s2_train" / f"audio")) 
        copy2(str(f"{name}.mpg"), str(d_path / f"grid_s2_train" / f"video")) 
    for name in audio_ind[700:800]:
        copy2(str(f"{name}.wav"), str(d_path / f"grid_s2_val" / f"audio")) 
        copy2(str(f"{name}.mpg"), str(d_path / f"grid_s2_val" / f"video")) 
    for name in audio_ind[800:1000]:
        copy2(str(f"{name}.wav"), str(d_path / f"grid_s2_test" / f"audio")) 
        copy2(str(f"{name}.mpg"), str(d_path / f"grid_s2_test" / f"video")) 

    print("Done!")

if __name__ == "__main__":
    move_n_files("/media/datas-2/steinsun/datasets/grid/s2/", "/media/datas-2/steinsun/datasets/grid_s2/")