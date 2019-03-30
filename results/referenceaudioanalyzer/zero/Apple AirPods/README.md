# Apple AirPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -1.0; 947 -1.8; 1042 -2.7; 1146 -4.1; 1261 -6.1; 1387 -8.7; 1526 -12.3; 1678 -16.4; 1846 -19.8; 2031 -21.4; 2234 -21.3; 2457 -20.8; 2703 -20.5; 2973 -19.9; 3270 -18.6; 3597 -16.5; 3957 -14.6; 4353 -13.2; 4788 -12.2; 5267 -12.5; 5793 -14.2; 6373 -14.5; 7010 -12.3; 7711 -9.9; 8482 -8.3; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple AirPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple AirPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 0.22 | 5.6 dB   |
| Peaking | 464 Hz  | 0.23 | 5.5 dB   |
| Peaking | 1139 Hz | 0.82 | 7.8 dB   |
| Peaking | 1990 Hz | 1.02 | -15.0 dB |
| Peaking | 2797 Hz | 0.54 | -7.8 dB  |
| Peaking | 2352 Hz | 5.52 | 0.6 dB   |
| Peaking | 3034 Hz | 3.05 | -1.7 dB  |
| Peaking | 4798 Hz | 1.74 | 3.1 dB   |
| Peaking | 6288 Hz | 2.47 | -5.7 dB  |
| Peaking | 9528 Hz | 1.26 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 4.3 dB   |
| Peaking | 125 Hz   | 1.41 | 4.5 dB   |
| Peaking | 250 Hz   | 1.41 | 4.5 dB   |
| Peaking | 500 Hz   | 1.41 | 5.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 8.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -16.8 dB |
| Peaking | 4000 Hz  | 1.41 | -6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 16000 Hz | 1.41 | 0.7 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Apple%20AirPods/Apple%20AirPods.png)