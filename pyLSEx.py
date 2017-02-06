# -*- coding: utf-8 -*-
"""
pyLSEX: Lindenmayer System Explorer for python 2.7 is designed to 
generate and/or modify Lindenmayer systems (grammars). 

In the main GUI you will have two choices (via two buttons):

Lindenmayer Sytem Generator
    Using the Generator you can generate predefined Lindenmayer systems 
    (e.g. Fibonacci) or you can define your own rules to create grammars. 

Lindenmayer System Modifier
    Using the Modifier you can change and modify existing L-systems, by 
    building rules to iteratively replace chains of n characters of the 
    system with chains of m other ones. 
     
See detailed description about the usage and the parameters in the 
User Manual or by pressing the help button.

Dependencies:

    For the usage of pyLSEx you need to have Python 2.7 installed. 
    Additionally the following python packages need to be installed:	
		wx
		datetime
		pickle


For help and support feel free to contact: l-s-ex@gmx.co.uk

Version 1.0 by Michael Lindner 
University of Reading, 2017
Center for Integrative Neuroscience and Neurodynamics

Copyright (c) 2017, Michael Lindner

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

   * Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
   * Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in
     the documentation and/or other materials provided with the distribution

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

"""

import wx
import wx.lib.agw.aquabutton as AB
import os
import sys
import datetime
import pickle

ver = '1.0'


class LSEX(wx.Frame):
    """ Main GUI """
        
    def __init__(self, *args, **kwargs):
        super(LSEX, self).__init__(*args, **kwargs) 
        self.InitUI()
        
    def InitUI(self):    
        
        guiwidth = 500
        # menubar
        # -----------------------------
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        helpMenu = wx.Menu()
        
        doc = wx.Menu()
        self.LSGhelp = doc.Append(wx.ID_ANY, 'Lindenmayer System Generator')
        self.LSMhelp = doc.Append(wx.ID_ANY, 'Lindenmayer System Modifier')
        
        self.fileitem = fileMenu.Append(wx.ID_EXIT, '&Quit\tCtrl+W', 'Quit application')
        self.helpitem2 = helpMenu.AppendMenu(wx.ID_ANY, '&Documentation', doc)
        self.aboutitem = helpMenu.Append(wx.ID_ANY, '&About', 'About LSEx')
        
        menubar.Append(fileMenu, '&File')
        menubar.Append(helpMenu, '&Help')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, self.fileitem)
        self.Bind(wx.EVT_MENU, self.OnLSGhelp, self.LSGhelp)
        self.Bind(wx.EVT_MENU, self.OnLSMhelp, self.LSMhelp)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.aboutitem)
       
        #pnl = wx.Panel(self)
        pnl = self
        
        # image and text
        # -----------------------------
        
        png1 = wx.StaticBitmap(self, -1, wx.Bitmap("pyLSEx_LOGO.bmp", wx.BITMAP_TYPE_ANY))
        hsizerm1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizerm1.Add(png1, 1, 0, 0)
        hsizerm1.SetItemMinSize(png1, (guiwidth, -1))
        
        textfont2 = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        txt3 = wx.StaticText(self, -1, 'version: '+ver,  style=wx.ALIGN_CENTRE)
        txt3.SetFont(textfont2)
        hsizerm3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizerm3.Add(txt3, 1, 0, 0)
        hsizerm3.SetItemMinSize(txt3, (guiwidth, -1))
        
        txt4 = wx.StaticText(self, -1, 'by Michael Lindner and Doug Saddy',  style=wx.ALIGN_CENTRE)
        txt4.SetFont(textfont2)
        hsizerm4 = wx.BoxSizer(wx.HORIZONTAL)
        hsizerm4.Add(txt4, 1, 0, 0)
        hsizerm4.SetItemMinSize(txt4, (guiwidth, -1))
        
        txt5 = wx.StaticText(self, -1, 'University of Reading',  style=wx.ALIGN_CENTRE)
        txt5.SetFont(textfont2)
        hsizerm5 = wx.BoxSizer(wx.HORIZONTAL)
        hsizerm5.Add(txt5, 1, 0, 0)
        hsizerm5.SetItemMinSize(txt5, (guiwidth, -1))
        
        txt6 = wx.StaticText(self, -1, 'School of Psychology and Clinical Languange Science',  style=wx.ALIGN_CENTRE)
        txt6.SetFont(textfont2)
        hsizerm6 = wx.BoxSizer(wx.HORIZONTAL)
        hsizerm6.Add(txt6, 1, 0, 0)
        hsizerm6.SetItemMinSize(txt6, (guiwidth, -1))
        
        txt7 = wx.StaticText(self, -1, 'Center for Integrative Neuroscience and Neurodynamics',  style = wx.ALIGN_CENTRE)
        txt7.SetFont(textfont2)
        hsizerm7 = wx.BoxSizer(wx.HORIZONTAL)
        hsizerm7.Add(txt7, 1, 0, 0)
        hsizerm7.SetItemMinSize(txt7, (guiwidth, -1))
        
        
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizerm1, 0, wx.EXPAND| wx.ALL, 10)
        vsizer1.Add(hsizerm3, 0, wx.EXPAND| wx.ALL, 5)
        vsizer1.Add(hsizerm4, 0, wx.EXPAND| wx.ALL, 10)
        vsizer1.Add(hsizerm5, 0, wx.EXPAND| wx.ALL, 5)
        vsizer1.Add(hsizerm6, 0, wx.EXPAND| wx.ALL, 5)
        vsizer1.Add(hsizerm7, 0, wx.EXPAND| wx.ALL, 5)
        self.SetSizer(vsizer1)
        
        # lines
        # -----------------------------
        wx.StaticLine(pnl, pos = (25, 300), size = (430, 1))
        wx.StaticLine(pnl, pos = (25, 500), size = (430, 1))
        wx.StaticLine(pnl, pos = (25, 700), size = (430, 1))
        
        # buttons
        # -----------------------------
        buttonfont = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        btnSize = ((470, 150))
        self.genbtn = AB.AquaButton(pnl, 
                                    label = 'Lindenmayer System Generator', 
                                    pos = (10, 325), size = btnSize)
        self.genbtn.SetForegroundColour("black")
        self.Bind(wx.EVT_BUTTON, self.OnLSGbtn, self.genbtn)
        
        self.modbtn = AB.AquaButton(pnl, 
                                    label = 'Lindenmayer System Modifier', 
                                    pos = (10, 525), size = btnSize)
        self.modbtn.SetForegroundColour("black")
        self.Bind(wx.EVT_BUTTON, self.OnLSMbtn, self.modbtn)
        
        
        self.closebtn = wx.Button(pnl, label = 'Quit', pos = (350, 710))
        self.Bind(wx.EVT_BUTTON, self.OnQuit, self.closebtn) 
        
        # GUI settings
        # -----------------------------
        self.SetSize((guiwidth, 800))
        self.SetTitle('pyLSEx')
        self.Centre()
        self.Show(True)


    """ Events for menubar. """         
    def OnQuit(self, e):
        self.Close()
        
    def OnAbout(self, e):
        self.new = AboutMsg(parent = None, id = -1)
        self.new.Show()

    def OnLSGhelp(self, e):
        self.new = LSGhelp(parent = None, id = -1)
        self.new.Show()
    
    def OnLSMhelp(self, e):
        self.new = LSMhelp(parent = None, id = -1)
        self.new.Show()
        

    """ Events for buttons """
    def OnLSGbtn(self, e):
        #self.new = LSEXgen(parent = None, id = -1)
        #self.new.Show()
        frame = LSEXgen("Lindenmayer System Generator")
        frame.Show(True)
        return True
    
    def OnLSMbtn(self, e):
        frame = LSEXmod("Lindenmayer System Modifier")
        frame.Show(True)
        return True
    
