import pyray as rl
rl.init_window(800, 450, "EchoExtract")
rl.gui_load_style("theme.rgs")
rl.gui_enable()
while not rl.window_should_close():

    

    rl.begin_drawing()
    rl.clear_background(rl.WHITE)
    rl.gui_dummy_rec(rl.Rectangle(10,10,200,200),"etare")
    rl.end_drawing()
rl.close_window()
