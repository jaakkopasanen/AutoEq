# Hifiman Ananda
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.3; 25 -2.5; 28 -2.7; 31 -2.9; 34 -3.1; 37 -3.1; 41 -3.2; 45 -3.2; 49 -3.1; 54 -3.2; 60 -4.2; 66 -4.6; 72 -4.7; 79 -4.9; 87 -5.1; 96 -5.4; 106 -5.7; 116 -6.0; 128 -6.3; 141 -6.6; 155 -6.9; 170 -7.1; 187 -7.3; 206 -7.6; 227 -7.7; 249 -7.1; 274 -7.1; 302 -7.0; 332 -6.6; 365 -5.8; 402 -6.8; 442 -6.6; 486 -7.3; 535 -7.9; 588 -8.0; 647 -7.6; 712 -4.4; 783 -4.3; 861 -5.8; 947 -6.8; 1042 -6.0; 1146 -3.1; 1261 -2.4; 1387 -1.1; 1526 -1.3; 1678 -0.5; 1846 -1.3; 2031 -1.9; 2234 -2.6; 2457 -4.2; 2703 -6.1; 2973 -7.0; 3270 -7.2; 3597 -6.6; 3957 -6.1; 4353 -6.3; 4788 -5.9; 5267 -4.0; 5793 -4.0; 6373 -7.1; 7010 -6.5; 7711 -5.6; 8482 -5.3; 9330 -5.4; 10263 -5.9; 11289 -8.8; 12418 -6.7; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -12.1; 20000 -18.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman Ananda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman Ananda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.32 | 3.2 dB   |
| Peaking | 198 Hz   | 0.85 | -2.3 dB  |
| Peaking | 562 Hz   | 3.67 | -2.8 dB  |
| Peaking | 1618 Hz  | 2.27 | 5.3 dB   |
| Peaking | 19696 Hz | 1.29 | -13.8 dB |
| Peaking | 972 Hz   | 7.1  | -2.9 dB  |
| Peaking | 1692 Hz  | 0.51 | 0.8 dB   |
| Peaking | 3194 Hz  | 2.61 | -2.9 dB  |
| Peaking | 11435 Hz | 5.76 | -3.7 dB  |
| Peaking | 15917 Hz | 2.23 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20Ananda/Hifiman%20Ananda.png)