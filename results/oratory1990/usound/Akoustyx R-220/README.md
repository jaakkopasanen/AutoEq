# Akoustyx R-220
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -0.9; 72 -1.3; 79 -1.7; 87 -2.1; 96 -2.5; 106 -3.0; 116 -3.5; 128 -3.7; 141 -4.0; 155 -4.5; 170 -4.9; 187 -5.0; 206 -5.7; 227 -6.4; 249 -6.5; 274 -6.3; 302 -6.2; 332 -6.2; 365 -6.3; 402 -6.3; 442 -6.2; 486 -6.1; 535 -6.0; 588 -6.0; 647 -5.9; 712 -5.8; 783 -5.6; 861 -5.6; 947 -5.9; 1042 -6.5; 1146 -7.3; 1261 -7.8; 1387 -8.1; 1526 -7.9; 1678 -7.6; 1846 -7.2; 2031 -7.0; 2234 -7.2; 2457 -7.8; 2703 -8.5; 2973 -8.7; 3270 -8.0; 3597 -7.0; 3957 -5.8; 4353 -4.8; 4788 -4.2; 5267 -4.2; 5793 -5.0; 6373 -6.5; 7010 -8.9; 7711 -11.1; 8482 -12.0; 9330 -10.6; 10263 -7.6; 11289 -6.5; 12418 -6.6; 13660 -6.7; 15026 -6.5; 16529 -6.5; 18182 -7.8; 20000 -11.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Akoustyx R-220 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Akoustyx R-220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.4  | 6.5 dB  |
| Peaking | 1417 Hz  | 3.7  | -1.7 dB |
| Peaking | 2985 Hz  | 2.38 | -2.8 dB |
| Peaking | 5072 Hz  | 1.64 | 3.4 dB  |
| Peaking | 8217 Hz  | 2.58 | -6.6 dB |
| Peaking | 243 Hz   | 3.64 | -1.1 dB |
| Peaking | 809 Hz   | 3.13 | 1.1 dB  |
| Peaking | 11035 Hz | 6.54 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Akoustyx%20R-220/Akoustyx%20R-220.png)