import os, sys, platform, pathlib

def fopen(path: str) -> str:
    with open(path, "r") as fp:
        source = fp.read()

    return source

def loader_parse(source: str, pload: str):
    lines = source.split('\n')
    for line in lines:
        segments = line.split(' ')
        if segments[0] != pload:
            continue
        else:
            command = ""
            for iterd in range(2, len(segments)):
                command += f"{segments[iterd]} "

            os.system(f'{command} {segments[1]}')

def main(args: list):
    if args[1] == '--version':
        return print(f"LDR ({platform.system()} {platform.release()}) Version 1.1")

    file_path = pathlib.Path("~/.config/loader/loader.conf").expanduser()
    loader_parse(fopen(file_path), args[1]);

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Insufficient arguments!")
    else:
        main(sys.argv);
