# HiFiMan LE-5LE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -5.4; 25 -6.2; 28 -6.9; 31 -7.3; 34 -7.3; 37 -7.1; 41 -6.8; 45 -6.5; 49 -6.4; 54 -6.2; 60 -6.1; 66 -5.9; 72 -5.8; 79 -5.6; 87 -5.4; 96 -5.4; 106 -5.2; 116 -5.3; 128 -5.4; 141 -5.7; 155 -6.0; 170 -6.3; 187 -6.7; 206 -6.7; 227 -6.7; 249 -6.7; 274 -6.6; 302 -6.3; 332 -6.1; 365 -6.1; 402 -6.1; 442 -5.9; 486 -5.6; 535 -5.2; 588 -4.6; 647 -4.0; 712 -3.5; 783 -2.9; 861 -2.5; 947 -2.5; 1042 -2.5; 1146 -2.5; 1261 -2.5; 1387 -2.0; 1526 -1.3; 1678 -0.9; 1846 -0.6; 2031 -0.5; 2234 -0.6; 2457 -1.2; 2703 -1.9; 2973 -2.6; 3270 -3.4; 3597 -4.5; 3957 -6.1; 4353 -7.9; 4788 -9.5; 5267 -10.2; 5793 -10.7; 6373 -11.9; 7010 -13.2; 7711 -13.8; 8482 -13.4; 9330 -12.6; 10263 -12.3; 11289 -12.3; 12418 -11.6; 13660 -9.2; 15026 -6.8; 16529 -6.0; 18182 -5.9; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan LE-5LE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan LE-5LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 2.25 | -1.8 dB |
| Peaking | 269 Hz   | 1.08 | -1.3 dB |
| Peaking | 840 Hz   | 2.24 | 1.8 dB  |
| Peaking | 2267 Hz  | 0.75 | 6.6 dB  |
| Peaking | 7843 Hz  | 0.62 | -9.0 dB |
| Peaking | 50 Hz    | 1.81 | -0.4 dB |
| Peaking | 109 Hz   | 3.11 | 0.6 dB  |
| Peaking | 9515 Hz  | 3.6  | 1.2 dB  |
| Peaking | 12177 Hz | 1.67 | -2.3 dB |
| Peaking | 15347 Hz | 1.19 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB   |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -10.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/HiFiMan%20LE-5LE/HiFiMan%20LE-5LE.png)