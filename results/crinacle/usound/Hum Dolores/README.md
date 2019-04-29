# Hum Dolores
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.7; 31 -2.0; 34 -2.3; 37 -2.5; 41 -2.7; 45 -2.9; 49 -3.2; 54 -3.4; 60 -3.7; 66 -4.0; 72 -4.3; 79 -4.6; 87 -5.0; 96 -5.4; 106 -5.8; 116 -6.2; 128 -6.4; 141 -6.7; 155 -6.9; 170 -7.0; 187 -7.1; 206 -7.2; 227 -7.2; 249 -7.1; 274 -7.0; 302 -6.9; 332 -6.7; 365 -6.5; 402 -6.3; 442 -6.1; 486 -5.9; 535 -5.6; 588 -5.3; 647 -5.0; 712 -4.7; 783 -4.4; 861 -4.3; 947 -4.5; 1042 -5.1; 1146 -6.3; 1261 -7.6; 1387 -8.5; 1526 -8.6; 1678 -7.4; 1846 -6.0; 2031 -6.2; 2234 -7.1; 2457 -6.3; 2703 -4.4; 2973 -3.0; 3270 -2.6; 3597 -2.9; 3957 -4.2; 4353 -6.4; 4788 -9.2; 5267 -8.7; 5793 -4.7; 6373 -2.3; 7010 -3.2; 7711 -6.6; 8482 -6.5; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hum Dolores GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hum Dolores ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.75 | 4.9 dB  |
| Peaking | 1472 Hz | 4.25 | -3.3 dB |
| Peaking | 3374 Hz | 3.13 | 3.9 dB  |
| Peaking | 4947 Hz | 5.22 | -5.0 dB |
| Peaking | 6467 Hz | 5.86 | 4.6 dB  |
| Peaking | 66 Hz   | 1.6  | 1.0 dB  |
| Peaking | 202 Hz  | 0.77 | -1.6 dB |
| Peaking | 808 Hz  | 2.16 | 1.9 dB  |
| Peaking | 2280 Hz | 8.3  | -1.8 dB |
| Peaking | 8073 Hz | 8.79 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Hum%20Dolores/Hum%20Dolores.png)