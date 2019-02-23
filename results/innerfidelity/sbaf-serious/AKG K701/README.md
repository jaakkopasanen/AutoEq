# AKG K701
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.9; 41 -1.4; 45 -1.8; 49 -2.2; 54 -2.7; 60 -3.0; 66 -2.7; 72 -2.8; 79 -3.5; 87 -3.8; 96 -4.9; 106 -5.6; 116 -6.0; 128 -6.5; 141 -6.9; 155 -7.0; 170 -7.1; 187 -7.4; 206 -7.5; 227 -7.4; 249 -7.5; 274 -7.5; 302 -7.4; 332 -7.1; 365 -7.0; 402 -6.8; 442 -6.3; 486 -6.0; 535 -5.8; 588 -5.2; 647 -4.7; 712 -4.1; 783 -3.7; 861 -4.4; 947 -5.0; 1042 -5.5; 1146 -5.6; 1261 -5.4; 1387 -5.6; 1526 -5.8; 1678 -6.6; 1846 -7.4; 2031 -8.2; 2234 -8.0; 2457 -7.7; 2703 -6.9; 2973 -5.2; 3270 -3.6; 3597 -4.1; 3957 -5.1; 4353 -6.7; 4788 -6.9; 5267 -6.6; 5793 -8.6; 6373 -9.8; 7010 -8.1; 7711 -8.2; 8482 -8.6; 9330 -7.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.67 | 6.4 dB  |
| Peaking | 785 Hz   | 2.25 | 2.8 dB  |
| Peaking | 2241 Hz  | 3.12 | -2.3 dB |
| Peaking | 3412 Hz  | 3.15 | 3.5 dB  |
| Peaking | 6698 Hz  | 1.72 | -2.7 dB |
| Peaking | 38 Hz    | 1.5  | -0.4 dB |
| Peaking | 75 Hz    | 2.33 | 1.7 dB  |
| Peaking | 197 Hz   | 0.89 | -1.5 dB |
| Peaking | 1346 Hz  | 4.11 | 0.9 dB  |
| Peaking | 11016 Hz | 5.42 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K701/AKG%20K701.png)