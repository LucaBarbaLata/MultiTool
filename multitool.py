import os
import platform
import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import psutil
import configparser
import threading
from datetime import datetime


# ─────────────────────────────────────────────────────────────────────────────
# Config
# ─────────────────────────────────────────────────────────────────────────────

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
_config = configparser.ConfigParser()


def _init_config():
    if not os.path.exists(CONFIG_FILE):
        _config["Settings"] = {"appearance": "System", "color": "blue", "scaling": "100%"}
        with open(CONFIG_FILE, "w") as f:
            _config.write(f)
    else:
        _config.read(CONFIG_FILE)


def get_config(key: str, fallback: str = "") -> str:
    return _config.get("Settings", key, fallback=fallback)


def set_config(key: str, value: str):
    _config.set("Settings", key, value)
    with open(CONFIG_FILE, "w") as f:
        _config.write(f)


_init_config()
customtkinter.set_appearance_mode(get_config("appearance", "System"))
customtkinter.set_default_color_theme(get_config("color", "blue"))


# ─────────────────────────────────────────────────────────────────────────────
# App data
# ─────────────────────────────────────────────────────────────────────────────

INSTALL_APPS: dict[str, dict[str, str]] = {
    "Browsers": {
        "Chrome":   "Google.Chrome",
        "Firefox":  "Mozilla.Firefox",
        "Brave":    "Brave.Brave",
        "Opera":    "Opera.Opera",
        "Vivaldi":  "Vivaldi.Vivaldi",
        "Edge":     "Microsoft.Edge",
    },
    "Compression": {
        "7-Zip":  "7zip.7zip",
        "PeaZip": "Giorgiotani.Peazip",
        "WinRAR": "RARLab.WinRAR",
    },
    "Messaging": {
        "Discord":     "Discord.Discord",
        "Telegram":    "Telegram.TelegramDesktop",
        "Slack":       "SlackTechnologies.Slack",
        "Zoom":        "Zoom.Zoom",
        "Thunderbird": "Mozilla.Thunderbird",
        "Skype":       "Microsoft.Skype",
    },
    "Media": {
        "Spotify":    "Spotify.Spotify",
        "VLC":        "VideoLAN.VLC",
        "MPC-HC":     "clsid2.mpc-hc",
        "AIMP":       "AIMP.AIMP",
        "foobar2000": "PeterPawlowski.foobar2000",
        "Audacity":   "Audacity.Audacity",
        "HandBrake":  "HandBrake.HandBrake",
    },
    "Imaging": {
        "GIMP":      "GIMP.GIMP",
        "Krita":     "KDE.Krita",
        "Inkscape":  "Inkscape.Inkscape",
        "Blender":   "BlenderFoundation.Blender",
        "ShareX":    "ShareX.ShareX",
        "IrfanView": "IrfanSkiljan.IrfanView",
        "Greenshot": "Greenshot.Greenshot",
        "FastStone": "FastStone.Viewer",
    },
    "Dev Tools": {
        "VS Code":           "Microsoft.VisualStudioCode",
        "Git":               "Git.Git",
        "Python 3.11":       "Python.Python.3.11",
        "Windows Terminal":  "Microsoft.WindowsTerminal",
        "Notepad++":         "Notepad++.Notepad++",
        "PuTTY":             "PuTTY.PuTTY",
        "WinSCP":            "WinSCP.WinSCP",
        "WinMerge":          "WinMerge.WinMerge",
        "Docker Desktop":    "Docker.DockerDesktop",
        "VMware Workstation":"VMware.WorkstationPro",
    },
    "Utilities": {
        "PowerToys":        "Microsoft.PowerToys",
        "Everything":       "voidtools.Everything",
        "WinDirStat":       "WinDirStat.WinDirStat",
        "Revo Uninstaller": "RevoUninstaller.RevoUninstaller",
        "AnyDesk":          "AnyDeskSoftwareGmbH.AnyDesk",
        "TeamViewer":       "TeamViewer.TeamViewer",
        "TeraCopy":         "CodeSector.TeraCopy",
    },
    "Documents": {
        "LibreOffice": "TheDocumentFoundation.LibreOffice",
        "SumatraPDF":  "SumatraPDF.SumatraPDF",
        "Obsidian":    "Obsidian.Obsidian",
        "Notion":      "Notion.Notion",
        "Foxit Reader":"Foxitreader",
    },
}

