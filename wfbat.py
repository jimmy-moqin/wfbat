import core
import fire

def main():
    pass
if __name__ == '__main__':
    try:
        fire.Fire(core.BioProject())
    except KeyboardInterrupt:
        print("\n\nBye-bye!")