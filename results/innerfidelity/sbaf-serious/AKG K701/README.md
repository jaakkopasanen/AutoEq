# AKG K701
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.0; 34 -1.5; 37 -2.0; 41 -2.5; 45 -2.9; 49 -3.3; 54 -3.8; 60 -4.1; 66 -3.8; 72 -3.9; 79 -4.6; 87 -4.9; 96 -6.0; 106 -6.7; 116 -7.1; 128 -7.6; 141 -8.0; 155 -8.1; 170 -8.2; 187 -8.5; 206 -8.6; 227 -8.5; 249 -8.6; 274 -8.6; 302 -8.5; 332 -8.2; 365 -8.1; 402 -7.9; 442 -7.4; 486 -7.1; 535 -6.9; 588 -6.3; 647 -5.8; 712 -5.2; 783 -4.8; 861 -5.5; 947 -6.1; 1042 -6.6; 1146 -6.7; 1261 -6.5; 1387 -6.7; 1526 -6.9; 1678 -7.7; 1846 -8.5; 2031 -9.3; 2234 -9.1; 2457 -8.8; 2703 -8.0; 2973 -6.3; 3270 -4.7; 3597 -5.2; 3957 -6.2; 4353 -7.8; 4788 -8.0; 5267 -7.7; 5793 -9.7; 6373 -10.9; 7010 -9.2; 7711 -9.3; 8482 -9.7; 9330 -9.0; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.0; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.69 | 6.2 dB  |
| Peaking | 73 Hz    | 2.79 | 1.5 dB  |
| Peaking | 201 Hz   | 0.89 | -2.5 dB |
| Peaking | 2115 Hz  | 3.93 | -3.1 dB |
| Peaking | 6971 Hz  | 1.75 | -3.8 dB |
| Peaking | 761 Hz   | 3.76 | 2.1 dB  |
| Peaking | 2658 Hz  | 3.33 | -1.3 dB |
| Peaking | 3348 Hz  | 4.08 | 3.0 dB  |
| Peaking | 10055 Hz | 1.2  | -1.1 dB |
| Peaking | 11068 Hz | 2.37 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K701/AKG%20K701.png)