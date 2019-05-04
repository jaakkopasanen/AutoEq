# Bluedio U Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.6; 23 -14.0; 25 -14.4; 28 -14.7; 31 -14.9; 34 -14.9; 37 -14.9; 41 -14.9; 45 -15.0; 49 -15.1; 54 -15.3; 60 -15.5; 66 -15.7; 72 -15.8; 79 -16.0; 87 -16.3; 96 -16.6; 106 -16.8; 116 -17.0; 128 -17.1; 141 -16.8; 155 -16.3; 170 -15.3; 187 -13.9; 206 -12.2; 227 -9.9; 249 -7.3; 274 -5.4; 302 -3.8; 332 -1.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -2.5; 947 -6.4; 1042 -8.9; 1146 -8.9; 1261 -8.2; 1387 -8.0; 1526 -9.2; 1678 -10.0; 1846 -10.1; 2031 -11.2; 2234 -13.1; 2457 -14.2; 2703 -14.6; 2973 -14.4; 3270 -13.2; 3597 -11.0; 3957 -7.3; 4353 -4.2; 4788 -6.8; 5267 -9.7; 5793 -8.2; 6373 -3.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -11.0; 10263 -8.9; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio U Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio U Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.35 | -7.9 dB |
| Peaking | 113 Hz  | 0.99 | -5.5 dB |
| Peaking | 174 Hz  | 1.49 | -5.7 dB |
| Peaking | 437 Hz  | 0.82 | 8.5 dB  |
| Peaking | 2493 Hz | 1.39 | -8.6 dB |
| Peaking | 787 Hz  | 3.85 | 3.9 dB  |
| Peaking | 1037 Hz | 3.79 | -4.4 dB |
| Peaking | 4329 Hz | 4.98 | 7.6 dB  |
| Peaking | 6123 Hz | 1.1  | -6.5 dB |
| Peaking | 6729 Hz | 3.29 | 10.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.2 dB  |
| Peaking | 62 Hz    | 1.41 | -5.8 dB  |
| Peaking | 125 Hz   | 1.41 | -11.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 9.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20U%20Plus/Bluedio%20U%20Plus.png)