from tkinter import *
import time


class APP:
    def __init__(self, title, bg, geometry, resizeable):
        window = Tk(className=title)
        window.geometry(geometry)  # set the window size [height x width]
        window.configure(bg=bg)  # set the window background color
        window.resizable(resizeable, resizeable)

        #    Setting the main frame    #
        main_frame = Frame(window)
        main_frame.pack(fill=BOTH)
        start_btn = Button(main_frame, text="Start", height=5, width=20, command=self.show_app)
        start_btn['bg'] = "#D1D1D1"
        start_btn.pack()

        #    Setting the console frame    #
        app_frame = Frame(window, height=50)
        canvas = Canvas(app_frame)
        scroll_y = Scrollbar(app_frame, orient="vertical", command=canvas.yview)
        frame = Frame(canvas)
        log_btn = Button(app_frame, text="Open Log", height=2)
        log_btn.pack(side=TOP, fill=X)

        self.start_btn = start_btn
        self.frame_can = frame
        self.canvas = canvas
        self.scroll_y = scroll_y
        self.main = main_frame
        self.app = app_frame
        self.window = window
        self.title = title
        self.bg = bg
        self.geometry = geometry
        self.resizeable = resizeable

    def show_app(self):
        self.main.pack_forget()
        self.app.pack(fill=BOTH)
        self.window['bg'] = "blue"
        time.sleep(2)
        self.launch()


    def update_scroll(self):
        # put the frame in the canvas
        self.canvas.create_window(0, 0, anchor='nw', window=self.frame_can)
        # make sure everything is displayed before configuring the scrollregion
        self.canvas.update_idletasks()

        self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.scroll_y.set)

        self.canvas.pack(fill='both', expand=True, side='left')
        self.scroll_y.pack(fill='y', side='right')

    def set_launch(self, launch):
        self.launch = launch

    def add_user_line(self, text):
        ui = Text(self.frame_can, height=1.1, width=100)
        ui['fg'] = "#37FF2B"
        ui['bg'] = self.bg
        ui.pack(side=TOP, fill=X)
        ui.insert(END, f"YOU: {str(text)}")
        ui.configure(state='disabled')
        self.update_scroll()
        pass

    def add_bot_line(self, text):
        ui = Text(self.frame_can, height=1.1, width=100)
        ui['fg'] = '#6BFCF7'
        ui['bg'] = self.bg
        ui.pack(side=TOP, fill=X)
        ui.insert(END, f"Snowy: {str(text)}")
        ui.configure(state='disabled')
        self.update_scroll()
        pass


'''class App:
    def __init__(self, title, bg, geometry, resizeable):
        window = Tk(className=title)
        window.geometry(geometry)  # set the window size [height x width]
        window.configure(bg=bg)  # set the window background color
        window.resizable(resizeable, resizeable)

        canvas = Canvas(window)
        canvas['bg'] = bg
        scroll_y = Scrollbar(window, orient="vertical", command=canvas.yview)
        frame = Frame(canvas)

        log_btn = Button(window, text="Open Log", height=2)
        log_btn.pack(side=TOP, fill=X)

        self.frame = frame
        self.canvas = canvas
        self.scroll_y = scroll_y
        self.window = window
        self.title = title
        self.bg = bg
        self.geometry = geometry
        self.resizeable = resizeable

        self.log_btn = log_btn

        set_app(self)

    def updtae_scroll(self):
        # put the frame in the canvas
        self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
        # make sure everything is displayed before configuring the scrollregion
        self.canvas.update_idletasks()

        self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.scroll_y.set)

        self.canvas.pack(fill='both', expand=True, side='left')
        self.scroll_y.pack(fill='y', side='right')

    def set_bg(self, bg):
        self.window.configure(bg=bg)  # set the window's background
        self.bg = bg

    def set_geometry(self, geometry):
        self.window.geometry(geometry)  # set the window size
        self.geometry = geometry

    def set_title(self, title):
        self.window.title = title
        self.title = title

    def set_launch(self, launch):
        self.log_btn['command'] = launch(self.log_btn, self)

    def get_title(self):
        return self.title

    def get_geometry(self):
        return self.geometry

    def get_bg(self):
        return self.bg

    def start(self):
        global main
        if get_main() is not None:
            main.kill()
        self.window.mainloop()

    def add_user_line(self, text):
        ui = Text(self.frame, height=1.1, width=100)
        ui['fg'] = "#37FF2B"
        ui['bg'] = self.bg
        ui.pack(side=TOP, fill=X)
        ui.insert(END, f"YOU: {str(text)}")
        ui.configure(state='disabled')
        self.updtae_scroll()
        pass

    def add_bot_line(self, text):
        ui = Text(self.frame, height=1.1, width=100)
        ui['fg'] = '#6BFCF7'
        ui['bg'] = self.bg
        ui.pack(side=TOP, fill=X)
        ui.insert(END, f"Snowy: {str(text)}")
        ui.configure(state='disabled')
        self.updtae_scroll()
        pass

    def kill(self):
        self.window.destroy()


class Main:
    def __init__(self, title, bg, geometry, resizeable, func):
        window = Tk(className=title)
        window.geometry(geometry)  # set the window size [height x width]
        window.configure(bg=bg)  # set the window background color
        window.resizable(resizeable, resizeable)
        log_btn = Button(window, text="Start", height=5, width=20, command=func)
        log_btn['bg'] = "#D1D1D1"
        _y = 150
        _x = 330
        log_btn.place(y=_y, x=_x)

        self.window = window
        self.title = title
        self.bg = bg
        self.geometry = geometry
        self.resizeable = resizeable
        set_main(self)

    def start(self):
        self.window.mainloop()

    def kill(self):
        self.window.destroy()
'''