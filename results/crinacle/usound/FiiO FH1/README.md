# FiiO FH1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -9.9; 25 -10.0; 28 -10.0; 31 -10.1; 34 -10.1; 37 -10.2; 41 -10.2; 45 -10.3; 49 -10.3; 54 -10.4; 60 -10.5; 66 -10.7; 72 -10.8; 79 -10.9; 87 -11.1; 96 -11.2; 106 -11.4; 116 -11.4; 128 -11.4; 141 -11.3; 155 -11.2; 170 -11.0; 187 -10.7; 206 -10.4; 227 -9.9; 249 -9.5; 274 -9.1; 302 -8.6; 332 -8.1; 365 -7.7; 402 -7.2; 442 -6.7; 486 -6.3; 535 -5.8; 588 -5.3; 647 -4.9; 712 -4.4; 783 -4.0; 861 -3.9; 947 -4.1; 1042 -4.9; 1146 -6.0; 1261 -7.1; 1387 -7.9; 1526 -8.3; 1678 -8.5; 1846 -8.5; 2031 -8.2; 2234 -7.4; 2457 -6.0; 2703 -4.8; 2973 -4.0; 3270 -3.6; 3597 -2.6; 3957 -0.5; 4353 -0.5; 4788 -2.9; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.9; 8482 -10.9; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.9; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO FH1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO FH1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.42 | -3.6 dB |
| Peaking | 118 Hz  | 1.1  | -3.3 dB |
| Peaking | 210 Hz  | 1.8  | -2.4 dB |
| Peaking | 4039 Hz | 3.04 | 5.9 dB  |
| Peaking | 5853 Hz | 4.29 | 6.0 dB  |
| Peaking | 839 Hz  | 1.73 | 3.2 dB  |
| Peaking | 1638 Hz | 2.15 | -3.0 dB |
| Peaking | 6763 Hz | 5.09 | 2.5 dB  |
| Peaking | 8421 Hz | 4.07 | -6.3 dB |
| Peaking | 9455 Hz | 2.54 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FiiO%20FH1/FiiO%20FH1.png)