TWEAKS = [
    {
        "name": "Show file extensions",
        "desc": "Makes Explorer show .txt, .exe, etc. next to every filename.",
        "cmd":  r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v HideFileExt /t REG_DWORD /d 0 /f',
    },
    {
        "name": "Show hidden files",
        "desc": "Makes hidden files and folders visible in Explorer.",
        "cmd":  r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /t REG_DWORD /d 1 /f',
    },
    {
        "name": "Delete temporary files",
        "desc": "Clears your %TEMP% folder to free up disk space.",
        "cmd":  'cmd /c "del /q /f /s %TEMP%\\*"',
    },
    {
        "name": "Update all apps",
        "desc": "Runs winget to upgrade every installed app to its latest version.",
        "cmd":  "winget upgrade --all --accept-source-agreements --accept-package-agreements",
    },
    {
        "name": "Disable Fast Startup",
        "desc": "Turns off hybrid sleep on shutdown, which fixes some driver and wake issues.",
        "cmd":  "powercfg /h off",
    },
    {
        "name": "Enable long file paths",
        "desc": "Removes the 260-character path limit. Requires administrator privileges.",
        "cmd":  r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f',
    },
    {
        "name": "Restore classic context menu  (Win 11)",
        "desc": "Brings back the full right-click menu instead of 'Show more options'.",
        "cmd":  r'reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve',
        "warning": "This requires signing out of Windows to take effect.\n\nSign out now?",
        "post_cmd": "shutdown /l",
    },
]


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def run_command(command: str, on_done=None):
    """Run a shell command in a background thread."""
    def _target():
        result = subprocess.run(command, shell=True)
        if on_done:
            on_done(result.returncode)
    threading.Thread(target=_target, daemon=True).start()


def fmt_gb(b: int) -> str:
    return f"{b / 1024 ** 3:.2f} GB"


def fmt_mb(b: int) -> str:
    return f"{b / 1024 ** 2:.0f} MB"


# ─────────────────────────────────────────────────────────────────────────────
# Pages
# ─────────────────────────────────────────────────────────────────────────────

class InstallPage(customtkinter.CTkFrame):
    """
    Multi-select install page.
    Tick the apps you want, then hit Install Selected.
    """

    def __init__(self, master, set_status):
        super().__init__(master, fg_color="transparent")
        self.set_status = set_status
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._checks: dict[str, customtkinter.BooleanVar] = {}
        self._build()

    def _build(self):
        tabview = customtkinter.CTkTabview(self)
        tabview.grid(row=0, column=0, sticky="nsew")

        for category, apps in INSTALL_APPS.items():
            tabview.add(category)
            tab = tabview.tab(category)
            tab.grid_columnconfigure(0, weight=1)
            tab.grid_rowconfigure(0, weight=1)

            scroll = customtkinter.CTkScrollableFrame(tab)
            scroll.grid(row=0, column=0, sticky="nsew", padx=5, pady=(5, 0))
            scroll.grid_columnconfigure(0, weight=1)

            for i, name in enumerate(apps):
                var = customtkinter.BooleanVar(value=False)
                self._checks[name] = var
                customtkinter.CTkCheckBox(scroll, text=name, variable=var).grid(
                    row=i, column=0, sticky="w", padx=15, pady=5
                )

            btn_row = customtkinter.CTkFrame(tab, fg_color="transparent")
            btn_row.grid(row=1, column=0, sticky="ew", padx=5, pady=8)
            btn_row.grid_columnconfigure((0, 1), weight=1)

            customtkinter.CTkButton(
                btn_row, text="Select All", width=130,
                command=self._make_select_all(apps),
            ).grid(row=0, column=0, padx=5)

            customtkinter.CTkButton(
                btn_row, text="Install Selected", width=150,
                command=self._make_install(apps),
            ).grid(row=0, column=1, padx=5)

    def _make_select_all(self, apps: dict):
        def toggle():
            all_on = all(self._checks[n].get() for n in apps)
            for n in apps:
                self._checks[n].set(not all_on)
        return toggle

    def _make_install(self, apps: dict):
        def install():
            selected = {n: wid for n, wid in apps.items() if self._checks[n].get()}
            if not selected:
                self.set_status("Select at least one app first.")
                return
            names = list(selected.keys())
            self.set_status(f"Installing: {', '.join(names)}...")
            cmds = " && ".join(
                f"winget install --id {wid} -e --accept-source-agreements --accept-package-agreements"
                for wid in selected.values()
            )
            run_command(
                cmds,
                on_done=lambda rc: self.set_status(
                    f"Done: {', '.join(names)}." if rc == 0
                    else f"Finished with code {rc}."
                ),
            )
        return install


