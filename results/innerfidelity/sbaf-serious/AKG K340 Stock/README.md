# AKG K340 Stock
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.9; 66 -2.2; 72 -3.1; 79 -4.1; 87 -5.2; 96 -6.2; 106 -6.9; 116 -7.5; 128 -8.2; 141 -8.7; 155 -9.1; 170 -9.2; 187 -9.6; 206 -9.8; 227 -9.9; 249 -10.0; 274 -9.9; 302 -9.8; 332 -9.6; 365 -9.2; 402 -9.0; 442 -8.3; 486 -7.7; 535 -6.4; 588 -5.5; 647 -5.2; 712 -5.0; 783 -4.2; 861 -5.2; 947 -6.1; 1042 -6.7; 1146 -3.7; 1261 -1.2; 1387 -5.0; 1526 -7.5; 1678 -7.9; 1846 -7.7; 2031 -7.4; 2234 -10.5; 2457 -11.3; 2703 -9.4; 2973 -6.6; 3270 -5.0; 3597 -4.1; 3957 -4.9; 4353 -3.5; 4788 -4.3; 5267 -3.8; 5793 -5.2; 6373 -6.9; 7010 -4.3; 7711 -7.4; 8482 -13.3; 9330 -14.4; 10263 -10.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.9; 20000 -12.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K340 Stock GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K340 Stock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 46 Hz   | 0.41 | 9.0 dB   |
| Peaking | 176 Hz  | 0.34 | -6.8 dB  |
| Peaking | 1999 Hz | 0.22 | 4.9 dB   |
| Peaking | 2313 Hz | 1.66 | -8.7 dB  |
| Peaking | 9043 Hz | 3.38 | -11.0 dB |
| Peaking | 701 Hz  | 2.55 | 1.2 dB   |
| Peaking | 1080 Hz | 3.95 | -4.3 dB  |
| Peaking | 1211 Hz | 6.84 | 6.6 dB   |
| Peaking | 1538 Hz | 6.55 | -2.6 dB  |
| Peaking | 3371 Hz | 8.27 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K340%20Stock/AKG%20K340%20Stock.png)