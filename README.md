# gardenai

## Installation Instructions:

1. Clone the repository 
`git clone https://github.com/Rudinius/gardenai.git`

2. Create a virtual environment for installing packages
`python -m venv .venv`
`cd .venv/Scripts`
`activate.bat` (for command prompt. choose script depending on console being used)

3. Navigate to the folder gardenai and install the packages of requirements.txt
`python -m pip install -r requirements.txt`

4. Start streamlit from the parent folder gardenai
`python -m streamlit run client.py`

5. The browser should open with the running application.
If not open the browser under http://localhost:8501/ or which ever is the output in the terminal.

## API Key
The API key has to be provided as an environment variable with name
`GARDENAI_API_KEY`.
The app uses gpt-3.5-turbo.
API keys can be created here: https://platform.openai.com/api-keys

## Example of usage:

**Example 1**

Prompt:
'I live in Alabama and my garden is sunny, dry and shaded. I prefer trees.'

Response:
'Based on the information provided for your garden in Alabama (sunny, dry, and shaded) with a preference for trees, here is a list of possible native tree plants:

Common Serviceberry, Downy Serviceberry, Shadbush, Juneberry, Junebush, Shadblow, Sarvis
Pignut Hickory, Sweet Pignut Hickory, Coast Pignut Hickory, Pignut, Sweet Pignut, Smoothbark Hickory, Broom Hickory, Red Hickory, Swamp Hickory, Switch Hickory, Switchbud Hickory
Green Ash, Red Ash, Swamp Ash, River Ash, Water Ash, Darlington Ash
American Holly, White Holly, Prickly Holly, Evergreen Holly, Christmas Holly, Yule Holly
Yaupon, Yaupon Holly, Cassina
Eastern Red Cedar, Eastern Redcedar, Virginia Juniper, Red Juniper, Pencil Cedar, Carolina Cedar, Red Savin
Eastern Hop-hornbeam, American Hop-hornbeam, Woolly Hop-hornbean, Eastern Ironwood, Roughbark Ironwood, Ironwood, Deerwood, Leverwood
Longleaf Pine, Georgia Pine, Longleaf Yellow Pine, Southern Yellow Pine, Longstraw Pine, Hill Pine, Hard Pine, Heart Pine
Chickasaw Plum, Sandhill Plum
Mexican Plum, Bigtree Plum, Inch Plum
Black Cherry, Wild Black Cherry, Rum Cherry
White Oak, Northern White Oak, Eastern White Oak, Stave Oak, Ridge White Oak, Forked-leaf White Oak
Shumard Oak, Shumard's Oak, Shumard Red Oak, Southern Red Oak, Swamp Red Oak, Spotted Oak
Black Locust
American Basswood, American Linden, Lime Tree, Bee Tree
These native tree plants are suitable for your garden in Alabama. Let me know if you need more information or have any specific preferences!'

Prompt:
'I am also looking for an annual plant.'

Response:
'Here is a list of possible native annual herb plants that may suit your garden in Alabama (sunny and dry):

Butterfly Milkweed
Black-eyed Susan
Coreopsis
Gaillardia
Purple Coneflower
Tickseed
Scarlet Sage
Blanket Flower
Eastern Red Columbine
Cardinal Flower
These native annual herbs can add color and variety to your garden. Feel free to explore these options and let me know if you need more information or have any specific preferences!'

**The AI agent correctly filters the list based on updated user input.**

**Example 2**

Prompt:
'I live in Pittsburgh'

Response:
'I'm sorry, but the information about plants is only available for the states of Michigan or Alabama. If you have a garden in Michigan or Alabama, please let me know the details about your garden.'

**The AI agent correctly hints, that the data is not available.**
