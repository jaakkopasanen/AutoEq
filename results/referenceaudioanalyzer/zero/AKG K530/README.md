# AKG K530
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.1; 49 -2.1; 54 -3.0; 60 -3.5; 66 -4.1; 72 -5.0; 79 -5.6; 87 -5.6; 96 -5.6; 106 -6.1; 116 -6.7; 128 -7.3; 141 -7.6; 155 -7.8; 170 -7.5; 187 -7.4; 206 -7.1; 227 -6.8; 249 -6.5; 274 -6.2; 302 -6.0; 332 -5.9; 365 -5.8; 402 -5.3; 442 -4.2; 486 -3.5; 535 -4.0; 588 -4.6; 647 -4.9; 712 -4.8; 783 -4.4; 861 -3.7; 947 -3.3; 1042 -3.5; 1146 -4.0; 1261 -4.7; 1387 -5.2; 1526 -5.8; 1678 -6.2; 1846 -6.2; 2031 -6.2; 2234 -6.3; 2457 -6.6; 2703 -6.4; 2973 -5.2; 3270 -4.0; 3597 -4.1; 3957 -4.6; 4353 -4.6; 4788 -7.9; 5267 -10.5; 5793 -10.2; 6373 -8.4; 7010 -9.1; 7711 -12.3; 8482 -14.9; 9330 -15.8; 10263 -15.4; 11289 -13.8; 12418 -11.2; 13660 -7.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K530 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.96 | 6.9 dB  |
| Peaking | 487 Hz   | 3.75 | 2.7 dB  |
| Peaking | 979 Hz   | 1.57 | 3.1 dB  |
| Peaking | 8801 Hz  | 2.23 | -7.3 dB |
| Peaking | 10864 Hz | 2.36 | -5.9 dB |
| Peaking | 50 Hz    | 2.66 | 1.0 dB  |
| Peaking | 153 Hz   | 1.98 | -1.7 dB |
| Peaking | 3881 Hz  | 2.27 | 3.3 dB  |
| Peaking | 5292 Hz  | 5.17 | -4.4 dB |
| Peaking | 14668 Hz | 4.34 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -9.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K530/AKG%20K530.png)