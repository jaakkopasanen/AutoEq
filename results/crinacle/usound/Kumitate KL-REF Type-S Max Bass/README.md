# Kumitate KL-REF Type-S Max Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.8; 25 -12.9; 28 -12.9; 31 -12.9; 34 -12.9; 37 -12.9; 41 -12.8; 45 -12.7; 49 -12.6; 54 -12.5; 60 -12.4; 66 -12.3; 72 -12.2; 79 -12.2; 87 -12.2; 96 -12.1; 106 -12.0; 116 -11.9; 128 -11.7; 141 -11.5; 155 -11.2; 170 -10.8; 187 -10.4; 206 -9.9; 227 -9.4; 249 -8.8; 274 -8.2; 302 -7.6; 332 -7.0; 365 -6.8; 402 -6.8; 442 -6.7; 486 -6.4; 535 -6.1; 588 -5.7; 647 -5.3; 712 -4.8; 783 -4.3; 861 -4.0; 947 -3.9; 1042 -4.1; 1146 -4.8; 1261 -5.6; 1387 -6.1; 1526 -6.0; 1678 -5.6; 1846 -4.9; 2031 -4.2; 2234 -3.5; 2457 -2.7; 2703 -1.7; 2973 -0.9; 3270 -0.5; 3597 -0.6; 3957 -1.6; 4353 -3.3; 4788 -4.7; 5267 -3.5; 5793 -1.2; 6373 -1.4; 7010 -5.4; 7711 -6.1; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-REF Type-S Max Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-REF Type-S Max Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 40 Hz   |  0.18 | -7.4 dB |
| Peaking | 831 Hz  |  2.01 | 2.1 dB  |
| Peaking | 3232 Hz |  1.96 | 5.4 dB  |
| Peaking | 6179 Hz |  4.6  | 5.5 dB  |
| Peaking | 7171 Hz |  3.17 | -2.2 dB |
| Peaking | 163 Hz  |  1.93 | -0.6 dB |
| Peaking | 334 Hz  |  2.96 | 0.9 dB  |
| Peaking | 1512 Hz |  2.46 | -2.3 dB |
| Peaking | 1576 Hz |  1.06 | 1.1 dB  |
| Peaking | 4781 Hz | 10.46 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-REF%20Type-S%20Max%20Bass/Kumitate%20KL-REF%20Type-S%20Max%20Bass.png)