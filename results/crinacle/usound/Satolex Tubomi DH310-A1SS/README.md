# Satolex Tubomi DH310-A1SS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.6; 25 -6.0; 28 -6.6; 31 -7.1; 34 -7.5; 37 -7.8; 41 -8.1; 45 -8.4; 49 -8.7; 54 -9.0; 60 -9.3; 66 -9.7; 72 -10.0; 79 -10.2; 87 -10.5; 96 -10.8; 106 -10.9; 116 -11.0; 128 -11.1; 141 -11.0; 155 -11.0; 170 -10.8; 187 -10.5; 206 -10.2; 227 -9.8; 249 -9.3; 274 -8.8; 302 -8.2; 332 -7.7; 365 -7.1; 402 -6.5; 442 -5.9; 486 -5.3; 535 -4.6; 588 -4.0; 647 -3.3; 712 -2.6; 783 -1.7; 861 -1.0; 947 -0.6; 1042 -0.5; 1146 -0.7; 1261 -1.0; 1387 -1.3; 1526 -1.3; 1678 -1.0; 1846 -0.8; 2031 -1.0; 2234 -1.4; 2457 -2.8; 2703 -4.3; 2973 -5.0; 3270 -4.9; 3597 -3.8; 3957 -2.7; 4353 -2.2; 4788 -2.8; 5267 -4.9; 5793 -8.9; 6373 -9.6; 7010 -6.1; 7711 -5.5; 8482 -6.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Satolex Tubomi DH310-A1SS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Satolex Tubomi DH310-A1SS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 58 Hz   | 0.77 | -1.5 dB |
| Peaking | 150 Hz  | 0.49 | -5.5 dB |
| Peaking | 912 Hz  | 1.15 | 2.4 dB  |
| Peaking | 1492 Hz | 0.52 | 3.5 dB  |
| Peaking | 6145 Hz | 6.46 | -6.1 dB |
| Peaking | 2107 Hz | 2.54 | 1.9 dB  |
| Peaking | 2991 Hz | 2.82 | -2.0 dB |
| Peaking | 3886 Hz | 0.7  | -1.5 dB |
| Peaking | 4464 Hz | 2.56 | 4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Satolex%20Tubomi%20DH310-A1SS/Satolex%20Tubomi%20DH310-A1SS.png)