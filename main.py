import pyray as rl
rl.init_window(800, 450, "EchoExtract")
rl.gui_enable()
rl.set_target_fps(60)
while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.WHITE)
    rl.gui_load_style("echo.rgs")
    rl.end_drawing()
rl.close_window()

