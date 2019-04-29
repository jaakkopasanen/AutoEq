# Symphonium Audio Aurora
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.0; 25 -5.3; 28 -5.7; 31 -6.0; 34 -6.2; 37 -6.4; 41 -6.6; 45 -6.8; 49 -7.0; 54 -7.2; 60 -7.6; 66 -7.9; 72 -8.2; 79 -8.5; 87 -8.9; 96 -9.3; 106 -9.7; 116 -9.9; 128 -10.2; 141 -10.4; 155 -10.6; 170 -10.6; 187 -10.7; 206 -10.5; 227 -10.4; 249 -10.2; 274 -10.0; 302 -9.8; 332 -9.5; 365 -9.2; 402 -8.9; 442 -8.6; 486 -8.2; 535 -7.8; 588 -7.4; 647 -6.9; 712 -6.4; 783 -5.9; 861 -5.4; 947 -5.2; 1042 -5.3; 1146 -5.9; 1261 -6.4; 1387 -6.6; 1526 -6.2; 1678 -5.4; 1846 -4.8; 2031 -4.6; 2234 -4.4; 2457 -3.6; 2703 -2.1; 2973 -1.0; 3270 -0.5; 3597 -0.8; 3957 -2.1; 4353 -3.3; 4788 -2.4; 5267 -2.1; 5793 -1.9; 6373 -1.2; 7010 -3.7; 7711 -6.2; 8482 -7.5; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Symphonium Audio Aurora GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Symphonium Audio Aurora ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.21 | 1.8 dB  |
| Peaking | 151 Hz  | 0.68 | -4.1 dB |
| Peaking | 320 Hz  | 1.3  | -1.7 dB |
| Peaking | 3275 Hz | 1.64 | 5.7 dB  |
| Peaking | 6031 Hz | 3.62 | 4.4 dB  |
| Peaking | 547 Hz  | 2    | -0.7 dB |
| Peaking | 970 Hz  | 1.41 | 1.6 dB  |
| Peaking | 1321 Hz | 3.16 | -1.5 dB |
| Peaking | 6702 Hz | 8.56 | 1.5 dB  |
| Peaking | 8222 Hz | 4.67 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Symphonium%20Audio%20Aurora/Symphonium%20Audio%20Aurora.png)