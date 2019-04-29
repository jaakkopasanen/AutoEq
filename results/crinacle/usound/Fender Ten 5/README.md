# Fender Ten 5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.1; 25 -5.5; 28 -6.0; 31 -6.3; 34 -6.6; 37 -6.9; 41 -7.1; 45 -7.3; 49 -7.4; 54 -7.6; 60 -7.8; 66 -8.1; 72 -8.2; 79 -8.4; 87 -8.5; 96 -8.7; 106 -8.9; 116 -8.9; 128 -8.9; 141 -8.8; 155 -8.7; 170 -8.4; 187 -8.2; 206 -7.9; 227 -7.6; 249 -7.2; 274 -6.9; 302 -6.5; 332 -6.1; 365 -5.8; 402 -5.4; 442 -5.1; 486 -4.8; 535 -4.5; 588 -4.3; 647 -4.2; 712 -4.0; 783 -3.9; 861 -3.9; 947 -4.4; 1042 -5.2; 1146 -6.6; 1261 -8.0; 1387 -9.1; 1526 -9.3; 1678 -8.4; 1846 -6.7; 2031 -4.9; 2234 -3.8; 2457 -3.7; 2703 -4.7; 2973 -6.1; 3270 -6.9; 3597 -6.1; 3957 -3.9; 4353 -1.5; 4788 -2.1; 5267 -3.4; 5793 -1.9; 6373 -0.5; 7010 -3.0; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fender Ten 5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fender Ten 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 80 Hz   | 0.82 | -2.7 dB |
| Peaking | 162 Hz  | 1.46 | -2.3 dB |
| Peaking | 1500 Hz | 3.69 | -4.5 dB |
| Peaking | 2287 Hz | 5.17 | 2.3 dB  |
| Peaking | 5809 Hz | 2.03 | 4.2 dB  |
| Peaking | 18 Hz   | 2.34 | 1.3 dB  |
| Peaking | 721 Hz  | 1.84 | 2.0 dB  |
| Peaking | 3332 Hz | 5.02 | -2.3 dB |
| Peaking | 4375 Hz | 7.84 | 3.1 dB  |
| Peaking | 8308 Hz | 4.11 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Fender%20Ten%205/Fender%20Ten%205.png)