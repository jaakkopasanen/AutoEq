# Fender FXA9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.0; 25 -6.2; 28 -6.4; 31 -6.6; 34 -6.9; 37 -7.1; 41 -7.4; 45 -7.6; 49 -7.8; 54 -8.0; 60 -8.3; 66 -8.7; 72 -9.1; 79 -9.4; 87 -9.8; 96 -10.4; 106 -10.8; 116 -11.2; 128 -11.5; 141 -11.8; 155 -12.1; 170 -12.3; 187 -12.4; 206 -12.4; 227 -12.5; 249 -12.5; 274 -12.4; 302 -12.2; 332 -12.0; 365 -11.8; 402 -11.5; 442 -11.2; 486 -10.8; 535 -10.5; 588 -10.1; 647 -9.7; 712 -9.3; 783 -8.8; 861 -8.4; 947 -8.2; 1042 -8.2; 1146 -8.5; 1261 -8.8; 1387 -8.5; 1526 -7.5; 1678 -5.9; 1846 -4.1; 2031 -2.4; 2234 -1.4; 2457 -1.1; 2703 -2.0; 2973 -4.2; 3270 -6.5; 3597 -5.6; 3957 -0.8; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fender FXA9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fender FXA9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 122 Hz  | 0.8  | -1.9 dB |
| Peaking | 282 Hz  | 0.46 | -5.3 dB |
| Peaking | 1338 Hz | 3.2  | -2.0 dB |
| Peaking | 2268 Hz | 2.66 | 5.8 dB  |
| Peaking | 5148 Hz | 1.92 | 6.9 dB  |
| Peaking | 20 Hz   | 1.62 | 0.9 dB  |
| Peaking | 3419 Hz | 4.64 | -7.0 dB |
| Peaking | 3864 Hz | 1.87 | 6.5 dB  |
| Peaking | 5744 Hz | 1.21 | -5.2 dB |
| Peaking | 6246 Hz | 3.57 | 5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Fender%20FXA9/Fender%20FXA9.png)