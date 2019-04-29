# Kumitate KL-Kanon 6-Minus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.9; 106 -1.3; 116 -1.8; 128 -2.3; 141 -2.7; 155 -3.2; 170 -3.6; 187 -4.0; 206 -4.2; 227 -4.5; 249 -4.8; 274 -5.0; 302 -5.2; 332 -5.3; 365 -5.4; 402 -5.5; 442 -5.6; 486 -5.6; 535 -5.5; 588 -5.5; 647 -5.4; 712 -5.2; 783 -4.9; 861 -4.8; 947 -4.9; 1042 -5.2; 1146 -6.0; 1261 -6.9; 1387 -7.6; 1526 -8.1; 1678 -8.6; 1846 -9.3; 2031 -9.8; 2234 -8.9; 2457 -7.0; 2703 -5.9; 2973 -6.1; 3270 -7.2; 3597 -8.8; 3957 -10.6; 4353 -12.4; 4788 -14.4; 5267 -14.0; 5793 -12.5; 6373 -13.6; 7010 -10.9; 7711 -7.1; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Kanon 6-Minus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Kanon 6-Minus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.29 | 6.5 dB  |
| Peaking | 893 Hz  | 1.7  | 2.0 dB  |
| Peaking | 2059 Hz | 1.54 | -4.2 dB |
| Peaking | 2746 Hz | 2.29 | 4.2 dB  |
| Peaking | 5128 Hz | 1.75 | -8.3 dB |
| Peaking | 17 Hz   | 0.98 | 1.4 dB  |
| Peaking | 59 Hz   | 0.36 | -0.9 dB |
| Peaking | 93 Hz   | 1.46 | 1.3 dB  |
| Peaking | 6666 Hz | 6.18 | -4.6 dB |
| Peaking | 7748 Hz | 1.75 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 3.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -4.6 dB |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Kanon%206-Minus/Kumitate%20KL-Kanon%206-Minus.png)