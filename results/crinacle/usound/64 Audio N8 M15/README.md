# 64 Audio N8 M15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.6; 25 -7.8; 28 -7.9; 31 -7.9; 34 -7.9; 37 -7.9; 41 -7.9; 45 -7.9; 49 -7.8; 54 -7.7; 60 -7.6; 66 -7.6; 72 -7.6; 79 -7.7; 87 -7.7; 96 -7.7; 106 -7.6; 116 -7.6; 128 -7.5; 141 -7.4; 155 -7.2; 170 -7.0; 187 -6.8; 206 -6.5; 227 -6.3; 249 -6.0; 274 -5.7; 302 -5.4; 332 -5.2; 365 -5.0; 402 -4.8; 442 -4.6; 486 -4.4; 535 -4.3; 588 -4.1; 647 -3.9; 712 -3.6; 783 -3.3; 861 -3.0; 947 -2.9; 1042 -3.1; 1146 -3.7; 1261 -4.4; 1387 -4.9; 1526 -4.8; 1678 -4.3; 1846 -3.8; 2031 -3.3; 2234 -2.9; 2457 -2.3; 2703 -1.6; 2973 -1.1; 3270 -1.0; 3597 -1.4; 3957 -2.2; 4353 -2.7; 4788 -3.9; 5267 -3.3; 5793 -0.5; 6373 -1.3; 7010 -3.0; 7711 -3.9; 8482 -4.1; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -7.2; 18182 -14.6; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.21 | -3.8 dB  |
| Peaking | 847 Hz   | 2.92 | 1.4 dB   |
| Peaking | 3747 Hz  | 0.85 | 2.6 dB   |
| Peaking | 15621 Hz | 1.37 | 4.5 dB   |
| Peaking | 18310 Hz | 1.02 | -12.2 dB |
| Peaking | 1491 Hz  | 3.72 | -1.5 dB  |
| Peaking | 3055 Hz  | 3.43 | 1.2 dB   |
| Peaking | 5085 Hz  | 3.27 | -3.6 dB  |
| Peaking | 5819 Hz  | 3.57 | 4.2 dB   |
| Peaking | 7952 Hz  | 3.2  | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -3.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20M15/64%20Audio%20N8%20M15.png)