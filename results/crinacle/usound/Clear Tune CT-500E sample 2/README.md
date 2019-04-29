# Clear Tune CT-500E sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.3; 25 -3.4; 28 -3.6; 31 -3.7; 34 -3.9; 37 -4.0; 41 -4.2; 45 -4.4; 49 -4.6; 54 -4.8; 60 -5.1; 66 -5.4; 72 -5.8; 79 -6.2; 87 -6.6; 96 -7.1; 106 -7.5; 116 -7.8; 128 -8.2; 141 -8.5; 155 -8.7; 170 -8.9; 187 -9.1; 206 -9.2; 227 -9.1; 249 -9.1; 274 -9.0; 302 -8.8; 332 -8.6; 365 -8.4; 402 -8.2; 442 -7.8; 486 -7.4; 535 -6.8; 588 -6.2; 647 -5.5; 712 -4.6; 783 -3.6; 861 -2.7; 947 -2.2; 1042 -2.3; 1146 -3.6; 1261 -5.7; 1387 -8.0; 1526 -9.2; 1678 -9.4; 1846 -9.4; 2031 -9.0; 2234 -8.3; 2457 -7.3; 2703 -6.6; 2973 -6.4; 3270 -5.8; 3597 -6.3; 3957 -6.8; 4353 -7.6; 4788 -7.8; 5267 -4.5; 5793 -0.5; 6373 -0.8; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-500E sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-500E sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.19 | 3.2 dB  |
| Peaking | 198 Hz  | 0.41 | -3.7 dB |
| Peaking | 1012 Hz | 1.33 | 7.1 dB  |
| Peaking | 1571 Hz | 1.42 | -5.8 dB |
| Peaking | 6107 Hz | 4.99 | 6.9 dB  |
| Peaking | 2122 Hz | 6.28 | -0.5 dB |
| Peaking | 3179 Hz | 2.31 | 1.0 dB  |
| Peaking | 4717 Hz | 3.83 | -2.8 dB |
| Peaking | 5544 Hz | 6.72 | 2.1 dB  |
| Peaking | 8298 Hz | 5.57 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Clear%20Tune%20CT-500E%20sample%202/Clear%20Tune%20CT-500E%20sample%202.png)