class TweaksPage(customtkinter.CTkFrame):
    """One-click Windows tweaks, each with a short description."""

    def __init__(self, master, set_status):
        super().__init__(master, fg_color="transparent")
        self.set_status = set_status
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._build()

    def _build(self):
        scroll = customtkinter.CTkScrollableFrame(self, label_text="Windows Tweaks")
        scroll.grid(row=0, column=0, sticky="nsew")
        scroll.grid_columnconfigure(0, weight=1)

        for i, tweak in enumerate(TWEAKS):
            card = customtkinter.CTkFrame(scroll)
            card.grid(row=i, column=0, sticky="ew", padx=10, pady=6)
            card.grid_columnconfigure(0, weight=1)

            customtkinter.CTkLabel(
                card, text=tweak["name"],
                font=customtkinter.CTkFont(weight="bold"),
                anchor="w",
            ).grid(row=0, column=0, padx=15, pady=(12, 2), sticky="w")

            customtkinter.CTkLabel(
                card, text=tweak["desc"],
                anchor="w", wraplength=560,
                text_color=("gray45", "gray65"),
            ).grid(row=1, column=0, padx=15, pady=(0, 12), sticky="w")

            customtkinter.CTkButton(
                card, text="Apply", width=85,
                command=self._make_apply(tweak),
            ).grid(row=0, column=1, rowspan=2, padx=15, pady=12)

    def _make_apply(self, tweak: dict):
        def apply():
            if tweak.get("warning"):
                if not tkinter.messagebox.askyesno("Confirm", tweak["warning"]):
                    return
            self.set_status(f"Applying: {tweak['name']}...")
            run_command(tweak["cmd"], on_done=lambda rc: self._done(tweak, rc))
        return apply

    def _done(self, tweak: dict, rc: int):
        if rc == 0:
            self.set_status(f"Done: {tweak['name']}.")
            if tweak.get("post_cmd"):
                run_command(tweak["post_cmd"])
        else:
            self.set_status(f"'{tweak['name']}' finished with code {rc}.")


