# Jomo Trinity Brass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.0; 25 -8.1; 28 -8.3; 31 -8.4; 34 -8.5; 37 -8.6; 41 -8.7; 45 -8.7; 49 -8.8; 54 -8.8; 60 -8.9; 66 -9.0; 72 -9.1; 79 -9.2; 87 -9.2; 96 -9.3; 106 -9.4; 116 -9.4; 128 -9.3; 141 -9.2; 155 -8.9; 170 -8.6; 187 -8.3; 206 -7.9; 227 -7.5; 249 -7.0; 274 -6.5; 302 -5.9; 332 -5.4; 365 -4.8; 402 -4.3; 442 -3.8; 486 -3.3; 535 -2.8; 588 -2.3; 647 -1.9; 712 -1.4; 783 -1.0; 861 -0.7; 947 -0.8; 1042 -1.3; 1146 -2.1; 1261 -3.0; 1387 -3.7; 1526 -3.8; 1678 -3.5; 1846 -2.9; 2031 -2.2; 2234 -2.2; 2457 -2.1; 2703 -1.9; 2973 -2.0; 3270 -2.4; 3597 -3.3; 3957 -4.2; 4353 -4.1; 4788 -2.5; 5267 -0.8; 5793 -0.5; 6373 -1.3; 7010 -3.1; 7711 -4.3; 8482 -4.0; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -7.1; 18182 -10.3; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Trinity Brass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Trinity Brass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.35 | -4.5 dB |
| Peaking | 137 Hz   | 0.87 | -4.0 dB |
| Peaking | 259 Hz   | 1.44 | -2.2 dB |
| Peaking | 920 Hz   | 0.11 | 2.1 dB  |
| Peaking | 18559 Hz | 1.28 | -6.9 dB |
| Peaking | 890 Hz   | 2.19 | 2.0 dB  |
| Peaking | 1481 Hz  | 2.23 | -2.3 dB |
| Peaking | 4240 Hz  | 2.28 | -5.4 dB |
| Peaking | 5673 Hz  | 1.01 | 6.1 dB  |
| Peaking | 7566 Hz  | 1.59 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Trinity%20Brass/Jomo%20Trinity%20Brass.png)