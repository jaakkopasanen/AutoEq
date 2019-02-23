# Ostry KC06
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.4; 25 -1.9; 28 -2.5; 31 -3.0; 34 -3.4; 37 -3.7; 41 -4.2; 45 -4.5; 49 -4.9; 54 -5.3; 60 -5.8; 66 -6.2; 72 -6.7; 79 -7.1; 87 -7.6; 96 -8.1; 106 -8.4; 116 -8.5; 128 -8.9; 141 -9.1; 155 -9.2; 170 -9.3; 187 -9.2; 206 -9.1; 227 -8.9; 249 -8.7; 274 -8.4; 302 -8.0; 332 -7.7; 365 -7.2; 402 -6.8; 442 -6.3; 486 -5.9; 535 -5.5; 588 -4.8; 647 -4.6; 712 -4.5; 783 -4.3; 861 -4.7; 947 -5.1; 1042 -5.8; 1146 -6.5; 1261 -7.4; 1387 -8.6; 1526 -9.6; 1678 -10.3; 1846 -10.5; 2031 -10.3; 2234 -9.8; 2457 -7.9; 2703 -5.4; 2973 -2.4; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -1.3; 5267 -1.3; 5793 -3.1; 6373 -7.6; 7010 -11.6; 7711 -9.7; 8482 -6.7; 9330 -6.9; 10263 -9.6; 11289 -7.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ostry KC06 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ostry KC06 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.39 | 6.5 dB   |
| Peaking | 179 Hz   | 0.56 | -3.5 dB  |
| Peaking | 1885 Hz  | 1.09 | -12.2 dB |
| Peaking | 4812 Hz  | 0.37 | 25.3 dB  |
| Peaking | 6883 Hz  | 0.52 | -22.7 dB |
| Peaking | 3195 Hz  | 7.15 | 2.3 dB   |
| Peaking | 6924 Hz  | 0.43 | -0.4 dB  |
| Peaking | 8463 Hz  | 8.25 | 2.3 dB   |
| Peaking | 9190 Hz  | 6.41 | 1.9 dB   |
| Peaking | 10463 Hz | 7.16 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 9.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ostry%20KC06/Ostry%20KC06.png)