# Telefunken TH-140
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -10.2; 25 -10.6; 28 -11.1; 31 -11.5; 34 -11.7; 37 -11.9; 41 -12.0; 45 -12.0; 49 -11.9; 54 -11.8; 60 -11.6; 66 -11.4; 72 -11.1; 79 -10.8; 87 -10.5; 96 -10.0; 106 -9.6; 116 -9.1; 128 -8.7; 141 -8.1; 155 -7.6; 170 -7.1; 187 -6.7; 206 -6.3; 227 -6.0; 249 -5.6; 274 -5.2; 302 -4.8; 332 -4.4; 365 -4.0; 402 -3.6; 442 -3.3; 486 -3.0; 535 -2.7; 588 -2.4; 647 -2.2; 712 -1.9; 783 -1.7; 861 -1.5; 947 -1.3; 1042 -1.1; 1146 -1.0; 1261 -1.0; 1387 -1.0; 1526 -1.3; 1678 -1.6; 1846 -2.0; 2031 -2.7; 2234 -3.7; 2457 -5.0; 2703 -6.5; 2973 -8.4; 3270 -10.3; 3597 -11.3; 3957 -11.6; 4353 -12.0; 4788 -11.5; 5267 -9.4; 5793 -5.1; 6373 -0.5; 7010 -2.2; 7711 -4.4; 8482 -4.7; 9330 -6.2; 10263 -6.8; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Telefunken TH-140 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Telefunken TH-140 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.77 | -3.0 dB  |
| Peaking | 62 Hz   | 0.47 | -5.9 dB  |
| Peaking | 1709 Hz | 0.39 | 5.9 dB   |
| Peaking | 4098 Hz | 0.91 | -11.9 dB |
| Peaking | 6483 Hz | 3.49 | 9.0 dB   |
| Peaking | 2310 Hz | 1.38 | 1.7 dB   |
| Peaking | 3125 Hz | 0.75 | -1.8 dB  |
| Peaking | 4000 Hz | 4.7  | 1.8 dB   |
| Peaking | 9885 Hz | 1.37 | 1.8 dB   |
| Peaking | 9927 Hz | 5.36 | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -8.5 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Telefunken%20TH-140/Telefunken%20TH-140.png)