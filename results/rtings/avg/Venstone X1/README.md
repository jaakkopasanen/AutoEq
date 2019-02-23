# Venstone X1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.4; 25 -5.8; 28 -6.4; 31 -6.8; 34 -7.2; 37 -7.6; 41 -8.0; 45 -8.4; 49 -8.8; 54 -9.2; 60 -9.7; 66 -10.1; 72 -10.5; 79 -10.9; 87 -11.4; 96 -11.8; 106 -12.3; 116 -12.8; 128 -13.1; 141 -13.4; 155 -13.4; 170 -13.4; 187 -13.3; 206 -13.0; 227 -12.7; 249 -12.4; 274 -12.3; 302 -12.1; 332 -11.8; 365 -11.2; 402 -10.4; 442 -9.5; 486 -8.4; 535 -7.1; 588 -6.0; 647 -5.1; 712 -4.4; 783 -4.2; 861 -3.6; 947 -2.8; 1042 -2.2; 1146 -1.5; 1261 -0.6; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -1.4; 2703 -1.7; 2973 -1.6; 3270 -2.2; 3597 -3.4; 3957 -5.1; 4353 -6.6; 4788 -9.4; 5267 -13.6; 5793 -11.2; 6373 -5.6; 7010 -4.0; 7711 -6.2; 8482 -8.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.7; 16529 -9.2; 18182 -9.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venstone X1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venstone X1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 149 Hz   | 0.56 | -6.8 dB  |
| Peaking | 356 Hz   | 1.28 | -3.1 dB  |
| Peaking | 1695 Hz  | 0.47 | 6.5 dB   |
| Peaking | 5275 Hz  | 4.45 | -10.0 dB |
| Peaking | 17570 Hz | 1.87 | -4.0 dB  |
| Peaking | 19 Hz    | 2.14 | 2.1 dB   |
| Peaking | 5829 Hz  | 7.26 | -1.9 dB  |
| Peaking | 6712 Hz  | 6.04 | 3.8 dB   |
| Peaking | 8390 Hz  | 6.44 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Venstone%20X1/Venstone%20X1.png)