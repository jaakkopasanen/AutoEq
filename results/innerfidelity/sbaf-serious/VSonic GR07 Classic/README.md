# VSonic GR07 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.9; 25 -5.3; 28 -5.7; 31 -6.1; 34 -6.3; 37 -6.6; 41 -6.8; 45 -7.0; 49 -7.2; 54 -7.5; 60 -7.8; 66 -8.0; 72 -8.2; 79 -8.6; 87 -8.8; 96 -9.1; 106 -9.3; 116 -9.3; 128 -9.5; 141 -9.6; 155 -9.6; 170 -9.6; 187 -9.5; 206 -9.4; 227 -9.3; 249 -9.2; 274 -8.9; 302 -8.7; 332 -8.5; 365 -8.3; 402 -8.1; 442 -7.7; 486 -7.6; 535 -7.3; 588 -6.7; 647 -6.5; 712 -6.3; 783 -6.0; 861 -6.1; 947 -6.3; 1042 -6.5; 1146 -6.7; 1261 -6.9; 1387 -7.3; 1526 -8.1; 1678 -8.5; 1846 -8.5; 2031 -8.3; 2234 -7.8; 2457 -6.5; 2703 -4.6; 2973 -2.2; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -3.5; 4788 -6.0; 5267 -7.4; 5793 -6.1; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR07 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.32 | 2.4 dB  |
| Peaking | 151 Hz   | 0.55 | -3.3 dB |
| Peaking | 1987 Hz  | 2.07 | -3.1 dB |
| Peaking | 3447 Hz  | 2.23 | 7.1 dB  |
| Peaking | 21795 Hz | 2.24 | 1.2 dB  |
| Peaking | 813 Hz   | 2.47 | 0.9 dB  |
| Peaking | 1564 Hz  | 5.17 | -0.4 dB |
| Peaking | 4066 Hz  | 6.39 | 2.2 dB  |
| Peaking | 5528 Hz  | 1.97 | -3.5 dB |
| Peaking | 6474 Hz  | 4.87 | 6.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR07%20Classic/VSonic%20GR07%20Classic.png)