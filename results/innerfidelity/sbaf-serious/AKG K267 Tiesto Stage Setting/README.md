# AKG K267 Tiesto Stage Setting
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.2; 25 -9.3; 28 -9.4; 31 -9.5; 34 -9.5; 37 -9.4; 41 -9.3; 45 -9.1; 49 -8.9; 54 -8.7; 60 -8.6; 66 -8.4; 72 -8.2; 79 -7.8; 87 -7.9; 96 -8.6; 106 -9.3; 116 -9.7; 128 -10.0; 141 -10.1; 155 -9.8; 170 -9.2; 187 -9.6; 206 -9.2; 227 -9.1; 249 -8.7; 274 -7.9; 302 -6.5; 332 -4.7; 365 -3.7; 402 -4.4; 442 -5.1; 486 -5.9; 535 -6.0; 588 -6.0; 647 -6.2; 712 -6.4; 783 -6.1; 861 -6.3; 947 -6.5; 1042 -6.7; 1146 -6.8; 1261 -7.6; 1387 -9.5; 1526 -10.6; 1678 -10.0; 1846 -8.8; 2031 -7.9; 2234 -7.0; 2457 -5.3; 2703 -5.2; 2973 -4.4; 3270 -4.1; 3597 -3.4; 3957 -1.4; 4353 -0.5; 4788 -0.5; 5267 -4.0; 5793 -0.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -7.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K267 Tiesto Stage Setting GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K267 Tiesto Stage Setting ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.7  | -3.0 dB |
| Peaking | 147 Hz  | 1.47 | -3.6 dB |
| Peaking | 1581 Hz | 3.4  | -4.6 dB |
| Peaking | 4282 Hz | 2.25 | 6.0 dB  |
| Peaking | 6200 Hz | 5.58 | 5.0 dB  |
| Peaking | 256 Hz  | 2.42 | -2.4 dB |
| Peaking | 358 Hz  | 2.13 | 3.6 dB  |
| Peaking | 2151 Hz | 3.96 | -1.3 dB |
| Peaking | 2502 Hz | 3.69 | 1.4 dB  |
| Peaking | 9143 Hz | 5.2  | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K267%20Tiesto%20Stage%20Setting/AKG%20K267%20Tiesto%20Stage%20Setting.png)