from appium.webdriver.common.appiumby import By


class MainScreen:
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
    """ - """

    """Screen Buttons Menu (Second Screen after press button Menu)"""
    BUTTON_PLAY_GOLF = (By.ID, 'com.l1inc.yamatrack3d:id/linearLayoutPlayGolf')
    BUTTON_SELECT_HOLE = (By.ID, 'com.l1inc.yamatrack3d:id/linearLayoutSelectHole')
    BUTTON_SCORECARD_2 = (By.ID, 'com.l1inc.yamatrack3d:id/linearLayoutScorecard')
    BUTTON_SELECT_COURSE = (By.ID, 'com.l1inc.yamatrack3d:id/linearLayoutChangeCourse')
    BUTTON_SEND_MESSAGE = (By.ID, 'com.l1inc.yamatrack3d:id/linearLayoutSendMessage')
    BUTTON_BLUETOOTH = (By.ID, 'com.l1inc.yamatrack3d:id/linearLayoutBluetooth')
    BUTTON_METERS = (By.ID, 'com.l1inc.yamatrack3d:id/linearLayoutYardsMeters')
    BUTTON_SETTINGS = (By.ID, 'com.l1inc.yamatrack3d:id/linearLayoutSettings')
    """ - """

    """Screen Enter Passcode (Screen after press button Settings)"""
    TEXT_VIEW_ENTER_PASSCODE = (By.ID, 'com.l1inc.yamatrack3d:id/textViewPasscode')
    BUTTON_1 = (By.ID, 'com.l1inc.yamatrack3d:id/button1')
    BUTTON_2 = (By.ID, 'com.l1inc.yamatrack3d:id/button2')
    BUTTON_3 = (By.ID, 'com.l1inc.yamatrack3d:id/button3')
    BUTTON_4 = (By.ID, 'com.l1inc.yamatrack3d:id/button4')
    BUTTON_5 = (By.ID, 'com.l1inc.yamatrack3d:id/button5')
    BUTTON_6 = (By.ID, 'com.l1inc.yamatrack3d:id/button6')
    BUTTON_7 = (By.ID, 'com.l1inc.yamatrack3d:id/button7')
    BUTTON_8 = (By.ID, 'com.l1inc.yamatrack3d:id/button8')
    BUTTON_9 = (By.ID, 'com.l1inc.yamatrack3d:id/button9')
    BUTTON_0 = (By.ID, 'com.l1inc.yamatrack3d:id/button0')
    BUTTON_CLEAR = (By.ID, 'com.l1inc.yamatrack3d:id/buttonClear')
    BUTTON_CANCEL = (By.ID, 'com.l1inc.yamatrack3d:id/buttonCancel')
    BUTTON_SUBMIT = (By.ID, 'com.l1inc.yamatrack3d:id/buttonSubmit')

    TEXT_VIEW_CAPTION_WRONG_PASSCODE_TITLE = (By.ID, 'com.l1inc.yamatrack3d:id/textViewCaption')
    TEXT_VIEW_CAPTION_WRONG_PASSCODE_MESSAGE = (By.ID, 'com.l1inc.yamatrack3d:id/textViewMessage')
    BUTTON_OK_VIEW_CAPTION_WRONG_PASSCODE = (By.ID, 'com.l1inc.yamatrack3d:id/buttonOk')
    """ - """


    """android widget password to menu"""
    ANDROID_WIDGET_PASSWORD = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.EditText')
    ANDROID_WIDGET_BUTTON_CANCEL = (By.ID, 'android:id/button2')
    ANDROID_WIDGET_BUTTON_OK = (By.ID, 'android:id/button1')

    """Buttons android widget menu"""
    ANDROID_WIDGET_MENU_BUTTON_STANDBY = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]')
    ANDROID_WIDGET_MENU_BUTTON_POWER_OFF = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]')
    ANDROID_WIDGET_MENU_BUTTON_RESTART = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]')
    ANDROID_WIDGET_MENU_BUTTON_SHIP_MODE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]')
    """ - """


el = MainScreen()
print(f'{el.ANDROID_WIDGET_PASSWORD}')






