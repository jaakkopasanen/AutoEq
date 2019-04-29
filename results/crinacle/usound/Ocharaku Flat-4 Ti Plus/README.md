# Ocharaku Flat-4 Ti Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.8; 25 -6.0; 28 -6.3; 31 -6.5; 34 -6.7; 37 -6.8; 41 -7.1; 45 -7.3; 49 -7.3; 54 -7.2; 60 -7.3; 66 -7.4; 72 -7.6; 79 -7.8; 87 -8.0; 96 -8.7; 106 -8.6; 116 -8.6; 128 -8.6; 141 -8.8; 155 -9.1; 170 -8.7; 187 -8.6; 206 -8.4; 227 -8.5; 249 -7.9; 274 -7.6; 302 -7.3; 332 -7.1; 365 -6.9; 402 -6.8; 442 -6.5; 486 -6.5; 535 -6.3; 588 -6.2; 647 -6.1; 712 -6.0; 783 -6.1; 861 -6.3; 947 -6.6; 1042 -7.1; 1146 -7.8; 1261 -8.0; 1387 -6.8; 1526 -4.0; 1678 -0.7; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -4.5; 2973 -9.0; 3270 -7.9; 3597 -4.3; 3957 -3.1; 4353 -3.7; 4788 -7.5; 5267 -10.4; 5793 -0.5; 6373 -3.8; 7010 -16.3; 7711 -21.6; 8482 -15.2; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -6.7; 15026 -6.5; 16529 -6.6; 18182 -11.9; 20000 -16.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Flat-4 Ti Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Flat-4 Ti Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 142 Hz  |  0.78 | -2.5 dB  |
| Peaking | 2039 Hz |  2.55 | 7.3 dB   |
| Peaking | 5778 Hz | 14.71 | 6.8 dB   |
| Peaking | 6196 Hz | 10.86 | 8.7 dB   |
| Peaking | 7604 Hz |  4.55 | -17.2 dB |
| Peaking | 1231 Hz |  4.7  | -3.0 dB  |
| Peaking | 3113 Hz |  4.55 | -9.2 dB  |
| Peaking | 3478 Hz |  1.52 | 5.6 dB   |
| Peaking | 5090 Hz | 10.14 | -6.9 dB  |
| Peaking | 9693 Hz |  8.15 | 2.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ocharaku%20Flat-4%20Ti%20Plus/Ocharaku%20Flat-4%20Ti%20Plus.png)