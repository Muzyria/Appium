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

    """Menu Settings"""
    BUTTON_CANCEL_MENU_SETTINGS = (By.ID, 'com.l1inc.yamatrack3d:id/imageButtonCancel')
    TEXT_VIEW_MENU_SETTINGS_TITLE = (By.ID, 'com.l1inc.yamatrack3d:id/textViewCaption')

    BUTTON_ASSET_DETAILS_MENU_SETTINGS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView')
    BUTTON_CLEAR_SCORECARD_END_ROUND_MENU_SETTINGS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView')
    BUTTON_DEMO_MODE_MENU_SETTINGS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView')
    BUTTON_UPDATES_MENU_SETTINGS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView')
    BUTTON_REQUEST_LOG_FILES_MENU_SETTINGS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.TextView')
    BUTTON_GPS_STATIC_HOLD_MENU_SETTINGS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.TextView')
    BUTTON_TABLET_SETTINGS_MENU_SETTINGS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.TextView')
    BUTTON_EXIT_APPLICATION_MENU_SETTINGS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[8]/android.widget.LinearLayout/android.widget.TextView')
    BUTTON_FULL_APP_RESET_MENU_SETTINGS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[9]/android.widget.LinearLayout/android.widget.TextView')
    """ - """

    """Asset_details"""
    BUTTON_CANCEL_ASSET_DETAILS = (By.ID, 'com.l1inc.yamatrack3d:id/imageButtonCancel')
    TEXT_VIEW_ASSET_DETAILS_TITLE = (By.ID, 'com.l1inc.yamatrack3d:id/textViewCaption')
    TEXT_VIEW_NAME_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]')
    TEXT_VIEW_NAME_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]')
    TEXT_VIEW_TRACKER_ID_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[3]')
    TEXT_VIEW_TRACKER_ID_VALUE_ASSET_DETAILS = (By.ID, 'com.l1inc.yamatrack3d:id/textViewTrackerId')
    TEXT_VIEW_ASSET_TYPE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]')
    TEXT_VIEW_ASSET_TYPE_VALUE_ASSET_DETAILS = (By.ID, 'com.l1inc.yamatrack3d:id/textViewAssetType')
    TEXT_VIEW_STATUS_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[3]')
    TEXT_VIEW_STATUS_VALUE_ASSET_DETAILS = (By.ID, 'com.l1inc.yamatrack3d:id/textViewStatus')
    #
    TEXT_VIEW_SERIAL_NUMBER_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_SERIAL_NUMBER_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_AMP_HOURS_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_AMP_HOURS_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_CART_BATTERY_VOLTAGE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_CART_BATTERY_VOLTAGE_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_BATTERY_VOLTAGE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_BATTERY_VOLTAGE_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_CABLE_VOLTAGE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_CABLE_VOLTAGE_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_TOTAL_HOURS_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_TOTAL_HOURS_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_TOTAL_MILES_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_TOTAL_MILES_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_MCU_MODE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_MCU_MODE_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_MCU_SOFTWARE_VERSION_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_MCU_SOFTWARE_VERSION_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_MOTOR_TYPE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_MOTOR_TYPE_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_APPLICATION_VERSION_APK_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_APPLICATION_VERSION_APK_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_OS_VERSION_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_OS_VERSION_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_KERNEL_VERSION_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_KERNEL_VERSION_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_CABLE_FIRMWARE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_CABLE_FIRMWARE_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_GPS_FIRMWARE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_GPS_FIRMWARE_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.TextView[2]')
    TEXT_VIEW_IMEI_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.TextView[1]')
    TEXT_VIEW_IMEI_VALUE_ASSET_DETAILS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.TextView[2]')
    """ - """

    """Clear ScoreCard / End Round"""
    BUTTON_CANCEL_CLEAR_SCORECARD = (By.ID, 'com.l1inc.yamatrack3d:id/imageButtonCancel')
    TEXT_VIEW_CLEAR_SCORECARD_TITLE = (By.ID, 'com.l1inc.yamatrack3d:id/textViewCaption')
    TEXT_VIEW_CLEAR_SCORECARD_MESSAGE = (By.ID, 'com.l1inc.yamatrack3d:id/textViewMessage')

    BUTTON_YES_CLEAR_SCORECARD = (By.ID, 'com.l1inc.yamatrack3d:id/buttonYes')
    BUTTON_NO_CLEAR_SCORECARD = (By.ID, 'com.l1inc.yamatrack3d:id/buttonNo')
    """ - """

    """Demo Mode"""
    BUTTON_CANCEL_DEMO_MODE = (By.ID, 'com.l1inc.yamatrack3d:id/imageButtonCancel')
    TEXT_VIEW_DEMO_MODE_TITLE = (By.ID, 'com.l1inc.yamatrack3d:id/textViewCaption')

    BUTTON_YES_DEMO_MODE = (By.ID, 'com.l1inc.yamatrack3d:id/buttonYes')
    BUTTON_NO_DEMO_MODE = (By.ID, 'com.l1inc.yamatrack3d:id/buttonNo')
    TEXT_VIEW_YES_LABEL = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView')
    TEXT_VIEW_NO_LABEL = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView')
    """ - """

    """Updates"""
    BUTTON_CANCEL_UPDATES = (By.ID, 'com.l1inc.yamatrack3d:id/imageButtonCancel')
    TEXT_VIEW_UPDATES_TITLE = (By.ID, 'com.l1inc.yamatrack3d:id/textViewCaption')

    BUTTON_UPDATE_ALL_SETTINGS_MENU_UPDATES = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView')
    BUTTON_UPDATE_ADVERTISEMENTS_MENU_UPDATES = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView')
    BUTTON_UPDATE_PIN_LOCATIONS_MENU_UPDATES = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView')
    BUTTON_UPDATE_FOOD_BEVERAGE_MENU_MENU_UPDATES = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView')
    BUTTON_UPDATE_YAMATRACK_APPLICATION_MENU_UPDATES = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.TextView')
    BUTTON_UPDATE_TOURNAMENTS_MENU_UPDATES = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.TextView')
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
