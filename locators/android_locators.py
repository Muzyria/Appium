from appium.webdriver.common.appiumby import By


class MainScreenLocators:
    """Screen Play Golf"""
    BUTTON_MENU = (By.ID, 'com.l1inc.yamatrack3d:id/buttonMenu')
    BUTTON_HOLE = (By.ID, 'com.l1inc.yamatrack3d:id/buttonHole')
    TEXT_VIEW_PAR = (By.ID, 'com.l1inc.yamatrack3d:id/textViewPar')
    TEXT_VIEW_PACE = (By.ID, 'com.l1inc.yamatrack3d:id/textViewPaceStatus')
    BUTTON_FLAG = (990, 90)  # x, y
    BUTTON_TIME = (By.ID, 'com.l1inc.yamatrack3d:id/textViewTime')
    BUTTON_LANGUAGE = (By.ID, 'com.l1inc.yamatrack3d:id/imageViewLanguage')
    BUTTON_FLYOVER = (By.ID, 'com.l1inc.yamatrack3d:id/textViewFlyover')
    BUTTON_GREEN_VIEW = (By.ID, 'com.l1inc.yamatrack3d:id/textViewGreenView')
    BUTTON_SHOT_DISTANCE = (By.ID, 'com.l1inc.yamatrack3d:id/textViewShotDistance')
    BUTTON_SCORECARD = (By.ID, 'com.l1inc.yamatrack3d:id/textViewScorecard')
    BUTTON_FOOD_AND_DRINK = (By.ID, 'com.l1inc.yamatrack3d:id/textViewFoodAndDrink')
    TEXT_VIEW_NO_ACTIVE_DOWNLOADS = (By.ID, 'com.l1inc.yamatrack3d:id/textViewNoActiveDownloads')

    BUTTON_AUTO_UPDATE_APK = (By.ID, 'com.l1inc.yamatrack3d:id/autoUpdateCellApk')
    BUTTON_AUTO_UPDATE_OS = (By.ID, 'com.l1inc.yamatrack3d:id/autoUpdateCellOs')


class MenuScreenLocators:
    BUTTON_PLAY_GOLF = (By.ID, 'com.l1inc.yamatrack3d:id/linearLayoutPlayGolf')
    BUTTON_SEND_MESSAGE = (By.ID, 'com.l1inc.yamatrack3d:id/linearLayoutSendMessage')
    BUTTON_SETTINGS = (By.ID, 'com.l1inc.yamatrack3d:id/linearLayoutSettings')


class SendMessageLocators:
    @staticmethod
    def SELECT_MESSAGE_BY_NUMBER(n):
        return (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[{n}]/android.widget.LinearLayout/android.widget.TextView")

    SEND_MESSAGE_BUTTON_YES = (By.ID, 'com.l1inc.yamatrack3d:id/buttonYes')
    SEND_MESSAGE_BUTTON_NO = (By.ID, 'com.l1inc.yamatrack3d:id/buttonNo')
    SEND_MESSAGE_BUTTON_CANCEL = (By.ID, 'com.l1inc.yamatrack3d:id/imageButtonCancel')


class SettingsLocators:
    @staticmethod
    def BUTTON_NUMBER(number):
        return (By.ID, f"com.l1inc.yamatrack3d:id/button{number}")

    BUTTON_SUBMIT = (By.ID, "com.l1inc.yamatrack3d:id/buttonSubmit")
    FIELD_ENTER_PASSWORD = (By.ID, "com.l1inc.yamatrack3d:id/textViewPasscode")
    ASSET_DETAILS = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView")
    @staticmethod
    def SELECT_SETTINGS_BY_NUMBER(number):
        return (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[{number}]/android.widget.LinearLayout/android.widget.TextView")


class AssetDetailsLocators:
    CART_NAME = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]")
    DEVICE_ID = (By.ID, "com.l1inc.yamatrack3d:id/textViewTrackerId")
    @staticmethod
    def SELECT_ASSET_DETAILS_KEY_BY_NUMBER(number):
        return (By.XPATH,
                f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[{number}]/android.widget.LinearLayout/android.widget.TextView[1]")
    @staticmethod
    def SELECT_ASSET_DETAILS_VALUE_BY_NUMBER(number):
        return (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[{number}]/android.widget.LinearLayout/android.widget.TextView[2]")


class SelectLanguageLocators:
    BUTTON_CANCEL = (By.ID, 'com.l1inc.yamatrack3d:id/imageButtonCancel')

    @staticmethod
    def SELECT_LANGUAGE_BY_NUMBER(n):
        return (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[{n}]/android.widget.LinearLayout/android.widget.TextView")
