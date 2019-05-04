# Bluedio T3 Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.0; 23 -16.2; 25 -16.3; 28 -16.4; 31 -16.4; 34 -16.3; 37 -16.2; 41 -16.0; 45 -15.8; 49 -15.8; 54 -15.9; 60 -16.2; 66 -16.6; 72 -16.9; 79 -17.3; 87 -17.8; 96 -18.3; 106 -18.8; 116 -19.2; 128 -19.6; 141 -19.6; 155 -19.5; 170 -19.1; 187 -18.3; 206 -17.2; 227 -15.9; 249 -14.2; 274 -12.1; 302 -9.7; 332 -7.3; 365 -4.3; 402 -1.1; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -2.7; 1678 -5.3; 1846 -9.2; 2031 -12.2; 2234 -14.1; 2457 -14.6; 2703 -14.7; 2973 -14.5; 3270 -14.1; 3597 -13.6; 3957 -11.0; 4353 -7.0; 4788 -4.5; 5267 -3.5; 5793 -3.2; 6373 -4.1; 7010 -5.0; 7711 -7.3; 8482 -7.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.0; 16529 -9.5; 18182 -9.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T3 Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T3 Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.12 | -9.0 dB  |
| Peaking | 182 Hz   | 0.72 | -13.9 dB |
| Peaking | 736 Hz   | 0.24 | 12.9 dB  |
| Peaking | 2694 Hz  | 0.85 | -17.1 dB |
| Peaking | 5389 Hz  | 2.11 | 7.1 dB   |
| Peaking | 428 Hz   | 2.95 | 4.4 dB   |
| Peaking | 573 Hz   | 0.63 | -2.0 dB  |
| Peaking | 1422 Hz  | 2.69 | 3.5 dB   |
| Peaking | 2009 Hz  | 5.18 | -2.5 dB  |
| Peaking | 17617 Hz | 2.15 | -3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.9 dB  |
| Peaking | 62 Hz    | 1.41 | -5.7 dB  |
| Peaking | 125 Hz   | 1.41 | -12.6 dB |
| Peaking | 250 Hz   | 1.41 | -7.0 dB  |
| Peaking | 500 Hz   | 1.41 | 7.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 8.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -2.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20T3%20Plus/Bluedio%20T3%20Plus.png)