import QtQuick 2.10
import QtQuick.Window 2.10
import QtQuick.Controls 2.13

Window {
    id: mainWindow

    width: 1000
    height: 720
    visible: true
    title: qsTr("VisualSense [PROTOTYPE]")

    Connections{
        target: backend

        function onFrameChanged(){
            imageDisplay.source = "../ui/assets/images/camera-desk-device-electronics.jpg"
            imageDisplay.source = "image://webcam/webcam"
        }
    }


    Rectangle{
        id: base

        anchors.fill: parent
        color: "#343337"

        Rectangle{
            id: leftBar

            width: 300
            color: "#28252b"
            anchors {left: base.left;
                top: base.top;
                bottom: base.bottom}

                Button {
                    id: startStopButton

                    property bool isStarted: false

                    function startStopToggle(){
                        if(isStarted){
                            backend.stop_cap()
                            startStopButton.text = qsTr("Start")
                            isStarted = false
                        }else{
                            backend.start_cap()
                            startStopButton.text = qsTr("Stop")
                            isStarted = true
                        }
                    }

                    x: 74
                    y: 146
                    text: qsTr("Start")
                    anchors.horizontalCenter: parent.horizontalCenter
                    onClicked: startStopToggle()


                }

                ComboBox {
                    id: comboBox
                    x: 27
                    y: 66
                    width: 197
                    height: 40
                    anchors.horizontalCenter: parent.horizontalCenter

                    model: ["Webcam", "None"]
                }

                Rectangle {
                    id: rectangle
                    x: 26
                    y: 260
                    width: 248
                    height: 396
                    color: "#232020"

                    Text {
                        id: element
                        x: 27
                        y: 35
                        color: "#ffffff"
                        text: qsTr("Brightness")
                        font.pixelSize: 12
                    }

                    Slider {
                        id: slider
                        x: 27
                        y: 75
                        height: 20
                        value: 0.5
                    }

                    Text {
                        id: element1
                        x: 27
                        y: 138
                        color: "#ffffff"
                        text: qsTr("Sharpen")
                        font.pixelSize: 12
                    }

                    Slider {
                        id: slider1
                        x: 27
                        y: 178
                        value: 0.5
                    }
                }
        }

        Image {
            id: imageDisplay
            anchors.left: leftBar.right
            anchors.leftMargin: 20
            anchors.right: parent.right
            anchors.rightMargin: 20
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 50
            anchors.top: parent.top
            anchors.topMargin: 50
            fillMode: Image.PreserveAspectFit
            source: "../ui/assets/images/dslr-camera-logo-design-png.png"
        }
    }
}
