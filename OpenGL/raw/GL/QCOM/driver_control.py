'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_QCOM_driver_control'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_QCOM_driver_control')

@_f
@_p.types(None,_cs.GLuint)
def glDisableDriverControlQCOM(driverControl):pass
@_f
@_p.types(None,_cs.GLuint)
def glEnableDriverControlQCOM(driverControl):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetDriverControlStringQCOM(driverControl,bufSize,length,driverControlString):pass
@_f
@_p.types(None,arrays.GLintArray,_cs.GLsizei,arrays.GLuintArray)
def glGetDriverControlsQCOM(num,size,driverControls):pass