# Satolex Tubomi DH298-A1Bk
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.5; 25 -8.9; 28 -9.3; 31 -9.7; 34 -9.9; 37 -10.1; 41 -10.3; 45 -10.6; 49 -10.7; 54 -10.9; 60 -11.1; 66 -11.2; 72 -11.4; 79 -11.5; 87 -11.7; 96 -11.9; 106 -11.9; 116 -11.9; 128 -11.9; 141 -11.7; 155 -11.6; 170 -11.4; 187 -11.0; 206 -10.6; 227 -10.1; 249 -9.6; 274 -8.9; 302 -8.3; 332 -7.8; 365 -7.2; 402 -6.5; 442 -5.9; 486 -5.2; 535 -4.5; 588 -3.8; 647 -3.1; 712 -2.2; 783 -1.5; 861 -0.9; 947 -0.5; 1042 -0.5; 1146 -0.9; 1261 -1.5; 1387 -2.0; 1526 -2.2; 1678 -2.1; 1846 -1.8; 2031 -1.6; 2234 -1.7; 2457 -2.5; 2703 -4.3; 2973 -5.2; 3270 -4.7; 3597 -3.3; 3957 -2.0; 4353 -1.7; 4788 -2.5; 5267 -4.8; 5793 -8.9; 6373 -9.3; 7010 -5.8; 7711 -5.3; 8482 -5.8; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Satolex Tubomi DH298-A1Bk GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Satolex Tubomi DH298-A1Bk ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.49 | -3.4 dB |
| Peaking | 145 Hz  | 0.51 | -5.5 dB |
| Peaking | 748 Hz  | 1.07 | 2.8 dB  |
| Peaking | 1006 Hz | 2    | 2.6 dB  |
| Peaking | 1978 Hz | 1.04 | 3.0 dB  |
| Peaking | 1573 Hz | 5.39 | -0.4 dB |
| Peaking | 2354 Hz | 3.26 | 1.4 dB  |
| Peaking | 2970 Hz | 2.47 | -3.3 dB |
| Peaking | 4318 Hz | 1.91 | 4.2 dB  |
| Peaking | 6032 Hz | 4.81 | -6.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Satolex%20Tubomi%20DH298-A1Bk/Satolex%20Tubomi%20DH298-A1Bk.png)