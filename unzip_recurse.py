import os
import re
import shutil
import zipfile
from pathlib import Path


def main():
    dst_manga_title = "MyHomeMyHero"
    p1 = Path("download/Mai Homu Hiro v01-20")
    p2 = Path("tmp")
    p3 = Path(f"dst/{dst_manga_title}")
    os.makedirs(p3, exist_ok=True)
    img_types = ("jpg", "png")

    for f in p1.glob("**/*.zip"):
        print(f)
        with zipfile.ZipFile(f) as zf:
            zf.extractall(p2)

    s = set()
    for t in img_types:
        for f in p2.glob("**/*." + t):
            s.add(f.parent)
            continue

    for f in s:
        # ファイル名から数字二桁を抽出(例. aaa_01_bb -> 01)
        num = re.search(r"\d{2}", f.name).group()

        # フォルダをZIPファイルに圧縮
        shutil.make_archive(p3 / f"{dst_manga_title}_{num}", "zip", root_dir=f)

    shutil.rmtree(p2)


if __name__ == "__main__":
    main()
