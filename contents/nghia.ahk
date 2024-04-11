; ====================================================================================================================================
Capslock::Shift ; CapsLock giống Shift
; ====================================================================================================================================
F1:: Run, https://chat.openai.com ; Bấm F1 mở ChatGPT
;F3:: Run, https://github.com/vvn20206205?tab=repositories&q=&type=public&language=&sort= ; Bấm F3 mở github

; F8:: Run, "C:\Users\vvn20206205\Desktop\einvoice-system\README.md"
; F9:: Run, "C:\Users\vvn20206205\Desktop\einvoice-system\einvoice-system.code-workspace"

; F12:: Run, "C:\Users\vvn20206205\Downloads\Video\a.lnk"
; ====================================================================================================================================
^!g:: ; Bấm Ctrl + Alt + G mở       Google Translate
    Send, ^c
    Sleep, 50
    ; Run, http://www.google.com/search?q=%clipboard%
    Run, https://translate.google.com/?hl=vi&sl=en&tl=vi&text=%clipboard%
return

; ====================================================================================================================================
;RButton::  
; F4:: 
    ;Run, "C:\Users\vvn20206205\Downloads\Programs\AutoHotkey\file1.md"
    ; Run, "C:\Users\vvn20206205\Desktop\py\video\main.bat"
; return
; ====================================================================================================================================

^!t:: ; Ctrl + Alt + T  
    Run, cmd.exe ; Mở Command Prompt, thay đổi thành câu lệnh của terminal của bạn nếu cần
Return
; ====================================================================================================================================
