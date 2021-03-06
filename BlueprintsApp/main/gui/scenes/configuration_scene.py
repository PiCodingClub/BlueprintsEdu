from gui.scenes.scene_builder import SceneBuilder
from utils import logger_utils
import pygame as pg
from gui.buttons.config_menu_buttons import *
from utils.gui_utils import Themes
from utils import gui_utils
from gui.forms.theme_selection_form import ThemeSelectionForm
from pygame.locals import *
from gui.buttons.back_button import BackButton
from gui.forms.language_selection_form import LanguageSelectionForm
from gui.forms.display_selection_form import DisplaySelectionForm
from utils.app_utils import DisplaySettings


class ConfigurationScene(SceneBuilder):

    def __init__(self, display):
        SceneBuilder.__init__(self, display)
        self.__logger = logger_utils.get_logger(__name__)
        self.btn_theme = ThemeButton()
        self.btn_theme.color = Themes.DEFAULT_THEME.get("front_screen")
        self.btn_language = LanguageButton()
        self.btn_language.color = Themes.DEFAULT_THEME.get("front_screen")
        self.btn_back = BackButton()
        self.btn_back.color = Themes.DEFAULT_THEME.get("front_screen")
        self.btn_display = DisplayButton()
        self.btn_display.color = Themes.DEFAULT_THEME.get("front_screen")
        self.frm_theme = ThemeSelectionForm(self.display)
        self.frm_lang = LanguageSelectionForm(self.display)
        self.frm_display = DisplaySelectionForm(self.display)

    def draw_scene(self):
        # PREPARE DATA
        font = pg.font.Font(Themes.DEFAULT_THEME.get("banner_font_style"),
                            int(DisplaySettings.get_size_by_key()[1] * .09))
        txt = font.render(StringUtils.get_string("ID_CONFIGURATION"), True, Themes.DEFAULT_THEME.get("font"))
        rect_txt = txt.get_rect()
        rect_txt.topleft = (
            int(DisplaySettings.get_size_by_key()[0] * .02), int(DisplaySettings.get_size_by_key()[1] * .05))
        # DISPLAY
        self.display.fill(Themes.DEFAULT_THEME.get("front_screen"))
        self.display.blit(txt, rect_txt)
        self.draw_buttons()
        self.check_button_hover()
        self.draw_forms()
        super().draw_scene()

    def draw_forms(self):
        self.frm_theme.draw_form()
        self.frm_lang.draw_form()
        self.frm_display.draw_form()

    def draw_buttons(self):
        # UPDATE BUTTON AFTER THEME/LANGUAGE SET
        self.btn_theme.update_button(color=Themes.DEFAULT_THEME.get("front_screen"))
        self.btn_language.update_button(color=Themes.DEFAULT_THEME.get("front_screen"))
        self.btn_back.update_button(color=Themes.DEFAULT_THEME.get("front_screen"))
        self.btn_display.update_button(color=Themes.DEFAULT_THEME.get("front_screen"))

        x = int(DisplaySettings.get_size_by_key()[0] * .02)
        y = DisplaySettings.get_size_by_key()[1] * .93
        pos = 0
        self.btn_back.set_custom_coordinates(
            (int(x + self.btn_back.get_rect().width * .5),
             int(y - pos * (
                     self.btn_back.get_rect().height + gui_utils.BUTTON_MARGIN * DisplaySettings.get_size_by_key()[
                 1]))))
        pg.draw.rect(self.display, self.btn_back.color, self.btn_back.get_rect(), 0)
        self.display.blit(self.btn_back.get_text(), self.btn_back.get_text_rect())
        pos += 1
        self.btn_theme.set_custom_coordinates(
            (int(x + self.btn_theme.get_rect().width * .5),
             int(y - pos * (
                     self.btn_theme.get_rect().height + gui_utils.BUTTON_MARGIN * DisplaySettings.get_size_by_key()[
                 1]))))
        pg.draw.rect(self.display, self.btn_theme.color, self.btn_theme.get_rect(), 0)
        self.display.blit(self.btn_theme.get_text(), self.btn_theme.get_text_rect())
        pos += 1
        self.btn_language.set_custom_coordinates(
            (int(x + self.btn_language.get_rect().width * .5),
             int(y - pos * (self.btn_language.get_rect().height + gui_utils.BUTTON_MARGIN *
                            DisplaySettings.get_size_by_key()[1]))))
        pg.draw.rect(self.display, self.btn_language.color, self.btn_language.get_rect(), 0)
        self.display.blit(self.btn_language.get_text(), self.btn_language.get_text_rect())
        pos += 1
        self.btn_display.set_custom_coordinates(
            (int(x + self.btn_display.get_rect().width * .5),
             int(y - pos * (self.btn_display.get_rect().height + gui_utils.BUTTON_MARGIN *
                            DisplaySettings.get_size_by_key()[1]))))
        pg.draw.rect(self.display, self.btn_display.color, self.btn_display.get_rect(), 0)
        self.display.blit(self.btn_display.get_text(), self.btn_display.get_text_rect())

    def check_events(self, event, board):
        super().check_events(event, board)
        if self.frm_theme.visible:
            self.frm_theme.check_form_events(event)
        elif self.frm_lang.visible:
            self.frm_lang.check_form_events(event)
        elif self.frm_display.visible:
            self.frm_display.check_form_events(event)
        if event.type == MOUSEBUTTONDOWN:
            self.check_button_press(board, pg.mouse.get_pos())

    def reset_forms(self):
        self.frm_theme.visible = False
        self.frm_lang.visible = False
        self.frm_display.visible = False

    def check_button_hover(self):
        # BUTTON HOVERING
        if self.btn_theme.is_hovered(pg.mouse.get_pos()):
            self.btn_theme.color = Themes.DEFAULT_THEME.get("selection_background")
        else:
            self.btn_theme.color = Themes.DEFAULT_THEME.get("front_screen")
        if self.btn_language.is_hovered(pg.mouse.get_pos()):
            self.btn_language.color = Themes.DEFAULT_THEME.get("selection_background")
        else:
            self.btn_language.color = Themes.DEFAULT_THEME.get("front_screen")
        if self.btn_back.is_hovered(pg.mouse.get_pos()):
            self.btn_back.color = Themes.DEFAULT_THEME.get("selection_background")
        else:
            self.btn_back.color = Themes.DEFAULT_THEME.get("front_screen")
        if self.btn_display.is_hovered(pg.mouse.get_pos()):
            self.btn_display.color = Themes.DEFAULT_THEME.get("selection_background")
        else:
            self.btn_display.color = Themes.DEFAULT_THEME.get("front_screen")

    def check_button_press(self, board, pos):
        if self.btn_theme.get_rect().collidepoint(pos):
            if self.frm_theme.visible:
                self.reset_forms()
            else:
                self.reset_forms()
                self.frm_theme.visible = True
            self.btn_theme.on_click(board)
        elif self.btn_back.get_rect().collidepoint(pos):
            self.btn_back.on_click(board)
        elif self.btn_language.get_rect().collidepoint(pos):
            if self.frm_lang.visible:
                self.reset_forms()
            else:
                self.reset_forms()
                self.frm_lang.visible = True
            self.btn_language.on_click(board)
        elif self.btn_display.get_rect().collidepoint(pos):
            if self.frm_display.visible:
                self.reset_forms()
            else:
                self.reset_forms()
                self.frm_display.visible = True
            self.btn_display.on_click(board)
