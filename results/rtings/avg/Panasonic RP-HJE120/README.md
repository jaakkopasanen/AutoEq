# Panasonic RP-HJE120
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.4; 25 -3.7; 28 -4.0; 31 -4.3; 34 -4.6; 37 -4.8; 41 -5.0; 45 -5.2; 49 -5.4; 54 -5.7; 60 -6.2; 66 -6.7; 72 -7.1; 79 -7.5; 87 -8.0; 96 -8.6; 106 -9.1; 116 -9.6; 128 -10.1; 141 -10.5; 155 -10.7; 170 -10.7; 187 -10.7; 206 -10.5; 227 -10.2; 249 -9.6; 274 -9.0; 302 -8.5; 332 -8.1; 365 -7.6; 402 -6.8; 442 -6.0; 486 -5.1; 535 -4.1; 588 -3.2; 647 -1.9; 712 -0.9; 783 -0.5; 861 -0.6; 947 -1.1; 1042 -1.4; 1146 -1.7; 1261 -1.9; 1387 -2.0; 1526 -2.1; 1678 -2.4; 1846 -2.9; 2031 -3.3; 2234 -3.0; 2457 -2.7; 2703 -2.7; 2973 -2.9; 3270 -3.0; 3597 -3.1; 3957 -3.6; 4353 -4.7; 4788 -5.9; 5267 -7.4; 5793 -6.0; 6373 -2.8; 7010 -2.3; 7711 -4.5; 8482 -4.8; 9330 -4.8; 10263 -4.8; 11289 -4.8; 12418 -4.8; 13660 -4.8; 15026 -4.8; 16529 -5.1; 18182 -4.8; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HJE120 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HJE120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 182 Hz  | 0.62 | -6.3 dB |
| Peaking | 787 Hz  | 1.39 | 4.4 dB  |
| Peaking | 2186 Hz | 0.49 | 2.0 dB  |
| Peaking | 5371 Hz | 3.66 | -4.0 dB |
| Peaking | 6703 Hz | 6.65 | 3.7 dB  |
| Peaking | 19 Hz   | 1.04 | 2.0 dB  |
| Peaking | 1448 Hz | 3.6  | 0.4 dB  |
| Peaking | 2030 Hz | 4.65 | -0.8 dB |
| Peaking | 3361 Hz | 2.29 | 0.3 dB  |
| Peaking | 8688 Hz | 2.74 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HJE120/Panasonic%20RP-HJE120.png)