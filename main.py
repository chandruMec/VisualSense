from actors.app_actor import AppActor
from actors import qml_file
import pykka


if __name__ == "__main__":
    app_actor = AppActor.start(qml_file)
    pykka.ActorRegistry.stop_all()
