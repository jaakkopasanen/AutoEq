# Clear Tune CT-500E
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.8; 25 -3.9; 28 -4.1; 31 -4.2; 34 -4.4; 37 -4.5; 41 -4.7; 45 -4.8; 49 -5.0; 54 -5.2; 60 -5.5; 66 -5.8; 72 -6.2; 79 -6.5; 87 -6.9; 96 -7.4; 106 -7.8; 116 -8.1; 128 -8.5; 141 -8.8; 155 -9.0; 170 -9.2; 187 -9.3; 206 -9.3; 227 -9.3; 249 -9.2; 274 -9.1; 302 -8.9; 332 -8.6; 365 -8.4; 402 -8.0; 442 -7.6; 486 -7.1; 535 -6.5; 588 -5.8; 647 -4.9; 712 -3.9; 783 -2.8; 861 -1.7; 947 -1.1; 1042 -1.3; 1146 -2.7; 1261 -4.9; 1387 -7.5; 1526 -9.4; 1678 -10.3; 1846 -10.1; 2031 -9.4; 2234 -8.6; 2457 -7.7; 2703 -7.0; 2973 -6.5; 3270 -5.9; 3597 -6.2; 3957 -7.1; 4353 -7.9; 4788 -7.6; 5267 -4.3; 5793 -0.5; 6373 -0.9; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-500E GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-500E ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.21 | 2.7 dB  |
| Peaking | 196 Hz  | 0.42 | -3.9 dB |
| Peaking | 1007 Hz | 1.28 | 8.0 dB  |
| Peaking | 1627 Hz | 1.51 | -6.7 dB |
| Peaking | 6062 Hz | 4.92 | 6.9 dB  |
| Peaking | 3285 Hz | 3.83 | 1.1 dB  |
| Peaking | 4665 Hz | 3.49 | -3.7 dB |
| Peaking | 5300 Hz | 2.79 | 2.0 dB  |
| Peaking | 8255 Hz | 5.14 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Clear%20Tune%20CT-500E/Clear%20Tune%20CT-500E.png)