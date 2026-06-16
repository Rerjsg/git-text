import os
import re
import glob
import argparse


def main():
    parser = argparse.ArgumentParser(description="rename file")
    parser.add_argument("oldpattern")
    parser.add_argument("newpattern")
    parser.add_argument("filepattern")
    parser.add_argument("--regex", action="store_true")

    args = parser.parse_args()

    files = glob.glob(args.filepattern)
    if not files:
        print(f"未匹配到'{args.filepattern}' ")
        return

    for filepath in sorted(files):
        dirname, basename = os.path.split(filepath)

        if args.regex:
            new_basename = re.sub(args.oldpattern, args.newpattern, basename)
        else:
            new_basename = basename.replace(args.oldpattern, args.newpattern)

        if new_basename == basename:
            continue

        new_path = os.path.join(dirname, new_basename)

        if os.path.exists(new_path):
            print(f"跳过：{filepath} -> {new_basename} （已存在）")
            continue

        try:
            os.rename(filepath, new_path)
            print(f"重命名：{filepath} -> {new_basename}")
        except PermissionError:
            print(f"跳过：{filepath} -> {new_basename} （文件正被使用）")
        except Exception as e:
            print(f"skip:{filepath} -> {new_basename}error:{e}")


main()
