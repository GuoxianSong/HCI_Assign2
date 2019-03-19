#-------------------------------------------------
#
# Project created by QtCreator 2017-08-16T09:37:36
#
#-------------------------------------------------
QT     += core gui
QT += network widgets
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets opengl
TEMPLATE = app
CONFIG += console
CONFIG += c++11

DEFINES += QT_DEPRECATED_WARNINGS
TARGET = 3DFrameWork

SOURCES += \
           main.cpp \
        mainwindow.cpp \
    HE_mesh/Mesh3D.cpp \
    renderingwidget.cpp \
    MiniSurf.cpp \
    ArcBall.cpp   



HEADERS  += mainwindow.h \
    renderingwidget.h \
    MiniSurf.h \
    HE_mesh/Mesh3D.h \
    ArcBall.h \
    globalFunctions.h \
    HE_mesh/Vec.h  


FORMS    += mainwindow.ui

RESOURCES += \
    mainwindow.qrc



DEPENDPATH += ...



INCLUDEPATH += /usr/local/include/opencv \
               /usr/local/include/opencv2 

LIBS += -L/usr/local/lib

LIBS +=  -lglut -lGLU -lGL

LIBS += -L/usr/local/lib -lopencv_core -lopencv_imgcodecs -lopencv_highgui -lopencv_imgproc -lopencv_aruco

LIBS += -L/usr/local/lib -lopencv_calib3d -lopencv_contrib -lopencv_features2d -lopencv_flann

LIBS += -L/usr/local/lib -lopencv_legacy -lopencv_ml -lopencv_objdetect -lopencv_photo -lopencv_stitching

LIBS += -L/usr/local/lib -lopencv_superres -lopencv_ts -lopencv_video  -lopencv_videostab  -lopencv_videoio


LIBS += -lOpenMeshCore 

INCLUDEPATH += $$PWD/../../../../../usr/local/include
DEPENDPATH += $$PWD/../../../../../usr/local/include
