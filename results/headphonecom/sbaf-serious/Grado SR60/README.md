# Grado SR60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.3; 41 -2.2; 45 -3.0; 49 -3.6; 54 -4.1; 60 -4.8; 66 -5.0; 72 -5.1; 79 -5.6; 87 -6.0; 96 -6.0; 106 -6.1; 116 -6.1; 128 -6.0; 141 -5.6; 155 -5.6; 170 -5.7; 187 -5.5; 206 -5.0; 227 -5.2; 249 -6.0; 274 -5.9; 302 -5.6; 332 -5.2; 365 -5.0; 402 -4.7; 442 -4.6; 486 -4.5; 535 -4.3; 588 -4.3; 647 -4.1; 712 -4.1; 783 -4.1; 861 -4.2; 947 -4.4; 1042 -4.8; 1146 -5.0; 1261 -5.5; 1387 -6.3; 1526 -7.4; 1678 -8.5; 1846 -9.2; 2031 -9.9; 2234 -10.3; 2457 -10.2; 2703 -9.2; 2973 -6.6; 3270 -4.4; 3597 -3.2; 3957 -4.7; 4353 -8.0; 4788 -12.3; 5267 -8.8; 5793 -7.1; 6373 -5.2; 7010 -7.9; 7711 -10.3; 8482 -12.7; 9330 -11.3; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.89 | 6.5 dB   |
| Peaking | 2165 Hz  | 0.91 | -15.7 dB |
| Peaking | 2666 Hz  | 0.33 | 12.0 dB  |
| Peaking | 4807 Hz  | 4.47 | -9.9 dB  |
| Peaking | 8459 Hz  | 2.15 | -10.1 dB |
| Peaking | 210 Hz   | 6.86 | 1.0 dB   |
| Peaking | 2697 Hz  | 6.98 | -1.8 dB  |
| Peaking | 3703 Hz  | 3.6  | 2.7 dB   |
| Peaking | 4227 Hz  | 3.16 | -1.5 dB  |
| Peaking | 14595 Hz | 2    | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR60/Grado%20SR60.png)