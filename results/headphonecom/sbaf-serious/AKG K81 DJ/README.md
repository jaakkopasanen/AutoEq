# AKG K81 DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.7; 170 -1.0; 187 -1.0; 206 -0.9; 227 -0.6; 249 -1.0; 274 -1.7; 302 -2.6; 332 -3.8; 365 -5.2; 402 -6.5; 442 -6.8; 486 -6.6; 535 -6.4; 588 -6.5; 647 -6.1; 712 -6.0; 783 -6.0; 861 -6.0; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -7.0; 1387 -7.5; 1526 -8.2; 1678 -8.1; 1846 -7.8; 2031 -7.7; 2234 -8.1; 2457 -6.5; 2703 -5.2; 2973 -3.8; 3270 -2.7; 3597 -3.3; 3957 -5.3; 4353 -6.5; 4788 -4.8; 5267 -1.3; 5793 -3.4; 6373 -7.9; 7010 -8.0; 7711 -6.5; 8482 -6.5; 9330 -7.4; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.9; 15026 -12.3; 16529 -12.1; 18182 -9.3; 20000 -8.6
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
| Peaking | 69 Hz    | 0.17 | 6.5 dB  |
| Peaking | 2282 Hz  | 0.16 | -2.5 dB |
| Peaking | 4077 Hz  | 0.85 | 5.1 dB  |
| Peaking | 13082 Hz | 1.51 | 5.5 dB  |
| Peaking | 15555 Hz | 1.04 | -8.1 dB |
| Peaking | 427 Hz   | 4.85 | -2.4 dB |
| Peaking | 3319 Hz  | 4.31 | 3.5 dB  |
| Peaking | 4378 Hz  | 2.09 | -4.0 dB |
| Peaking | 5437 Hz  | 4.73 | 6.6 dB  |
| Peaking | 6503 Hz  | 5.92 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 4.7 dB  |
| Peaking | 250 Hz   | 1.41 | 4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -5.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K81%20DJ/AKG%20K81%20DJ.png)