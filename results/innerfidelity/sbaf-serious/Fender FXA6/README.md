# Fender FXA6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -10.7; 25 -10.7; 28 -10.6; 31 -10.5; 34 -10.5; 37 -10.4; 41 -10.4; 45 -10.4; 49 -10.4; 54 -10.5; 60 -10.5; 66 -10.7; 72 -10.9; 79 -11.1; 87 -11.3; 96 -11.5; 106 -11.6; 116 -11.6; 128 -11.7; 141 -11.7; 155 -11.7; 170 -11.6; 187 -11.4; 206 -11.1; 227 -10.8; 249 -10.5; 274 -10.0; 302 -9.6; 332 -9.1; 365 -8.6; 402 -8.1; 442 -7.5; 486 -7.1; 535 -6.6; 588 -5.9; 647 -5.5; 712 -5.3; 783 -4.9; 861 -5.1; 947 -5.3; 1042 -5.7; 1146 -5.9; 1261 -6.4; 1387 -7.4; 1526 -8.6; 1678 -10.0; 1846 -11.5; 2031 -12.3; 2234 -11.1; 2457 -7.7; 2703 -4.8; 2973 -2.3; 3270 -1.2; 3597 -2.7; 3957 -4.3; 4353 -3.6; 4788 -1.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 28 Hz   | 0.21 | -4.0 dB |
| Peaking | 169 Hz  | 0.87 | -3.8 dB |
| Peaking | 2027 Hz | 3.1  | -7.1 dB |
| Peaking | 3143 Hz | 3.19 | 5.6 dB  |
| Peaking | 5589 Hz | 2.49 | 6.6 dB  |
| Peaking | 44 Hz   | 2.52 | 0.2 dB  |
| Peaking | 332 Hz  | 1.89 | -1.0 dB |
| Peaking | 802 Hz  | 1.17 | 2.1 dB  |
| Peaking | 1613 Hz | 4.36 | -1.4 dB |
| Peaking | 8218 Hz | 4.44 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fender%20FXA6/Fender%20FXA6.png)