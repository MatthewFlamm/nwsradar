# nwsradar

Custom component for short range NWS radar loops for Home Assistant.
Radar stations can be found by clicking on this [map](https://radar.weather.gov/Conus/index_lite.php).

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

## Installation

* This custom integration can be installed and managed using HACS.
* If you want to manually install, place files in the `custom_components/nwsradar/` folder into `path/to/haconfig/custom_components/nwsradar/`
* There is a jpeg library dependency, `libjpeg-dev`, or similar, might need to be separately installed. See [here](https://community.home-assistant.io/t/nws-radar-images/118203/2) for report.

Sample config:
```
camera:
  - platform: nwsradar
    station: VWX
```

![radar](https://github.com/MatthewFlamm/nws_radar/blob/master/images/radar.gif?raw=True)

Different radar types can be displayed (Note all 0s are zeros):
* NCR - Composite Reflectivity (default)
* N0R - Base Reflectivity (out to 124 nm)
* N0Z - Base Reflectivity (out to 248 nm)
* N0S - Storm Relative Motion
* N1P - One-Hour Precipitation
* NTP - Storm Total Precipitation

```
camera:
  - platform: nwsradar
    station: VWX
    type: N0R
```

Different length animations can be produced (default is 6):
 ```
camera:
  - platform: nwsradar
    station: VWX
    frames: 8
```

Entity name can be specified:
```
camera:
  - platform: nwsradar
    station: VWX
    name: radarname
```

Works with picture-entity card:

```
- type: picture-entity
  entity: camera.vwx
```


