# AKG K267 Tiesto Club Setting
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.6; 25 -6.6; 28 -6.6; 31 -6.5; 34 -6.4; 37 -6.3; 41 -6.1; 45 -5.9; 49 -5.7; 54 -5.5; 60 -5.4; 66 -5.2; 72 -5.0; 79 -5.0; 87 -5.9; 96 -6.9; 106 -7.1; 116 -7.7; 128 -8.4; 141 -8.4; 155 -8.2; 170 -7.7; 187 -8.1; 206 -8.2; 227 -7.9; 249 -7.5; 274 -6.8; 302 -5.5; 332 -4.5; 365 -5.0; 402 -6.1; 442 -6.8; 486 -7.4; 535 -7.4; 588 -7.3; 647 -7.4; 712 -7.5; 783 -7.3; 861 -7.6; 947 -7.9; 1042 -8.3; 1146 -8.8; 1261 -9.9; 1387 -11.6; 1526 -11.5; 1678 -10.4; 1846 -9.0; 2031 -8.1; 2234 -7.4; 2457 -6.0; 2703 -5.9; 2973 -5.2; 3270 -4.9; 3597 -4.1; 3957 -2.0; 4353 -0.5; 4788 -0.5; 5267 -4.2; 5793 -1.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.1; 9330 -9.7; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K267 Tiesto Club Setting GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K267 Tiesto Club Setting ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 155 Hz  | 2.05 | -2.0 dB |
| Peaking | 1461 Hz | 2.11 | -5.4 dB |
| Peaking | 4345 Hz | 2.6  | 6.0 dB  |
| Peaking | 6274 Hz | 4.49 | 5.1 dB  |
| Peaking | 9103 Hz | 4.83 | -4.0 dB |
| Peaking | 68 Hz   | 2.33 | 1.8 dB  |
| Peaking | 242 Hz  | 2.5  | -1.2 dB |
| Peaking | 341 Hz  | 2.57 | 3.5 dB  |
| Peaking | 435 Hz  | 1.03 | -1.3 dB |
| Peaking | 1200 Hz | 3.73 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K267%20Tiesto%20Club%20Setting/AKG%20K267%20Tiesto%20Club%20Setting.png)