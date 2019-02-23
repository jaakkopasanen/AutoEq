# Bluedio T3 Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.2; 23 -16.4; 25 -16.5; 28 -16.6; 31 -16.6; 34 -16.5; 37 -16.3; 41 -16.1; 45 -16.0; 49 -16.0; 54 -16.1; 60 -16.4; 66 -16.8; 72 -17.2; 79 -17.5; 87 -18.0; 96 -18.5; 106 -19.0; 116 -19.5; 128 -19.8; 141 -19.8; 155 -19.7; 170 -19.3; 187 -18.5; 206 -17.3; 227 -16.0; 249 -14.3; 274 -12.1; 302 -9.8; 332 -7.2; 365 -4.4; 402 -1.2; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -2.6; 1678 -4.9; 1846 -8.8; 2031 -11.7; 2234 -13.2; 2457 -13.7; 2703 -14.2; 2973 -14.4; 3270 -14.3; 3597 -13.9; 3957 -11.3; 4353 -7.4; 4788 -4.2; 5267 -3.2; 5793 -3.1; 6373 -5.1; 7010 -4.9; 7711 -6.5; 8482 -7.8; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.4; 16529 -9.6; 18182 -9.6; 20000 -6.5
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
| Peaking | 25 Hz    | 0.1  | -9.1 dB  |
| Peaking | 181 Hz   | 0.71 | -14.2 dB |
| Peaking | 675 Hz   | 0.25 | 12.8 dB  |
| Peaking | 2818 Hz  | 0.82 | -16.0 dB |
| Peaking | 5309 Hz  | 2.06 | 8.1 dB   |
| Peaking | 426 Hz   | 3.03 | 4.3 dB   |
| Peaking | 601 Hz   | 0.64 | -1.9 dB  |
| Peaking | 1428 Hz  | 2.53 | 3.4 dB   |
| Peaking | 2009 Hz  | 5.15 | -2.7 dB  |
| Peaking | 17382 Hz | 2.07 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB  |
| Peaking | 125 Hz   | 1.41 | -12.8 dB |
| Peaking | 250 Hz   | 1.41 | -7.0 dB  |
| Peaking | 500 Hz   | 1.41 | 7.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -2.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20T3%20Plus/Bluedio%20T3%20Plus.png)