; ====================================================================================================================================
Capslock::Shift ; CapsLock giống Shift
; ====================================================================================================================================
F1:: Run, https://chat.openai.com ; Bấm F1 mở ChatGPT
; ====================================================================================================================================
^!g:: ; Bấm Ctrl + Alt + G mở Google Translate
    Send, ^c
    Sleep, 50
    ; Run, http://www.google.com/search?q=%clipboard%
    Run, https://translate.google.com/?hl=vi&sl=en&tl=vi&text=%clipboard%
Return
; ====================================================================================================================================
^!t:: ; Bấm Ctrl + Alt + T mở Command Prompt
    Run, cmd.exe 
    WinWait, ahk_class ConsoleWindowClass
    WinMove, % "ahk_id " . WinExist("A"), , 0, 0, A_ScreenWidth, A_ScreenHeight
    SendInput cd %USERPROFILE%{Enter}
    SendInput {Home}cls{Enter}
Return
; ====================================================================================================================================
