# Beyerdynamic DT 48
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.2; 72 -7.9; 79 -14.4; 87 -13.1; 96 -10.7; 106 -10.7; 116 -10.4; 128 -9.8; 141 -9.2; 155 -8.3; 170 -9.1; 187 -8.9; 206 -8.3; 227 -7.7; 249 -7.2; 274 -6.6; 302 -5.9; 332 -5.4; 365 -5.0; 402 -4.4; 442 -3.3; 486 -2.4; 535 -1.3; 588 -0.5; 647 -1.2; 712 -3.0; 783 -3.7; 861 -4.3; 947 -6.1; 1042 -7.8; 1146 -9.6; 1261 -10.7; 1387 -11.5; 1526 -12.4; 1678 -13.5; 1846 -14.0; 2031 -13.7; 2234 -12.8; 2457 -9.9; 2703 -7.1; 2973 -5.2; 3270 -4.7; 3597 -2.9; 3957 -1.6; 4353 -1.2; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.4; 7711 -11.7; 8482 -16.6; 9330 -13.4; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -11.2; 16529 -16.3; 18182 -17.2; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 163 Hz   | 0.8  | -5.9 dB  |
| Peaking | 1776 Hz  | 0.75 | -22.4 dB |
| Peaking | 3030 Hz  | 0.11 | 14.5 dB  |
| Peaking | 8595 Hz  | 3.12 | -19.0 dB |
| Peaking | 17334 Hz | 0.67 | -16.2 dB |
| Peaking | 29 Hz    | 0.54 | 6.4 dB   |
| Peaking | 66 Hz    | 2.25 | 9.9 dB   |
| Peaking | 79 Hz    | 2.78 | -14.5 dB |
| Peaking | 601 Hz   | 5.28 | 2.8 dB   |
| Peaking | 1144 Hz  | 4.5  | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 8.3 dB   |
| Peaking | 62 Hz    | 1.41 | 1.0 dB   |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 6.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.2 dB |
| Peaking | 4000 Hz  | 1.41 | 9.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB  |
| Peaking | 16000 Hz | 1.41 | -8.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048/Beyerdynamic%20DT%2048.png)