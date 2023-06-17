import QtQuick 2.10
import QtQuick.Window 2.10
import QtQuick.Controls 2.13

Window {
    id: mainWindow

    width: 1000
    height: 720
    visible: true
    title: qsTr("VisualSense [PROTOTYPE]")

    property string imageSource: "../ui/assets/images/dslr-camera-logo-design-png.png"

    Connections{
        target: backend

        function onFrameChanged(){
            imageSource = "image://webcam/refresh"
            imageSource = "image://webcam/webcam"
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
                    id: processingContainer
                    x: 26
                    y: 260
                    width: 248
                    height: 396
                    color: "#232020"

                    Text {
                        id: brightnessTag
                        x: 27
                        y: 35
                        color: "#ffffff"
                        text: qsTr("Brightness")
                        font.pixelSize: 12
                    }

                    Slider {
                        id: brightnessSlider
                        x: 27
                        y: 75
                        height: 20
                        snapMode: Slider.SnapAlways
                        stepSize: 2
                        to: 10
                        from: -10
                        value: 0.5
                        onMoved: {
                            brightnessValue.text = value
                        }
                    }

                    TextInput {
                        id: brightnessValue
                        x: 183
                        y: 35
                        width: 44
                        height: 20
                        color: "#ffffff"
                        text: qsTr("0")
                        verticalAlignment: Text.AlignVCenter
                        horizontalAlignment: Text.AlignRight
                        inputMask: "###"
                        font.pixelSize: 12

                        onEditingFinished: {
                            brightnessSlider.value = text
                        }
                    }

                    Text {
                        id: sharpenTag
                        x: 27
                        y: 138
                        color: "#ffffff"
                        text: qsTr("Sharpen")
                        font.pixelSize: 12
                    }

                    Slider {
                        id: sharpenSlider
                        x: 27
                        y: 178
                        snapMode: Slider.SnapAlways
                        stepSize: 2
                        to: 10
                        from: -10
                        value: 0.5

                        onMoved: {
                            sharpenValue.text = value
                        }
                    }

                    TextInput {
                        id: sharpenValue
                        x: 183
                        y: 138
                        width: 44
                        height: 20
                        color: "#ffffff"
                        text: qsTr("0")
                        verticalAlignment: Text.AlignVCenter
                        horizontalAlignment: Text.AlignRight
                        inputMask: "###"
                        font.pixelSize: 12

                        onEditingFinished: {
                            if(parseInt(text)%2 > 0){
                                sharpenSlider.value = parseInt(text) + 1
                                text = parseInt(text) + 1
                            }else{
                                sharpenSlider.value = parseInt(text)
                            }
                        }
                    }

                    Button {
                        id: applyButton
                        x: 77
                        y: 276
                        text: qsTr("Apply")
                        onPressed: {
                            backend.apply_image_corrections(brightnessSlider.value, sharpenSlider.value)
                        }
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
            source: mainWindow.imageSource
        }
    }
}
