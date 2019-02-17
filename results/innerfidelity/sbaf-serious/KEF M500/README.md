# KEF M500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.5; 25 -9.5; 28 -9.5; 31 -9.5; 34 -9.5; 37 -9.5; 41 -9.5; 45 -9.5; 49 -9.4; 54 -9.4; 60 -9.7; 66 -9.8; 72 -10.0; 79 -10.1; 87 -10.2; 96 -10.2; 106 -10.5; 116 -10.9; 128 -11.6; 141 -12.0; 155 -11.8; 170 -11.7; 187 -11.6; 206 -11.4; 227 -11.6; 249 -10.7; 274 -9.9; 302 -9.0; 332 -8.1; 365 -7.6; 402 -7.3; 442 -7.6; 486 -8.6; 535 -9.1; 588 -8.8; 647 -8.8; 712 -8.5; 783 -8.1; 861 -7.5; 947 -6.6; 1042 -6.0; 1146 -5.4; 1261 -5.3; 1387 -5.4; 1526 -5.6; 1678 -5.6; 1846 -5.5; 2031 -5.7; 2234 -6.3; 2457 -6.7; 2703 -7.5; 2973 -8.1; 3270 -8.6; 3597 -7.9; 3957 -6.1; 4353 -4.7; 4788 -3.1; 5267 -2.0; 5793 -0.5; 6373 -2.6; 7010 -4.1; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KEF M500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KEF M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.23 | -2.9 dB |
| Peaking | 175 Hz  | 0.98 | -4.5 dB |
| Peaking | 613 Hz  | 3.01 | -2.3 dB |
| Peaking | 3271 Hz | 4.17 | -3.0 dB |
| Peaking | 5615 Hz | 2.71 | 6.0 dB  |
| Peaking | 241 Hz  | 6.81 | -0.9 dB |
| Peaking | 382 Hz  | 4.76 | 0.9 dB  |
| Peaking | 805 Hz  | 2.71 | -1.1 dB |
| Peaking | 1269 Hz | 1.51 | 1.5 dB  |
| Peaking | 8294 Hz | 4.11 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KEF%20M500/KEF%20M500.png)