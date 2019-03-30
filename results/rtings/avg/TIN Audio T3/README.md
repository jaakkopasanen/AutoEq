# TIN Audio T3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -6.8; 25 -6.8; 28 -6.7; 31 -6.5; 34 -6.4; 37 -6.2; 41 -6.0; 45 -5.8; 49 -5.7; 54 -5.6; 60 -5.7; 66 -5.8; 72 -5.9; 79 -5.9; 87 -6.0; 96 -6.3; 106 -6.6; 116 -6.9; 128 -7.3; 141 -7.4; 155 -7.5; 170 -7.5; 187 -7.6; 206 -7.6; 227 -7.6; 249 -7.4; 274 -7.2; 302 -6.8; 332 -6.4; 365 -6.0; 402 -5.6; 442 -5.2; 486 -4.7; 535 -4.1; 588 -3.5; 647 -2.8; 712 -2.3; 783 -2.0; 861 -1.9; 947 -2.2; 1042 -2.6; 1146 -3.0; 1261 -3.4; 1387 -3.7; 1526 -3.8; 1678 -4.1; 1846 -4.5; 2031 -4.6; 2234 -4.1; 2457 -3.2; 2703 -2.0; 2973 -0.6; 3270 -0.5; 3597 -1.2; 3957 -2.5; 4353 -4.1; 4788 -5.3; 5267 -5.8; 5793 -4.5; 6373 -3.5; 7010 -3.0; 7711 -5.0; 8482 -9.4; 9330 -13.9; 10263 -13.6; 11289 -7.1; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TIN Audio T3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TIN Audio T3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.1  | -2.0 dB  |
| Peaking | 199 Hz   | 0.66 | -2.9 dB  |
| Peaking | 806 Hz   | 1.28 | 3.4 dB   |
| Peaking | 3209 Hz  | 2.7  | 4.8 dB   |
| Peaking | 9736 Hz  | 4.21 | -11.1 dB |
| Peaking | 5125 Hz  | 4.85 | -1.9 dB  |
| Peaking | 6944 Hz  | 2.94 | 2.9 dB   |
| Peaking | 8744 Hz  | 6.66 | -2.6 dB  |
| Peaking | 12146 Hz | 7.13 | 1.5 dB   |
| Peaking | 21183 Hz | 0.93 | 0.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/TIN%20Audio%20T3/TIN%20Audio%20T3.png)