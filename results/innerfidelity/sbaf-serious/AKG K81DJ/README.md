# AKG K81DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.9; 28 -1.5; 31 -2.0; 34 -2.6; 37 -3.0; 41 -3.5; 45 -3.8; 49 -4.1; 54 -4.6; 60 -5.3; 66 -5.7; 72 -5.9; 79 -6.3; 87 -6.7; 96 -6.2; 106 -6.5; 116 -7.6; 128 -8.6; 141 -9.3; 155 -9.3; 170 -9.1; 187 -9.2; 206 -8.0; 227 -7.5; 249 -7.0; 274 -7.2; 302 -7.0; 332 -6.6; 365 -5.0; 402 -4.3; 442 -4.2; 486 -4.4; 535 -4.7; 588 -4.7; 647 -5.0; 712 -5.5; 783 -5.5; 861 -6.0; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -6.9; 1387 -7.6; 1526 -8.3; 1678 -8.8; 1846 -9.0; 2031 -8.5; 2234 -8.0; 2457 -6.0; 2703 -4.7; 2973 -3.2; 3270 -2.8; 3597 -3.3; 3957 -3.7; 4353 -4.5; 4788 -3.7; 5267 -3.1; 5793 -4.8; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.1; 16529 -8.7; 18182 -8.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K81DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K81DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.68 | 6.0 dB   |
| Peaking | 160 Hz   | 1.65 | -3.5 dB  |
| Peaking | 1705 Hz  | 0.96 | -10.8 dB |
| Peaking | 1878 Hz  | 0.43 | 8.1 dB   |
| Peaking | 6413 Hz  | 8.79 | 3.2 dB   |
| Peaking | 448 Hz   | 1.85 | 3.1 dB   |
| Peaking | 485 Hz   | 0.77 | -1.6 dB  |
| Peaking | 3169 Hz  | 5.54 | 1.6 dB   |
| Peaking | 8654 Hz  | 2.97 | -1.2 dB  |
| Peaking | 17106 Hz | 1.67 | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K81DJ/AKG%20K81DJ.png)