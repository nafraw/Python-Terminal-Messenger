# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:46:14 2021

@author: Ping-Keng Jao (pingkeng.jao@gmail.com)
"""
# Idea of this file:
#   defines frequently used warn and error message function to highlight texts
#   add personal styles of highlighting messages if desired

# Some related reference below
# ref: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
# ref: note: the best answer did not work

from termcolor import colored, COLORS, HIGHLIGHTS, ATTRIBUTES

class Messenger:    
    WARNING_TEXT = None
    WARNING_BACK = 'on_magenta'
    WARNING_STYLE = None # note style must be a list    
    ERROR_TEXT = None
    ERROR_BACK = 'on_red'
    ERROR_STYLE = None
    #ENDC = '\x1b[0m'
    
    def __init__(self):
        self.reset_default_color()

    def show_available_text_colors():
        print(COLORS.keys())

    def show_available_background_colors():
        print(HIGHLIGHTS.keys())
    
    def show_available_styles():
        print(ATTRIBUTES.keys())
    
    def set_format(name_of_format: str, color=None, back_color=None, style=None):        
        if color:
            if color not in COLORS:
                Messenger.error(f"{color} doesn't exist, please call Messenger.show_available_text_colors() for a supported list")
            exec(f"Messenger.{name_of_format}_TEXT='{color}'")
        else:
            exec(f"Messenger.{name_of_format}_TEXT=None")
        if back_color:
            if back_color not in HIGHLIGHTS:
                Messenger.error(f"{back_color} doesn't exist, please call Messenger.show_available_back_colors() for a supported list")
            exec(f"Messenger.{name_of_format}_BACK='{back_color}'")
        else:
            exec(f"Messenger.{name_of_format}_BACK=None")        
        if style:
            if not isinstance(style, list):
                Messenger.error("The style argument must be a list")
            for s in style:
                if s not in ATTRIBUTES:
                    Messenger.error(f"{s} doesn't exist, please call Messenger.show_available_styles() for a supported list")
            exec(f"Messenger.{name_of_format}_STYLE={style}")
        else:
            exec(f"Messenger.{name_of_format}_STYLE=None")
        
    
    def reset_default_color():
        Messenger.WARNING_TEXT = None
        Messenger.WARNING_BACK = 'on_magenta'
        Messenger.WARNING_STYLE = None # note style must be a list    
        Messenger.ERROR_TEXT = None
        Messenger.ERROR_BACK = 'on_red'
        Messenger.ERROR_STYLE = None
    
    def custom_msg(name_of_format: str, msg: str, show=True):
        msg = eval(f"colored(msg, color=Messenger.{name_of_format}_TEXT, on_color=Messenger.{name_of_format}_BACK, attrs=Messenger.{name_of_format}_STYLE)")
        if show: print(msg)
        return msg
        
    
    def error(msg: str, show=True) -> str:
        msg = colored(msg, color=Messenger.ERROR_TEXT, on_color=Messenger.ERROR_BACK, attrs=Messenger.ERROR_STYLE)
        if show: print(msg)        
        return msg    
    
    def warn(msg: str, show=True) -> str:
        msg = colored(msg, color=Messenger.WARNING_TEXT, on_color=Messenger.WARNING_BACK, attrs=Messenger.WARNING_STYLE)
        if show: print(msg)        
        return msg
    
    
if __name__ == '__main__':        
    Messenger.warn('warn')
    Messenger.error('error')
    a = 3
    msg = f"{a}+b"
    Messenger.set_format('format_1', color='green', back_color='on_red', style=['bold'])
    Messenger.custom_msg('format_1', msg)
    Messenger.set_format('WARNING', color='green', back_color='on_red', style=['bold'])
    Messenger.warn(msg)
    Messenger.reset_default_color()
    print('reset warning message color')
    Messenger.warn(msg)
    Messenger.set_format('format_1', color='green', back_color='on_red', style=['test']) # output error message due to wrong input
    Messenger.set_format('format_1', color='green', back_color='on_yes', style=None) # output error message due to wrong input