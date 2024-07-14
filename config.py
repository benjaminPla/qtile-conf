# https://docs.qtile.org/en/latest/manual/config/lazy.html
from libqtile import bar, layout, widget
from libqtile.config import Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    # move windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),
    # lauch terminal
    Key([mod], "Return", lazy.spawn(terminal)),
    # reload config
    Key([mod, "control"], "r", lazy.reload_config()),
    # search
    Key([mod], "space", lazy.spawncmd()),
    # others
    Key([mod], "w", lazy.window.kill()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    # brightness
    Key([mod], "Down", lazy.spawn("/usr/local/bin/set_brightness.sh 1000")),
    Key([mod], "Up", lazy.spawn("/usr/local/bin/set_brightness.sh 4000")),
]

groups = [Group(i) for i in "123456789"]
for i in groups:
    keys.extend(
        [
            # switch group
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            # switch group and move
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        ]
    )

layouts = [
    layout.Columns(
        border_normal="#222", border_focus="#555", border_width=1, margin=20
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    hide_unused=True,
                    highlight_method="text",
                    this_current_screen_border="#ff0",
                ),
                widget.Spacer(),
                widget.Prompt(prompt=""),
                widget.Clock(format="%d/%m/%y | %H:%M"),
                # widget.QuickExit(default_text='X', countdown_format='{}'),
            ],
            25,
        ),
    ),
]

follow_mouse_focus = False
bring_front_click = False
