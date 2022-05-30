# Rapyd-checkout-page-ue4
Integrating rapyd checkout page with cloud streaming game powered by unreal engine

# Game
1. The game uses third person template from unreal engine
2. We created a modular city package map as the default game map. The map is available free from unreal market place.
3. Created custom 3D metahuman from metahuman editor and is mapped with the throd person template mannequin skeleton.
4. Created thrid person and first person camera swapping feature.
5. Created Gold coins and coin counter feature along with VARest plugin for REST Api integration.
![alt text](./screenshots/1.jpg)
## RESTful API integration on game
1. The Lambda functions are on **LambdaFunctions** folder with Rapyd ID creation for guests, putting the Rapyd ID along with success or failure boolean values(0&1) on dynamodb database, getting values and much more.
![alt text](./screenshots/2.jpg)
## Running the app. 
1. The app can be run with standard support on pixel streaming. https://docs.unrealengine.com/5.0/en-US/pixel-streaming-in-unreal-engine/
2. download https://drive.google.com/file/d/1LQpZbCzgXRD4-sHFwFCGkCWPOmBJGBqL/view?usp=sharing and move the file to **./Rapyd-checkout-page-ue4\Game\WindowsNoEditor\thirdpersonvr\Content\Paks**
3. download https://drive.google.com/file/d/1T2eUEkGNdLRKjWFEbuvnOUbPvD64DGL5/view?usp=sharing and move to **./Rapyd-checkout-page-ue4\Game\WindowsNoEditor\thirdpersonvr\Binaries\Win64**
![alt text](./screenshots/3.jpg)
![alt text](./screenshots/4.jpg)
## VR Box support
1. The app support Google VR plugin with VR controller for joystick control

![alt text](./screenshots/5.jpg)
