# Skullcandy Grind
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -5.0; 25 -5.4; 28 -6.0; 31 -6.4; 34 -6.7; 37 -6.8; 41 -7.0; 45 -7.0; 49 -7.1; 54 -7.1; 60 -7.0; 66 -6.9; 72 -6.8; 79 -6.8; 87 -6.7; 96 -6.6; 106 -6.5; 116 -6.3; 128 -6.2; 141 -6.5; 155 -6.8; 170 -6.4; 187 -6.5; 206 -6.5; 227 -6.2; 249 -5.9; 274 -5.4; 302 -5.1; 332 -5.2; 365 -4.9; 402 -4.4; 442 -3.4; 486 -3.2; 535 -2.7; 588 -1.7; 647 -1.0; 712 -0.5; 783 -0.7; 861 -3.5; 947 -5.6; 1042 -4.5; 1146 -3.4; 1261 -3.6; 1387 -5.5; 1526 -6.7; 1678 -7.8; 1846 -9.3; 2031 -10.0; 2234 -9.3; 2457 -8.5; 2703 -6.7; 2973 -4.6; 3270 -3.1; 3597 -1.9; 3957 -7.1; 4353 -7.7; 4788 -6.7; 5267 -3.4; 5793 -1.4; 6373 -2.3; 7010 -4.2; 7711 -6.6; 8482 -9.2; 9330 -8.9; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Grind GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Grind ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 683 Hz  | 2.08 | 5.1 dB  |
| Peaking | 2065 Hz | 2.46 | -5.2 dB |
| Peaking | 3413 Hz | 8.74 | 4.6 dB  |
| Peaking | 6061 Hz | 5.11 | 4.6 dB  |
| Peaking | 8758 Hz | 4.65 | -4.9 dB |
| Peaking | 17 Hz   | 1.37 | 2.5 dB  |
| Peaking | 45 Hz   | 0.54 | -2.0 dB |
| Peaking | 182 Hz  | 1.88 | -1.1 dB |
| Peaking | 4329 Hz | 1.61 | 2.5 dB  |
| Peaking | 4349 Hz | 3.9  | -5.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Grind/Skullcandy%20Grind.png)