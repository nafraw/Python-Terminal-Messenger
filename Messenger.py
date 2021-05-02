# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:46:14 2021

@author: Ping-Keng Jao (pingkeng.jao@gmail.com)
"""
# Purpose of this file:
#   defines frequently used warn and error message functions to highlight texts
#   add personal formats of highlighting messages if desired

# Some related reference below
# ref: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
# ref: note: the best answer did not work

from termcolor import colored, COLORS, HIGHLIGHTS, ATTRIBUTES

class Messenger:
    ''' The following three variables are together refered as format here '''
    TEXT_COLOR = {'WARN': None, 'ERROR': None}
    BACK_COLOR = {'WARN': 'on_magenta', 'ERROR': 'on_red'}
    STYLE = {'WARN': None, 'ERROR': None}
    
    def __init__(self):
        self.reset_default_color()
    ''' Functions to Print colored texts '''
    def custom_format(name_of_format: str, msg: str, show=True):
        msg = colored(msg, color=Messenger.TEXT_COLOR[name_of_format], on_color=Messenger.BACK_COLOR[name_of_format], attrs=Messenger.STYLE[name_of_format])
        if show: print(msg)
        return msg        
    
    def error(msg: str, show=True) -> str:
        return Messenger.custom_format('ERROR', msg, show)
    
    def warn(msg: str, show=True) -> str:
        return Messenger.custom_format('WARN', msg, show)
    
    ''' Functions to Print supported colors and styles '''
    def show_available_text_colors():
        print(COLORS.keys())

    def show_available_background_colors():
        print(HIGHLIGHTS.keys())
    
    def show_available_styles():
        print(ATTRIBUTES.keys())
    
    ''' Functions to Change formats '''    
    def set_format(name_of_format: str, color=None, back_color=None, style=None):        
        if color:
            if color not in COLORS:
                Messenger.error(f"{color} doesn't exist, please call Messenger.show_available_text_colors() for a supported list")
            Messenger.TEXT_COLOR[name_of_format] = color
        else:
            Messenger.TEXT_COLOR[name_of_format] = None
        if back_color:
            if back_color not in HIGHLIGHTS:
                Messenger.error(f"{back_color} doesn't exist, please call Messenger.show_available_back_colors() for a supported list")
            Messenger.BACK_COLOR[name_of_format] = back_color
        else:
            Messenger.BACK_COLOR[name_of_format] = None
        if style:
            if not isinstance(style, list):
                Messenger.error("The style argument must be a list")
            for s in style:
                if s not in ATTRIBUTES:
                    Messenger.error(f"{s} doesn't exist, please call Messenger.show_available_styles() for a supported list")
            Messenger.STYLE[name_of_format] = style
        else:
            Messenger.STYLE[name_of_format] = None
        
    def reset_default_color(): # only reset default colors of WARN and ERROR
        Messenger.TEXT_COLOR['WARN'] = None
        Messenger.BACK_COLOR['WARN'] = 'on_magenta'
        Messenger.STYLE['WARN'] = None
        Messenger.TEXT_COLOR['ERROR'] = None
        Messenger.BACK_COLOR['ERROR'] = 'on_red'
        Messenger.STYLE['ERROR'] = None
    
    def reset_default_format(): # remove all personalized formats
        Messenger.TEXT_COLOR = {'WARN': None, 'ERROR': None}
        Messenger.BACK_COLOR = {'WARN': 'on_magenta', 'ERROR': 'on_red'}
        Messenger.STYLE = {'WARN': None, 'ERROR': None}
    
    
    
if __name__ == '__main__':
    Messenger.warn('warn')
    Messenger.error('error')
    a = 3
    msg = f"{a}+b"
    Messenger.set_format('format_1', color='green', back_color='on_red', style=['bold'])
    Messenger.custom_format('format_1', msg)
    Messenger.set_format('WARNING', color='green', back_color='on_red', style=['bold'])
    Messenger.warn(msg)
    Messenger.reset_default_color()
    print('reset warning message color')
    Messenger.warn(msg)
    Messenger.set_format('format_1', color='green', back_color='on_red', style=['test']) # output error message due to wrong input
    Messenger.set_format('format_1', color='green', back_color='on_yes', style=None) # output error message due to wrong input