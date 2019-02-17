# HyperX Cloud Stinger
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.7; 25 -11.8; 28 -12.0; 31 -12.1; 34 -12.1; 37 -12.0; 41 -12.0; 45 -12.1; 49 -12.2; 54 -12.2; 60 -12.3; 66 -12.3; 72 -12.3; 79 -12.3; 87 -12.5; 96 -12.7; 106 -12.9; 116 -13.0; 128 -12.8; 141 -12.5; 155 -12.2; 170 -11.7; 187 -11.0; 206 -9.9; 227 -8.7; 249 -7.6; 274 -6.4; 302 -5.0; 332 -3.5; 365 -1.7; 402 -0.5; 442 -0.8; 486 -2.5; 535 -4.4; 588 -6.1; 647 -7.1; 712 -7.4; 783 -7.0; 861 -6.2; 947 -5.9; 1042 -6.0; 1146 -6.5; 1261 -7.4; 1387 -8.6; 1526 -9.9; 1678 -11.0; 1846 -11.7; 2031 -12.5; 2234 -12.0; 2457 -11.4; 2703 -11.0; 2973 -11.2; 3270 -10.4; 3597 -8.5; 3957 -6.4; 4353 -5.7; 4788 -5.1; 5267 -3.9; 5793 -7.0; 6373 -9.2; 7010 -6.9; 7711 -8.1; 8482 -11.4; 9330 -12.9; 10263 -10.2; 11289 -6.2; 12418 -5.9; 13660 -6.3; 15026 -10.6; 16529 -13.4; 18182 -14.4; 20000 -15.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Stinger GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Stinger ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.59 | -6.5 dB |
| Peaking | 105 Hz   | 1.66 | -4.9 dB |
| Peaking | 165 Hz   | 3.03 | -4.2 dB |
| Peaking | 2184 Hz  | 1.51 | -6.8 dB |
| Peaking | 19928 Hz | 0.31 | -9.8 dB |
| Peaking | 385 Hz   | 0.7  | -2.8 dB |
| Peaking | 405 Hz   | 1.99 | 9.2 dB  |
| Peaking | 5031 Hz  | 5.36 | 3.4 dB  |
| Peaking | 9260 Hz  | 2.98 | -6.6 dB |
| Peaking | 12375 Hz | 2.14 | 4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -7.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Stinger/HyperX%20Cloud%20Stinger.png)