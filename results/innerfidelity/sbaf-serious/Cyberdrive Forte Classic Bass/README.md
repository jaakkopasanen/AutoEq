# Cyberdrive Forte Classic Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.1; 23 -16.1; 25 -16.2; 28 -16.2; 31 -16.2; 34 -16.2; 37 -16.2; 41 -16.2; 45 -16.2; 49 -16.2; 54 -16.2; 60 -16.2; 66 -16.2; 72 -16.3; 79 -16.3; 87 -16.4; 96 -16.4; 106 -16.2; 116 -16.0; 128 -15.9; 141 -15.6; 155 -15.2; 170 -14.8; 187 -14.3; 206 -13.9; 227 -13.2; 249 -12.7; 274 -11.9; 302 -11.2; 332 -10.5; 365 -9.7; 402 -8.9; 442 -8.1; 486 -7.6; 535 -6.8; 588 -5.9; 647 -5.4; 712 -5.0; 783 -4.0; 861 -4.3; 947 -4.2; 1042 -4.2; 1146 -4.3; 1261 -4.3; 1387 -4.5; 1526 -4.8; 1678 -4.5; 1846 -3.8; 2031 -3.0; 2234 -2.3; 2457 -1.2; 2703 -0.8; 2973 -0.5; 3270 -0.9; 3597 -2.4; 3957 -5.1; 4353 -8.0; 4788 -9.3; 5267 -10.0; 5793 -13.2; 6373 -17.0; 7010 -12.7; 7711 -9.0; 8482 -8.1; 9330 -8.8; 10263 -8.2; 11289 -4.9; 12418 -3.9; 13660 -3.9; 15026 -4.1; 16529 -7.6; 18182 -7.1; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cyberdrive Forte Classic Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cyberdrive Forte Classic Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.13 | -12.9 dB |
| Peaking | 3580 Hz  | 0.08 | 2.9 dB   |
| Peaking | 6287 Hz  | 2.09 | -15.0 dB |
| Peaking | 9795 Hz  | 3.32 | -4.8 dB  |
| Peaking | 17380 Hz | 1.19 | -5.7 dB  |
| Peaking | 19 Hz    | 2.23 | -1.0 dB  |
| Peaking | 726 Hz   | 1.48 | 1.1 dB   |
| Peaking | 1666 Hz  | 1.23 | -3.2 dB  |
| Peaking | 3090 Hz  | 1.08 | 3.8 dB   |
| Peaking | 4390 Hz  | 3.61 | -4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.6 dB |
| Peaking | 62 Hz    | 1.41 | -8.6 dB  |
| Peaking | 125 Hz   | 1.41 | -9.7 dB  |
| Peaking | 250 Hz   | 1.41 | -7.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cyberdrive%20Forte%20Classic%20Bass/Cyberdrive%20Forte%20Classic%20Bass.png)