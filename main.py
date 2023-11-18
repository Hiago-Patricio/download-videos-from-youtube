import tkinter as tk
import ssl
from pytube import YouTube
from tkinter import filedialog


root = tk.Tk()


def download_videos_from_file():
    input_file_path = select_input_file()
    output_path = select_output_path()
    urls = load_urls_from_file(input_file_path)
    download_videos(urls, output_path)


def select_input_file():
    input_file = filedialog.askopenfilename(
        parent=root,
        title="Selecione o arquivo que contém os links dos vídeos a serem baixados",
        filetypes=[("Text Files", "*.txt")],
    )
    return input_file


def select_output_path():
    output_path = filedialog.askdirectory(
        parent=root, title="Selecione a pasta onde os vídeos serão salvos"
    )
    return output_path


def load_urls_from_file(file_path: str):
    with open(file_path, "r") as file:
        urls = file.readlines()
    return urls


def download_videos(urls: list, output_path: str = "./videos"):
    for url in urls:
        download_video(url, output_path)


def download_video(url, output_path="./"):
    try:
        video = YouTube(url)

        stream = video.streams.get_highest_resolution()

        print(f"Baixando: {video.title}...")
        stream.download(output_path=output_path)
        print("Download concluído com sucesso!")

    except Exception as e:
        print(f"Erro: {str(e)}")


ssl._create_default_https_context = ssl._create_unverified_context
download_videos_from_file()
