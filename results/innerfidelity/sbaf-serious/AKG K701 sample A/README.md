# AKG K701 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.0; 41 -1.5; 45 -2.0; 49 -2.3; 54 -2.8; 60 -3.3; 66 -3.4; 72 -3.2; 79 -3.3; 87 -3.8; 96 -4.8; 106 -5.6; 116 -6.2; 128 -6.7; 141 -7.1; 155 -7.3; 170 -7.4; 187 -7.7; 206 -7.9; 227 -7.9; 249 -8.0; 274 -7.9; 302 -7.9; 332 -7.7; 365 -7.7; 402 -7.5; 442 -7.1; 486 -6.7; 535 -6.7; 588 -5.9; 647 -5.3; 712 -4.8; 783 -4.4; 861 -4.9; 947 -5.1; 1042 -5.5; 1146 -5.3; 1261 -4.9; 1387 -5.0; 1526 -5.4; 1678 -6.2; 1846 -7.0; 2031 -7.9; 2234 -7.7; 2457 -7.4; 2703 -6.2; 2973 -4.2; 3270 -2.7; 3597 -3.3; 3957 -4.6; 4353 -6.2; 4788 -6.5; 5267 -6.7; 5793 -9.0; 6373 -9.5; 7010 -7.3; 7711 -7.3; 8482 -7.4; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.72 | 6.4 dB  |
| Peaking | 784 Hz   | 3.95 | 2.2 dB  |
| Peaking | 1275 Hz  | 4.33 | 1.7 dB  |
| Peaking | 3410 Hz  | 4.54 | 4.3 dB  |
| Peaking | 6183 Hz  | 4.86 | -3.6 dB |
| Peaking | 30 Hz    | 2.24 | -0.3 dB |
| Peaking | 80 Hz    | 2.81 | 1.9 dB  |
| Peaking | 220 Hz   | 0.89 | -1.9 dB |
| Peaking | 2165 Hz  | 4.56 | -1.9 dB |
| Peaking | 20366 Hz | 1.92 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K701%20sample%20A/AKG%20K701%20sample%20A.png)