# angm2305-f25-final-project

## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: https://github.com/reezi143/angm2305-f25-final-project.git

## Description

Your readme file should be a few paragraphs in length and explain what your project is, what do the different files you included in your repository contain or does, any design considerations, future areas of improvements, etc. It’s your written explanation of your project, so take pride in it.

My project is a music player, that plays a selected mp3 from a specified folder; the application contains buttons to load a playlist, play a song, pause a song, skip a song, and rewind a song. The music player also display's the currently playing song's filename. 

The additional files in the "src" directory include "icon.png," "play.png," "pause.png," "skip.png," "prev.png" and an additional folder titled "playlist." The file "icon.png" is the image used as a rerplacement for the default Tkinter app icon photo. The remaining files are used as the icons for the player's control buttons. The folder "playlist" holds the songs for the music player to load and play.

For the application's design, I wanted It to look like an mp3 player, which is why the app is longer than it is wide, and has the main control buttons arranged in a circular manner. Colorwise, I wanted something soft, muted, and pink to reflect the atmosphere of some of the songs I downloaded

In regards to firure areas of improvement, as it currently stands, the "skip_song" function does not work as intended; when a song x is skipped, the selection of the next song, song y, is not processed automatically even though song y is playing--the selection highlight remains on the previously played song, song x, and pressing the skip button again will only restart song y, instead of moving on to song z. However, after to skipping to song y, if I were to select song y with my cursor, it becomes highlighted, and pressing the skip button will move on to song z--though this results in the same issue. If I were to work on this more in the future, having the function execute the task properly, is something I'd like to fix. In the same vein, as the skip function isn't properly registering the current song, the names of the song aren't being displayed properly when the skip button is used; "song x" will be shown when skipped to song y, "song y" will be shown when skipped to song z, etc. Additionally, I would like to add a feature that automatically plays song y once song x is finished, as that is something I was not able to figure out, but would like to spend more time on. I'd also like to try getting the "rewind" button to go from song y to song x, in addition to going back to the begining of the currently selected song. 