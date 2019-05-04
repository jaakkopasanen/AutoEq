# HyperX Cloud Core
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -5.1; 25 -5.6; 28 -6.3; 31 -6.8; 34 -7.1; 37 -7.4; 41 -7.5; 45 -7.6; 49 -7.6; 54 -7.7; 60 -7.8; 66 -8.0; 72 -8.2; 79 -8.5; 87 -8.9; 96 -9.3; 106 -9.7; 116 -9.9; 128 -10.1; 141 -10.2; 155 -10.1; 170 -9.7; 187 -9.1; 206 -8.5; 227 -7.6; 249 -6.7; 274 -5.9; 302 -5.3; 332 -5.2; 365 -5.3; 402 -5.3; 442 -5.3; 486 -5.6; 535 -5.8; 588 -5.7; 647 -5.6; 712 -5.5; 783 -5.4; 861 -5.4; 947 -4.5; 1042 -4.1; 1146 -4.1; 1261 -4.3; 1387 -4.7; 1526 -5.3; 1678 -6.1; 1846 -7.0; 2031 -8.1; 2234 -8.9; 2457 -8.2; 2703 -7.0; 2973 -6.1; 3270 -5.1; 3597 -3.2; 3957 -0.6; 4353 -0.5; 4788 -5.2; 5267 -7.7; 5793 -6.6; 6373 -6.5; 7010 -8.0; 7711 -10.3; 8482 -12.1; 9330 -12.0; 10263 -9.2; 11289 -7.0; 12418 -8.1; 13660 -10.3; 15026 -9.6; 16529 -7.8; 18182 -10.3; 20000 -15.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Core GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Core ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 140 Hz   | 0.8  | -5.4 dB |
| Peaking | 328 Hz   | 0.37 | 2.4 dB  |
| Peaking | 4132 Hz  | 4.78 | 7.2 dB  |
| Peaking | 8728 Hz  | 2.66 | -6.0 dB |
| Peaking | 20606 Hz | 0.49 | -9.2 dB |
| Peaking | 19 Hz    | 2.54 | 2.0 dB  |
| Peaking | 1212 Hz  | 2.83 | 1.9 dB  |
| Peaking | 2218 Hz  | 3.75 | -3.1 dB |
| Peaking | 13953 Hz | 4.99 | -3.0 dB |
| Peaking | 19853 Hz | 3.15 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Core/HyperX%20Cloud%20Core.png)