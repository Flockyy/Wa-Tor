from cx_Freeze import setup, Executable

setup(
    name="MyApp",
    version="1.0",
    description="My Python App",
    executables=[Executable("main_pygame.py")],
    options={
        "build_exe": {
            "packages": ["pygame", "pygame_menu"],
        }
    },
    include_files=["assets/bg.png", "assets/music.mp3", "assets/music2.mp3"]
)