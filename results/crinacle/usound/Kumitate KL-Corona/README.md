# Kumitate KL-Corona
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.3; 31 -2.9; 34 -3.4; 37 -3.8; 41 -4.3; 45 -4.7; 49 -5.1; 54 -5.5; 60 -5.9; 66 -6.3; 72 -6.8; 79 -7.1; 87 -7.5; 96 -7.9; 106 -8.2; 116 -8.5; 128 -8.7; 141 -8.8; 155 -8.8; 170 -8.8; 187 -8.8; 206 -8.7; 227 -8.5; 249 -8.3; 274 -8.1; 302 -7.9; 332 -7.7; 365 -7.4; 402 -7.2; 442 -6.9; 486 -6.7; 535 -6.4; 588 -6.1; 647 -5.7; 712 -5.3; 783 -4.9; 861 -4.6; 947 -4.4; 1042 -4.7; 1146 -5.4; 1261 -6.1; 1387 -6.6; 1526 -6.8; 1678 -6.6; 1846 -6.5; 2031 -6.7; 2234 -6.8; 2457 -6.7; 2703 -6.3; 2973 -5.6; 3270 -4.9; 3597 -4.1; 3957 -3.3; 4353 -2.6; 4788 -2.5; 5267 -3.1; 5793 -4.8; 6373 -7.4; 7010 -8.4; 7711 -9.2; 8482 -6.5; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Corona GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Corona ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.56 | 6.8 dB  |
| Peaking | 153 Hz  | 0.59 | -2.8 dB |
| Peaking | 869 Hz  | 2.4  | 2.2 dB  |
| Peaking | 4661 Hz | 2.16 | 4.5 dB  |
| Peaking | 7231 Hz | 3.52 | -3.7 dB |
| Peaking | 614 Hz  | 2.67 | 0.3 dB  |
| Peaking | 2287 Hz | 1.26 | -0.9 dB |
| Peaking | 3417 Hz | 3.13 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Corona/Kumitate%20KL-Corona.png)