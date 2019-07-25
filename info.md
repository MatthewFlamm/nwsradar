# nwsradar

Custom component for short range NWS radar loops for Home Assistant.

There is a jpeg library dependency, `libjpeg-dev`, or similar, might need to be separately installed.

## Sample configuration
```
camera:
  - platform: nwsradar
    station: VWX
```

See [README](README.md) for more info on configuration.

## Change log
* 0.3.0
  * Add Standard style option
  * BREAKING CHANGE: Default is now Standard style

## Detailed configuration

Different radar types can be displayed (Note all 0s are zeros):
* NCR - Composite Reflectivity (default)
* N0R - Base Reflectivity (out to 124 nm)
* N0Z - Base Reflectivity (out to 248 nm)
* N0S - Storm Relative Motion
* N1P - One-Hour Precipitation
* NTP - Storm Total Precipitation

Works with picture-entity card:
```
- type: picture-entity
  entity: camera.vwx
```

<img src="https://github.com/MatthewFlamm/nws_radar/blob/master/images/radar.gif?raw=True" width="400px">

