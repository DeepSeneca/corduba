from corduba import __version__

class WelcomeHeader:

    def print_welcome_header(self) -> None:
        print("###################################")
        print("##                               ##")
        print("##  Corduba provisioning server  ##")
        print(f"##  Version: {__version__}               ##")
        print("##                               ##")
        print("###################################")