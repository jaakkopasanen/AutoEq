# FiiO FH5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.7; 28 -8.8; 31 -8.8; 34 -8.8; 37 -8.8; 41 -8.8; 45 -8.8; 49 -8.8; 54 -8.8; 60 -8.8; 66 -8.8; 72 -8.8; 79 -8.9; 87 -8.9; 96 -9.0; 106 -9.2; 116 -9.2; 128 -9.2; 141 -9.2; 155 -9.1; 170 -9.0; 187 -8.9; 206 -8.9; 227 -8.7; 249 -8.5; 274 -8.4; 302 -8.2; 332 -8.0; 365 -7.8; 402 -7.7; 442 -7.6; 486 -7.4; 535 -7.3; 588 -7.2; 647 -7.0; 712 -6.9; 783 -6.8; 861 -7.0; 947 -7.3; 1042 -8.0; 1146 -8.8; 1261 -9.3; 1387 -9.1; 1526 -8.4; 1678 -7.8; 1846 -7.7; 2031 -8.1; 2234 -8.0; 2457 -6.5; 2703 -4.9; 2973 -3.9; 3270 -2.1; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.0; 5267 -6.1; 5793 -4.8; 6373 -5.2; 7010 -8.4; 7711 -6.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO FH5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO FH5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 79 Hz   | 0.22 | -2.7 dB |
| Peaking | 1302 Hz | 2.75 | -2.9 dB |
| Peaking | 2144 Hz | 3.35 | -2.4 dB |
| Peaking | 3905 Hz | 1.84 | 6.8 dB  |
| Peaking | 7108 Hz | 6.94 | -3.1 dB |
| Peaking | 16 Hz   | 0.6  | -0.4 dB |
| Peaking | 62 Hz   | 1.16 | 0.7 dB  |
| Peaking | 655 Hz  | 0.93 | 0.6 dB  |
| Peaking | 778 Hz  | 0.06 | -0.3 dB |
| Peaking | 3325 Hz | 0.77 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FiiO%20FH5/FiiO%20FH5.png)