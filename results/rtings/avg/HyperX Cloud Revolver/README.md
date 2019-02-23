# HyperX Cloud Revolver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.3; 25 -6.4; 28 -6.6; 31 -6.7; 34 -6.8; 37 -6.8; 41 -6.9; 45 -7.1; 49 -7.3; 54 -7.6; 60 -8.1; 66 -8.4; 72 -8.6; 79 -8.8; 87 -9.0; 96 -9.1; 106 -9.1; 116 -9.1; 128 -9.1; 141 -8.9; 155 -8.7; 170 -8.4; 187 -8.0; 206 -7.5; 227 -7.0; 249 -6.4; 274 -6.2; 302 -5.9; 332 -5.2; 365 -4.8; 402 -4.9; 442 -5.1; 486 -4.7; 535 -4.3; 588 -4.1; 647 -4.0; 712 -4.0; 783 -3.7; 861 -4.1; 947 -4.6; 1042 -5.2; 1146 -5.8; 1261 -6.2; 1387 -6.9; 1526 -7.9; 1678 -9.7; 1846 -10.4; 2031 -10.1; 2234 -8.7; 2457 -7.1; 2703 -6.5; 2973 -6.1; 3270 -4.3; 3597 -1.4; 3957 -0.5; 4353 -1.6; 4788 -2.5; 5267 -3.0; 5793 -2.5; 6373 -2.2; 7010 -3.2; 7711 -5.4; 8482 -6.0; 9330 -7.8; 10263 -6.2; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -7.7; 18182 -9.9; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Revolver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Revolver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 100 Hz   | 0.86 | -3.8 dB |
| Peaking | 1925 Hz  | 2.79 | -5.4 dB |
| Peaking | 3979 Hz  | 3.07 | 5.5 dB  |
| Peaking | 6213 Hz  | 3.62 | 3.5 dB  |
| Peaking | 18490 Hz | 1.27 | -4.5 dB |
| Peaking | 184 Hz   | 1.64 | -1.5 dB |
| Peaking | 622 Hz   | 0.29 | 1.2 dB  |
| Peaking | 782 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1447 Hz  | 0.75 | -1.5 dB |
| Peaking | 9239 Hz  | 6.16 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Revolver/HyperX%20Cloud%20Revolver.png)