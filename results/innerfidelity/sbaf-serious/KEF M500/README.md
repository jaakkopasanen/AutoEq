# KEF M500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.6; 28 -8.6; 31 -8.6; 34 -8.6; 37 -8.6; 41 -8.6; 45 -8.6; 49 -8.6; 54 -8.5; 60 -8.8; 66 -9.0; 72 -9.1; 79 -9.3; 87 -9.3; 96 -9.3; 106 -9.6; 116 -10.1; 128 -10.7; 141 -11.1; 155 -10.9; 170 -10.8; 187 -10.8; 206 -10.5; 227 -10.7; 249 -9.8; 274 -9.0; 302 -8.1; 332 -7.3; 365 -6.7; 402 -6.4; 442 -6.7; 486 -7.7; 535 -8.2; 588 -8.0; 647 -7.9; 712 -7.6; 783 -7.2; 861 -6.6; 947 -5.8; 1042 -5.1; 1146 -4.5; 1261 -4.4; 1387 -4.5; 1526 -4.7; 1678 -4.7; 1846 -4.7; 2031 -4.9; 2234 -5.5; 2457 -5.8; 2703 -6.6; 2973 -7.2; 3270 -7.8; 3597 -7.0; 3957 -5.2; 4353 -3.8; 4788 -2.2; 5267 -1.1; 5793 -0.5; 6373 -1.7; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KEF M500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KEF M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.27 | -2.1 dB |
| Peaking | 169 Hz  | 1.08 | -4.0 dB |
| Peaking | 652 Hz  | 2.63 | -1.7 dB |
| Peaking | 1334 Hz | 1.52 | 2.4 dB  |
| Peaking | 5634 Hz | 2.89 | 6.6 dB  |
| Peaking | 238 Hz  | 6.67 | -1.0 dB |
| Peaking | 382 Hz  | 4.5  | 1.2 dB  |
| Peaking | 3224 Hz | 2.67 | -4.1 dB |
| Peaking | 3562 Hz | 1.14 | 2.1 dB  |
| Peaking | 8423 Hz | 3.15 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KEF%20M500/KEF%20M500.png)