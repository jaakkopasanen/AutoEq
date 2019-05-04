# HyperX Cloud Flight
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.1; 25 -4.5; 28 -5.0; 31 -5.3; 34 -5.5; 37 -5.6; 41 -5.9; 45 -6.1; 49 -6.4; 54 -6.6; 60 -6.8; 66 -7.0; 72 -7.2; 79 -7.4; 87 -7.6; 96 -7.8; 106 -7.9; 116 -8.0; 128 -8.0; 141 -7.7; 155 -7.4; 170 -7.0; 187 -6.4; 206 -5.7; 227 -4.8; 249 -4.1; 274 -3.3; 302 -2.4; 332 -1.7; 365 -1.0; 402 -0.5; 442 -1.0; 486 -2.1; 535 -3.2; 588 -4.1; 647 -4.3; 712 -5.0; 783 -6.5; 861 -6.3; 947 -6.0; 1042 -5.2; 1146 -4.3; 1261 -3.5; 1387 -4.0; 1526 -4.9; 1678 -5.3; 1846 -6.0; 2031 -6.6; 2234 -5.9; 2457 -4.6; 2703 -4.1; 2973 -4.6; 3270 -4.5; 3597 -5.7; 3957 -6.1; 4353 -7.2; 4788 -8.5; 5267 -6.9; 5793 -4.1; 6373 -3.8; 7010 -7.5; 7711 -10.2; 8482 -10.6; 9330 -10.1; 10263 -9.7; 11289 -9.1; 12418 -7.6; 13660 -5.7; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Flight GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Flight ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.78 | 2.2 dB  |
| Peaking | 113 Hz  | 0.78 | -2.9 dB |
| Peaking | 377 Hz  | 1.57 | 5.4 dB  |
| Peaking | 4659 Hz | 8.29 | -2.9 dB |
| Peaking | 9365 Hz | 1.89 | -5.6 dB |
| Peaking | 835 Hz  | 4.82 | -1.7 dB |
| Peaking | 1299 Hz | 3.2  | 2.7 dB  |
| Peaking | 2989 Hz | 1.65 | 3.7 dB  |
| Peaking | 3151 Hz | 0.52 | -2.5 dB |
| Peaking | 6114 Hz | 5.73 | 4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Flight/HyperX%20Cloud%20Flight.png)