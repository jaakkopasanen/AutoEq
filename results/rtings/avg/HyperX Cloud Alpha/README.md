# HyperX Cloud Alpha
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.5; 25 -8.6; 28 -8.6; 31 -8.7; 34 -8.7; 37 -8.6; 41 -8.5; 45 -8.4; 49 -8.4; 54 -8.3; 60 -8.2; 66 -8.4; 72 -8.5; 79 -8.7; 87 -9.0; 96 -9.3; 106 -9.7; 116 -10.0; 128 -10.2; 141 -10.3; 155 -10.3; 170 -10.3; 187 -10.1; 206 -10.0; 227 -9.8; 249 -9.6; 274 -9.6; 302 -9.8; 332 -9.7; 365 -9.3; 402 -8.9; 442 -8.5; 486 -8.3; 535 -7.9; 588 -7.5; 647 -7.1; 712 -6.7; 783 -6.6; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.8; 1261 -7.2; 1387 -7.9; 1526 -8.7; 1678 -9.5; 1846 -10.1; 2031 -10.2; 2234 -9.3; 2457 -8.3; 2703 -7.8; 2973 -7.5; 3270 -7.5; 3597 -6.2; 3957 -4.1; 4353 -1.9; 4788 -0.5; 5267 -0.6; 5793 -4.8; 6373 -6.2; 7010 -6.8; 7711 -9.8; 8482 -11.8; 9330 -12.1; 10263 -10.6; 11289 -7.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -11.3; 18182 -13.7; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Alpha GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Alpha ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 155 Hz   | 0.42 | -3.7 dB |
| Peaking | 1991 Hz  | 2.1  | -3.9 dB |
| Peaking | 4880 Hz  | 3.14 | 7.4 dB  |
| Peaking | 8916 Hz  | 2.77 | -6.4 dB |
| Peaking | 18197 Hz | 1.55 | -8.1 dB |
| Peaking | 26 Hz    | 1.67 | -1.8 dB |
| Peaking | 351 Hz   | 3.2  | -0.8 dB |
| Peaking | 854 Hz   | 1.88 | 1.0 dB  |
| Peaking | 3276 Hz  | 7.6  | -1.3 dB |
| Peaking | 13736 Hz | 2.42 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Alpha/HyperX%20Cloud%20Alpha.png)