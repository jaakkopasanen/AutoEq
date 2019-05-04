# HiFiMan Sundara
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.1; 31 -1.5; 34 -1.9; 37 -2.2; 41 -2.6; 45 -2.8; 49 -3.1; 54 -3.3; 60 -3.6; 66 -3.8; 72 -4.0; 79 -4.2; 87 -4.5; 96 -4.8; 106 -5.1; 116 -5.4; 128 -5.7; 141 -5.9; 155 -6.1; 170 -6.2; 187 -6.3; 206 -6.4; 227 -6.5; 249 -6.6; 274 -6.7; 302 -6.9; 332 -7.0; 365 -7.2; 402 -7.2; 442 -6.6; 486 -6.3; 535 -6.8; 588 -7.1; 647 -7.1; 712 -7.0; 783 -6.9; 861 -6.8; 947 -5.7; 1042 -5.1; 1146 -5.1; 1261 -5.0; 1387 -5.0; 1526 -4.6; 1678 -4.6; 1846 -4.4; 2031 -4.1; 2234 -3.3; 2457 -4.5; 2703 -5.1; 2973 -7.0; 3270 -7.8; 3597 -8.6; 3957 -8.6; 4353 -8.4; 4788 -10.9; 5267 -8.4; 5793 -3.1; 6373 -6.4; 7010 -9.9; 7711 -10.5; 8482 -9.8; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -8.1; 13660 -9.4; 15026 -9.6; 16529 -9.3; 18182 -9.5; 20000 -11.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Sundara GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Sundara ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.66 | 5.9 dB  |
| Peaking | 69 Hz    | 1.29 | 1.3 dB  |
| Peaking | 7727 Hz  | 4.35 | -4.4 dB |
| Peaking | 14662 Hz | 2.13 | -2.5 dB |
| Peaking | 20037 Hz | 0.57 | -4.8 dB |
| Peaking | 485 Hz   | 0.71 | -0.7 dB |
| Peaking | 1941 Hz  | 1.08 | 3.0 dB  |
| Peaking | 4842 Hz  | 1.65 | -4.8 dB |
| Peaking | 5787 Hz  | 6.12 | 7.4 dB  |
| Peaking | 22050 Hz | 1.98 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20Sundara/HiFiMan%20Sundara.png)