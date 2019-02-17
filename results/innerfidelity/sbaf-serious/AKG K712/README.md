# AKG K712
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.3; 31 -2.8; 34 -3.3; 37 -3.7; 41 -4.2; 45 -4.6; 49 -4.9; 54 -5.3; 60 -5.7; 66 -6.1; 72 -6.4; 79 -6.9; 87 -7.3; 96 -7.8; 106 -8.1; 116 -8.2; 128 -8.5; 141 -8.5; 155 -8.8; 170 -9.0; 187 -8.6; 206 -8.7; 227 -8.9; 249 -9.0; 274 -8.9; 302 -8.7; 332 -8.4; 365 -8.1; 402 -7.9; 442 -7.7; 486 -7.4; 535 -6.8; 588 -6.2; 647 -6.0; 712 -5.9; 783 -5.7; 861 -5.8; 947 -5.6; 1042 -5.7; 1146 -5.3; 1261 -5.2; 1387 -6.1; 1526 -7.3; 1678 -8.5; 1846 -10.0; 2031 -10.5; 2234 -9.9; 2457 -7.8; 2703 -4.6; 2973 -2.9; 3270 -2.9; 3597 -4.2; 3957 -6.6; 4353 -8.6; 4788 -7.7; 5267 -5.6; 5793 -5.7; 6373 -7.5; 7010 -9.3; 7711 -10.4; 8482 -11.3; 9330 -8.7; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -6.8; 18182 -11.7; 20000 -8.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.69 | 5.8 dB  |
| Peaking | 186 Hz   | 0.56 | -3.6 dB |
| Peaking | 1990 Hz  | 4.15 | -5.5 dB |
| Peaking | 8079 Hz  | 3.18 | -6.0 dB |
| Peaking | 18731 Hz | 1.62 | -7.1 dB |
| Peaking | 997 Hz   | 2.14 | 0.7 dB  |
| Peaking | 2352 Hz  | 5.11 | -2.8 dB |
| Peaking | 3090 Hz  | 2.59 | 4.1 dB  |
| Peaking | 4342 Hz  | 5.29 | -3.8 dB |
| Peaking | 13185 Hz | 1.26 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K712/AKG%20K712.png)