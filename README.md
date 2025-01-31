# Roku Remote Python Script

The remote that came with the Roku streaming stick is showing some wear. Replacements are $30 CAD so it seemed like a good 
idea to find an alternative to reduce the rate of wear on the remote. The computer apps I looked at require mouse clicks. One does
not want to be looking at the computer screen when controlling the Roku and TV so I would perfer an app that is controlled by the keyboard and not a mouse.
Some consideration was given to making a DYI remote but in investigating that it became apparent it would be possible to make a simple Python script that 
can control the Roku. Since I use a split keyboard, with a only 21 keys per side, it is easy to use the keyboard without looking at it.

![](image/keys.png)

This is essentially the first layer of this keyboard. The alternate functions of the keys in this case only are in effect when the python script has focus.

Below is a screenshot of the Anaconda window. The app was written for use in windows and would need adjustment for other operating systems.

![](commandLine.png)

## Roku Settings

As of January 2025 the roku received an update. It no longer responded to ECP kepresses by default. Changing the 
"Control by mobile apps" to **Enabled** rather than the now default **limited** fixed the issue.

[Wi-Fi-connectivity/No-more-ECP](https://community.roku.com/t5/Wi-Fi-connectivity/No-more-ECP-or-how-to-loses-customers-in-a-single-update/td-p/1033350)

![](image/settings.png)

## Exploring Using Curl on the Command Line

Roku has published information on controlling Roku devices via WiFi at:

[external-control-api.md](https://developer.roku.com/en-ca/docs/developer-program/dev-tools/external-control-api.md)

On a computer one can send commands to a Roku using curl. For example:

````
C:\Users\xxx>curl http://192.168.0.25:8060/query/apps
````

* Note that one needs to replace the IP address with the IP address for their own Roku.
* The port 8060 should be correct for all Roku devices that permit use of WiFi for control as far as I am aware

The Roku will respond with a list of apps. The list includes the app-id for each app. This id can be used to 
launch the individual apps with another command:

````
C:\Users\xxx>curl -d '' http://192.168.0.25:8060/launch/837
````

That will launch the YouTube app.

### Examples of remote keypress emulation

~~~~
C:\Users\xxx>curl -d '' http://192.168.0.25:8060/keypress/Setect

C:\Users\xxx>curl -d '' http://192.168.0.25:8060/keypress/Home

C:\Users\xxx>curl -d '' http://192.168.0.25:8060/keypress/Left

C:\Users\xxx>curl -d '' http://192.168.0.25:8060/keypress/Right
~~~~

## Using a Simple Python Script

Looking for a simple Python script for controlling a Roku I came across:

[Roku-control-client-for-Python/td-p/395718](https://community.roku.com/t5/Roku-Developer-Program/Roku-control-client-for-Python/td-p/395718)

The code was old and written for python 2. A utility was used to convert the code to work in python 3.
The code obtain provided functions that could be used to interact with a Roku. A control loop was added that would
respond to single character key presses on a computer keyboard and send commands to the Roku. Note that the script 
is active when the command window has focus.

The script can be launched with a batch file. I use an Anaconda terminal as shown in the screen shot.

The script is exited by pressing the **Tab** key.

### Typing Text

Filling text into search screens with a real keyboard is a lot more efficient than using a remote. The script switches to fill text mode
after pressing the **f** key. 

To exit the fill text mode press the **Return** key.

The text input interface is not consistent in all Roku applications. The text entry in this script is working with YouTube, Netflix and Roku but not
working in Prime video and possibly others. In those cases one needs to revert to using the interface in the same way they would with the original remote, which 
is to say when the keyboard text input interface is not working one needs to revert to the on screen keyboard. In all cases one can send basic characters and numerals 
but generally not most symbols or white space. To send a space in all cases one needs to use the one screen keyboard.

### YouTube Lingering Select

In the YouTube app holding the remote OK key will bring up additional options. Options like **Don't recomend this channel**. 
Holding the Select key does not work the same way but sending keydown rather then keypress on the Select does bring the options up. This Python 
script will do this if one uses the capital K. Use the lower case k for normal select.
