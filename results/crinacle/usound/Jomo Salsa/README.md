# Jomo Salsa
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.3; 25 -3.5; 28 -3.9; 31 -4.1; 34 -4.3; 37 -4.5; 41 -4.8; 45 -5.0; 49 -5.2; 54 -5.4; 60 -5.7; 66 -6.1; 72 -6.5; 79 -6.9; 87 -7.3; 96 -7.8; 106 -8.1; 116 -8.5; 128 -8.9; 141 -9.1; 155 -9.4; 170 -9.5; 187 -9.6; 206 -9.6; 227 -9.6; 249 -9.5; 274 -9.3; 302 -9.1; 332 -9.0; 365 -8.8; 402 -8.5; 442 -8.1; 486 -7.6; 535 -7.1; 588 -6.6; 647 -6.0; 712 -5.3; 783 -4.6; 861 -4.2; 947 -4.4; 1042 -5.5; 1146 -7.4; 1261 -9.1; 1387 -9.7; 1526 -9.4; 1678 -8.5; 1846 -7.2; 2031 -5.8; 2234 -4.3; 2457 -2.8; 2703 -1.7; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.0; 4788 -3.8; 5267 -2.4; 5793 -3.3; 6373 -7.8; 7010 -11.4; 7711 -10.8; 8482 -8.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Salsa GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Salsa ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.63 | 3.5 dB  |
| Peaking | 1510 Hz | 2.88 | -4.7 dB |
| Peaking | 3393 Hz | 1.21 | 6.6 dB  |
| Peaking | 5666 Hz | 5.23 | 3.6 dB  |
| Peaking | 7138 Hz | 3.17 | -7.0 dB |
| Peaking | 56 Hz   | 0.78 | 2.2 dB  |
| Peaking | 198 Hz  | 0.36 | -3.5 dB |
| Peaking | 951 Hz  | 1.13 | 4.1 dB  |
| Peaking | 1213 Hz | 3.35 | -3.5 dB |
| Peaking | 1929 Hz | 4.6  | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Salsa/Jomo%20Salsa.png)