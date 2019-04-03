from pathlib import Path

def delete_n_files(source_path):
    print("Start!")
    s_path = Path(source_path)

    audio_path = s_path / f"audio"


    audio_ind = [a for a in audio_path.glob("*.wav") if a.is_file()]

    for i in range(0,len(audio_ind),5):
        Path(f"{audio_ind[i]}").unlink()

    print("Done!")

if __name__ == "__main__":
    delete_n_files("/media/datas-2/steinsun/datasets/grid_noise/s3/")
