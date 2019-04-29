# AZLA 01R Mk2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.3; 25 -6.6; 28 -7.0; 31 -7.3; 34 -7.5; 37 -7.7; 41 -7.9; 45 -8.0; 49 -8.0; 54 -8.1; 60 -8.2; 66 -8.2; 72 -8.3; 79 -8.4; 87 -8.5; 96 -8.5; 106 -8.6; 116 -8.5; 128 -8.5; 141 -8.4; 155 -8.2; 170 -7.9; 187 -7.7; 206 -7.3; 227 -6.9; 249 -6.6; 274 -6.1; 302 -5.7; 332 -5.3; 365 -4.9; 402 -4.5; 442 -4.1; 486 -3.7; 535 -3.3; 588 -3.0; 647 -2.6; 712 -2.2; 783 -1.8; 861 -1.6; 947 -1.7; 1042 -2.1; 1146 -2.9; 1261 -3.8; 1387 -4.5; 1526 -4.9; 1678 -5.1; 1846 -5.5; 2031 -6.2; 2234 -7.3; 2457 -8.2; 2703 -7.9; 2973 -6.5; 3270 -5.3; 3597 -5.1; 3957 -6.7; 4353 -9.1; 4788 -9.4; 5267 -7.9; 5793 -3.6; 6373 -0.5; 7010 -2.8; 7711 -5.0; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AZLA 01R Mk2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AZLA 01R Mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 90 Hz   | 0.39 | -3.4 dB |
| Peaking | 777 Hz  | 0.92 | 3.9 dB  |
| Peaking | 2423 Hz | 3.11 | -3.4 dB |
| Peaking | 4775 Hz | 3.8  | -5.2 dB |
| Peaking | 6377 Hz | 4.97 | 5.9 dB  |
| Peaking | 711 Hz  | 1.89 | -2.0 dB |
| Peaking | 806 Hz  | 1.07 | 1.9 dB  |
| Peaking | 1413 Hz | 2.11 | -1.1 dB |
| Peaking | 3484 Hz | 8.63 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/AZLA%2001R%20Mk2/AZLA%2001R%20Mk2.png)