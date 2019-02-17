# Beyerdynamic T90
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.5; 31 -1.8; 34 -2.1; 37 -2.3; 41 -2.4; 45 -2.5; 49 -2.8; 54 -2.8; 60 -2.4; 66 -3.4; 72 -4.3; 79 -5.0; 87 -5.6; 96 -6.2; 106 -6.7; 116 -7.1; 128 -7.6; 141 -7.8; 155 -8.0; 170 -8.0; 187 -8.3; 206 -8.4; 227 -8.4; 249 -8.5; 274 -8.2; 302 -8.3; 332 -8.0; 365 -7.7; 402 -7.5; 442 -7.1; 486 -6.9; 535 -6.4; 588 -5.7; 647 -5.3; 712 -5.0; 783 -4.7; 861 -4.6; 947 -4.6; 1042 -4.8; 1146 -4.8; 1261 -5.0; 1387 -5.7; 1526 -6.5; 1678 -7.3; 1846 -7.6; 2031 -7.8; 2234 -7.9; 2457 -7.7; 2703 -8.2; 2973 -8.8; 3270 -8.8; 3597 -8.2; 3957 -8.4; 4353 -8.3; 4788 -2.8; 5267 -4.1; 5793 -5.0; 6373 -11.5; 7010 -13.7; 7711 -15.3; 8482 -16.8; 9330 -16.2; 10263 -12.7; 11289 -9.8; 12418 -8.7; 13660 -7.9; 15026 -7.8; 16529 -9.9; 18182 -11.1; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T90 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.21 | 4.1 dB   |
| Peaking | 189 Hz   | 0.57 | -4.4 dB  |
| Peaking | 2630 Hz  | 1.48 | -3.6 dB  |
| Peaking | 8614 Hz  | 1.96 | -12.7 dB |
| Peaking | 18080 Hz | 0.88 | -6.4 dB  |
| Peaking | 860 Hz   | 2.81 | 1.2 dB   |
| Peaking | 4244 Hz  | 2.71 | -5.3 dB  |
| Peaking | 5005 Hz  | 2.33 | 7.5 dB   |
| Peaking | 6651 Hz  | 6.19 | -4.8 dB  |
| Peaking | 7178 Hz  | 3.02 | -0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB   |
| Peaking | 62 Hz    | 1.41 | 1.5 dB   |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -11.0 dB |
| Peaking | 16000 Hz | 1.41 | -5.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T90/Beyerdynamic%20T90.png)