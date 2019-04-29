# Kinera BD005
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.7; 23 -17.6; 25 -17.5; 28 -17.3; 31 -17.1; 34 -16.9; 37 -16.7; 41 -16.5; 45 -16.2; 49 -16.0; 54 -15.7; 60 -15.4; 66 -15.2; 72 -15.0; 79 -14.8; 87 -14.6; 96 -14.5; 106 -14.3; 116 -14.0; 128 -13.7; 141 -13.4; 155 -13.1; 170 -12.6; 187 -12.1; 206 -11.6; 227 -11.0; 249 -10.4; 274 -9.8; 302 -9.3; 332 -8.7; 365 -8.2; 402 -7.6; 442 -7.2; 486 -6.7; 535 -6.2; 588 -5.8; 647 -5.4; 712 -4.7; 783 -4.2; 861 -4.2; 947 -4.5; 1042 -4.9; 1146 -5.6; 1261 -6.4; 1387 -6.8; 1526 -6.9; 1678 -6.6; 1846 -6.3; 2031 -6.2; 2234 -6.0; 2457 -5.7; 2703 -5.3; 2973 -5.2; 3270 -5.4; 3597 -5.4; 3957 -6.1; 4353 -7.1; 4788 -4.9; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.0; 18182 -11.8; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kinera BD005 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kinera BD005 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.54 | -8.9 dB |
| Peaking | 101 Hz   | 0.31 | -6.8 dB |
| Peaking | 450 Hz   | 0.81 | 1.8 dB  |
| Peaking | 826 Hz   | 2.16 | 2.6 dB  |
| Peaking | 5845 Hz  | 3.46 | 6.8 dB  |
| Peaking | 1475 Hz  | 3.97 | -0.9 dB |
| Peaking | 3072 Hz  | 1.82 | 1.2 dB  |
| Peaking | 4392 Hz  | 4.5  | -2.4 dB |
| Peaking | 5093 Hz  | 9.11 | 2.0 dB  |
| Peaking | 19122 Hz | 1.14 | -6.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB  |
| Peaking | 125 Hz   | 1.41 | -6.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -2.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kinera%20BD005/Kinera%20BD005.png)