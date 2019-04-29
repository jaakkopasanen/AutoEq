# Kumitate KL-REF Type-S Max Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.8; 23 -14.9; 25 -15.0; 28 -15.0; 31 -15.0; 34 -15.0; 37 -14.9; 41 -14.9; 45 -14.8; 49 -14.7; 54 -14.5; 60 -14.5; 66 -14.4; 72 -14.3; 79 -14.3; 87 -14.2; 96 -14.2; 106 -14.1; 116 -13.9; 128 -13.7; 141 -13.5; 155 -13.2; 170 -12.9; 187 -12.5; 206 -12.0; 227 -11.4; 249 -10.9; 274 -10.2; 302 -9.6; 332 -8.9; 365 -8.6; 402 -8.5; 442 -8.4; 486 -8.1; 535 -7.7; 588 -7.3; 647 -6.9; 712 -6.4; 783 -5.9; 861 -5.6; 947 -5.6; 1042 -5.8; 1146 -6.4; 1261 -7.0; 1387 -7.1; 1526 -6.9; 1678 -6.4; 1846 -5.6; 2031 -4.5; 2234 -3.2; 2457 -1.9; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.9; 4353 -3.0; 4788 -4.8; 5267 -3.6; 5793 -1.0; 6373 -1.0; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.8; 16529 -12.2; 18182 -13.1; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-REF Type-S Max Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-REF Type-S Max Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.16 | -8.5 dB |
| Peaking | 796 Hz   | 3.17 | 1.4 dB  |
| Peaking | 3502 Hz  | 1.01 | 6.2 dB  |
| Peaking | 14198 Hz | 1.61 | 3.1 dB  |
| Peaking | 17677 Hz | 0.8  | -7.7 dB |
| Peaking | 1547 Hz  | 2.74 | -1.8 dB |
| Peaking | 2658 Hz  | 4.23 | 1.5 dB  |
| Peaking | 4841 Hz  | 4.1  | -3.7 dB |
| Peaking | 6201 Hz  | 2.88 | 5.3 dB  |
| Peaking | 7552 Hz  | 2.63 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -4.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-REF%20Type-S%20Max%20Bass/Kumitate%20KL-REF%20Type-S%20Max%20Bass.png)