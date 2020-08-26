# nwsradar

Custom integration for NWS radar loops for Home Assistant.
Radar stations can be found by clicking on this [map](https://radar.weather.gov/).

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

![radar](https://github.com/MatthewFlamm/nws_radar/blob/master/images/radar.gif?raw=True)

## Installation

* This custom integration can be installed and managed using HACS.
* If you want to manually install, place files in the `custom_components/nwsradar/` folder into `path/to/haconfig/custom_components/nwsradar/`

## Configuration

Use UI to configure: **Configuration** -> **Integrations** -> **National Weather Service (NWS) Radar**

* The `Standard` radar style offers a simple white background.
* The `Enhanced` radar style offers a topographical background.
* The `Mosaic` radar style offers a longer range radar view of regions or the entire US.

Works with picture-entity card:

```
- type: picture-entity
  entity: camera.vwx  # use your entity name
```

## Change log
* 0.5.1
  * Use standard homeassistant method for updating data
* 0.5.0
  * Use UI configuration
  * DEPRECATION: YAML configuration to be removed in 0.6.0
* 0.4.0
  * Add Mosaic style option
* 0.3.0
  * Add Standard style option
  * BREAKING CHANGE: Default is now Standard style

## :warning: Required Dependencies for Installation
There are system image library dependencies for the python Pillow package that may be required.  Here are some reported by users:
* A jpeg library dependency, `libjpeg-dev`, `libjpeg-turbo` or similar, that needs to be separately installed via `sudo apt-get install libjpeg-turbo`. See [here](https://community.home-assistant.io/t/nws-radar-images/118203/2) for report. You will get an error message like this otherwise: `ImportError: libopenjp2.so.7: cannot open shared object file: No such file or directory`.
* A tiff library dependency, `libtiff5` or similar, that needs to be separately installed via `sudo apt-get install libtiff5`. See [here](https://github.com/MatthewFlamm/nwsradar/issues/1) for report. You will get an error message like this otherwise: `ImportError: libtiff.so.5: cannot open shared object file: No such file or directory`.
