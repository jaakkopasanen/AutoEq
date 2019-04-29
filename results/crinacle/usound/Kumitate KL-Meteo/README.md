# Kumitate KL-Meteo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.2; 25 -9.2; 28 -9.3; 31 -9.3; 34 -9.3; 37 -9.4; 41 -9.4; 45 -9.4; 49 -9.4; 54 -9.3; 60 -9.3; 66 -9.4; 72 -9.4; 79 -9.4; 87 -9.3; 96 -9.3; 106 -9.1; 116 -8.9; 128 -8.6; 141 -8.2; 155 -7.7; 170 -7.1; 187 -6.5; 206 -5.7; 227 -4.9; 249 -4.1; 274 -3.3; 302 -2.5; 332 -1.8; 365 -1.3; 402 -1.0; 442 -0.8; 486 -0.8; 535 -1.0; 588 -1.4; 647 -1.8; 712 -2.2; 783 -2.7; 861 -3.2; 947 -3.8; 1042 -4.8; 1146 -6.1; 1261 -7.2; 1387 -7.8; 1526 -7.8; 1678 -7.2; 1846 -6.3; 2031 -5.4; 2234 -4.7; 2457 -4.1; 2703 -3.6; 2973 -3.2; 3270 -2.8; 3597 -2.6; 3957 -2.4; 4353 -1.8; 4788 -1.1; 5267 -0.6; 5793 -0.5; 6373 -1.6; 7010 -5.6; 7711 -7.1; 8482 -4.3; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -4.0; 18182 -4.0; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Meteo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Meteo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 71 Hz    | 0.17 | -6.0 dB |
| Peaking | 405 Hz   | 0.68 | 6.4 dB  |
| Peaking | 1439 Hz  | 1.78 | -4.9 dB |
| Peaking | 5804 Hz  | 1.31 | 4.7 dB  |
| Peaking | 7443 Hz  | 3.63 | -6.3 dB |
| Peaking | 11 Hz    | 0.73 | -0.9 dB |
| Peaking | 49 Hz    | 2.23 | 0.5 dB  |
| Peaking | 3011 Hz  | 4.41 | 0.4 dB  |
| Peaking | 11493 Hz | 2.2  | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 4.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Meteo/Kumitate%20KL-Meteo.png)