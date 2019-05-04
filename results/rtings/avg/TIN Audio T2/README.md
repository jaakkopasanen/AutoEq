# TIN Audio T2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.1; 25 -2.6; 28 -3.1; 31 -3.6; 34 -3.9; 37 -4.3; 41 -4.6; 45 -5.0; 49 -5.3; 54 -5.6; 60 -6.0; 66 -6.4; 72 -6.7; 79 -7.1; 87 -7.5; 96 -7.9; 106 -8.3; 116 -8.6; 128 -8.9; 141 -9.0; 155 -9.1; 170 -9.2; 187 -9.1; 206 -9.1; 227 -8.9; 249 -9.0; 274 -9.0; 302 -8.9; 332 -8.7; 365 -8.4; 402 -8.1; 442 -7.8; 486 -7.4; 535 -6.9; 588 -6.4; 647 -5.8; 712 -5.3; 783 -4.9; 861 -4.7; 947 -4.9; 1042 -5.4; 1146 -6.0; 1261 -6.1; 1387 -4.9; 1526 -4.8; 1678 -5.0; 1846 -4.4; 2031 -3.7; 2234 -3.7; 2457 -3.2; 2703 -3.5; 2973 -4.5; 3270 -5.4; 3597 -6.1; 3957 -6.5; 4353 -7.0; 4788 -8.2; 5267 -6.3; 5793 -1.8; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.3; 10263 -9.3; 11289 -9.6; 12418 -6.6; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -8.8; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TIN Audio T2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TIN Audio T2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.58 | 5.1 dB  |
| Peaking | 181 Hz   | 0.6  | -3.6 dB |
| Peaking | 2226 Hz  | 1.93 | 2.8 dB  |
| Peaking | 6294 Hz  | 6.23 | 6.5 dB  |
| Peaking | 10845 Hz | 3.81 | -4.4 dB |
| Peaking | 391 Hz   | 2.16 | -0.8 dB |
| Peaking | 800 Hz   | 2.42 | 1.7 dB  |
| Peaking | 4917 Hz  | 3.63 | -3.7 dB |
| Peaking | 5633 Hz  | 4.56 | 2.5 dB  |
| Peaking | 18929 Hz | 2.08 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/TIN%20Audio%20T2/TIN%20Audio%20T2.png)