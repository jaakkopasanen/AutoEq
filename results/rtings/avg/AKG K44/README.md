# AKG K44
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.2; 41 -1.7; 45 -2.1; 49 -2.3; 54 -2.6; 60 -2.8; 66 -3.1; 72 -3.3; 79 -3.4; 87 -3.6; 96 -3.6; 106 -3.8; 116 -4.0; 128 -4.2; 141 -4.4; 155 -4.6; 170 -4.8; 187 -4.9; 206 -4.9; 227 -4.9; 249 -5.1; 274 -5.3; 302 -5.5; 332 -5.7; 365 -5.7; 402 -5.9; 442 -6.3; 486 -6.1; 535 -5.3; 588 -4.9; 647 -6.1; 712 -5.7; 783 -4.2; 861 -4.4; 947 -6.0; 1042 -6.7; 1146 -6.6; 1261 -5.6; 1387 -4.1; 1526 -2.5; 1678 -0.9; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K44 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K44 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.49 | 6.0 dB  |
| Peaking | 124 Hz  | 0.58 | 1.5 dB  |
| Peaking | 578 Hz  | 3.27 | 0.6 dB  |
| Peaking | 2306 Hz | 1.13 | 6.0 dB  |
| Peaking | 4985 Hz | 1.55 | 5.5 dB  |
| Peaking | 833 Hz  | 5.28 | 2.7 dB  |
| Peaking | 1073 Hz | 1.87 | -2.2 dB |
| Peaking | 1663 Hz | 4.5  | 2.1 dB  |
| Peaking | 6478 Hz | 4.48 | 3.4 dB  |
| Peaking | 7545 Hz | 1.75 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.8 dB  |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K44/AKG%20K44.png)