"""
##############################################################################

    LSEX classes
    
##############################################################################    
"""    
    


class LSEXgen(wx.Frame):
    """ 
    Lindenmayer System Generator GUI
    """
    def __init__(self,title):
        wx.Frame.__init__(self, None, title = title, size = (400, 480))
        wx.Frame.CenterOnScreen(self)
        
        # Rule selection
        # -----------------------------
        self.userdefined = False
        self.samplelist = ["Fibonacci", "Algea", "Thue-Morse", "Feigenbaum", "Cantor dust", "Pythagoras tree", "Koch curve", "Sierpinksi triangle", "User defined"]
        self.rulelist = [[["0", "1"], ["1", "10"]], 
                  [["0", "1"], ["01", "0"]], 
                  [["0", "1"], ["01", "10"]], 
                  [["0", "1"], ["11", "01"]], 
                  [["0", "1"], ["010", "111"]], 
                  [["0", "1"], ["1[0]1", "11"]], 
                  [["1"], ["1+1-1-1+1"]], 
                  [["0", "1"], ["+1-0-1+", "-0+1+0-"]], 
                  [["", ""], ["", ""]]]
        
        cb = wx.ComboBox(self, -1, "Select System", 
                         (-1, -1), (-1, -1), self.samplelist, wx.CB_DROPDOWN)
        self.cb = cb
        self.cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        
        self.r11 = ""#self.rulelist[1][0][0]
        self.r12 = ""#self.rulelist[1][1][0]
        self.r21 = ""#self.rulelist[1][0][1]
        self.r22 = ""#self.rulelist[1][1][1]
        
        self.rule_field1_1 = wx.StaticText(self, -1, self.r11, 
                                           (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.rule_field1_2 = wx.StaticText(self, -1, self.r12, 
                                           (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.rule_field2_1 = wx.StaticText(self, -1, self.r21, 
                                           (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.rule_field2_2 = wx.StaticText(self, -1, self.r22, 
                                           (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        
        self.rule_field1_1.SetForegroundColour((100, 100, 100))
        self.rule_field1_2.SetForegroundColour((100, 100, 100))
        self.rule_field2_1.SetForegroundColour((100, 100, 100))
        self.rule_field2_2.SetForegroundColour((100, 100, 100))
        
        # texts
        # -----------------------------
        stattext1 = wx.StaticText(self, -1, 'Select Lindenmayer system:', 
                                  (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext2 = wx.StaticText(self, -1, 'Start value:', 
                                  (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext3 = wx.StaticText(self, -1, 'Number of recursions :', 
                                  (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext4 = wx.StaticText(self, -1, 'Specify output folder :', 
                                  (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext5 = wx.StaticText(self, -1, 'Output file prefix :', 
                                  (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext6 = wx.StaticText(self, -1, '                              ', 
                                  (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext7 = wx.StaticText(self, -1, 'Text (.txt) :', 
                                  (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext8 = wx.StaticText(self, -1, 'Select output type : ', 
                                  (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext9 = wx.StaticText(self, -1, 'Pickle (.dat) :', 
                                  (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext01 = wx.StaticText(self, -1, '      -->  ', 
                                   (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext02 = wx.StaticText(self, -1, '      -->  ', 
                                   (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattextx = wx.StaticText(self, -1, 'Lindenmayer generator v0.94 by Michael Lindner and Doug Saddy, University of Reading', 
                                  (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        font = wx.Font(8, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        stattextx.SetFont(font)
        stattextx.SetForegroundColour((100, 100, 100))
        
        self.outpath = '';
        
        self.txt_field1 = wx.TextCtrl(self, -1, '0', 
                                      (-1, -1), (-1, -1))
        self.txt_field2 = wx.TextCtrl(self, -1, '', 
                                      (-1, -1), (-1, -1))
        self.txt_field3 = wx.TextCtrl(self, -1, self.outpath, 
                                      (-1, -1), (-1, -1))
        self.txt_field4 = wx.TextCtrl(self, -1, 'output', 
                                      (-1, -1), (-1, -1))

        # buttons
        # -----------------------------
        self.button1 = wx.Button(self, wx.NewId(), '&Browse', 
                                 (-1, -1), wx.DefaultSize)
        self.button2 = wx.Button(self, wx.NewId(), '&Generate grammar', 
                                 (-1, -1), wx.DefaultSize)
        
        self.button1.Bind(wx.EVT_BUTTON, self.OnBrowse)        
        self.button2.Bind(wx.EVT_BUTTON, self.OnGenerate)        
        
        # checkboxes
        # -----------------------------
        self.checkbox1 = wx.CheckBox(self, wx.NewId(), '')
        self.checkbox1.SetValue(True)
        self.checkbox2 = wx.CheckBox(self, wx.NewId(), '')
        self.checkbox2.SetValue(True)
        
        # lines
        # -----------------------------
        staline1 = wx.StaticLine(self, wx.NewId(), 
                                 (-1, -1), (-1, 2), wx.LI_HORIZONTAL)
        staline2 = wx.StaticLine(self, wx.NewId(), 
                                 (-1, -1), (-1, 2), wx.LI_HORIZONTAL)
        staline3 = wx.StaticLine(self, wx.NewId(),
                                 (-1, -1), (-1, 2), wx.LI_HORIZONTAL)
        
        # horizontal box sizers
        # -----------------------------
        b = 5
        hsizer1a = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1a.Add(stattext1, wx.EXPAND | wx.ALL, wx.RIGHT, b)
        hsizer1a.SetItemMinSize(stattext1, (300, -1))

        hsizer1b = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1b.Add(cb, wx.EXPAND | wx.ALL, wx.RIGHT, b)

        hsizer1c = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1c.Add(self.rule_field1_1, 1, wx.LEFT, 40)
        hsizer1c.Add(stattext01, wx.CENTER, 40)
        hsizer1c.Add(self.rule_field1_2, 1, wx.RIGHT, 40)
        
        hsizer1d = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1d.Add(self.rule_field2_1, 1, wx.LEFT, 40)
        hsizer1d.Add(stattext02, wx.CENTRE, 50)
        hsizer1d.Add(self.rule_field2_2, 1, wx.RIGHT, 40)
                
        hsizer2a = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2a.Add(stattext2, 0, wx.LEFT, 20)
        hsizer2a.SetItemMinSize(stattext2, (200, -1))
        hsizer2a.Add(self.txt_field1, 1, wx.RIGHT, 50)
        hsizer2a.SetItemMinSize(self.txt_field1, (100, -1))
        
        hsizer2b = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2b.Add(stattext3, 0, wx.LEFT, 20)
        hsizer2b.SetItemMinSize(stattext3, (200, -1))
        hsizer2b.Add(self.txt_field2, 1, wx.RIGHT, 50)
        hsizer2b.SetItemMinSize(self.txt_field2, (100, -1))
                
        hsizer3a = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3a.Add(stattext4, 0, wx.RIGHT, b)
        hsizer3a.SetItemMinSize(stattext4, (300, -1))

        hsizer3b = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3b.Add(self.txt_field3, 1, wx.RIGHT, b)
        hsizer3b.SetItemMinSize(self.txt_field3, (40, -1))
        hsizer3b.Add(self.button1, 0)
        
        hsizer3c = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3c.Add(stattext5, 0, wx.RIGHT, b)
        hsizer3c.SetItemMinSize(stattext5, (150, -1))
        hsizer3c.Add(self.txt_field4, 1, wx.GROW, b)
        hsizer3c.SetItemMinSize(self.txt_field4, (200, -1))
        
        hsizer3e = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3e.Add(stattext8, 0, wx.RIGHT, b)
        hsizer3e.SetItemMinSize(stattext8, (200, -1))
        hsizer3e.Add(self.checkbox2, 0, wx.RIGHT, b)
        hsizer3e.Add(stattext9, 0, wx.RIGHT, b)
        hsizer3e.SetItemMinSize(stattext9, (100, -1))
               
        hsizer3d = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3d.Add(stattext6, 0, wx.RIGHT, b)
        hsizer3d.SetItemMinSize(stattext6, (200, -1))
        hsizer3d.Add(self.checkbox1, 0, wx.RIGHT, b)
        hsizer3d.Add(stattext7, 0, wx.RIGHT, b)
        hsizer3d.SetItemMinSize(stattext7, (100, -1))
        
        hsizer4 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer4.Add(self.button2, 0, wx.RIGHT, 10)
        hsizer4.SetItemMinSize(self.button2, (400, 50))
        
        hsizer5 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer5.Add(stattextx, 0, wx.RIGHT, b)
        
        # vertical box sizers
        # -----------------------------
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizer1a, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer1b, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer1c, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer1d, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(staline1, 0, wx.EXPAND| wx.ALL, b)
        
        vsizer1.Add(hsizer2a, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer2b, 0, wx.EXPAND | wx.ALL, b)
        
        vsizer1.Add(staline2, 0, wx.EXPAND| wx.ALL, b)
        
        vsizer1.Add(hsizer3a, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer3b, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer3c, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer3e, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer3d, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(staline3, 0, wx.EXPAND | wx.ALL, b)
        
        vsizer1.Add(hsizer4, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer5, 0, wx.EXPAND| wx.ALL, b)
        
        self.SetSizer(vsizer1)
        
        
    def SetRule(self, rule):
        self.rule = rule
        print(self.rule)
    
    
    def OnClickExit(self, event):
        sys.exit()
        

    def OnSelect(self, event):
        item = event.GetSelection()
        self.gram = item
        
        if item == 8:
            """ User defined """
            self.r11 = " "
            self.r12 = " "
            self.r21 = " "
            self.r22 = " "
            
            self.userdefined=True
            
            
            dlg = TextEntryDialog(None, 'Input', 'How many rules (different replacements) do you want to define?')
            dlg.Center()
            dlg.SetValue('2')
            if dlg.ShowModal() == wx.ID_OK:
                self.replacements = int(dlg.GetValue())
            dlg.Destroy()
            
            Ruleframe = RuleDialog(self, 'Define Rules', self.replacements)
            Ruleframe.Show()
            Ruleframe.Center()
            
        else:
            """ Predefined rules """
            self.r11 = self.rulelist[item][0][0]
            self.r12 = self.rulelist[item][1][0]
            self.r21 = self.rulelist[item][0][1]
            self.r22 = self.rulelist[item][1][1]
            
            self.type='Classic'
        
            self.rule_field1_1.SetLabel(self.r11) 
            self.rule_field1_2.SetLabel(self.r12) 
            self.rule_field2_1.SetLabel(self.r21) 
            self.rule_field2_2.SetLabel(self.r22) 
            
        
    def OnBrowse(self, event):
        dlg = wx.DirDialog(self, "Choose an output directory:", 
                           style = wx.DD_DEFAULT_STYLE
                           )
        if dlg.ShowModal() == wx.ID_OK:
            self.outpath = dlg.GetPath()
            
        dlg.Destroy()
        self.txt_field3.SetValue(self.outpath)
        
        
    def OnGenerate(self, event):
        cfg = type('', (), {})()
        
        if self.userdefined == True:
            cfg.rule = self.rule
        else:
            cfg.rule = self.rulelist[self.gram]
        
        rl=[]
        for ii in range(0, len(cfg.rule[0])):
            rl.append(int(len(cfg.rule[0][ii])))
            
        if min(rl) != max(rl):
            # error message
            wx.MessageBox("""All replacement rules must have the same length!""",
                          "INPUT ERROR", wx.OK)
        
        else:
            cfg.start = str(self.txt_field1.GetValue())
            cfg.recs = int(self.txt_field2.GetValue())
            cfg.outputpath = str(self.txt_field3.GetValue())
            cfg.prefix = str(self.txt_field4.GetValue())
            cfg.txtout = self.checkbox1.GetValue()
            cfg.pickout = self.checkbox2.GetValue()
        
            L = LSEXfunctions()
            
            if max(rl) == 1:
                L.Generate_classic(cfg)
            elif max(rl) > 1:
            
                Typedlg = TypeDialog(self, 'Replacement type', cfg)
                Typedlg.Center()
                Typedlg.Show()
        
        
    def OnQuit(self, e):
        self.Close()



class LSEXmod(wx.Frame):
    """ Lindenmayer System Modifier GUI """
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, pos=(200, 200), size=(360, 400))
        
        self.loadinfo='File: not loaded'
        self.stattext1 = wx.StaticText(self, -1, self.loadinfo, (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.stattext1.SetForegroundColour((255,0,0))
        self.loadinfo='Rule not specified'
        self.stattext1b = wx.StaticText(self, -1, self.loadinfo, (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.stattext1b.SetForegroundColour((255,0,0))
        stattext2 = wx.StaticText(self, -1, 'Type of Replacement :', (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext3 = wx.StaticText(self, -1, 'Number of recursions :', (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext4 = wx.StaticText(self, -1, 'Specify output folder :', (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext5 = wx.StaticText(self, -1, 'Output file prefix :', (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext6 = wx.StaticText(self, -1, '                              ', (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext7 = wx.StaticText(self, -1, 'Text (.txt) :', (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext8 = wx.StaticText(self, -1, 'Select output type : ', (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattext9 = wx.StaticText(self, -1, 'Pickle (.dat) :', (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        stattextx = wx.StaticText(self, -1, 'Lindenmayer generator v0.94 by Michael Lindner and Doug Saddy, University of Reading', (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        font = wx.Font(8, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        stattextx.SetFont(font)
        stattextx.SetForegroundColour((100,100,100))
        
        self.outpath='';
        
        self.replacelist = ["segmentwise", "continuous", "continuous (skip last n)"]
        
        cb = wx.ComboBox(self, -1, "Select", 
                         (-1, -1), (-1, -1), self.replacelist, wx.CB_DROPDOWN)
        self.cb = cb
        self.cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)
       
       
        self.txt_field2 = wx.TextCtrl(self, -1, '', (-1, -1), (-1, -1))
        self.txt_field3 = wx.TextCtrl(self, -1, self.outpath, (-1, -1), (-1, -1))
        self.txt_field4 = wx.TextCtrl(self, -1, 'mod_output', (-1, -1), (-1, -1))

        self.button1 = wx.Button(self, wx.NewId(), '&Load L-system (grammar) from .dat file', (-1, -1), wx.DefaultSize)
        self.button2 = wx.Button(self, wx.NewId(), '&Define rules', (-1, -1), wx.DefaultSize)
        self.button3 = wx.Button(self, wx.NewId(), '&Browse', (-1, -1), wx.DefaultSize)
        self.button4 = wx.Button(self, wx.NewId(), '&Generate grammar', (-1, -1), wx.DefaultSize)
        
        self.button1.Bind(wx.EVT_BUTTON, self.OnLoad)        
        self.button2.Bind(wx.EVT_BUTTON, self.OnDefine)        
        self.button3.Bind(wx.EVT_BUTTON, self.OnBrowse)        
        self.button4.Bind(wx.EVT_BUTTON, self.OnGenerate)        
        
        self.checkbox1 = wx.CheckBox(self, wx.NewId(), '')
        self.checkbox1.SetValue(True)
        self.checkbox2 = wx.CheckBox(self, wx.NewId(), '')
        self.checkbox2.SetValue(False)
        
        staline1 = wx.StaticLine(self, wx.NewId(), (-1, -1), (-1, 2), wx.LI_HORIZONTAL)
        staline2 = wx.StaticLine(self, wx.NewId(), (-1, -1), (-1, 2), wx.LI_HORIZONTAL)
        staline3 = wx.StaticLine(self, wx.NewId(), (-1, -1), (-1, 2), wx.LI_HORIZONTAL)
        
        b = 5
        hsizer1a = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1a.Add(self.button1, 0, wx.RIGHT, 10)
        hsizer1a.SetItemMinSize(self.button1, (440, 50))
     
        hsizer1b = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1b.Add(self.stattext1, wx.EXPAND | wx.ALL, wx.RIGHT, b)

        hsizer1c = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1c.Add(self.button2, 0, wx.RIGHT, 10)
        hsizer1c.SetItemMinSize(self.button2, (440, 50))
     
        hsizer1b2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1b2.Add(self.stattext1b, wx.EXPAND | wx.ALL, wx.RIGHT, b)

        hsizer1d = wx.BoxSizer(wx.HORIZONTAL)
        
        hsizer2a = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2a.Add(stattext2, 0, wx.LEFT, 20)
        hsizer2a.SetItemMinSize(stattext2, (200, -1))
        hsizer2a.Add(self.cb, 1, wx.RIGHT, 50)
        
        hsizer2b = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2b.Add(stattext3, 0, wx.LEFT, 20)
        hsizer2b.SetItemMinSize(stattext3, (200, -1))
        hsizer2b.Add(self.txt_field2, 1, wx.RIGHT, 50)
        hsizer2b.SetItemMinSize(self.txt_field2, (100, -1))
        
        
        hsizer3a = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3a.Add(stattext4, 0, wx.RIGHT, b)
        hsizer3a.SetItemMinSize(stattext4, (200, -1))

        hsizer3b = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3b.Add(self.txt_field3, 1, wx.RIGHT, b)
        hsizer3b.SetItemMinSize(self.txt_field3, (40, -1))
        hsizer3b.Add(self.button3, 0)
        
        hsizer3c = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3c.Add(stattext5, 0, wx.RIGHT, b)
        hsizer3c.SetItemMinSize(stattext5, (150, -1))
        hsizer3c.Add(self.txt_field4, 1, wx.GROW, b)
        hsizer3c.SetItemMinSize(self.txt_field4, (200, -1))
        
        
        hsizer3e = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3e.Add(stattext8, 0, wx.RIGHT, b)
        hsizer3e.SetItemMinSize(stattext8, (200, -1))
        hsizer3e.Add(self.checkbox2, 0, wx.RIGHT, b)
        hsizer3e.Add(stattext9, 0, wx.RIGHT, b)
        hsizer3e.SetItemMinSize(stattext9, (100, -1))
        
        hsizer3d = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3d.Add(stattext6, 0, wx.RIGHT, b)
        hsizer3d.SetItemMinSize(stattext6, (200, -1))
        hsizer3d.Add(self.checkbox1, 0, wx.RIGHT, b)
        hsizer3d.Add(stattext7, 0, wx.RIGHT, b)
        hsizer3d.SetItemMinSize(stattext7, (100, -1))
        
        hsizer4 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer4.Add(self.button4, 0, wx.RIGHT, 10)
        hsizer4.SetItemMinSize(self.button4, (440, 50))
        
        hsizer5 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer5.Add(stattextx, 0, wx.RIGHT, b)
        
        
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizer1a, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer1b, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer1c, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer1b2, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer1d, 0, wx.EXPAND | wx.ALL, b)
        
        vsizer1.Add(staline1, 0, wx.EXPAND| wx.ALL, b)
        
        vsizer1.Add(hsizer2a, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer2b, 0, wx.EXPAND | wx.ALL, b)
        
        vsizer1.Add(staline2, 0, wx.EXPAND | wx.ALL, b)
        
        vsizer1.Add(hsizer3a, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer3b, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer3c, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer3e, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer3d, 0, wx.EXPAND | wx.ALL, b)
        
        vsizer1.Add(staline3, 0, wx.EXPAND | wx.ALL, b)
        
        vsizer1.Add(hsizer4, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer5, 0, wx.EXPAND | wx.ALL, b)
        
        self.SetSizer(vsizer1)
        vsizer1.Fit(self)

    
    def SetRule(self, rule):
        self.rule = rule
        print(self.rule)
    
    def Settext1(self, loadname):
        newlabel='File loaded: ' +loadname
        self.stattext1.SetLabel(newlabel)
        self.stattext1.SetForegroundColour((0,255,0))
    
    def Settext2(self):
        self.stattext1b.SetLabel('Rule defined ')
        self.stattext1b.SetForegroundColour((0,255,0))
    
    def OnClickExit(self, event):
        sys.exit()
        
    def OnLoad(self, event):    
        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", "*.dat", wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            loadname = dialog.GetPath()
            G = pickle.load( open(loadname , "rb" ) )
        
        dlg = TextEntryDialog(None, 'Input', 'Recursion of L-System you want to use? max:')
        dlg.Center()
        dlg.SetValue(str(len(G)))
        if dlg.ShowModal() == wx.ID_OK:
            Grec = int(dlg.GetValue())
        dlg.Destroy()
        
        self.Grammar = G[Grec-1]
        
        self.Settext1(loadname)
        

    def OnDefine(self, event):    
        self.userdefined=True
            
        dlg = TextEntryDialog(None, 'Input', 'How many rules (different replacements) do you want to define?')
        dlg.Center()
        dlg.SetValue('2')
        if dlg.ShowModal() == wx.ID_OK:
            self.replacements = int(dlg.GetValue())
        dlg.Destroy()
            
            
        Ruleframe = RuleDialog(self, 'Define Rules', self.replacements)
        Ruleframe.Show()
        Ruleframe.Center()
            
        self.Settext2()
        

    def OnSelect(self, event):
        item = event.GetSelection()
        
        self.cfg = []
        self.replace = []
        
        if item == 0:
            self.replace = 'segm'
        elif item == 1:
            self.replace = 'cont'
        elif item == 2:
            self.replace = 'cont_n'
       
       
    def OnBrowse(self, event):
        dlg = wx.DirDialog(self, "Choose an output directory:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            self.outpath = dlg.GetPath()
            
        dlg.Destroy()
        self.txt_field3.SetValue(self.outpath)
        
    def OnGenerate(self, event):
        cfg = type('', (), {})()
        
        cfg.rule = self.rule
            
        rl=[]
        for ii in range(0, len(cfg.rule[0])):
            rl.append(int(len(cfg.rule[0][ii])))
            
        if min(rl) != max(rl):
            # error message
            wx.MessageBox("""All replacement rules must have the same length!""",
                          "INPUT ERROR", wx.OK)
        
        else:
            cfg.start = self.Grammar
            cfg.recs = int(self.txt_field2.GetValue())
            cfg.outputpath = str(self.txt_field3.GetValue())
            cfg.prefix = str(self.txt_field4.GetValue())
            cfg.txtout = self.checkbox1.GetValue()
            cfg.pickout = self.checkbox2.GetValue()
            cfg.replacetype = self.replace
            
            print(cfg.replacetype)
            
            L = LSEXfunctions()
            
            if max(rl) == 1:
                L.Generate_classic(cfg)
            elif max(rl) > 1:
                L.Generate_extended(cfg)

        
"""
##############################################################################

    dialog classes
    
##############################################################################    
"""    

class TextEntryDialog(wx.Dialog):
    def __init__(self, parent, title, caption):
        style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        super(TextEntryDialog, self).__init__(parent, -1, title, style=style)
        text = wx.StaticText(self, -1, caption)
        input = wx.TextCtrl(self, -1)
        buttons = self.CreateButtonSizer(wx.OK|wx.CANCEL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, 0, wx.ALL, 5)
        sizer.Add(input, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(buttons, 0, wx.EXPAND|wx.ALL, 5)
        self.SetSizerAndFit(sizer)
        self.input = input
    def SetValue(self, value):
        self.input.SetValue(value)
    def GetValue(self):
        return self.input.GetValue()   
        

class TypeDialog(wx.Frame):
    def __init__(self, parent, title, cfg):
        wx.Frame.__init__(self, parent, -1, title, wx.DefaultPosition, wx.Size(250, 150))
        self.parent = parent
        panel = wx.Panel(self, -1)
        self.cfg = cfg
        self.L = LSEXfunctions()
        
        self.rb1 = wx.RadioButton(panel, -1, 'segmentwise', (10, 10), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(panel, -1, 'continuous', (10, 30))
        self.rb3 = wx.RadioButton(panel, -1, 'continuous (skip last n)', (10, 50))
        self.button1 = wx.Button(panel, wx.NewId(), '&OK',  
                                 (10, 80), wx.DefaultSize)
        self.Bind(wx.EVT_RADIOBUTTON, self.SetVal, id=self.rb1.GetId())
        self.Bind(wx.EVT_RADIOBUTTON, self.SetVal, id=self.rb2.GetId())
        self.Bind(wx.EVT_RADIOBUTTON, self.SetVal, id=self.rb3.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnOK, self.button1)    
        
        self.SetVal(True)

    def SetVal(self, e):
        state1 = str(self.rb1.GetValue())
        state2 = str(self.rb2.GetValue())
        state3 = str(self.rb3.GetValue())
        
        if state1 == 'True':
            self.cfg.replacetype = 'segm'
        elif state2 == 'True':
            self.cfg.replacetype = 'cont'
        elif state3 == 'True':
            self.cfg.replacetype = 'cont_n'
        
        
    def OnOK(self, e):
        cfg = self.cfg
        print(cfg.replacetype)
        
        self.L.Generate_extended(cfg)
        self.OnQuit(self)

    def OnQuit(self, e):
        self.Close()   
        

class RuleDialog(wx.Frame):
    def __init__(self, parent, title, NrRules):
        self.myFrame = wx.Frame.__init__(self, parent, title = title, size = (200, 200))
        self.state = 'Yes'
        self.NrRules = NrRules
        self.parent = parent
                          
        stattext=[None]*NrRules
        
        for ii in range(0, NrRules):
            stattext[ii] = wx.StaticText(self, -1, '               -->  ', 
                                   (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        
        self.rule_field1=[None]*NrRules
        self.rule_field2=[None]*NrRules
        
        for ii in range(0, NrRules):
            self.rule_field1[ii] = wx.TextCtrl(self, -1, '', (-1, -1), (-1, -1))
            self.rule_field2[ii] = wx.TextCtrl(self, -1, '', (-1, -1), (-1, -1))
        
        self.button1 = wx.Button(self, wx.NewId(), '&OK',  
                                 (-1, -1), wx.DefaultSize)
        self.button2 = wx.Button(self, wx.NewId(), '&Save Rules', 
                                 (-1, -1), wx.DefaultSize)
        self.button3 = wx.Button(self, wx.NewId(), '&Quit', 
                                 (-1, -1), wx.DefaultSize)
        
        self.button1.Bind(wx.EVT_BUTTON, self.OnOK) 
        
        self.Bind(wx.EVT_BUTTON, self.OnSaveRule, self.button2) 
        self.Bind(wx.EVT_BUTTON, self.OnQuit, self.button3)         
        
        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        
        for ii in range(0,NrRules):
            
            hsizer = wx.BoxSizer(wx.HORIZONTAL)
            hsizer.Add(self.rule_field1[ii], 1, wx.LEFT, 40)
            hsizer.Add(stattext[ii], 1, wx.CENTRE, 30)
            hsizer.Add(self.rule_field2[ii], 1, wx.RIGHT, 40)
            
            vsizer1.Add(hsizer, 0, wx.EXPAND | wx.ALL, b)
        
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.button1, wx.CENTRE, 50)    
        hsizer.Add(self.button2, wx.CENTRE, 50)    
        hsizer.Add(self.button3, wx.CENTRE, 50)    
        vsizer1.Add(hsizer, 0, wx.EXPAND | wx.ALL, b)
        
        self.SetSizer(vsizer1)

        self.SetAutoLayout(1)
        vsizer1.Fit(self)
        self.Show()
    
         
    def OnOK(self, e):
        rules = [[0 for x in range(self.NrRules)] for y in range(2)] 
        
        for ii in range(0, self.NrRules):
            rules[0][ii] = str(self.rule_field1[ii].GetValue())
            rules[1][ii] = str(self.rule_field2[ii].GetValue())       
        
        self.parent.SetRule(rules)
        
        self.OnQuit(self)
        
        
    def OnSaveRule(self, e):
        rules = [[0 for x in range(self.NrRules)] for y in range(2)] 
        
        for ii in range(0, self.NrRules):
            #print(ii)
            rules[0][ii] = str(self.rule_field1[ii].GetValue())
            rules[1][ii] = str(self.rule_field2[ii].GetValue())       
        
        dt=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = ''.join(["User_defined_rules_", dt, ".txt"])
        
        rulefile = open(filename, 'w')
        for ii in range(0, self.NrRules):
            rulefile.write("%s\n" % ''.join([rules[0][ii],"  -->  ",rules[1][ii]]))
        rulefile.close() 
        

    def OnQuit(self, e):
        self.Close()
        
"""
##############################################################################

    function class
    
##############################################################################    
"""    

class LSEXfunctions():    
    """ Class with main grammar functions"""
    
    def Generate_classic(self, cfg):
        
        Grammar = ["nan"]*(cfg.recs+1)
        Grammar[0] = cfg.start
        
        for rr in range(0, cfg.recs):
            ag = list(Grammar[rr])
            ng = ["nan"]*len(ag)
            for ss in range(0, len(cfg.rule[1])):
                indexes = [i for i, x in enumerate(ag) if x == cfg.rule[0][ss]]
                for ii in indexes:
                    ng[ii] = cfg.rule[1][ss]
            Grammar[rr+1] = ''.join(ng)
            del ag 
            del ng

        Grammar_length = map(len, Grammar)              
        
        if cfg.txtout == True:
            self.Savetextfile(cfg, Grammar, Grammar_length)
        
        if cfg.pickout == True:
            self.Savepicklefile(cfg, Grammar, Grammar_length)
            
            
    def Generate_extended(self, cfg):
        
        Grammar = ["nan"]*(cfg.recs+1)
        Grammar[0] = cfg.start
        
        print( len(cfg.rule[0]))
        print( cfg.rule[0][0])
        print( cfg.rule[1][0])
        
        # #################################################################
        if cfg.replacetype == "segm": # segmentwise replacement
            
            steps=max(len(s) for s in cfg.rule[0])
            
            for rr in range(0, cfg.recs):
    
                ag = Grammar[rr]
                ng = [""]*len(ag) # create empty new grammar
                
                for xx in range(0, len(ag), steps):
        
                    tag = ag[xx:xx+steps]
                    
                    re=1
                    for ii in range(0, len(cfg.rule[0])):
            
                        if  tag == cfg.rule[0][ii]:
                            ng[xx] = cfg.rule[1][ii]
                            re=0
                        elif len(tag) < steps:
                            re=0
            
                    if re == 1:
                        ng[xx]=ag[xx:xx+steps]
    
                Grammar[rr+1] = ''.join(ng)    
            
        
        elif cfg.replacetype == "cont":  # continuous replacement
           
            for rr in range(0, cfg.recs):
    
                ag = Grammar[rr]
                ng = [""]*len(ag) # create empty new grammar
    
                for xx in range(0, len(ag)):
        
                    re=1
                    for ii in range(0, len(cfg.rule[0])):
                        
                        tag = ag[xx:xx+len(cfg.rule[0][ii])]
                        print(len(tag))
                        
                        if  tag == cfg.rule[0][ii]:
                            ng[xx] = cfg.rule[1][ii]
                            re=0
                        elif len(tag) < len(cfg.rule[0]):
                            re=0
                            
                    if re == 1:
                        ng[xx]=ag[xx]
        
                Grammar[rr+1] = ''.join(ng)    

 
        elif cfg.replacetype == "cont_n":   # continuous replacement (skip last n)
            
            
            for rr in range(0, cfg.recs):
    
                ag = Grammar[rr]
                ng = [""]*len(ag) 
    
                xxflag = 0
                xx = -1
                while xxflag == 0:
                    xx = xx + 1
                    if xx > len(ag) - 1:
                        break
        
                    tag = ag[xx:xx+len(cfg.rule[0][0])]
                    re=1
                    
                    for ii in range(0, len(cfg.rule[0])):
            
                        if  tag == cfg.rule[0][ii]:
                            ng[xx] = cfg.rule[1][ii]
                            xx = xx + len(cfg.rule[0][0])-1
                            re=0
                        elif len(tag) < len(cfg.rule[0]):
                            re=0
                            
                    if re == 1:
                        ng[xx]=ag[xx]
        
                Grammar[rr+1] = ''.join(ng)    
        
        # #################################################################
        
        Grammar_length = map(len, Grammar) 
        
        if cfg.txtout == True:
            self.Savetextfile(cfg, Grammar, Grammar_length)
        
        if cfg.pickout == True:
            self.Savepicklefile(cfg, Grammar, Grammar_length)



    def Savetextfile(self, cfg, Grammar, Grammar_length):
    
        dt=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
         
        filename1 = ''.join([cfg.outputpath, os.sep, cfg.prefix, "_grammar_", dt, ".txt"])
        filename2 = ''.join([cfg.outputpath, os.sep, cfg.prefix, "_grammar_length_", dt, ".txt"])
        filename3 = ''.join([cfg.outputpath, os.sep, cfg.prefix, "_grammar_rule_", dt, ".txt"])
        
        
        grammarfile = open(filename1, 'w')
        for item in Grammar:
            grammarfile.write("%s\n" % item)
        grammarfile.close()

        lengthfile = open(filename2, 'w')
        for item in Grammar_length:
            lengthfile.write("%s\n" % item)
        lengthfile.close()
        
        rulefile = open(filename3, 'w')
        for ii in range(0, len(cfg.rule[0])):
            rulefile.write("%s\n" % ''.join([cfg.rule[0][ii],"  -->  ",cfg.rule[1][ii]]))
        rulefile.close()
        
        wx.MessageBox("""Grammar text files created and saved!""",
                          "Done", wx.OK)
                          
                          
    def Savepicklefile(self, cfg, Grammar, Grammar_length):
    
        dt=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
         
        filename1 = ''.join([cfg.outputpath, os.sep, cfg.prefix, "_grammar_", dt, ".dat"])
        filename12 = ''.join([cfg.outputpath, os.sep, cfg.prefix, "_grammar_", dt, ".p"])
        #filename2 = ''.join([cfg.outputpath, os.sep, cfg.prefix, "_grammar_length_", dt, ".dat"])
        #filename3 = ''.join([cfg.outputpath, os.sep, cfg.prefix, "_grammar_rule_", dt, ".dat"])
        
        rule = cfg.rule
        
        with open(filename1, 'wb') as f:
            pickle.dump(Grammar, f)
        
        pickle.dump( Grammar, open( filename12, "wb" ) )
            
        wx.MessageBox("""Grammar file saved!""",
                          "Done", wx.OK)
"""
##############################################################################

    Menu bar classes
    
##############################################################################    
"""    
    
class AboutMsg(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'About LSEX', size = (400, 300))
        wx.Frame.CenterOnScreen(self)
        self.panel = wx.Panel(self) 
        
        s = '          Lindenmayer System Explorer'
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'This tool is designed to generate and/or modify Lindenmayer ')
        s +=  (os.linesep + 'systems/grammars.')
        s +=  (os.linesep + 'Using the Generator you can generate predefined')
        s +=  (os.linesep + 'Lindenmayer systems (e.g. Fibonacci) or you can define your own')
        s +=  (os.linesep + 'rules to create grammar.')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'Using the Modifier you can change and modify existing L-systems, ')
        s +=  (os.linesep + 'by building rules to iteratively replace chains of n characters')
        s +=  (os.linesep + 'of the system with chains of m other ones.')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'Enjoy playing around with this tool!')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'This program is distributed in the hope that it will be useful, ')
        s +=  (os.linesep + 'but WITHOUT ANY WARRANTY!')
        s +=  (os.linesep + '') 
        s +=  (os.linesep + 'by Michael Lindner and Doug Saddy')
        s +=  (os.linesep + 'm.lindner@reading.ac.uk')
        s +=  (os.linesep + 'University of Reading, 2016')
        s +=  (os.linesep + 'Center for Integrative Neuroscience and Neurodynamics')
        s +=  (os.linesep + 'https://www.reading.ac.uk/cinn/cinn-home.aspx')

        statxt = wx.StaticText(self, -1, s, (-1, -1), (-1, -1))
        staline = wx.StaticLine(self, -1, (-1, -1), (-1, -1), 
                                wx.LI_HORIZONTAL)
        
        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(statxt, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(staline, 0, wx.GROW | wx.ALL, b)
        vsizer1.SetMinSize((200, -1))
        self.SetSizerAndFit(vsizer1)

        
class LSGhelp(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, 
                          id, 'Help for Lindenmayer System Generator', 
                          size = (400, 300))
        wx.Frame.CenterOnScreen(self)
        self.panel = wx.Panel(self) 
        
        s = '       '
        s +=  (os.linesep + '           Lindenmayer System Generator')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'This tool is designed to generate Lindenmayer systems (grammar).')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'USAGE:')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'Select L-system')
        s +=  (os.linesep + 'You can select a predefined system (e.g. Fibonacci), specify new')
        s +=  (os.linesep + 'rule or load user defined rules.')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'predefined rules')
        s +=  (os.linesep + 'The rules for the predefined system will be presented in the ')
        s +=  (os.linesep + 'fields under the drop-down menu after making your choice.')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'User defined')
        s +=  (os.linesep + 'You can also define a new grammar by selecting User defined.')
        s +=  (os.linesep + 'Here you have two different options:')
        s +=  (os.linesep + '   1. The classical version where you can specify rule for ')
        s +=  (os.linesep + '      replacing one cahracter with a specific amount of other ')
        s +=  (os.linesep + '      characters.')
        s +=  (os.linesep + '   2. An extended version where you can specify rule for ')
        s +=  (os.linesep + '      replacing m number of characters with a specific amount of ')
        s +=  (os.linesep + '      other n number of chracters.')
        s +=  (os.linesep + 'You can make your choice by pressing the appropriate button.')
        s +=  (os.linesep + 'In both cases a new window will open to specify the number of')
        s +=  (os.linesep + 'rules (replacements). A window, where you can specify the')
        s +=  (os.linesep + 'rules will then open.')
        s +=  (os.linesep + 'You can save the defined rules by pressing the "Save rules" button.')
        s +=  (os.linesep + 'Then you can specify a name for the rule and it will be saved in a ')
        s +=  (os.linesep + 'file called generator_user_rules.mat. The saved rules will appear in')
        s +=  (os.linesep + 'the drop down menu with the prefix USER. The rules can be ')
        s +=  (os.linesep + 'deleted by deleting the generator_user_rules.mat file. BUT BE ')
        s +=  (os.linesep + 'AWARE that all rules will be deleted by doing this!')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'In case of the extended replacement you can further select the')
        s +=  (os.linesep + 'type of replacement which should be performed:')
        s +=  (os.linesep + 'You have three options for types of replacement (how the rules')
        s +=  (os.linesep + 'should be applied to the system):')
        s +=  (os.linesep + '1. segmentwise')
        s +=  (os.linesep + ' In the segmentwise replacement all vocabulars need to have the')
        s +=  (os.linesep + 'same length. (e.g. 101, 111, 000, etc, ). The grammar is then')
        s +=  (os.linesep + 'cut into segments of the same length and the replacement')
        s +=  (os.linesep + 'is then performed for each segment.')
        s +=  (os.linesep + '2, continuously')
        s +=  (os.linesep + ' In the continuous replacement the algorithm goes through the ')
        s +=  (os.linesep + 'whole grammar elementwise and replaces the n elements from the')
        s +=  (os.linesep + 'vocabulary with the m elements that you defined! Each element')
        s +=  (os.linesep + 'will be checked and can be used more than once for a replacement!')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'e.g. system:  001110110010011110010011110000')
        s +=  (os.linesep + '     rule: 111-->2 ; 110-->3 ; 100-->4')
        s +=  (os.linesep + '     results: 002310340040022340040022340000')
        s +=  (os.linesep + '')
        s +=  (os.linesep + '')
        s +=  (os.linesep + '3. continuously (skip last n)')
        s +=  (os.linesep + ' This type of replacement follows the same protocol as the one above, but')
        s +=  (os.linesep + 'when identifying a match with your rule the next n-1 characters (length of')
        s +=  (os.linesep + 'the vocabular) of the system are skipped. Here, each element will')
        s +=  (os.linesep + 'only be used once for a replacement!')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'e.g. system:  001110110010011110010011110000')
        s +=  (os.linesep + '     rule: 111-->2 ; 110-->3 ; 100-->4')
        s +=  (os.linesep + '     results: 0020304230423000')
        s +=  (os.linesep + '')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'The start value for the grammar generation is by default: 0 for')
        s +=  (os.linesep + 'for the predefined systems and for the user defined system it is')
        s +=  (os.linesep + 'the value (lefthand side) of the first rule!') 
        s +=  (os.linesep + 'But the start vlaue can be changes changed individually.')
        s +=  (os.linesep + 'IMPORTANT: The values in the "start values" field')
        s +=  (os.linesep + 'need to be included within the rules you define!')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'With the number of recursions you can specify how often the')
        s +=  (os.linesep + 'rules should be used iteratively.')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'You need to specify an output folder by typing in a path or')
        s +=  (os.linesep + 'by using the browse button.')
        s +=  (os.linesep + 'Furthermore, you can specify an output file prefix and the type of')
        s +=  (os.linesep + 'output which should be stored. Either a Pickle .dat file, ')
        s +=  (os.linesep + 'a text file, or both are valid:')
        s +=  (os.linesep + 'In the case of a .mat file, three variables are stored: a cell')
        s +=  (os.linesep + 'with the grammar of each iteration, the rule and a vector with the')
        s +=  (os.linesep + 'length of each iteration.')
        s +=  (os.linesep + 'In the case of a .txt file, three output files are stored. One with')
        s +=  (os.linesep + 'the grammar, one including the length of each iteration and one')
        s +=  (os.linesep + 'containing the rule.')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'After setting up all parameters, you simply need to press the')
        s +=  (os.linesep + 'generate grammar button.')
        s +=  (os.linesep + '')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'This program is distributed in the hope that it will be useful, ')
        s +=  (os.linesep + 'but WITHOUT ANY WARRANTY!')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'by Michael Lindner and Doug Saddy')
        s +=  (os.linesep + 'm.lindner@reading.ac.uk')
        s +=  (os.linesep + 'University of Reading, 2016')
        s +=  (os.linesep + 'Center for Integrative Neuroscience and Neurodynamics')
        s +=  (os.linesep + 'https://www.reading.ac.uk/cinn/cinn-home.aspx')

        MultiLine = wx.TextCtrl(self, -1, s, (-1, -1), (500, 400), 
                                style = wx.TE_MULTILINE|wx.TE_READONLY|
                                wx.TE_AUTO_URL)
        
        staline = wx.StaticLine(self, -1, (-1, -1), (-1, -1), 
                                wx.LI_HORIZONTAL)
        
        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(MultiLine, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(staline, 0, wx.GROW | wx.ALL, b)
        vsizer1.SetMinSize((200, -1))
        self.SetSizerAndFit(vsizer1)

        
class LSMhelp(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, 
                          id, 'Help for Lindenmayer System Modifier', 
                          size = (400, 300))
        wx.Frame.CenterOnScreen(self)
        self.panel = wx.Panel(self) 

        s = '       '
        s +=  (os.linesep + '           Lindenmayer System Modifier')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'This tool is designed to modify Lindenmayer systems (grammar).')
        s +=  (os.linesep + 'With this tool, rules can be defined to replace n with m number of')
        s +=  (os.linesep + 'elements in the system.')
        s +=  (os.linesep + ' e.g. 111 with 1')
        s +=  (os.linesep + '      10  with 2')
        s +=  (os.linesep + '      110 with 10')
        s +=  (os.linesep + '      1   with 1011 etc.')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'USAGE:')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'First you need to load a system by using the Load L-system button.')
        s +=  (os.linesep + 'You can easily load a Pickle output file from the Lindenmayer')
        s +=  (os.linesep + 'System Generator. You can also load other systems, as long as the system')
        s +=  (os.linesep + 'is stored in a Pickle .dat file!')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'You can define any rules for replacement by pressing')
        s +=  (os.linesep + 'the "Define rules" button. After pressing the button')
        s +=  (os.linesep + 'a new window opens where you can specify the number of')
        s +=  (os.linesep + 'rules (replacements). Afterwards another window opens, where ')
        s +=  (os.linesep + 'you can specify the rules')
        s +=  (os.linesep + ' e.g. 101 ---> 1')
        s +=  (os.linesep + '      010 ---> 0  etc.')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'You can save the defined rules by pressing the "Save rules" button.')
        s +=  (os.linesep + 'Then you can specify a name for the rule and it will be saved in a ')
        s +=  (os.linesep + 'file called modifier_user_rules.mat. After creating this file by ')
        s +=  (os.linesep + 'saving one or more rules, you will get the option to load the rules')
        s +=  (os.linesep + 'after pressing the "Define Rules" button. The rules can be ')
        s +=  (os.linesep + 'deleted by deleting the modifier_user_rules.mat file. BUT BE ')
        s +=  (os.linesep + 'AWARE that all rules will be deleted by doing this!')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'You have three options for types of replacement (how the rules')
        s +=  (os.linesep + 'should be applied to the system):')
        s +=  (os.linesep + '1. segmentwise')
        s +=  (os.linesep + ' In the segmentwise replacement all vocabulars need to have the')
        s +=  (os.linesep + 'same length. (e.g. 101, 111, 000, etc, ). The grammar is then')
        s +=  (os.linesep + 'cut into segments of the same length and the replacement')
        s +=  (os.linesep + 'is then performed for each segment.')
        s +=  (os.linesep + '2, continuously')
        s +=  (os.linesep + ' In the continuous replacement the algorithm goes through the ')
        s +=  (os.linesep + 'whole grammar elementwise and replaces the n elements from the')
        s +=  (os.linesep + 'vocabulary with the m elements that you defined! Each element')
        s +=  (os.linesep + 'will be checked and can be used more than once for a replacement!')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'e.g. system:  001110110010011110010011110000')
        s +=  (os.linesep + '     rule: 111-->2 ; 110-->3 ; 100-->4')
        s +=  (os.linesep + '     results: 002310340040022340040022340000')
        s +=  (os.linesep + '')
        s +=  (os.linesep + '')
        s +=  (os.linesep + '3. continuously (skip last n)')
        s +=  (os.linesep + ' This type of replacement follows the same protocol as the one above, but')
        s +=  (os.linesep + 'when identifying a match with your rule the next n-1 characters (length of')
        s +=  (os.linesep + 'the vocabular) of the system are skipped. Here, each element will')
        s +=  (os.linesep + 'only be used once for a replacement!')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'e.g. system:  001110110010011110010011110000')
        s +=  (os.linesep + '     rule: 111-->2 ; 110-->3 ; 100-->4')
        s +=  (os.linesep + '     results: 0020304230423000')
        s +=  (os.linesep + '')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'With the number of recursions you can specify how often the')
        s +=  (os.linesep + 'rules should be used iteratively.')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'You need to specify an output folder by typing in a path or')
        s +=  (os.linesep + 'by using the browse button.')
        s +=  (os.linesep + 'Furthermore, you can specify an output file prefix and the type of')
        s +=  (os.linesep + 'output which should be stored. Either a pickle .dat file, ')
        s +=  (os.linesep + 'a text file, or both are valid:')
        s +=  (os.linesep + 'In the case of a .mat file, three variables are stored: a cell')
        s +=  (os.linesep + 'with the grammar of each iteration, the rule and a vector with the')
        s +=  (os.linesep + 'length of each iteration.')
        s +=  (os.linesep + 'In the case of a .txt file, three output files are stored. One with')
        s +=  (os.linesep + 'the grammar, one including the length of each iteration and one')
        s +=  (os.linesep + 'containing the rule.')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'After setting up all parameters, you simply need to press the')
        s +=  (os.linesep + 'Modify L-system button.')
        s +=  (os.linesep + '')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'This program is distributed in the hope that it will be useful, ')
        s +=  (os.linesep + 'but WITHOUT ANY WARRANTY!')
        s +=  (os.linesep + '')
        s +=  (os.linesep + 'by Michael Lindner and Doug Saddy')
        s +=  (os.linesep + 'm.lindner@reading.ac.uk')
        s +=  (os.linesep + 'University of Reading, 2016')
        s +=  (os.linesep + 'Center for Integrative Neuroscience and Neurodynamics')
        s +=  (os.linesep + 'https://www.reading.ac.uk/cinn/cinn-home.aspx')
        
        
        MultiLine = wx.TextCtrl(self, -1, s, (-1, -1), (500, 400), 
                                style = wx.TE_MULTILINE|
                                wx.TE_READONLY|wx.TE_AUTO_URL)
        staline = wx.StaticLine(self, -1, (-1, -1), (-1, -1), 
                                wx.LI_HORIZONTAL)
        
        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(MultiLine, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(staline, 0, wx.GROW | wx.ALL, b)
        vsizer1.SetMinSize((200, -1))
        self.SetSizerAndFit(vsizer1)
    
        
def main():
    
    ex = wx.App()
    LSEX(None)
    ex.MainLoop()    


if __name__ ==  '__main__':
    main()
    
    
