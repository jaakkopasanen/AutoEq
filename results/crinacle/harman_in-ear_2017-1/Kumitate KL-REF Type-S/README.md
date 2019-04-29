# Kumitate KL-REF Type-S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.2; 25 -6.3; 28 -6.4; 31 -6.4; 34 -6.5; 37 -6.6; 41 -6.6; 45 -6.7; 49 -6.7; 54 -6.7; 60 -6.8; 66 -6.9; 72 -7.1; 79 -7.2; 87 -7.5; 96 -7.7; 106 -8.0; 116 -8.1; 128 -8.3; 141 -8.6; 155 -8.7; 170 -8.8; 187 -8.9; 206 -8.8; 227 -8.8; 249 -8.8; 274 -8.7; 302 -8.6; 332 -8.4; 365 -8.4; 402 -8.4; 442 -8.4; 486 -8.3; 535 -8.1; 588 -8.0; 647 -7.8; 712 -7.5; 783 -7.2; 861 -7.0; 947 -7.1; 1042 -7.5; 1146 -8.2; 1261 -8.8; 1387 -8.9; 1526 -8.6; 1678 -8.1; 1846 -7.4; 2031 -6.3; 2234 -4.9; 2457 -3.3; 2703 -1.9; 2973 -0.8; 3270 -0.5; 3597 -0.7; 3957 -2.0; 4353 -4.3; 4788 -6.2; 5267 -4.9; 5793 -2.3; 6373 -2.2; 7010 -5.9; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.8; 16529 -14.8; 18182 -17.3; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-REF Type-S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-REF Type-S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 235 Hz   | 0.5  | -2.4 dB  |
| Peaking | 1484 Hz  | 1.95 | -2.9 dB  |
| Peaking | 3173 Hz  | 1.89 | 6.8 dB   |
| Peaking | 6123 Hz  | 6.15 | 4.7 dB   |
| Peaking | 18269 Hz | 1.21 | -12.2 dB |
| Peaking | 20 Hz    | 0.55 | 0.3 dB   |
| Peaking | 513 Hz   | 4.94 | -0.4 dB  |
| Peaking | 3884 Hz  | 7.15 | 1.1 dB   |
| Peaking | 4773 Hz  | 7.56 | -1.9 dB  |
| Peaking | 13539 Hz | 3.11 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -7.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-REF%20Type-S/Kumitate%20KL-REF%20Type-S.png)