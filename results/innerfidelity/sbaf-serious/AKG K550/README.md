# AKG K550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.4; 25 -5.5; 28 -5.7; 31 -5.8; 34 -5.9; 37 -5.9; 41 -5.7; 45 -5.5; 49 -5.3; 54 -5.2; 60 -5.0; 66 -4.4; 72 -3.7; 79 -3.5; 87 -3.8; 96 -5.1; 106 -6.2; 116 -6.9; 128 -7.1; 141 -6.9; 155 -6.0; 170 -4.8; 187 -6.1; 206 -5.7; 227 -5.5; 249 -5.5; 274 -5.3; 302 -5.1; 332 -5.2; 365 -4.9; 402 -4.7; 442 -4.3; 486 -4.2; 535 -3.8; 588 -3.3; 647 -3.1; 712 -3.0; 783 -2.7; 861 -3.4; 947 -4.0; 1042 -4.6; 1146 -5.2; 1261 -5.8; 1387 -6.1; 1526 -6.2; 1678 -5.9; 1846 -5.2; 2031 -4.5; 2234 -4.4; 2457 -4.0; 2703 -3.7; 2973 -2.6; 3270 -1.6; 3597 -0.7; 3957 -0.5; 4353 -0.8; 4788 -0.9; 5267 -3.8; 5793 -5.1; 6373 -4.4; 7010 -2.6; 7711 -5.3; 8482 -10.2; 9330 -10.8; 10263 -5.6; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 131 Hz  | 2.55 | -2.6 dB |
| Peaking | 738 Hz  | 2.14 | 2.2 dB  |
| Peaking | 1460 Hz | 1.88 | -2.0 dB |
| Peaking | 3924 Hz | 1.81 | 4.6 dB  |
| Peaking | 8955 Hz | 5.14 | -7.9 dB |
| Peaking | 34 Hz   | 0.98 | -1.2 dB |
| Peaking | 78 Hz   | 3.78 | 2.0 dB  |
| Peaking | 248 Hz  | 2.08 | -0.7 dB |
| Peaking | 5766 Hz | 7.44 | -1.9 dB |
| Peaking | 7037 Hz | 8.88 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K550/AKG%20K550.png)