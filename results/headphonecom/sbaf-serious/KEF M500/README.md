# KEF M500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.4; 25 -11.4; 28 -11.4; 31 -11.4; 34 -11.4; 37 -11.3; 41 -11.2; 45 -11.3; 49 -11.4; 54 -11.3; 60 -11.4; 66 -11.5; 72 -11.7; 79 -11.9; 87 -11.9; 96 -11.7; 106 -12.1; 116 -12.1; 128 -12.9; 141 -13.4; 155 -13.6; 170 -13.6; 187 -13.5; 206 -13.4; 227 -13.6; 249 -13.2; 274 -12.5; 302 -11.3; 332 -9.8; 365 -8.7; 402 -8.6; 442 -8.6; 486 -9.0; 535 -9.6; 588 -9.7; 647 -9.5; 712 -9.0; 783 -8.3; 861 -7.5; 947 -6.8; 1042 -6.1; 1146 -5.4; 1261 -5.1; 1387 -5.4; 1526 -5.3; 1678 -5.3; 1846 -5.0; 2031 -5.1; 2234 -5.0; 2457 -5.2; 2703 -5.5; 2973 -5.7; 3270 -6.2; 3597 -5.6; 3957 -4.6; 4353 -2.5; 4788 -1.3; 5267 -1.3; 5793 -0.5; 6373 -1.6; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KEF M500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KEF M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.18 | -4.8 dB |
| Peaking | 200 Hz  | 0.98 | -5.3 dB |
| Peaking | 651 Hz  | 2.23 | -2.7 dB |
| Peaking | 1455 Hz | 1.02 | 1.6 dB  |
| Peaking | 5453 Hz | 2.29 | 6.4 dB  |
| Peaking | 273 Hz  | 4.85 | -1.0 dB |
| Peaking | 367 Hz  | 4.74 | 1.1 dB  |
| Peaking | 3365 Hz | 8.66 | -1.0 dB |
| Peaking | 6636 Hz | 6.16 | 2.2 dB  |
| Peaking | 7777 Hz | 2.46 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/KEF%20M500/KEF%20M500.png)