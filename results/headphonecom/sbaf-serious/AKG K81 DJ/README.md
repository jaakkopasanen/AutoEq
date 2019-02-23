# AKG K81 DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -1.1; 141 -1.9; 155 -2.6; 170 -2.8; 187 -2.8; 206 -2.7; 227 -2.4; 249 -2.9; 274 -3.6; 302 -4.4; 332 -5.7; 365 -7.1; 402 -8.3; 442 -8.7; 486 -8.5; 535 -8.3; 588 -8.3; 647 -7.9; 712 -7.9; 783 -7.8; 861 -7.8; 947 -8.1; 1042 -8.5; 1146 -8.7; 1261 -8.9; 1387 -9.3; 1526 -10.1; 1678 -10.0; 1846 -9.6; 2031 -9.6; 2234 -10.0; 2457 -8.4; 2703 -7.1; 2973 -5.7; 3270 -4.5; 3597 -5.1; 3957 -7.2; 4353 -8.4; 4788 -6.7; 5267 -3.2; 5793 -5.3; 6373 -9.8; 7010 -9.9; 7711 -8.3; 8482 -7.9; 9330 -9.3; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -8.1; 15026 -14.1; 16529 -14.0; 18182 -11.2; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K81 DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K81 DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 56 Hz    | 0.22 | 6.7 dB  |
| Peaking | 247 Hz   | 2.77 | 2.4 dB  |
| Peaking | 660 Hz   | 0.31 | -3.2 dB |
| Peaking | 15738 Hz | 2.58 | -6.8 dB |
| Peaking | 18648 Hz | 0.68 | -4.2 dB |
| Peaking | 2046 Hz  | 2.34 | -1.9 dB |
| Peaking | 3272 Hz  | 3.6  | 4.0 dB  |
| Peaking | 5440 Hz  | 5.28 | 9.7 dB  |
| Peaking | 5984 Hz  | 1.82 | -5.5 dB |
| Peaking | 18839 Hz | 3.15 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 4.3 dB  |
| Peaking | 250 Hz   | 1.41 | 2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -7.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K81%20DJ/AKG%20K81%20DJ.png)