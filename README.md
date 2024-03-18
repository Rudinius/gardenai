# gardenai

## Installation instructions using git:

1. Clone the repository 
`git clone https://github.com/mircorudolph/gardenai.git`

2. Create a virtual environment for installing packages outside the root folder of the cloned repository
`python -m venv .gardenai_venv`
`cd .gardenai_venv/Scripts`
`activate.bat` (for command prompt. choose script depending on console being used)

3. Navigate to the folder gardenai and install the packages of requirements.txt
`python -m pip install -r requirements.txt`

4. Start streamlit from the parent folder gardenai
`python -m streamlit run client.py`

5. The browser should open with the running application.
If not open the browser under http://localhost:8501/ or which ever is the output in the terminal.

### API Key
The API key has to be provided as an environment variable with name
`GARDENAI_API_KEY`.
The app uses gpt-3.5-turbo.
API keys can be created here: https://platform.openai.com/api-keys

## Installation instructions using Docker
1. Open CLI and pull the docker image from dockerhub `docker pull mircorudolph/gardenai-app`
2. Run the docker image `docker run -p 8501:8501 -e "GARDENAI_API_KEY=value" mircorudolph/gardenai-app`.`value` in `GARDENAI_API_KEY=value` must be replaced with a valid openai API key.
3. Open the app in a browser under adress `localhost:8501`

## Example of usage:

**General**

Providing text into the chat input field, will send the prompt to the chat agent. The response will be displayed in the text box with different icons for user or assistant.
The reset button will clear all `session_state` and reinitialize the default values. 
If an error message is provided, this typically means that no API key is provided or another error regarding the openai API occured. In this case, the terminal output of the app has to be checked.

**Example 1**

Prompt:
'I live in Alabama and my garden is sunny, dry and shaded. I prefer trees.'

Response:
'Based on your garden information and preference for trees, here is a list of possible native plants for your garden in Alabama:

1. Common Serviceberry, Downy Serviceberry, Shadbush, Juneberry, Junebush, Shadblow, Sarvis
2. Pignut Hickory, Sweet Pignut Hickory, Coast Pignut Hickory, Pignut, Sweet Pignut, Smoothbark Hickory, Broom Hickory, Red Hickory, Swamp Hickory, Switch Hickory, Switchbud Hickory
3. Green Ash, Red Ash, Swamp Ash, River Ash, Water Ash, Darlington Ash
4. American Holly, White Holly, Prickly Holly, Evergreen Holly, Christmas Holly, Yule Holly
5. Yaupon, Yaupon Holly, Cassina
6. Eastern Red Cedar, Eastern Redcedar, Virginia Juniper, Red Juniper, Pencil Cedar, Carolina Cedar, Red Savin
7. Eastern Hop-hornbeam, American Hop-hornbeam, Woolly Hop-hornbeam, Eastern Ironwood, Roughbark Ironwood, Ironwood, Deerwood, Leverwood
8. Longleaf Pine, Georgia Pine, Longleaf Yellow Pine, Southern Yellow Pine, Longstraw Pine, Hill Pine, Hard Pine, Heart Pine
9. Chickasaw Plum, Sandhill Plum
10. Mexican Plum, Bigtree Plum, Inch Plum
11. Black Cherry, Wild Black Cherry, Rum Cherry
12. White Oak, Northern White Oak, Eastern White Oak, Stave Oak, Ridge White Oak, Forked-leaf White Oak
13. Shumard Oak, Shumard's Oak, Shumard Red Oak, Southern Red Oak, Swamp Red Oak, Spotted Oak
14. Black Locust
15. American Basswood, American Linden, Lime Tree, Bee Tree

These native trees are suitable for a sunny, dry, and shaded garden in Alabama. Let me know if you need more information about any specific plant.'

Prompt:
'I am looking for a herb for my same garden instead of a tree'

Response:
'Based on your preference for a herb in a sunny and dry garden in Alabama, here are some native plant options:

1. Common Yarrow, Western Yarrow, Yarrow, Milfoil
2. Butterflyweed, Butterfly Weed, Butterfly Milkweed, Orange Milkweed, Pleurisy Root, Chigger Flower, Chiggerweed
3. Eastern Purple Coneflower, Purple Coneflower
4. Indian Blanket, Firewheel, Girasol Rojo
5. Standing Cypress, Texas Plume, Red Texas Star, Red Gilia
6. Lemon Beebalm, Purple Horsemint, Lemon Mint, Plains Horsemint, Lemon Horsemint, Horsemint, Purple Lemon Mint
7. Pink Evening Primrose, Showy Evening Primrose, Mexican Evening Primrose, Showy Primrose, Pink Ladies, Buttercups, Pink Buttercups
8. Mississippi Penstemon, Mississippi Beardtongue, Smooth White Penstemon, Smooth White Beardtongue, Talus Slope Penstemon, Talus Slope Beardtongue, Foxglove Penstemon, Foxglove 9. Beardtongue
9. Black-eyed Susan, Common Black-eyed Susan, Brown-eyed Susan, Blackeyed Susan

These native herbs are suitable for a sunny and dry garden in Alabama. Let me know if you need more information about any specific plant from the list.'

Prompt:
'The duration of the herb should be annual'

Response:
'Based on your preference for an annual herb in a sunny and dry garden in Alabama, here are some native plant options:

1. Indian Blanket, Firewheel, Girasol Rojo
2. Lemon Beebalm, Purple Horsemint, Lemon Mint, Plains Horsemint, Lemon Horsemint, Horsemint, Purple Lemon Mint
3. Black-eyed Susan, Common Black-eyed Susan, Brown-eyed Susan, Blackeyed Susan

These native annual herbs are suitable for your garden conditions in Alabama. Let me know if you need more information about any specific plant from the list.'

**The AI agent correctly filters the list based on updated user input and finally selects a subset for herbs**

**Example 2**

Prompt:
'I live in Pittsburgh'

Response:
'I'm sorry, but the information about plants is only available for the states of Michigan or Alabama. If you have a garden in Michigan or Alabama, please let me know the details about your garden.'

**The AI agent correctly hints, that the data is not available.**
