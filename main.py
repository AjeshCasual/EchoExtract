import pyray as rl
from pathlib import Path
rl.init_window(960, 540, "EchoExtract")
rl.gui_enable()
rl.set_target_fps(60)
rl.gui_load_style("theme.rgs")

rl.set_window_state(rl.FLAG_WINDOW_UNDECORATED)

layoutRecs = (
        rl.Rectangle( 0, 0, 960, 540 ),
        rl.Rectangle( 8, 488, 944, 44 ),
        rl.Rectangle( 824, 448, 128, 32 ),
        rl.Rectangle( 8, 408, 808, 32 ),
        rl.Rectangle( 824, 408, 128, 32 ),
        rl.Rectangle( 8, 32, 464, 368 ),
        rl.Rectangle( 488, 32, 464, 368 ),
        rl.Rectangle( 696, 448, 120, 32 ),
        rl.Rectangle( 8, 448, 680, 32 ),
    );

#hmm


WindowBoxText = "SAMPLE TEXT"
ButtonDownloadText = "Download"
DropdownBoxTypeText = "MP4;MP3"
ButtonCreateText = "Create"
ListViewFolderText = "ONE;TWO;THREE;4;5;5;3;2;2;6;7;8;9;0;0;7;"
ListViewMusicText = "ONE;TWO;THREE;4;5;5;3;2;2;6;7;8;9;0;0;7;"
ButtonGetLinkText = "Paste Link"
DummyRecLinkText = "Link"

WindowBoxActive = True
DropdownBoxTypeEditMode = False
DropdownBoxTypeActive = rl.ffi.new('int *',0)
TextBoxFolderEditMode = False
TextBoxFolderText = rl.ffi.new("char []", b"Folder")
ListViewFolderScrollIndex = rl.ffi.new('int *',0)
ListViewFolderActive = rl.ffi.new('int *',0)
ListViewMusicScrollIndex = rl.ffi.new('int *',0)
ListViewMusicActive = rl.ffi.new('int *',0)
DownloadableLink = False


def ListDir():

    temp = Path.cwd()

    Dir = [item.name for item in temp.iterdir() if item.is_dir()]
    DirSep = ';'.join(Dir) + ';'
    return DirSep

def ListFileMP3(fol):
    temp = Path.cwd()/fol
    Files = [file.name[:70] for file in temp.rglob('*.mp3') if file.is_file()]
    FileSep = ';'.join(Files) + ';'
    return FileSep

def ListFileMP4(fol):
    temp = Path.cwd()/fol
    Files = [file.name[:70] for file in temp.rglob('*.mp4') if file.is_file()]
    FileSep = ';'.join(Files) + ';'
    return FileSep
    
def Splitter(text):
    return text.strip(';').split(';')

ListViewFolderText = ListDir()
ListViewMusicText = ListFileMP3("kj")

def ButtonDownload():
    print("Downloading")

def ButtonCreate():
    mkdir(parents=True, exist_ok=True)
    print("Created")
def ButtonGetLink():
    global DummyRecLinkText
    if len(rl.get_clipboard_text()) < 150 and rl.get_clipboard_text().startswith("https://www.youtube.com/watch?"):
        DummyRecLinkText = rl.get_clipboard_text()
    else:
        DummyRecLinkText = "Link Error"

while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.WHITE)
    rl.gui_button(rl.Rectangle(10,10,100,100),"hello")

    if (DropdownBoxTypeEditMode):
        rl.gui_lock()

    if (WindowBoxActive):
        WindowBoxActive = not(rl.gui_window_box(layoutRecs[0], WindowBoxText))
        if (rl.gui_button(layoutRecs[1], ButtonDownloadText)):
            ButtonDownload()
        if (rl.gui_text_box(layoutRecs[3], TextBoxFolderText, 128, TextBoxFolderEditMode)):
            TextBoxFolderEditMode = not(TextBoxFolderEditMode)
        if (rl.gui_button(layoutRecs[4], ButtonCreateText)):
            ButtonCreate() 
        rl.gui_list_view(layoutRecs[5], ListViewFolderText, ListViewFolderScrollIndex, ListViewFolderActive)
        rl.gui_list_view(layoutRecs[6], ListViewMusicText, ListViewMusicScrollIndex, ListViewMusicActive)
        if (rl.gui_button(layoutRecs[7], ButtonGetLinkText)):
            ButtonGetLink() 
        rl.gui_dummy_rec(layoutRecs[8], DummyRecLinkText)
        if (rl.gui_dropdown_box(layoutRecs[2], DropdownBoxTypeText, DropdownBoxTypeActive, DropdownBoxTypeEditMode)):
            DropdownBoxTypeEditMode = not(DropdownBoxTypeEditMode)
        print(ListViewFolderActive[0])
    rl.gui_unlock()


    rl.end_drawing()
rl.close_window()
