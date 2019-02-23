# AKG K501
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -1.5; 72 -1.5; 79 -1.7; 87 -2.5; 96 -3.6; 106 -4.1; 116 -4.5; 128 -4.8; 141 -5.1; 155 -5.3; 170 -5.3; 187 -5.4; 206 -5.5; 227 -5.5; 249 -5.6; 274 -5.6; 302 -5.5; 332 -5.4; 365 -5.3; 402 -5.3; 442 -5.2; 486 -5.3; 535 -5.2; 588 -5.0; 647 -5.0; 712 -4.8; 783 -4.1; 861 -5.2; 947 -5.8; 1042 -6.4; 1146 -6.9; 1261 -7.6; 1387 -8.3; 1526 -8.7; 1678 -9.2; 1846 -9.0; 2031 -7.9; 2234 -8.2; 2457 -7.5; 2703 -7.7; 2973 -7.9; 3270 -8.3; 3597 -8.3; 3957 -7.5; 4353 -7.2; 4788 -6.3; 5267 -4.7; 5793 -6.3; 6373 -10.8; 7010 -7.5; 7711 -7.7; 8482 -9.9; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K501 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K501 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.46 | 6.6 dB  |
| Peaking | 752 Hz  | 0.87 | 3.1 dB  |
| Peaking | 1472 Hz | 0.51 | -2.1 dB |
| Peaking | 1607 Hz | 2.64 | -1.5 dB |
| Peaking | 8633 Hz | 4.84 | -3.6 dB |
| Peaking | 35 Hz   | 2.92 | -0.7 dB |
| Peaking | 76 Hz   | 5.47 | 0.9 dB  |
| Peaking | 3649 Hz | 3.87 | -1.1 dB |
| Peaking | 5604 Hz | 3.43 | 3.8 dB  |
| Peaking | 6227 Hz | 7.38 | -6.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K501/AKG%20K501.png)