# Kumitate KL-Kanon 6-Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.2; 25 -7.2; 28 -7.1; 31 -7.1; 34 -7.1; 37 -7.2; 41 -7.3; 45 -7.4; 49 -7.5; 54 -7.7; 60 -8.0; 66 -8.2; 72 -8.5; 79 -8.8; 87 -9.1; 96 -9.5; 106 -9.9; 116 -10.1; 128 -10.3; 141 -10.5; 155 -10.7; 170 -10.7; 187 -10.6; 206 -10.5; 227 -10.3; 249 -10.1; 274 -9.7; 302 -9.3; 332 -8.9; 365 -8.4; 402 -7.9; 442 -7.3; 486 -6.7; 535 -6.0; 588 -5.3; 647 -4.4; 712 -3.5; 783 -2.4; 861 -1.5; 947 -0.7; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.9; 1678 -2.1; 1846 -3.8; 2031 -5.2; 2234 -4.9; 2457 -3.2; 2703 -2.1; 2973 -2.4; 3270 -3.8; 3597 -5.7; 3957 -7.9; 4353 -10.3; 4788 -12.6; 5267 -12.4; 5793 -10.8; 6373 -11.8; 7010 -10.3; 7711 -7.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Kanon 6-Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Kanon 6-Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 115 Hz  | 1.1  | -0.3 dB |
| Peaking | 189 Hz  | 0.5  | -4.2 dB |
| Peaking | 1095 Hz | 0.97 | 7.0 dB  |
| Peaking | 2991 Hz | 2.9  | 4.7 dB  |
| Peaking | 5167 Hz | 1.71 | -6.9 dB |
| Peaking | 18 Hz   | 1.43 | -0.7 dB |
| Peaking | 1553 Hz | 5.76 | 1.2 dB  |
| Peaking | 2050 Hz | 6.61 | -1.9 dB |
| Peaking | 6757 Hz | 5.24 | -3.6 dB |
| Peaking | 7558 Hz | 1.51 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Kanon%206-Plus/Kumitate%20KL-Kanon%206-Plus.png)