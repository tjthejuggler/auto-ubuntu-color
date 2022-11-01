import os
import time
#SAVE THIS TO GITHUB ASAP!
#Required startup command for this to run when the habitsCounter file changes
# watchmedo shell-command     --patterns='totalHabitCount.txt'     --recursive     --command='python3 /home/lunkwill/projects/auto-ubuntu-color/main.py'

#hook this up to watchdog so that when the habits counters change, the color changes
# first just mimic the colors that i use on phone, but if i can get the tasker guy to make
# more icon colors then maybe do colors of rainbow (maybe even do it as best i can if he doesn't)
file = '/home/lunkwill/Documents/obsidian_note_vault/noteVault/habitCounters/totalHabitCount.txt'
#get the text from the file
with open(file, 'r') as f:
    lines = f.readlines()
#convert the first line to an int
habit_count = int(lines[0])
#gtk-theme, icon-theme (*** maybe both of these should be Yaru-COLOR-dark)
#orange Yaru-dark, Yaru (maybe orange should be in there like the other colors)
#brown Yaru-bark-dark, Yaru-bark

icon_theme = 'Yaru-red-dark'
gtk_theme = 'Yaru-red-dark'
#blue, orange, green, red, gold, silver, clear, light blue
#orange, olive, red, bark, sage
#red, bark, sage, orange, green, viridian, prussiangreen, blue, purple, magenta


#switch the theme based on the habit count
if habit_count > 6:
    icon_theme = 'Yaru-bark-dark'
    gtk_theme = 'Yaru-bark-dark'
if habit_count > 13:
    icon_theme = 'Yaru'
    gtk_theme = 'Yaru-dark'
if habit_count > 20:  
    icon_theme = 'Yaru-olive'
    gtk_theme = 'Yaru-olive-dark' 
if habit_count > 27:
    icon_theme = 'Yaru-viridian-dark'
    gtk_theme = 'Yaru-viridian-dark'
if habit_count > 34:
    icon_theme = 'Yaru-prussiangreen'
    gtk_theme = 'Yaru-prussiangreen-dark'
if habit_count > 41:
    icon_theme = 'Yaru-blue-dark'
    gtk_theme = 'Yaru-blue-dark'
if habit_count > 48:
    icon_theme = 'Yaru-purple-dark'
    gtk_theme = 'Yaru-purple-dark'
if habit_count > 55:
    icon_theme = 'Yaru-magenta'
    gtk_theme = 'Yaru-magenta-dark'


os.system("dconf write /org/gnome/desktop/interface/icon-theme \"'"+icon_theme+"'\"")
os.system("dconf write /org/gnome/desktop/interface/gtk-theme \"'"+gtk_theme+"'\"")
os.system("dconf write /org/gnome/desktop/interface/color-scheme \"'prefer-light'\"")
time.sleep(1)
os.system("dconf write /org/gnome/desktop/interface/color-scheme \"'prefer-dark'\"")

#terminal command to set a watch on the file
#watchmedo shell-command     --patterns="totalHabitCount.txt"     --recursive     --command='echo "${watch_src_path}"'

#i think i can get this to run a python script instead of just a terminal command

#i need a terminal command or a way to shutdown a watchmedo so it doesnt clog up inotify
#view it with this
#find /proc/*/fd -lname anon_inode:inotify |    cut -d/ -f3 |    xargs -I '{}' -- ps --no-headers -o '%p %U %c' -p '{}' |    uniq -c |    sort -nr

