# RHA S500i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.5; 28 -1.9; 31 -2.3; 34 -2.6; 37 -2.8; 41 -3.1; 45 -3.4; 49 -3.7; 54 -4.0; 60 -4.4; 66 -4.8; 72 -5.1; 79 -5.5; 87 -6.0; 96 -6.3; 106 -6.4; 116 -6.6; 128 -6.6; 141 -7.0; 155 -7.1; 170 -7.0; 187 -6.9; 206 -6.9; 227 -6.6; 249 -6.5; 274 -6.2; 302 -6.0; 332 -5.7; 365 -5.4; 402 -5.1; 442 -4.7; 486 -4.6; 535 -4.3; 588 -3.8; 647 -3.7; 712 -3.8; 783 -3.6; 861 -3.9; 947 -4.2; 1042 -4.9; 1146 -5.6; 1261 -6.2; 1387 -7.2; 1526 -8.2; 1678 -9.1; 1846 -9.6; 2031 -10.2; 2234 -11.4; 2457 -12.7; 2703 -14.9; 2973 -13.7; 3270 -9.0; 3597 -5.2; 3957 -3.9; 4353 -4.9; 4788 -5.1; 5267 -4.2; 5793 -4.7; 6373 -7.4; 7010 -10.7; 7711 -10.7; 8482 -8.7; 9330 -5.9; 10263 -4.6; 11289 -4.6; 12418 -6.1; 13660 -8.5; 15026 -7.3; 16529 -4.6; 18182 -4.6; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA S500i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA S500i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.58 | 4.9 dB  |
| Peaking | 147 Hz   | 0.81 | -2.8 dB |
| Peaking | 2537 Hz  | 2.13 | -9.9 dB |
| Peaking | 7506 Hz  | 4.37 | -7.0 dB |
| Peaking | 14050 Hz | 3.46 | -4.4 dB |
| Peaking | 786 Hz   | 1.52 | 1.8 dB  |
| Peaking | 1801 Hz  | 1.34 | -3.3 dB |
| Peaking | 2524 Hz  | 2.24 | 5.3 dB  |
| Peaking | 2881 Hz  | 3.65 | -6.9 dB |
| Peaking | 3688 Hz  | 2.34 | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20S500i/RHA%20S500i.png)