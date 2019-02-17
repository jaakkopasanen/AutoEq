# Fender FXA6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -11.7; 25 -11.6; 28 -11.6; 31 -11.5; 34 -11.4; 37 -11.4; 41 -11.4; 45 -11.3; 49 -11.4; 54 -11.4; 60 -11.5; 66 -11.6; 72 -11.8; 79 -12.0; 87 -12.2; 96 -12.5; 106 -12.5; 116 -12.6; 128 -12.7; 141 -12.7; 155 -12.6; 170 -12.5; 187 -12.3; 206 -12.1; 227 -11.7; 249 -11.4; 274 -11.0; 302 -10.5; 332 -10.1; 365 -9.6; 402 -9.1; 442 -8.4; 486 -8.1; 535 -7.6; 588 -6.8; 647 -6.5; 712 -6.3; 783 -5.9; 861 -6.0; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.3; 1387 -8.3; 1526 -9.5; 1678 -11.0; 1846 -12.4; 2031 -13.3; 2234 -12.0; 2457 -8.6; 2703 -5.8; 2973 -3.2; 3270 -2.2; 3597 -3.7; 3957 -5.3; 4353 -4.5; 4788 -2.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fender FXA6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fender FXA6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.14 | -4.9 dB |
| Peaking | 182 Hz  | 0.74 | -4.1 dB |
| Peaking | 2011 Hz | 2.58 | -7.8 dB |
| Peaking | 3124 Hz | 3.54 | 5.1 dB  |
| Peaking | 5657 Hz | 2.71 | 6.8 dB  |
| Peaking | 361 Hz  | 2    | -0.8 dB |
| Peaking | 777 Hz  | 2.37 | 0.5 dB  |
| Peaking | 806 Hz  | 1.11 | 1.0 dB  |
| Peaking | 1575 Hz | 4.68 | -1.0 dB |
| Peaking | 8213 Hz | 4.65 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fender%20FXA6/Fender%20FXA6.png)