# 64 Audio U18Tzar
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.6; 25 -6.0; 28 -6.4; 31 -6.8; 34 -7.2; 37 -7.5; 41 -7.8; 45 -8.0; 49 -8.2; 54 -8.4; 60 -8.6; 66 -8.9; 72 -9.1; 79 -9.4; 87 -9.6; 96 -9.9; 106 -10.1; 116 -10.1; 128 -10.2; 141 -10.3; 155 -10.3; 170 -10.2; 187 -10.0; 206 -9.8; 227 -9.6; 249 -9.4; 274 -9.1; 302 -8.8; 332 -8.5; 365 -8.2; 402 -7.9; 442 -7.6; 486 -7.3; 535 -7.0; 588 -6.6; 647 -6.3; 712 -5.8; 783 -5.4; 861 -5.0; 947 -4.9; 1042 -5.1; 1146 -5.6; 1261 -6.2; 1387 -6.5; 1526 -6.3; 1678 -5.9; 1846 -5.5; 2031 -5.6; 2234 -5.9; 2457 -4.7; 2703 -3.5; 2973 -3.7; 3270 -4.2; 3597 -3.5; 3957 -1.5; 4353 -0.5; 4788 -2.6; 5267 -3.7; 5793 -3.4; 6373 -5.8; 7010 -6.8; 7711 -6.4; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.6; 15026 -9.7; 16529 -16.3; 18182 -19.4; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio U18Tzar GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio U18Tzar ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 110 Hz   | 0.65 | -3.6 dB  |
| Peaking | 239 Hz   | 1.21 | -1.8 dB  |
| Peaking | 2700 Hz  | 3.96 | 1.9 dB   |
| Peaking | 4334 Hz  | 2.32 | 5.5 dB   |
| Peaking | 17906 Hz | 1.54 | -15.1 dB |
| Peaking | 18 Hz    | 2.24 | 1.2 dB   |
| Peaking | 903 Hz   | 2.99 | 1.8 dB   |
| Peaking | 6928 Hz  | 8.9  | -1.4 dB  |
| Peaking | 13480 Hz | 1.65 | 2.1 dB   |
| Peaking | 16457 Hz | 3.47 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -9.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20U18Tzar/64%20Audio%20U18Tzar.png)