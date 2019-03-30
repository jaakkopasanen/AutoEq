# HiFiMan Re2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.5; 25 -5.5; 28 -5.5; 31 -5.5; 34 -5.5; 37 -5.5; 41 -5.5; 45 -5.6; 49 -5.7; 54 -5.8; 60 -5.9; 66 -5.8; 72 -5.8; 79 -5.8; 87 -5.8; 96 -5.8; 106 -5.8; 116 -5.8; 128 -5.8; 141 -5.8; 155 -5.8; 170 -5.8; 187 -5.9; 206 -6.1; 227 -6.4; 249 -6.6; 274 -6.8; 302 -7.1; 332 -7.2; 365 -7.1; 402 -7.3; 442 -7.5; 486 -7.5; 535 -7.8; 588 -8.0; 647 -8.3; 712 -8.8; 783 -9.2; 861 -9.9; 947 -10.7; 1042 -11.6; 1146 -12.7; 1261 -13.8; 1387 -14.5; 1526 -14.3; 1678 -13.2; 1846 -11.2; 2031 -8.8; 2234 -7.0; 2457 -6.0; 2703 -5.8; 2973 -5.6; 3270 -5.0; 3597 -4.9; 3957 -5.6; 4353 -6.9; 4788 -7.4; 5267 -5.8; 5793 -1.9; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Re2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Re2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 17 Hz   | 0.23 | 0.4 dB   |
| Peaking | 1539 Hz | 0.94 | -14.0 dB |
| Peaking | 2216 Hz | 0.8  | 7.6 dB   |
| Peaking | 4803 Hz | 4.3  | -2.9 dB  |
| Peaking | 6194 Hz | 4.81 | 6.4 dB   |
| Peaking | 317 Hz  | 3.09 | -0.6 dB  |
| Peaking | 799 Hz  | 2.4  | 0.3 dB   |
| Peaking | 8212 Hz | 4.81 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -6.2 dB |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/HiFiMan%20Re2/HiFiMan%20Re2.png)