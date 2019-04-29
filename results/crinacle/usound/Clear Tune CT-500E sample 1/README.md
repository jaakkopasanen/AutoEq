# Clear Tune CT-500E sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.5; 25 -4.6; 28 -4.8; 31 -4.9; 34 -5.0; 37 -5.1; 41 -5.3; 45 -5.4; 49 -5.6; 54 -5.8; 60 -6.1; 66 -6.4; 72 -6.7; 79 -7.0; 87 -7.4; 96 -7.9; 106 -8.2; 116 -8.6; 128 -8.9; 141 -9.2; 155 -9.4; 170 -9.6; 187 -9.7; 206 -9.7; 227 -9.6; 249 -9.5; 274 -9.3; 302 -9.1; 332 -8.8; 365 -8.4; 402 -8.0; 442 -7.5; 486 -7.0; 535 -6.3; 588 -5.4; 647 -4.5; 712 -3.3; 783 -2.1; 861 -0.9; 947 -0.5; 1042 -0.6; 1146 -2.0; 1261 -4.3; 1387 -7.1; 1526 -9.8; 1678 -11.3; 1846 -11.1; 2031 -10.1; 2234 -9.0; 2457 -8.2; 2703 -7.5; 2973 -6.8; 3270 -6.3; 3597 -6.4; 3957 -7.5; 4353 -8.4; 4788 -7.5; 5267 -4.3; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-500E sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-500E sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.24 | 2.2 dB  |
| Peaking | 198 Hz  | 0.42 | -4.1 dB |
| Peaking | 1012 Hz | 1.19 | 9.2 dB  |
| Peaking | 1669 Hz | 1.57 | -8.1 dB |
| Peaking | 6112 Hz | 4.86 | 6.9 dB  |
| Peaking | 3410 Hz | 3.12 | 1.3 dB  |
| Peaking | 4454 Hz | 3.41 | -2.8 dB |
| Peaking | 5520 Hz | 7.89 | 2.2 dB  |
| Peaking | 8249 Hz | 5.48 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Clear%20Tune%20CT-500E%20sample%201/Clear%20Tune%20CT-500E%20sample%201.png)