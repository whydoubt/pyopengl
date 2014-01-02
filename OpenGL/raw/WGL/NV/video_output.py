'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'WGL_NV_video_output'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_NV_video_output')
WGL_BIND_TO_VIDEO_RGBA_NV=_C('WGL_BIND_TO_VIDEO_RGBA_NV',0x20C1)
WGL_BIND_TO_VIDEO_RGB_AND_DEPTH_NV=_C('WGL_BIND_TO_VIDEO_RGB_AND_DEPTH_NV',0x20C2)
WGL_BIND_TO_VIDEO_RGB_NV=_C('WGL_BIND_TO_VIDEO_RGB_NV',0x20C0)
WGL_VIDEO_OUT_ALPHA_NV=_C('WGL_VIDEO_OUT_ALPHA_NV',0x20C4)
WGL_VIDEO_OUT_COLOR_AND_ALPHA_NV=_C('WGL_VIDEO_OUT_COLOR_AND_ALPHA_NV',0x20C6)
WGL_VIDEO_OUT_COLOR_AND_DEPTH_NV=_C('WGL_VIDEO_OUT_COLOR_AND_DEPTH_NV',0x20C7)
WGL_VIDEO_OUT_COLOR_NV=_C('WGL_VIDEO_OUT_COLOR_NV',0x20C3)
WGL_VIDEO_OUT_DEPTH_NV=_C('WGL_VIDEO_OUT_DEPTH_NV',0x20C5)
WGL_VIDEO_OUT_FIELD_1=_C('WGL_VIDEO_OUT_FIELD_1',0x20C9)
WGL_VIDEO_OUT_FIELD_2=_C('WGL_VIDEO_OUT_FIELD_2',0x20CA)
WGL_VIDEO_OUT_FRAME=_C('WGL_VIDEO_OUT_FRAME',0x20C8)
WGL_VIDEO_OUT_STACKED_FIELDS_1_2=_C('WGL_VIDEO_OUT_STACKED_FIELDS_1_2',0x20CB)
WGL_VIDEO_OUT_STACKED_FIELDS_2_1=_C('WGL_VIDEO_OUT_STACKED_FIELDS_2_1',0x20CC)
@_f
@_p.types(_cs.BOOL,_cs.HPVIDEODEV,_cs.HPBUFFERARB,_cs.c_int)
def wglBindVideoImageNV(hVideoDevice,hPbuffer,iVideoBuffer):pass
@_f
@_p.types(_cs.BOOL,_cs.HDC,_cs.c_int,ctypes.POINTER(_cs.HPVIDEODEV))
def wglGetVideoDeviceNV(hDC,numDevices,hVideoDevice):pass
@_f
@_p.types(_cs.BOOL,_cs.HPVIDEODEV,ctypes.POINTER(_cs.c_ulong),ctypes.POINTER(_cs.c_ulong))
def wglGetVideoInfoNV(hpVideoDevice,pulCounterOutputPbuffer,pulCounterOutputVideo):pass
@_f
@_p.types(_cs.BOOL,_cs.HPVIDEODEV)
def wglReleaseVideoDeviceNV(hVideoDevice):pass
@_f
@_p.types(_cs.BOOL,_cs.HPBUFFERARB,_cs.c_int)
def wglReleaseVideoImageNV(hPbuffer,iVideoBuffer):pass
@_f
@_p.types(_cs.BOOL,_cs.HPBUFFERARB,_cs.c_int,ctypes.POINTER(_cs.c_ulong),_cs.BOOL)
def wglSendPbufferToVideoNV(hPbuffer,iBufferType,pulCounterPbuffer,bBlock):pass