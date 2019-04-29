# Kumitate KL-REF Type-S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.0; 25 -3.1; 28 -3.1; 31 -3.2; 34 -3.3; 37 -3.3; 41 -3.4; 45 -3.5; 49 -3.5; 54 -3.5; 60 -3.5; 66 -3.7; 72 -3.9; 79 -4.0; 87 -4.2; 96 -4.5; 106 -4.8; 116 -4.9; 128 -5.1; 141 -5.3; 155 -5.5; 170 -5.6; 187 -5.6; 206 -5.6; 227 -5.6; 249 -5.6; 274 -5.5; 302 -5.4; 332 -5.4; 365 -5.5; 402 -5.5; 442 -5.5; 486 -5.5; 535 -5.4; 588 -5.2; 647 -5.0; 712 -4.7; 783 -4.5; 861 -4.2; 947 -4.3; 1042 -4.6; 1146 -5.4; 1261 -6.2; 1387 -6.7; 1526 -6.7; 1678 -6.2; 1846 -5.5; 2031 -4.8; 2234 -4.0; 2457 -3.0; 2703 -2.0; 2973 -1.0; 3270 -0.5; 3597 -0.6; 3957 -1.5; 4353 -3.4; 4788 -5.0; 5267 -3.7; 5793 -1.3; 6373 -1.6; 7010 -6.1; 7711 -7.0; 8482 -4.7; 9330 -4.4; 10263 -4.4; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -4.4; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-REF Type-S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-REF Type-S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 1.09 | 1.5 dB  |
| Peaking | 1500 Hz | 2.11 | -2.6 dB |
| Peaking | 3242 Hz | 2.35 | 4.5 dB  |
| Peaking | 6137 Hz | 6.13 | 4.2 dB  |
| Peaking | 7407 Hz | 5.01 | -3.7 dB |
| Peaking | 68 Hz   | 0.99 | 1.5 dB  |
| Peaking | 183 Hz  | 0.25 | -1.3 dB |
| Peaking | 905 Hz  | 2.43 | 1.2 dB  |
| Peaking | 4687 Hz | 2.13 | 1.5 dB  |
| Peaking | 4722 Hz | 5.27 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-REF%20Type-S/Kumitate%20KL-REF%20Type-S.png)