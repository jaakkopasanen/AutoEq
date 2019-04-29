# Kumitate KL-REF Type-S Half Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.2; 25 -6.3; 28 -6.3; 31 -6.4; 34 -6.4; 37 -6.4; 41 -6.4; 45 -6.4; 49 -6.3; 54 -6.3; 60 -6.2; 66 -6.2; 72 -6.3; 79 -6.3; 87 -6.5; 96 -6.6; 106 -6.7; 116 -6.7; 128 -6.8; 141 -6.8; 155 -6.8; 170 -6.7; 187 -6.6; 206 -6.5; 227 -6.3; 249 -6.1; 274 -5.9; 302 -5.7; 332 -5.6; 365 -5.7; 402 -5.8; 442 -5.7; 486 -5.6; 535 -5.5; 588 -5.3; 647 -5.1; 712 -4.8; 783 -4.5; 861 -4.2; 947 -4.2; 1042 -4.5; 1146 -5.3; 1261 -6.1; 1387 -6.6; 1526 -6.5; 1678 -6.1; 1846 -5.4; 2031 -4.6; 2234 -3.8; 2457 -3.0; 2703 -2.0; 2973 -1.1; 3270 -0.5; 3597 -0.6; 3957 -1.6; 4353 -3.4; 4788 -4.9; 5267 -3.7; 5793 -1.4; 6373 -1.8; 7010 -6.1; 7711 -6.6; 8482 -4.6; 9330 -4.6; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-REF Type-S Half Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-REF Type-S Half Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 84 Hz   | 0.23 | -2.0 dB |
| Peaking | 1507 Hz | 3.18 | -2.3 dB |
| Peaking | 3256 Hz | 2.3  | 4.6 dB  |
| Peaking | 6097 Hz | 5.87 | 4.1 dB  |
| Peaking | 7296 Hz | 5.24 | -3.2 dB |
| Peaking | 64 Hz   | 1.74 | 0.7 dB  |
| Peaking | 143 Hz  | 0.03 | -0.2 dB |
| Peaking | 884 Hz  | 3.08 | 1.1 dB  |
| Peaking | 4605 Hz | 1.95 | 1.6 dB  |
| Peaking | 4808 Hz | 5.02 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-REF%20Type-S%20Half%20Bass/Kumitate%20KL-REF%20Type-S%20Half%20Bass.png)