import customtkinter as ctk
from random import choice
from CTkMessagebox import CTkMessagebox
import config as cfg


class GreetingsPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.FRM_COLOR)
        self.controller = controller

        label_data = [
            ('Приветствую тебя!', cfg.TXT_COLOR_2),
            ('Я - магический шар', cfg.TXT_COLOR_1),
            ('Готов сыграть?', cfg.TXT_COLOR_2)
        ]

        for idx, (text, color) in enumerate(label_data):
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=('Constantia', 30)
            )
            label.place(relx =0.5, rely=0.25 + (idx * 0.2), anchor='c')

        button_data = [
            ('Не хочу', lambda: self.controller.end_game()),
            ('Давай!', lambda: self.controller.switch_to('RulesPage'))
        ]

        for idx, (text, command) in enumerate(button_data):
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS
            )
            button.place(relx=0.35 + (idx * 0.3), rely=0.85, anchor='c')


class RulesPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.FRM_COLOR)
        self.controller = controller

        label_data = [
            ('Задай мне любой вопрос...', cfg.TXT_COLOR_2),
            ('О прошлом, о будущем, о настоящем...', cfg.TXT_COLOR_1),
            ('И получи свой судьбоносный ответ', cfg.TXT_COLOR_2)
        ]

        for idx, (text, color) in enumerate(label_data):
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=('Constantia', 27)
            )
            label.place(relx=0.5, rely=0.2 + (idx * 0.2), anchor='c')

        button_data = [
            ('Не сейчас', lambda: self.controller.end_game()),
            ('Поехали!', lambda: self.controller.create_game())
        ]

        for idx, (text, command) in enumerate(button_data):
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS
            )
            button.place(relx=0.35 + (idx * 0.3), rely=0.8, anchor='c')


class GamePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.FRM_COLOR)
        self.controller = controller

        label_data = [
            ('Введи свой вопрос...', cfg.TXT_COLOR_1),
            ('...и нажми на шар...', cfg.TXT_COLOR_2)
        ]

        for idx, (text, color) in enumerate(label_data):
            label = ctk.CTkLabel(
                self,
                text=text,
                text_color=color,
                font=('Constantia', 27)
            )
            label.place(relx=0.5, rely=0.15 + (idx * 0.25), anchor='c')

        self.entry = ctk.CTkEntry(self, **cfg.ENTRY_PARAMS)
        self.entry.place(relx=0.5, rely=0.28, anchor='c')

        self.button = ctk.CTkButton(
            self,
            **cfg.BALL_PARAMS,
            command=lambda: self.get_status(self.entry.get())
        )
        self.button.place(relx=0.5, rely=0.7, anchor='c')

    def get_status(self, user_input):
        status = self.controller.transfer_data(user_input)

        if status in cfg.ERROR_MESSAGES:
            error_message = CTkMessagebox(
                self.controller,
                **cfg.MSG_PARAMS,
                message=cfg.ERROR_MESSAGES[status]
            )
            self.controller.wait_window(error_message)
            self.prepare_entry()
            return

        self.controller.show_result()

    def prepare_entry(self):
        self.entry.delete(0, 'end')
        self.entry.focus_set()

    def update_game(self):
        self.prepare_entry()
        self.button.configure(
            fg_color=choice(cfg.COLORS),
            hover_color=choice(cfg.COLORS)
        )


class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.FRM_COLOR)
        self.controller = controller

        self.message_label = ctk.CTkLabel(
            self,
            text='',
            text_color=cfg.TXT_COLOR_1,
            font=('Constantia', 27)
        )
        self.message_label.place(relx=0.5, rely=0.5, anchor='c')

    def update_message(self, phrase):
        if phrase in cfg.GAME_MESSAGES['answers']:
            self.message_label.configure(
                text=f'Шар говорит:\n\n{phrase}',
                text_color=cfg.TXT_COLOR_3,
                font=('Constantia', 35, 'bold')
            )
            return
        self.message_label.configure(
            text=phrase,
            text_color=cfg.TXT_COLOR_1,
            font=('Constantia', 27)
        )

class FinalPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.FRM_COLOR)
        self.controller = controller

        label = ctk.CTkLabel(
            self,
            text='Хочешь сыграть снова?',
            text_color=cfg.TXT_COLOR_1,
            font=('Constantia', 27)
        )
        label.place(relx=0.5, rely=0.4, anchor='c')

        button_data = [
            ('Не сейчас', lambda: self.controller.end_game()),
            ('Поехали!', lambda: self.controller.create_game())
        ]

        for idx, (text, command) in enumerate(button_data):
            button = ctk.CTkButton(
                self,
                text=text,
                command=command,
                **cfg.BTN_PARAMS
            )
            button.place(relx=0.35 + (idx * 0.3), rely=0.6, anchor='c')

class MainLogic():
    def check_input(self, user_input):
        cleaned_input = user_input.strip()

        if not cleaned_input:
            return 'empty'
        if len(cleaned_input) < 5:
            return 'too_short'
        if not any(c.isalpha() for c in cleaned_input):
            return 'not_alpha'
        if not cleaned_input.endswith('?'):
            return 'not_question'

        return 'success'

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('the magic ball')
        self.geometry('700x500+700+350')
        self.resizable(False, False)
        self.attributes('-alpha', 0.8)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)

        self.main_logic = MainLogic()

        self.transfer_data = self.main_logic.check_input

        self.pages = {}
        self.current_frame = None

        for F in (GreetingsPage, RulesPage,
            GamePage, MessagePage, FinalPage
        ):
            page_name = F.__name__
            self.pages[page_name] = F(
                master=self.main_frame,
                controller=self
            )
        self.switch_to("GreetingsPage")

    def switch_to(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.pages[page_name]
        self.current_frame.pack(fill="both", expand=True)

    def show_result(self):
        waiting = choice(cfg.GAME_MESSAGES['waiting_words'])
        answer = choice(cfg.GAME_MESSAGES['answers'])
        page = self.pages['MessagePage']

        page.update_message(waiting)
        self.switch_to('MessagePage')
        self.after(3000, lambda: page.update_message(answer))
        self.after(8000, lambda: self.switch_to('FinalPage'))

    def create_game(self):
        loading = choice(cfg.GAME_MESSAGES['loading_words'])
        page = self.pages['MessagePage']
        page.update_message(loading)
        self.switch_to('MessagePage')
        self.pages['GamePage'].update_game()
        self.after(3000, lambda: self.switch_to('GamePage'))

    def end_game(self):
        farewell = choice(cfg.GAME_MESSAGES['farewell_words'])
        page = self.pages['MessagePage']
        page.update_message(farewell)
        self.switch_to('MessagePage')
        self.after(3000, self.destroy)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()