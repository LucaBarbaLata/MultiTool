import tkinter
import tkinter.messagebox
import customtkinter
import requests
import urllib.request
import os
import time




user = os.getlogin()
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("MultiTool")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="MultiTool", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Install", command=self.Install)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Tweaks", command=self.Tweaks)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Config", command=self.Install)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["System", "Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", "Terms and Conditions:\n\n" + "hi" * 1)

    
    
    def setvar(self):
        global value
        value = self.optionmenu_1.get()
        print(f"Value is now set to {value}")
        if value == "Chrome":
            cmd = "winget install Google.chrome"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Opera":
            cmd = "winget install Opera.Opera"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Firefox":
            cmd = "winget install Mozilla.Firefox"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Brave":
            cmd = "winget install Brave.Brave"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
    def setvar2(self):
        global value
        value = self.optionmenu_2.get()
        print(f"Value is now set to {value}")
        if value == "7-Zip":
            cmd = "winget install 7zip.7zip"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "PeaZip":
            cmd = "winget install Giorgiotani.Peazip"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "WinRar":
            cmd = "winget install RARLab.WinRAR"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
    def setvar3(self):
        global value
        value = self.optionmenu_3.get()
        print(f"Value is now set to {value}")
        if value == "Zoom":
            cmd = "winget install Zoom.Zoom"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Discord":
            cmd = "winget install Discord.Discord"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Skype":
            cmd = "winget install Microsoft.Skype"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Pidgin":
            cmd = "winget install Pidgin.Pidgin"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Thunderbird":
            cmd = "winget install Mozilla.Thunderbird"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Trillian":
            cmd = "winget install Trillian.Trillian"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
    def setvar4(self):
        global value
        value = self.optionmenu_4.get()
        print(f"Value is now set to {value}")
        if value == "Spotify":
            cmd = "winget install Spotify.Spotify"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "VLC":
            cmd = "winget install VideoLAN.VLC"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "AIMP":
            cmd = "winget install AIMP.AIMP"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "foobar2000":
            cmd = "winget install PeterPawlowski.foobar2000"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Audacity":
            cmd = "winget install Audacity.Audacity"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "GOM":
            cmd = "winget install GOMLab.GOMPlayer"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
    def setvar5(self):
        global value
        value = self.optionmenu_5.get()
        print(f"Value is now set to {value}")
        if value == "Krita":
            cmd = "winget install KDE.Krita"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Blender":
            cmd = "winget install BlenderFoundation.Blender"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "GIMP":
            cmd = "winget install GIMP.GIMP"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "IrfanView":
            cmd = "winget install IrfanSkiljan.IrfanView"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "XnView":
            cmd = "winget install XnSoft.XnView.Classic"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Inkscape":
            cmd = "winget install Inkscape.Inkscape"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "FastStone":
            cmd = "winget install FastStone.Viewer"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Greenshot":
            cmd = "winget install Greenshot.Greenshot"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "ShareX":
            cmd = "winget install ShareX.ShareX"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
    def setvar6(self):
        global value
        value = self.optionmenu_6.get()
        print(f"Value is now set to {value}")
        if value == "Python x64 3":
            cmd = "winget install Python.Python.3.11"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Notepad++":
            cmd = "winget install Notepad++.Notepad++"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "WinSCP":
            cmd = "winget install WinSCP.WinSCP"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "PuTTY":
            cmd = "winget install PuTTY.PuTTY"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "WinMerge":
            cmd = "winget install WinMerge.WinMerge"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Eclipse":
            cmd = "winget install EclipseFoundation.TheiaBlueprint"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "VS Code(Visual Studio Code)":
            cmd = "winget install Microsoft.VisualStudioCode"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "VMWare Workstation 17":
            cmd = "winget install VMware.WorkstationPro"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Windows 10 ISO":
            urllib.request.urlretrieve("https://dw4.uptodown.com/dwn/Z5K6puj3G_H88j8T1cdaR94-_ymHzIa9iak3gtnQ4ZcU4fBzNv8FlwC1mRKJoNX0RfNbZEL0jGITwfvjoys7Fp5W-UynADwPjBpbegvZ1T6RgEy5DY9azL3xj4mFg5xW/2jRfzII6khimcsXl0O8L9yzEQBz0hR3gIs6qIt4s-PRJWazbpr-pbXhUnRXZyOJkiCN1wnXEc6aX1USdXF4i9MPOJNMuLkvK2fbm1sr2rltjdfLf2hhBj3MVeDC3G8qX/uTWR6o5NMwQ_5VyO208RQ533z8aczm-MrqLw87pADzQ-unkz-SEoPr3FGGMCGT69WiP4vN_idlcr9p3hDWPcD2zpSBXUF9aMo0OfadtfWMQ=/windows-10-22h2-build-19045.iso", "windows-10-22h2-build-19045.iso", reporthook=update_progress)
        if value == "Windows 11 ISO":
            urllib.request.urlretrieve("https://aka.ms/windev_VM_vmware", "Win11.zip")
    def setvar7(self):
        global value
        value = self.optionmenu_7.get()
        print(f"Value is now set to {value}")
        if value == "TeamViewer 15":
            cmd = "winget install TeamViewer.TeamViewer"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "AnyDesk":
            cmd = "winget install AnyDeskSoftwareGmbH.AnyDesk"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "ImgBurn":
            cmd = "winget install LIGHTNINGUK.ImgBurn"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "TeraCopy":
            cmd = "winget install CodeSector.TeraCopy"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "CDBurnerXP":
            cmd = "Canneverbe.CDBurnerXP"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Revo":
            cmd = "winget install RevoUninstaller.RevoUninstaller"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Launchy":
            cmd = "winget install CodeJelly.Launchy"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "WinDirStat":
            cmd = "winget install WinDirStat.WinDirStat"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "Glary":
            cmd = "winget install Glarysoft.GlaryUtilities"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "InfraRecorder":
            cmd = "winget install ChristianKindahl.InfraRecorder"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
    def setvar8(self):
        global value
        value = self.optionmenu_8.get()
        print(f"Value is now set to {value}")
        if value == "Foxit Reader":
            cmd = "winget install Foxitreader"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "LibreOffice":
            cmd = "winget install TheDocumentFoundation.LibreOffice"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "SumatraPDF":
            cmd = "winget install SumatraPDF.SumatraPDF"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "CutePDF":
            cmd = "winget install AcroSoftware.CutePDFWriter"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        if value == "OpenOffice":
            cmd = "winget install TheDocumentFoundation.LibreOffice"
            with open("temp.bat", "w") as f:
                f.write(cmd)
            os.system("temp.bat")
            time.sleep(1)
            os.remove("temp.bat")
        
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
    def Install(self):
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Browsers")
        self.tabview.add("Compression")
        self.tabview.add("Messaging")
        self.tabview.add("Media")
        self.tabview.add("Imaging")
        self.tabview.add("Dev Tools")
        self.tabview.add("Utilities")
        self.tabview.add("Documents")
        
       
        
        
        
        #Browsers
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Browsers"), dynamic_resizing=True,
                                                        values=["Chrome", "Opera", "Firefox", "Brave"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Browsers"), text="Set choice",
                                                           command=self.setvar)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        #Compression
        self.optionmenu_2 = customtkinter.CTkOptionMenu(self.tabview.tab("Compression"), dynamic_resizing=True,
                                                        values=["7-Zip", "PeaZip", "WinRar"])
        self.optionmenu_2.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Compression"), text="Set choice",
                                                           command=self.setvar2)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        #Messaging
        self.optionmenu_3 = customtkinter.CTkOptionMenu(self.tabview.tab("Messaging"), dynamic_resizing=True,
                                                        values=["Zoom", "Discord", "Skype", "Pidgin", "Thunderbird", "Trillian"])
        self.optionmenu_3.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Messaging"), text="Set choice",
                                                           command=self.setvar3)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        #Media
        self.optionmenu_4 = customtkinter.CTkOptionMenu(self.tabview.tab("Media"), dynamic_resizing=True,
                                                        values=["Spotify", "VLC", "AIMP", "foobar2000", "Audacity", "GOM"])
        self.optionmenu_4.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Media"), text="Set choice",
                                                           command=self.setvar4)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        #Imaging
        self.optionmenu_5 = customtkinter.CTkOptionMenu(self.tabview.tab("Imaging"), dynamic_resizing=True,
                                                        values=["Krita", "Blender", "GIMP", "IrfanView", "XnView", "Inkscape", "FastStone", "Greenshot", "ShareX"])
        self.optionmenu_5.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Imaging"), text="Set choice",
                                                           command=self.setvar5)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        #Dev Tools
        self.optionmenu_6 = customtkinter.CTkOptionMenu(self.tabview.tab("Dev Tools"), dynamic_resizing=True,
                                                        values=["Python x64 3", "Notepad++", "WinSCP", "PuTTY", "WinMerge", "Eclipse", "VS Code(Visual Studio Code)", "VMWare Workstation 17", "Windows 10 ISO", "Windows 11 ISO", "Windows 11 .ovf file"])
        self.optionmenu_6.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Dev Tools"), text="Set choice",
                                                           command=self.setvar6)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        #Utilities
        self.optionmenu_8 = customtkinter.CTkOptionMenu(self.tabview.tab("Utilities"), dynamic_resizing=True,
                                                        values=["TeamViewer 15", "AnyDesk", "ImgBurn", "TeraCopy", "CDBurnerXP", "Revo", "Launchy", "WinDirStat", "Glary", "InfraRecorder"])
        self.optionmenu_8.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Utilities"), text="Set choice",
                                                           command=self.setvar8)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        #Documents
        self.optionmenu_7 = customtkinter.CTkOptionMenu(self.tabview.tab("Documents"), dynamic_resizing=True,
                                                        values=["Foxit Reader", "LibreOffice", "SumatraPDF", "CutePDF", "OpenOffice"])
        self.optionmenu_7.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Documents"), text="Set choice",
                                                           command=self.setvar7)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        
    def Tweaks(self):
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Show file extensions.", command=self.sfe)
        self.sidebar_button_1.grid(row=1, column=2, padx=20, pady=10)
        #temp
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Delete temporary files", command=self.dtemporary)
        self.sidebar_button_1.grid(row=2, column=2, padx=20, pady=10)
        #Update Apps
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Update all apps", command=self.updateapps)
        self.sidebar_button_1.grid(row=2, column=2, padx=20, pady=10)
    #Tweaks
    def sfe(self):
        cmd = "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v HideFileExt /t REG_DWORD /d 0 /"
        with open("temp.bat","w") as f:
            f.write(cmd)
        os.system("temp.bat")
        time.sleep(5)
        os.remove("temp.bat")
        return
    def dtemporary(self):
        cmd = "del /q/f/s %TEMP%\*"
        with open("temp.bat","w") as f:
            f.write(cmd)
        os.system("temp.bat")
        time.sleep(10)
        os.remove("temp.bat")
        return
    def updateapps(self):
        cmd = "winget upgrade --all"
        with open("temp.bat", "w") as f:
            f.write(cmd)
        os.system("temp.bat")
        time.sleep(1)
        os.remove("temp.bat")
    
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
    
