# AUKEY Latitude
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -1.6; 25 -1.5; 28 -1.4; 31 -1.4; 34 -1.3; 37 -1.3; 41 -1.3; 45 -1.3; 49 -1.4; 54 -1.6; 60 -2.0; 66 -2.5; 72 -2.8; 79 -3.3; 87 -3.8; 96 -4.3; 106 -5.0; 116 -5.6; 128 -6.1; 141 -6.5; 155 -6.8; 170 -6.9; 187 -7.0; 206 -7.1; 227 -7.3; 249 -7.1; 274 -6.6; 302 -6.2; 332 -5.7; 365 -5.2; 402 -4.7; 442 -4.2; 486 -3.6; 535 -3.0; 588 -2.4; 647 -1.6; 712 -1.0; 783 -0.5; 861 -0.5; 947 -0.7; 1042 -1.4; 1146 -2.0; 1261 -1.9; 1387 -1.9; 1526 -1.7; 1678 -1.4; 1846 -1.2; 2031 -0.8; 2234 -0.5; 2457 -0.6; 2703 -1.3; 2973 -2.9; 3270 -4.7; 3597 -6.0; 3957 -5.8; 4353 -5.7; 4788 -5.3; 5267 -5.5; 5793 -5.8; 6373 -6.3; 7010 -5.7; 7711 -3.8; 8482 -4.0; 9330 -6.7; 10263 -10.3; 11289 -7.3; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -6.0; 18182 -7.1; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AUKEY Latitude GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AUKEY Latitude ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.41 | 3.5 dB  |
| Peaking | 178 Hz   | 0.56 | -4.4 dB |
| Peaking | 802 Hz   | 1.08 | 4.0 dB  |
| Peaking | 2182 Hz  | 2.88 | 3.5 dB  |
| Peaking | 10337 Hz | 4.28 | -6.8 dB |
| Peaking | 2768 Hz  | 4.19 | 2.5 dB  |
| Peaking | 3712 Hz  | 1.34 | -3.3 dB |
| Peaking | 6400 Hz  | 4.43 | -2.5 dB |
| Peaking | 10301 Hz | 0.14 | 1.0 dB  |
| Peaking | 17761 Hz | 1.76 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AUKEY%20Latitude/AUKEY%20Latitude.png)