# Ostry KC06
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.4; 25 -2.9; 28 -3.5; 31 -3.9; 34 -4.4; 37 -4.7; 41 -5.2; 45 -5.5; 49 -5.9; 54 -6.3; 60 -6.8; 66 -7.2; 72 -7.7; 79 -8.1; 87 -8.6; 96 -9.1; 106 -9.4; 116 -9.5; 128 -9.9; 141 -10.1; 155 -10.2; 170 -10.3; 187 -10.2; 206 -10.1; 227 -9.9; 249 -9.7; 274 -9.4; 302 -9.0; 332 -8.7; 365 -8.2; 402 -7.8; 442 -7.3; 486 -6.9; 535 -6.5; 588 -5.8; 647 -5.6; 712 -5.5; 783 -5.3; 861 -5.7; 947 -6.1; 1042 -6.8; 1146 -7.5; 1261 -8.4; 1387 -9.6; 1526 -10.6; 1678 -11.3; 1846 -11.5; 2031 -11.3; 2234 -10.8; 2457 -8.9; 2703 -6.4; 2973 -3.4; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -1.4; 4788 -2.3; 5267 -2.3; 5793 -4.1; 6373 -8.6; 7010 -12.6; 7711 -10.7; 8482 -7.5; 9330 -7.8; 10263 -10.6; 11289 -8.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ostry KC06 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ostry KC06 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.82 | 4.7 dB  |
| Peaking | 158 Hz   | 0.76 | -4.1 dB |
| Peaking | 2034 Hz  | 1.55 | -9.0 dB |
| Peaking | 3866 Hz  | 0.87 | 8.8 dB  |
| Peaking | 7196 Hz  | 2.17 | -8.5 dB |
| Peaking | 754 Hz   | 2.07 | 1.9 dB  |
| Peaking | 1451 Hz  | 4.37 | -1.4 dB |
| Peaking | 5609 Hz  | 9.92 | 1.9 dB  |
| Peaking | 8608 Hz  | 6.54 | 2.4 dB  |
| Peaking | 10457 Hz | 5.2  | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ostry%20KC06/Ostry%20KC06.png)