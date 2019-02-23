# AKG K272HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.2; 37 -2.0; 41 -2.9; 45 -3.8; 49 -4.5; 54 -5.1; 60 -5.8; 66 -6.7; 72 -7.4; 79 -8.2; 87 -8.4; 96 -6.0; 106 -3.2; 116 -4.2; 128 -7.0; 141 -8.0; 155 -8.0; 170 -7.3; 187 -7.7; 206 -7.7; 227 -8.2; 249 -8.5; 274 -8.7; 302 -8.8; 332 -8.8; 365 -8.8; 402 -8.9; 442 -8.8; 486 -9.0; 535 -9.1; 588 -9.3; 647 -10.2; 712 -7.0; 783 -6.8; 861 -6.7; 947 -6.7; 1042 -7.5; 1146 -7.5; 1261 -8.3; 1387 -9.0; 1526 -10.0; 1678 -10.0; 1846 -8.8; 2031 -6.0; 2234 -4.9; 2457 -3.3; 2703 -2.8; 2973 -2.2; 3270 -2.6; 3597 -1.7; 3957 -1.1; 4353 -1.9; 4788 -1.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.9; 8482 -11.3; 9330 -13.7; 10263 -10.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K272HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K272HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 1.14 | 6.7 dB   |
| Peaking | 1071 Hz | 0.17 | -2.5 dB  |
| Peaking | 2839 Hz | 2.31 | 4.0 dB   |
| Peaking | 5569 Hz | 0.92 | 8.1 dB   |
| Peaking | 9005 Hz | 2.81 | -10.5 dB |
| Peaking | 96 Hz   | 1.73 | -3.8 dB  |
| Peaking | 108 Hz  | 4.4  | 7.4 dB   |
| Peaking | 895 Hz  | 3.17 | 2.4 dB   |
| Peaking | 1680 Hz | 3.16 | -3.1 dB  |
| Peaking | 2135 Hz | 4.7  | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K272HD/AKG%20K272HD.png)