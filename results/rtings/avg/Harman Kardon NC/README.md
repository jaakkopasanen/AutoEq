# Harman Kardon NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.0; 25 -9.8; 28 -9.6; 31 -9.4; 34 -9.3; 37 -9.1; 41 -9.0; 45 -8.8; 49 -8.7; 54 -8.5; 60 -8.4; 66 -8.3; 72 -8.3; 79 -8.4; 87 -8.5; 96 -8.7; 106 -8.8; 116 -8.9; 128 -8.9; 141 -8.9; 155 -8.8; 170 -8.6; 187 -8.4; 206 -8.1; 227 -8.2; 249 -8.0; 274 -7.9; 302 -7.7; 332 -7.6; 365 -7.4; 402 -7.0; 442 -6.8; 486 -6.8; 535 -6.7; 588 -6.6; 647 -6.4; 712 -6.1; 783 -5.8; 861 -5.2; 947 -4.3; 1042 -3.3; 1146 -2.5; 1261 -1.9; 1387 -2.5; 1526 -4.4; 1678 -6.1; 1846 -6.8; 2031 -6.1; 2234 -5.1; 2457 -4.5; 2703 -5.1; 2973 -10.0; 3270 -11.8; 3597 -6.5; 3957 -2.7; 4353 -1.8; 4788 -2.1; 5267 -3.3; 5793 -0.5; 6373 -0.6; 7010 -5.0; 7711 -7.2; 8482 -6.5; 9330 -6.0; 10263 -7.2; 11289 -11.0; 12418 -14.1; 13660 -14.1; 15026 -12.0; 16529 -7.8; 18182 -6.0; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Harman Kardon NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Harman Kardon NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.06 | -3.0 dB |
| Peaking | 1199 Hz  | 2.82 | 4.4 dB  |
| Peaking | 3200 Hz  | 6.07 | -9.3 dB |
| Peaking | 5036 Hz  | 1.09 | 5.3 dB  |
| Peaking | 13259 Hz | 1.55 | -9.4 dB |
| Peaking | 21 Hz    | 2.21 | -0.9 dB |
| Peaking | 1843 Hz  | 3.5  | -4.5 dB |
| Peaking | 1901 Hz  | 1.79 | 2.6 dB  |
| Peaking | 6303 Hz  | 8.65 | 3.1 dB  |
| Peaking | 7519 Hz  | 6.31 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -7.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Harman%20Kardon%20NC/Harman%20Kardon%20NC.png)