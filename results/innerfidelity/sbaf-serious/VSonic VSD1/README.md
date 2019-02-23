# VSonic VSD1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.7; 25 -7.0; 28 -7.4; 31 -7.7; 34 -8.0; 37 -8.2; 41 -8.4; 45 -8.6; 49 -8.8; 54 -9.0; 60 -9.2; 66 -9.4; 72 -9.6; 79 -9.9; 87 -10.1; 96 -10.3; 106 -10.4; 116 -10.3; 128 -10.4; 141 -10.4; 155 -10.3; 170 -10.1; 187 -9.9; 206 -9.6; 227 -9.3; 249 -9.1; 274 -8.7; 302 -8.4; 332 -8.1; 365 -7.7; 402 -7.4; 442 -7.0; 486 -6.8; 535 -6.5; 588 -6.0; 647 -5.8; 712 -5.8; 783 -5.5; 861 -5.6; 947 -5.9; 1042 -6.2; 1146 -6.5; 1261 -6.8; 1387 -7.4; 1526 -8.1; 1678 -8.6; 1846 -8.2; 2031 -8.3; 2234 -8.0; 2457 -6.7; 2703 -4.9; 2973 -2.1; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -3.7; 4788 -6.4; 5267 -8.1; 5793 -6.3; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 88 Hz    | 0.64 | -3.3 dB |
| Peaking | 192 Hz   | 1.2  | -2.0 dB |
| Peaking | 2024 Hz  | 2.06 | -3.0 dB |
| Peaking | 3435 Hz  | 2.42 | 7.2 dB  |
| Peaking | 21957 Hz | 2.16 | 1.4 dB  |
| Peaking | 788 Hz   | 1.82 | 1.3 dB  |
| Peaking | 1535 Hz  | 5.34 | -0.9 dB |
| Peaking | 4134 Hz  | 6.28 | 2.4 dB  |
| Peaking | 5401 Hz  | 2.27 | -3.6 dB |
| Peaking | 6403 Hz  | 5.14 | 6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD1/VSonic%20VSD1.png)