# Westone W20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.0; 25 -6.0; 28 -6.2; 31 -6.3; 34 -6.4; 37 -6.5; 41 -6.7; 45 -6.9; 49 -7.0; 54 -7.2; 60 -7.5; 66 -7.8; 72 -8.1; 79 -8.5; 87 -8.9; 96 -9.4; 106 -9.8; 116 -10.2; 128 -10.5; 141 -10.8; 155 -11.1; 170 -11.2; 187 -11.4; 206 -11.4; 227 -11.4; 249 -11.4; 274 -11.3; 302 -11.2; 332 -11.0; 365 -10.8; 402 -10.5; 442 -10.3; 486 -9.9; 535 -9.5; 588 -9.1; 647 -8.6; 712 -8.0; 783 -7.4; 861 -6.8; 947 -6.5; 1042 -6.6; 1146 -7.1; 1261 -7.7; 1387 -8.1; 1526 -8.0; 1678 -7.6; 1846 -7.2; 2031 -7.0; 2234 -6.7; 2457 -5.7; 2703 -3.8; 2973 -1.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.1; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -9.1; 20000 -17.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.38 | 0.8 dB  |
| Peaking | 182 Hz   | 0.58 | -4.7 dB |
| Peaking | 413 Hz   | 1.24 | -2.0 dB |
| Peaking | 1921 Hz  | 1.45 | -3.0 dB |
| Peaking | 3994 Hz  | 0.99 | 7.3 dB  |
| Peaking | 934 Hz   | 4.27 | 0.9 dB  |
| Peaking | 3073 Hz  | 5.09 | 0.8 dB  |
| Peaking | 6363 Hz  | 3.94 | 3.4 dB  |
| Peaking | 7668 Hz  | 3.22 | -2.3 dB |
| Peaking | 20730 Hz | 0.06 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Westone%20W20/Westone%20W20.png)