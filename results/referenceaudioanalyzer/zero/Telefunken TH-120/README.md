# Telefunken TH-120
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.2; 23 -13.8; 25 -14.3; 28 -14.8; 31 -15.2; 34 -15.5; 37 -15.7; 41 -15.9; 45 -16.0; 49 -16.1; 54 -16.2; 60 -16.2; 66 -16.2; 72 -16.1; 79 -15.9; 87 -15.8; 96 -15.6; 106 -15.4; 116 -15.1; 128 -14.8; 141 -14.4; 155 -14.0; 170 -13.8; 187 -13.6; 206 -13.2; 227 -12.6; 249 -12.0; 274 -11.4; 302 -10.7; 332 -9.9; 365 -9.2; 402 -8.4; 442 -7.6; 486 -6.7; 535 -5.7; 588 -4.8; 647 -3.7; 712 -2.8; 783 -2.1; 861 -1.7; 947 -1.6; 1042 -1.7; 1146 -1.4; 1261 -0.9; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -1.1; 2973 -3.4; 3270 -6.6; 3597 -9.4; 3957 -11.0; 4353 -12.4; 4788 -13.9; 5267 -13.8; 5793 -11.0; 6373 -4.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Telefunken TH-120 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Telefunken TH-120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 33 Hz   | 0.44 | -6.3 dB  |
| Peaking | 186 Hz  | 0.26 | -7.9 dB  |
| Peaking | 1573 Hz | 0.25 | 9.4 dB   |
| Peaking | 4810 Hz | 1.27 | -14.4 dB |
| Peaking | 6662 Hz | 5.34 | 7.3 dB   |
| Peaking | 771 Hz  | 1.75 | 2.2 dB   |
| Peaking | 929 Hz  | 0.88 | -1.7 dB  |
| Peaking | 2711 Hz | 2.74 | 3.0 dB   |
| Peaking | 3537 Hz | 2.18 | -2.6 dB  |
| Peaking | 4439 Hz | 5.34 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.9 dB |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Telefunken%20TH-120/Telefunken%20TH-120.png)