class SysInfoPage(customtkinter.CTkFrame):
    """Live system stats with progress bars for CPU, RAM and disk."""

    _ROWS = [
        # (section_title, [(display_label, data_key, show_bar)])
        ("CPU", [
            ("Usage",                   "cpu_pct",   True),
            ("Cores (physical/logical)", "cpu_cores", False),
        ]),
        ("Memory", [
            ("Total",     "ram_total", False),
            ("Used",      "ram_used",  True),
            ("Available", "ram_avail", False),
        ]),
        ("Disk  (C:\\)", [
            ("Total", "disk_total", False),
            ("Used",  "disk_used",  True),
            ("Free",  "disk_free",  False),
        ]),
        ("Network", [
            ("Sent",     "net_sent", False),
            ("Received", "net_recv", False),
        ]),
        ("System", [
            ("OS",        "os",        False),
            ("Last Boot", "boot_time", False),
        ]),
    ]

    def __init__(self, master, set_status):
        super().__init__(master, fg_color="transparent")
        self.set_status = set_status
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self._value_labels: dict[str, customtkinter.CTkLabel] = {}
        self._bars: dict[str, customtkinter.CTkProgressBar] = {}
        self._build()
        self._refresh()

    def _build(self):
        header = customtkinter.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 8))

        customtkinter.CTkLabel(
            header, text="System Information",
            font=customtkinter.CTkFont(size=18, weight="bold"),
        ).pack(side="left")

        customtkinter.CTkButton(
            header, text="Refresh", width=90, command=self._refresh,
        ).pack(side="right")

        scroll = customtkinter.CTkScrollableFrame(self)
        scroll.grid(row=1, column=0, sticky="nsew")
        scroll.grid_columnconfigure(1, weight=1)

        row = 0
        for section, fields in self._ROWS:
            customtkinter.CTkLabel(
                scroll, text=section,
                font=customtkinter.CTkFont(weight="bold"),
                anchor="w",
            ).grid(row=row, column=0, columnspan=3, sticky="w", padx=12, pady=(14, 3))
            row += 1

            for label, key, show_bar in fields:
                customtkinter.CTkLabel(
                    scroll, text=label + ":", anchor="w", width=210,
                ).grid(row=row, column=0, sticky="w", padx=(24, 6), pady=3)

                val = customtkinter.CTkLabel(scroll, text="—", anchor="w")
                val.grid(row=row, column=1, sticky="w", padx=4, pady=3)
                self._value_labels[key] = val

                if show_bar:
                    bar = customtkinter.CTkProgressBar(scroll, width=180)
                    bar.set(0)
                    bar.grid(row=row, column=2, padx=12, pady=3, sticky="w")
                    self._bars[key] = bar

                row += 1

    def _refresh(self):
        vm    = psutil.virtual_memory()
        disk  = psutil.disk_usage("/")
        net   = psutil.net_io_counters()
        cpu   = psutil.cpu_percent(interval=0.2)
        boot  = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

        data = {
            "cpu_pct":    (f"{cpu:.1f}%",                                          cpu / 100),
            "cpu_cores":  (f"{psutil.cpu_count(logical=False)} / {psutil.cpu_count()} logical", None),
            "ram_total":  (fmt_gb(vm.total),                                       None),
            "ram_used":   (f"{fmt_gb(vm.used)}  ({vm.percent:.0f}%)",              vm.percent / 100),
            "ram_avail":  (fmt_gb(vm.available),                                   None),
            "disk_total": (fmt_gb(disk.total),                                     None),
            "disk_used":  (f"{fmt_gb(disk.used)}  ({disk.percent:.0f}%)",          disk.percent / 100),
            "disk_free":  (fmt_gb(disk.free),                                      None),
            "net_sent":   (fmt_mb(net.bytes_sent),                                 None),
            "net_recv":   (fmt_mb(net.bytes_recv),                                 None),
            "os":         (f"{platform.system()} {platform.release()} ({platform.machine()})", None),
            "boot_time":  (boot,                                                   None),
        }

        for key, (text, bar_val) in data.items():
            if key in self._value_labels:
                self._value_labels[key].configure(text=text)
            if bar_val is not None and key in self._bars:
                self._bars[key].set(bar_val)

        self.set_status("Refreshed.", timeout_ms=3000)


class SettingsPage(customtkinter.CTkFrame):
    """Appearance, theme, and scaling settings."""

    def __init__(self, master, set_status, on_appearance_change, on_scaling_change):
        super().__init__(master, fg_color="transparent")
        self.set_status = set_status
        self.on_appearance_change = on_appearance_change
        self.on_scaling_change = on_scaling_change
        self.grid_columnconfigure(1, weight=1)
        self._build()

    def _build(self):
        customtkinter.CTkLabel(
            self, text="Settings",
            font=customtkinter.CTkFont(size=18, weight="bold"),
        ).grid(row=0, column=0, columnspan=2, sticky="w", padx=12, pady=(10, 24))

        options = [
            ("Appearance Mode", ["System", "Light", "Dark"],              "appearance", self._apply_appearance),
            ("Color Theme",     ["blue", "green", "dark-blue"],           "color",      self._apply_theme),
            ("UI Scaling",      ["80%", "90%", "100%", "110%", "120%"],   "scaling",    self._apply_scaling),
        ]

        for i, (label, values, key, cmd) in enumerate(options, start=1):
            customtkinter.CTkLabel(self, text=label + ":", anchor="w").grid(
                row=i, column=0, sticky="w", padx=(12, 8), pady=14,
            )
            saved = get_config(key, values[0])
            menu = customtkinter.CTkOptionMenu(self, values=values, command=cmd, width=160)
            menu.set(saved if saved in values else values[0])
            menu.grid(row=i, column=1, sticky="w", padx=4, pady=14)

        customtkinter.CTkLabel(
            self, text="Color theme change takes effect on next launch.",
            text_color=("gray55", "gray60"), anchor="w",
        ).grid(row=len(options) + 1, column=0, columnspan=2, sticky="w", padx=12, pady=(4, 0))

    def _apply_appearance(self, value: str):
        self.on_appearance_change(value)
        set_config("appearance", value)

    def _apply_theme(self, value: str):
        set_config("color", value)
        self.set_status("Theme saved. Restart to apply.", timeout_ms=5000)

    def _apply_scaling(self, value: str):
        self.on_scaling_change(value)
        set_config("scaling", value)


