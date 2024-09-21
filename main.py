import pyray as rl
rl.init_window(800, 450, "EchoExtract")
rl.gui_load_style("theme.rgs")
rl.gui_enable()
te = ''
rl.draw_fps(100,100)
rl.set_target_fps(60)
while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.WHITE)
    rl.gui_dummy_rec(rl.Rectangle(0,0,rl.get_screen_width(),rl.get_screen_height())," ")

    rl.gui_text_box(rl.Rectangle(20,400,760,20),te,100,1)
    rl.draw_fps(100,100)
    rl.end_drawing()
rl.close_window()

