# AKG K812
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.4; 25 -2.7; 28 -3.0; 31 -3.3; 34 -3.5; 37 -3.6; 41 -3.8; 45 -4.0; 49 -4.1; 54 -4.3; 60 -4.5; 66 -4.7; 72 -4.9; 79 -5.1; 87 -5.6; 96 -6.0; 106 -6.3; 116 -6.5; 128 -7.0; 141 -7.1; 155 -7.3; 170 -7.2; 187 -7.3; 206 -7.4; 227 -7.3; 249 -7.2; 274 -7.1; 302 -7.0; 332 -6.9; 365 -6.7; 402 -6.5; 442 -6.1; 486 -6.0; 535 -5.7; 588 -5.1; 647 -4.8; 712 -4.5; 783 -3.8; 861 -3.5; 947 -3.2; 1042 -2.7; 1146 -2.4; 1261 -2.2; 1387 -2.6; 1526 -3.2; 1678 -3.1; 1846 -2.1; 2031 -2.0; 2234 -2.4; 2457 -0.5; 2703 -0.6; 2973 -4.3; 3270 -5.4; 3597 -5.4; 3957 -3.2; 4353 -0.8; 4788 -3.0; 5267 -7.4; 5793 -11.1; 6373 -8.6; 7010 -3.7; 7711 -4.9; 8482 -6.5; 9330 -6.1; 10263 -3.5; 11289 -2.9; 12418 -2.9; 13660 -2.9; 15026 -2.9; 16529 -3.2; 18182 -5.0; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K812 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 219 Hz   | 0.39 | -4.6 dB |
| Peaking | 1542 Hz  | 1.29 | 3.2 dB  |
| Peaking | 1576 Hz  | 3.52 | -3.2 dB |
| Peaking | 5935 Hz  | 4.84 | -9.2 dB |
| Peaking | 19780 Hz | 1.3  | -7.3 dB |
| Peaking | 20 Hz    | 1.62 | 1.2 dB  |
| Peaking | 2610 Hz  | 7.5  | 4.1 dB  |
| Peaking | 3356 Hz  | 2.54 | -3.4 dB |
| Peaking | 4385 Hz  | 5.9  | 4.2 dB  |
| Peaking | 8879 Hz  | 5.62 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K812/AKG%20K812.png)