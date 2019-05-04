# Superlux HD 681 EVO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.4; 25 -8.9; 28 -9.6; 31 -10.1; 34 -10.5; 37 -10.8; 41 -11.0; 45 -11.1; 49 -11.1; 54 -11.0; 60 -10.9; 66 -10.7; 72 -10.4; 79 -10.2; 87 -10.1; 96 -10.0; 106 -10.0; 116 -9.9; 128 -9.5; 141 -8.8; 155 -7.9; 170 -7.4; 187 -7.0; 206 -6.6; 227 -6.4; 249 -6.1; 274 -5.8; 302 -5.6; 332 -5.3; 365 -4.9; 402 -4.8; 442 -4.8; 486 -4.8; 535 -4.4; 588 -4.5; 647 -4.3; 712 -4.7; 783 -5.2; 861 -5.4; 947 -5.3; 1042 -4.9; 1146 -4.4; 1261 -4.3; 1387 -4.5; 1526 -5.6; 1678 -7.3; 1846 -9.2; 2031 -10.4; 2234 -10.3; 2457 -9.6; 2703 -8.5; 2973 -7.8; 3270 -6.5; 3597 -3.2; 3957 -0.5; 4353 -2.1; 4788 -5.8; 5267 -6.7; 5793 -7.0; 6373 -5.5; 7010 -7.0; 7711 -10.5; 8482 -11.4; 9330 -10.3; 10263 -10.7; 11289 -11.4; 12418 -11.3; 13660 -10.9; 15026 -7.4; 16529 -6.5; 18182 -6.8; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 EVO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 EVO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 64 Hz    | 0.4  | -4.9 dB |
| Peaking | 1057 Hz  | 0.13 | 2.6 dB  |
| Peaking | 2235 Hz  | 1.77 | -6.6 dB |
| Peaking | 4016 Hz  | 5.22 | 6.6 dB  |
| Peaking | 10594 Hz | 0.86 | -5.8 dB |
| Peaking | 870 Hz   | 4.11 | -1.1 dB |
| Peaking | 1327 Hz  | 4.44 | 1.4 dB  |
| Peaking | 6644 Hz  | 4.48 | 4.7 dB  |
| Peaking | 7743 Hz  | 1.53 | -3.5 dB |
| Peaking | 9740 Hz  | 3.27 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Superlux%20HD%20681%20EVO/Superlux%20HD%20681%20EVO.png)