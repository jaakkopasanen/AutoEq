# AKG K44
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.3; 25 -3.0; 28 -3.9; 31 -4.7; 34 -5.3; 37 -5.8; 41 -6.3; 45 -6.7; 49 -6.9; 54 -7.2; 60 -7.4; 66 -7.7; 72 -7.9; 79 -8.0; 87 -8.2; 96 -8.2; 106 -8.4; 116 -8.6; 128 -8.8; 141 -9.0; 155 -9.2; 170 -9.4; 187 -9.5; 206 -9.5; 227 -9.5; 249 -9.7; 274 -9.9; 302 -10.1; 332 -10.3; 365 -10.3; 402 -10.5; 442 -10.9; 486 -10.7; 535 -9.9; 588 -9.5; 647 -10.7; 712 -10.3; 783 -8.8; 861 -9.0; 947 -10.6; 1042 -11.3; 1146 -11.2; 1261 -10.2; 1387 -8.7; 1526 -7.1; 1678 -5.5; 1846 -4.2; 2031 -4.2; 2234 -2.5; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.3; 5267 -2.2; 5793 -0.5; 6373 -2.1; 7010 -5.4; 7711 -6.5; 8482 -7.3; 9330 -8.8; 10263 -10.6; 11289 -11.1; 12418 -9.6; 13660 -8.0; 15026 -7.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K44 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K44 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.78 | 5.1 dB  |
| Peaking | 853 Hz   | 0.14 | -4.4 dB |
| Peaking | 2573 Hz  | 1.34 | 7.0 dB  |
| Peaking | 4854 Hz  | 0.82 | 7.1 dB  |
| Peaking | 10678 Hz | 1.38 | -5.6 dB |
| Peaking | 726 Hz   | 0.35 | 0.3 dB  |
| Peaking | 828 Hz   | 6.07 | 2.3 dB  |
| Peaking | 1110 Hz  | 2.21 | -2.6 dB |
| Peaking | 1791 Hz  | 3.05 | 2.1 dB  |
| Peaking | 2059 Hz  | 4.82 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | -4.9 dB |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K44/AKG%20K44.png)