# RHA TrueConnect
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.0; 25 -10.8; 28 -10.5; 31 -10.3; 34 -10.0; 37 -9.7; 41 -9.4; 45 -9.1; 49 -8.9; 54 -8.7; 60 -8.7; 66 -8.8; 72 -8.8; 79 -8.8; 87 -8.9; 96 -9.1; 106 -9.3; 116 -9.6; 128 -9.9; 141 -10.1; 155 -10.4; 170 -10.4; 187 -10.2; 206 -9.9; 227 -9.5; 249 -9.1; 274 -8.6; 302 -8.0; 332 -7.5; 365 -7.0; 402 -6.5; 442 -6.0; 486 -5.4; 535 -4.8; 588 -4.3; 647 -3.9; 712 -3.5; 783 -3.2; 861 -3.2; 947 -3.7; 1042 -4.4; 1146 -5.1; 1261 -5.7; 1387 -6.0; 1526 -6.0; 1678 -6.0; 1846 -6.0; 2031 -5.7; 2234 -4.7; 2457 -3.9; 2703 -3.5; 2973 -2.4; 3270 -0.7; 3597 -0.5; 3957 -1.3; 4353 -2.2; 4788 -2.2; 5267 -2.1; 5793 -2.2; 6373 -3.4; 7010 -6.9; 7711 -11.1; 8482 -11.3; 9330 -10.7; 10263 -13.3; 11289 -15.8; 12418 -13.3; 13660 -8.2; 15026 -7.3; 16529 -12.9; 18182 -17.4; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA TrueConnect GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA TrueConnect ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.21 | -5.2 dB  |
| Peaking | 167 Hz   | 1.19 | -4.2 dB  |
| Peaking | 4211 Hz  | 0.97 | 5.8 dB   |
| Peaking | 10534 Hz | 1.41 | -8.9 dB  |
| Peaking | 18546 Hz | 1.3  | -12.3 dB |
| Peaking | 777 Hz   | 1.66 | 3.2 dB   |
| Peaking | 1665 Hz  | 1.79 | -1.5 dB  |
| Peaking | 6210 Hz  | 4.84 | 2.3 dB   |
| Peaking | 7703 Hz  | 6.57 | -3.9 dB  |
| Peaking | 14514 Hz | 5.08 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | -8.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/RHA%20TrueConnect/RHA%20TrueConnect.png)