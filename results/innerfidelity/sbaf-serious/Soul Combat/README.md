# Soul Combat
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.2; 28 -2.5; 31 -3.8; 34 -4.9; 37 -5.8; 41 -6.7; 45 -7.3; 49 -7.8; 54 -8.2; 60 -8.6; 66 -9.0; 72 -9.2; 79 -9.6; 87 -9.9; 96 -10.2; 106 -10.4; 116 -10.7; 128 -11.1; 141 -11.5; 155 -12.0; 170 -12.1; 187 -12.3; 206 -12.7; 227 -13.1; 249 -13.6; 274 -14.1; 302 -14.6; 332 -14.9; 365 -15.2; 402 -15.6; 442 -16.3; 486 -16.4; 535 -15.4; 588 -12.8; 647 -9.8; 712 -6.6; 783 -3.6; 861 -2.0; 947 -2.6; 1042 -4.6; 1146 -6.5; 1261 -6.9; 1387 -5.9; 1526 -5.3; 1678 -6.5; 1846 -7.6; 2031 -6.3; 2234 -3.8; 2457 -0.9; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -7.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul Combat GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul Combat ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.53 | 6.7 dB  |
| Peaking | 421 Hz  | 0.18 | -6.0 dB |
| Peaking | 501 Hz  | 1.14 | -6.9 dB |
| Peaking | 833 Hz  | 1.7  | 12.1 dB |
| Peaking | 3563 Hz | 0.83 | 8.5 dB  |
| Peaking | 1977 Hz | 3.9  | -4.4 dB |
| Peaking | 2396 Hz | 1.36 | 3.6 dB  |
| Peaking | 3440 Hz | 1.98 | -2.5 dB |
| Peaking | 6165 Hz | 2.42 | 4.6 dB  |
| Peaking | 7907 Hz | 1.17 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.8 dB |
| Peaking | 500 Hz   | 1.41 | -9.1 dB |
| Peaking | 1000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20Combat/Soul%20Combat.png)