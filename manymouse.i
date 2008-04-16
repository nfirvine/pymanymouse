%module manymouse
%{
#include "manymouse.h"
%}

%rename(__version__)        MANYMOUSE_VERSION;
%rename(EVENT_ABSMOTION)    MANYMOUSE_EVENT_ABSMOTION;
%rename(EVENT_RELMOTION)    MANYMOUSE_EVENT_RELMOTION;
%rename(EVENT_BUTTON)       MANYMOUSE_EVENT_BUTTON;
%rename(EVENT_SCROLL)       MANYMOUSE_EVENT_SCROLL;
%rename(EVENT_DISCONNECT)   MANYMOUSE_EVENT_DISCONNECT;
%rename(EVENT_MAX)          MANYMOUSE_EVENT_MAX;
%rename(EventTypes)         ManyMouseEventType;
%rename(Event)              ManyMouseEvent;
%rename(init)               ManyMouse_Init;
%rename(quit)               ManyMouse_Quit;
%rename(device_name)        ManyMouse_DeviceName;
%rename(poll_event)         ManyMouse_PollEvent;



%include "manymouse.h"


