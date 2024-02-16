import QtQuick
import QtLocation
import QtPositioning

Item {
    property var route1Points: []
    property var route2Points: []

    function updateMapView() {
        if (route1Points.length > 0) {
            let latSum = 0;
            let lonSum = 0;
            for (var i = 0; i < route1Points.length; i++) {
                latSum += route1Points[i][0];
                lonSum += route1Points[i][1];
            }
            let latAvg = latSum / route1Points.length;
            let lonAvg = lonSum / route1Points.length;
            map.center = QtPositioning.coordinate(latAvg, lonAvg);
            map.zoomLevel = 14;
        }
    }

    function createPath(routePoints) {
        let pathArray = [];
        for (let i = 0; i < routePoints.length; i++) {
            pathArray.push(QtPositioning.coordinate(routePoints[i][0], routePoints[i][1]));
        }
        return pathArray;
    }

    Map {
        id: map
        anchors.fill: parent
        plugin: Plugin {
            name: "osm"
        }
        zoomLevel: 14

        MouseArea {
            anchors.fill: parent
            property point lastPos

            onPressed: {
                lastPos = Qt.point(mouse.x, mouse.y)
            }

            onPositionChanged: {
                if (mouse.buttons & Qt.LeftButton) {
                    let dx = mouse.x - lastPos.x
                    let dy = mouse.y - lastPos.y;
                    lastPos = Qt.point(mouse.x, mouse.y)

                    map.pan(-dx, -dy)
                }
            }

            onWheel: {
                if (wheel.angleDelta.y > 0) {
                    map.zoomLevel += 1
                } else {
                    map.zoomLevel -= 1
                }
            }
        }

        MapPolyline {
            line.width: 3
            line.color: 'red'
            path: createPath(route1Points)
        }

        MapPolyline {
            line.width: 3
            line.color: 'blue'
            path: createPath(route2Points)
        }
    }
}
