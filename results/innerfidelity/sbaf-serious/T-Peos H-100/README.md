# T-Peos H-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.9; 23 -12.6; 25 -12.4; 28 -11.9; 31 -11.6; 34 -11.2; 37 -10.8; 41 -10.4; 45 -10.1; 49 -9.7; 54 -9.4; 60 -9.1; 66 -8.9; 72 -8.7; 79 -8.5; 87 -8.4; 96 -8.3; 106 -8.1; 116 -7.8; 128 -7.7; 141 -7.6; 155 -7.3; 170 -7.1; 187 -6.9; 206 -6.6; 227 -6.3; 249 -6.1; 274 -5.8; 302 -5.6; 332 -5.3; 365 -5.1; 402 -4.9; 442 -4.6; 486 -4.6; 535 -4.5; 588 -4.3; 647 -4.3; 712 -4.5; 783 -4.6; 861 -5.1; 947 -5.8; 1042 -6.6; 1146 -7.5; 1261 -8.4; 1387 -9.8; 1526 -11.0; 1678 -12.3; 1846 -13.7; 2031 -14.8; 2234 -15.4; 2457 -14.3; 2703 -13.2; 2973 -12.1; 3270 -11.7; 3597 -6.9; 3957 -2.8; 4353 -3.3; 4788 -3.9; 5267 -2.0; 5793 -0.5; 6373 -0.8; 7010 -3.8; 7711 -6.0; 8482 -7.6; 9330 -12.7; 10263 -15.9; 11289 -13.7; 12418 -9.6; 13660 -6.8; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos H-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos H-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.26 | -7.0 dB  |
| Peaking | 2289 Hz  | 1.52 | -9.8 dB  |
| Peaking | 4030 Hz  | 6.38 | 5.0 dB   |
| Peaking | 5996 Hz  | 2.17 | 7.6 dB   |
| Peaking | 10366 Hz | 2.66 | -10.9 dB |
| Peaking | 662 Hz   | 0.87 | 2.8 dB   |
| Peaking | 1697 Hz  | 1.49 | -2.7 dB  |
| Peaking | 2379 Hz  | 1.22 | 1.8 dB   |
| Peaking | 3175 Hz  | 6.69 | -3.2 dB  |
| Peaking | 14390 Hz | 4.28 | 1.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB   |
| Peaking | 500 Hz   | 1.41 | 2.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -1.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20H-100/T-Peos%20H-100.png)