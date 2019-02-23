# Focal Utopia
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.8; 25 -1.0; 28 -1.2; 31 -1.4; 34 -1.7; 37 -1.9; 41 -2.1; 45 -2.2; 49 -2.4; 54 -2.6; 60 -3.0; 66 -3.3; 72 -3.7; 79 -4.0; 87 -4.5; 96 -4.9; 106 -5.3; 116 -5.7; 128 -6.0; 141 -6.3; 155 -6.5; 170 -6.6; 187 -6.7; 206 -6.8; 227 -6.8; 249 -6.7; 274 -6.4; 302 -6.2; 332 -6.0; 365 -5.8; 402 -5.7; 442 -5.6; 486 -5.5; 535 -5.4; 588 -5.4; 647 -5.4; 712 -5.7; 783 -6.1; 861 -6.6; 947 -6.9; 1042 -7.4; 1146 -7.6; 1261 -7.6; 1387 -6.4; 1526 -4.9; 1678 -2.7; 1846 -1.2; 2031 -0.5; 2234 -1.6; 2457 -3.6; 2703 -4.8; 2973 -4.3; 3270 -3.9; 3597 -3.3; 3957 -5.2; 4353 -5.9; 4788 -5.9; 5267 -7.3; 5793 -10.2; 6373 -5.6; 7010 -3.9; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -6.7; 12418 -6.9; 13660 -5.7; 15026 -5.7; 16529 -7.5; 18182 -12.4; 20000 -23.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Utopia GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Utopia ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.2  | 4.6 dB   |
| Peaking | 51 Hz    | 2.02 | 2.2 dB   |
| Peaking | 1258 Hz  | 1.5  | -3.5 dB  |
| Peaking | 1933 Hz  | 2.06 | 6.0 dB   |
| Peaking | 5691 Hz  | 8.49 | -5.6 dB  |
| Peaking | 197 Hz   | 1.46 | -1.7 dB  |
| Peaking | 2659 Hz  | 7.64 | -1.1 dB  |
| Peaking | 3528 Hz  | 7.71 | 1.8 dB   |
| Peaking | 7015 Hz  | 7.32 | 2.0 dB   |
| Peaking | 19768 Hz | 1.25 | -17.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.2 dB |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Utopia/Focal%20Utopia.png)