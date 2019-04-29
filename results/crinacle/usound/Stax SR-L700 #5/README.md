# Stax SR-L700 #5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -2.0; 66 -3.0; 72 -3.4; 79 -4.1; 87 -4.6; 96 -4.8; 106 -5.0; 116 -5.2; 128 -5.4; 141 -5.6; 155 -5.8; 170 -5.9; 187 -5.9; 206 -5.9; 227 -6.1; 249 -6.1; 274 -6.2; 302 -6.5; 332 -6.6; 365 -6.8; 402 -6.8; 442 -7.1; 486 -7.1; 535 -7.5; 588 -7.7; 647 -7.9; 712 -8.4; 783 -8.8; 861 -8.7; 947 -9.4; 1042 -9.4; 1146 -9.9; 1261 -9.6; 1387 -9.2; 1526 -8.0; 1678 -6.5; 1846 -5.2; 2031 -4.7; 2234 -3.9; 2457 -4.5; 2703 -4.6; 2973 -4.1; 3270 -3.6; 3597 -4.4; 3957 -3.7; 4353 -2.9; 4788 -1.9; 5267 -4.4; 5793 -9.2; 6373 -9.4; 7010 -7.0; 7711 -6.9; 8482 -8.5; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -7.8; 13660 -12.6; 15026 -10.8; 16529 -9.0; 18182 -11.5; 20000 -14.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L700 #5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L700 #5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.6  | 6.6 dB  |
| Peaking | 1112 Hz  | 1.11 | -4.3 dB |
| Peaking | 3809 Hz  | 0.55 | 4.2 dB  |
| Peaking | 6141 Hz  | 5.18 | -6.0 dB |
| Peaking | 20529 Hz | 0.12 | -5.7 dB |
| Peaking | 3647 Hz  | 5.27 | -1.1 dB |
| Peaking | 4813 Hz  | 5.6  | 2.8 dB  |
| Peaking | 11779 Hz | 2.17 | 7.1 dB  |
| Peaking | 14334 Hz | 0.81 | -8.2 dB |
| Peaking | 15971 Hz | 1.55 | 7.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -4.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -5.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Stax%20SR-L700%20#5/Stax%20SR-L700%20#5.png)