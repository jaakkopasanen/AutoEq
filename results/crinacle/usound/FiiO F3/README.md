# FiiO F3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.7; 25 -6.9; 28 -7.3; 31 -7.5; 34 -7.7; 37 -7.9; 41 -8.1; 45 -8.3; 49 -8.5; 54 -8.7; 60 -8.9; 66 -9.1; 72 -9.4; 79 -9.7; 87 -10.0; 96 -10.3; 106 -10.5; 116 -10.7; 128 -10.8; 141 -10.8; 155 -10.8; 170 -10.8; 187 -10.6; 206 -10.3; 227 -10.0; 249 -9.7; 274 -9.3; 302 -8.9; 332 -8.5; 365 -8.1; 402 -7.7; 442 -7.3; 486 -6.9; 535 -6.5; 588 -6.2; 647 -5.9; 712 -5.5; 783 -5.2; 861 -5.0; 947 -5.0; 1042 -5.4; 1146 -5.9; 1261 -6.6; 1387 -7.1; 1526 -7.0; 1678 -6.4; 1846 -5.5; 2031 -4.5; 2234 -3.4; 2457 -2.3; 2703 -1.6; 2973 -1.2; 3270 -1.3; 3597 -1.5; 3957 -1.4; 4353 -0.8; 4788 -0.5; 5267 -1.0; 5793 -3.1; 6373 -6.8; 7010 -9.1; 7711 -11.6; 8482 -11.4; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -8.1; 16529 -6.5; 18182 -6.7; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO F3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO F3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 100 Hz   | 0.65 | -3.4 dB |
| Peaking | 203 Hz   | 1.19 | -2.4 dB |
| Peaking | 2907 Hz  | 1.81 | 4.6 dB  |
| Peaking | 4879 Hz  | 1.98 | 5.9 dB  |
| Peaking | 7770 Hz  | 3.12 | -7.0 dB |
| Peaking | 880 Hz   | 1.81 | 1.8 dB  |
| Peaking | 1463 Hz  | 2.28 | -1.7 dB |
| Peaking | 2222 Hz  | 4.5  | 0.7 dB  |
| Peaking | 9570 Hz  | 7.93 | 1.4 dB  |
| Peaking | 20232 Hz | 0.92 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FiiO%20F3/FiiO%20F3.png)