# Art_Tools
Some art tools I have built.  The main purpose of this tool is to help me know what to draw when I can't think of anything. It also helps identify practice exercise to hone my skills in drawing.

## Requirements
  - Python 3.7.2 or higher
  - To run the program you will need to ensure you have Kivy installed https://kivy.org/doc/stable/gettingstarted/installation.html
  - Be sure to install all items noted in the requirements.txt file.

## Tool Options

- Image References: 
    To enable image reference just click on add folder path and add a new folder path.  Once you have a new folder path added it will randomly generate images from that folder when you click on the folder name.  This is great for figure drawing.
    You can also specify how long you want each image to show for and how many images to display.
- Draw -- Having a hard time coming up with things to draw this is the tool for you. With the given lists it will display random things to draw.
    - Environment Generator -- Program will randomly select options from the Environments list.
    - Item Generator -- Program will randomly select how many items you tell it from the items list.
    - Character Generator -- Program will generate a random character based on these three criteria
        - Shapes (Basic shapes to use while constructing the character.)
        - Physical Nature (Male, Female, Cat, Dog, etc...)
        - distinguishing characteristic (Warlock, Cowboy, Bookworm, etc...)
    - Scene builder -- Program generates a random scene from each of the items above.
    - Edit lists -- Edit the lists the program pulls from with this option.

## Running Tests
If you want to run tests you will need to add the rootdirectory flag to the commandline.  Tests must run from the /Art_Tools/ Folder otherwise tests will not be able to find needed files to run properly. 