# ─────────────────────────────────────────────────────────────────────────────
# Main window
# ─────────────────────────────────────────────────────────────────────────────

class App(customtkinter.CTk):
    _PAGES = ["Install", "Tweaks", "System Info", "Settings"]

    def __init__(self):
        super().__init__()
        self.title("MultiTool")
        self.geometry("1150x660")
        self.minsize(920, 540)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._current_page: customtkinter.CTkFrame | None = None
        self._nav_btns: dict[str, customtkinter.CTkButton] = {}
        self._status_after = None

        self._build_sidebar()
        self._build_statusbar()
        self._show_page("Install")

    # ── Sidebar ──────────────────────────────────────────────────────────── #

    def _build_sidebar(self):
        sidebar = customtkinter.CTkFrame(self, width=185, corner_radius=0)
        sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")
        sidebar.grid_rowconfigure(len(self._PAGES) + 1, weight=1)

        customtkinter.CTkLabel(
            sidebar, text="MultiTool",
            font=customtkinter.CTkFont(size=22, weight="bold"),
        ).grid(row=0, column=0, padx=20, pady=(28, 22))

        for i, name in enumerate(self._PAGES, start=1):
            btn = customtkinter.CTkButton(
                sidebar, text=name, width=145,
                fg_color="transparent",
                text_color=("gray15", "gray90"),
                hover_color=("gray82", "gray28"),
                command=lambda n=name: self._show_page(n),
            )
            btn.grid(row=i, column=0, padx=20, pady=4)
            self._nav_btns[name] = btn

        customtkinter.CTkLabel(
            sidebar, text="v2.0",
            text_color=("gray60", "gray50"),
            font=customtkinter.CTkFont(size=11),
        ).grid(row=len(self._PAGES) + 2, column=0, pady=(0, 14))

    def _build_statusbar(self):
        self._status_lbl = customtkinter.CTkLabel(
            self, text="", anchor="w",
            text_color=("gray50", "gray65"),
            font=customtkinter.CTkFont(size=12),
        )
        self._status_lbl.grid(row=1, column=1, sticky="ew", padx=22, pady=(2, 7))

    # ── Navigation ───────────────────────────────────────────────────────── #

    def _show_page(self, name: str):
        for page, btn in self._nav_btns.items():
            active = page == name
            btn.configure(
                fg_color=("gray76", "gray26") if active else "transparent",
            )

        if self._current_page:
            self._current_page.destroy()

        page = self._make_page(name)
        page.grid(row=0, column=1, sticky="nsew", padx=22, pady=22)
        self._current_page = page

    def _make_page(self, name: str) -> customtkinter.CTkFrame:
        match name:
            case "Install":
                return InstallPage(self, self.set_status)
            case "Tweaks":
                return TweaksPage(self, self.set_status)
            case "System Info":
                return SysInfoPage(self, self.set_status)
            case "Settings":
                return SettingsPage(
                    self, self.set_status,
                    on_appearance_change=customtkinter.set_appearance_mode,
                    on_scaling_change=lambda s: customtkinter.set_widget_scaling(
                        int(s.replace("%", "")) / 100
                    ),
                )
        raise ValueError(f"Unknown page: {name}")

    # ── Status bar ───────────────────────────────────────────────────────── #

    def set_status(self, msg: str, timeout_ms: int = 6000):
        self._status_lbl.configure(text=msg)
        if self._status_after:
            self.after_cancel(self._status_after)
        self._status_after = self.after(timeout_ms, lambda: self._status_lbl.configure(text=""))


if __name__ == "__main__":
    app = App()
    app.mainloop()
