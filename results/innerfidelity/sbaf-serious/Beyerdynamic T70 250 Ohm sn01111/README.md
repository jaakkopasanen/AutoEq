# Beyerdynamic T70 250 Ohm sn01111
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.0; 25 -2.2; 28 -2.5; 31 -2.8; 34 -3.0; 37 -3.1; 41 -3.4; 45 -3.6; 49 -3.8; 54 -4.0; 60 -4.2; 66 -4.4; 72 -4.6; 79 -4.9; 87 -5.1; 96 -5.3; 106 -5.5; 116 -5.9; 128 -6.7; 141 -7.4; 155 -7.5; 170 -6.5; 187 -7.3; 206 -7.1; 227 -6.7; 249 -6.5; 274 -6.4; 302 -6.4; 332 -6.7; 365 -6.9; 402 -7.1; 442 -6.4; 486 -6.3; 535 -6.0; 588 -5.9; 647 -6.1; 712 -6.3; 783 -6.2; 861 -6.4; 947 -6.5; 1042 -6.4; 1146 -6.5; 1261 -6.6; 1387 -6.9; 1526 -7.0; 1678 -6.8; 1846 -5.9; 2031 -4.8; 2234 -3.1; 2457 -2.1; 2703 -2.6; 2973 -2.4; 3270 -2.5; 3597 -2.2; 3957 -0.5; 4353 -1.7; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -6.0; 7711 -11.2; 8482 -14.5; 9330 -14.4; 10263 -11.0; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70 250 Ohm sn01111 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm sn01111 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.56 | 4.4 dB   |
| Peaking | 2490 Hz  | 3.66 | 3.5 dB   |
| Peaking | 3931 Hz  | 2.03 | 4.5 dB   |
| Peaking | 5985 Hz  | 2.25 | 7.2 dB   |
| Peaking | 8635 Hz  | 2.55 | -10.9 dB |
| Peaking | 71 Hz    | 1.92 | 0.6 dB   |
| Peaking | 111 Hz   | 2.35 | 1.5 dB   |
| Peaking | 137 Hz   | 1.59 | -2.0 dB  |
| Peaking | 1546 Hz  | 4.21 | -1.1 dB  |
| Peaking | 11694 Hz | 5.96 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm%20sn01111/Beyerdynamic%20T70%20250%20Ohm%20sn01111.png)