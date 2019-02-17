# AKG K501
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.0; 66 -1.8; 72 -1.9; 79 -2.1; 87 -2.9; 96 -4.0; 106 -4.5; 116 -4.8; 128 -5.2; 141 -5.4; 155 -5.7; 170 -5.6; 187 -5.8; 206 -5.8; 227 -5.9; 249 -6.0; 274 -6.0; 302 -5.8; 332 -5.7; 365 -5.7; 402 -5.7; 442 -5.6; 486 -5.7; 535 -5.6; 588 -5.4; 647 -5.4; 712 -5.2; 783 -4.5; 861 -5.6; 947 -6.2; 1042 -6.8; 1146 -7.3; 1261 -8.0; 1387 -8.7; 1526 -9.1; 1678 -9.6; 1846 -9.4; 2031 -8.2; 2234 -8.6; 2457 -7.9; 2703 -8.0; 2973 -8.2; 3270 -8.7; 3597 -8.7; 3957 -7.9; 4353 -7.6; 4788 -6.7; 5267 -5.1; 5793 -6.7; 6373 -11.1; 7010 -7.9; 7711 -8.1; 8482 -10.3; 9330 -9.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K501 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K501 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.51 | 6.6 dB  |
| Peaking | 747 Hz   | 1.3  | 1.9 dB  |
| Peaking | 1629 Hz  | 1.36 | -3.2 dB |
| Peaking | 3445 Hz  | 3.2  | -1.8 dB |
| Peaking | 8487 Hz  | 3.39 | -3.7 dB |
| Peaking | 38 Hz    | 3.02 | -0.6 dB |
| Peaking | 79 Hz    | 5.19 | 0.9 dB  |
| Peaking | 5453 Hz  | 6.29 | 2.9 dB  |
| Peaking | 6243 Hz  | 9.41 | -5.1 dB |
| Peaking | 10273 Hz | 5.69 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K501/AKG%20K501.png)