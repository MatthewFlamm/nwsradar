# nwsradar

Custom integration for short range NWS radar loops for Home Assistant.
Radar stations can be found by clicking on this [map](https://radar.weather.gov/Conus/index_lite.php).

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

## Installation

* This custom integration can be installed and managed using HACS.
* If you want to manually install, place files in the `custom_components/nwsradar/` folder into `path/to/haconfig/custom_components/nwsradar/`

### :warning: Required Dependencies for Installation
There are system image library dependencies for the python Pillow package that may be required.  Here are some reported by users:
* A jpeg library dependency, `libjpeg-dev`, `libjpeg-turbo` or similar, that needs to be separately installed via `sudo apt-get install libjpeg-turbo`. See [here](https://community.home-assistant.io/t/nws-radar-images/118203/2) for report. You will get an error message like this otherwise: `ImportError: libopenjp2.so.7: cannot open shared object file: No such file or directory`.
* A tiff library dependency, `libtiff5` or similar, that needs to be separately installed via `sudo apt-get install libtiff5`. See [here](https://github.com/MatthewFlamm/nwsradar/issues/1) for report. You will get an error message like this otherwise: `ImportError: libtiff.so.5: cannot open shared object file: No such file or directory`.

## Sample configuration
```
camera:
  - platform: nwsradar
    station: VWX
```

![radar](https://github.com/MatthewFlamm/nws_radar/blob/master/images/radar.gif?raw=True)

## Change log
* 0.4.0
  * Add Mosaic style option
* 0.3.0
  * Add Standard style option
  * BREAKING CHANGE: Default is now Standard style

## Detailed Configuration

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

The `Standard` radar style (the default) offers a simple white background and either a still picture (`frames: 1`) or a loop (any number larger than 1). Looping is the default.

The 'Enhanced' radar style offers a topographical background and a configurable loop length.

The `Mosaic` radar style offers a longer range radar view of regions or the entire US.  Supported stations are:


```
camera:
  - platform: nwsradar
    station: VWX
    style: Standard
```


Different length animations can be produced (default is 6) for `Enhanced` style:
 ```
camera:
  - platform: nwsradar
    station: VWX
    style: Enhanced
    frames: 8
```

Mosaic radar loops can be produced with configurable frame number, but radar type isnt supported:
 ```
camera:
  - platform: nwsradar
    station: VWX
    style: Mosaic
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
