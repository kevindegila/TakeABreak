import webbrowser
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--session", "-s", type=int)
parser.add_argument("--duree", "-d", help="Duree d'une session en minute", type=int)
parser.add_argument("--pause", "-p", help="La durée de la pause en minute", type=int)
args = parser.parse_args()



def session(duree, pause):
    """
    Lance une session de travail de "durée" minute,
    ouvre une vidéo dans le navigateur
    et fais une pause de "pause" minute
    :param duree:
    :param pause:
    :return:
    """
    print("Une session a commencé")
    time.sleep(duree * 60)
    webbrowser.open("https://www.youtube.com/watch?v=yzg94Iamm_c")
    print("Pause en cours")
    time.sleep(pause * 60)


for i in range(args.session):
    session(args.duree, args.pause)
    print(f"Session {i + 1} terminée, il reste {args.session - i - 1} sessions")
