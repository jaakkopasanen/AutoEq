# Lypertek Bevi
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.4; 31 -1.6; 34 -1.8; 37 -1.9; 41 -2.1; 45 -2.2; 49 -2.4; 54 -2.7; 60 -3.0; 66 -3.2; 72 -3.6; 79 -3.9; 87 -4.3; 96 -4.8; 106 -5.1; 116 -5.6; 128 -5.9; 141 -6.1; 155 -6.4; 170 -6.6; 187 -6.8; 206 -6.9; 227 -7.0; 249 -7.0; 274 -7.0; 302 -7.0; 332 -6.9; 365 -6.9; 402 -6.8; 442 -6.7; 486 -6.5; 535 -6.3; 588 -6.1; 647 -5.9; 712 -5.5; 783 -5.1; 861 -4.8; 947 -4.7; 1042 -5.0; 1146 -5.6; 1261 -6.3; 1387 -6.5; 1526 -6.2; 1678 -5.5; 1846 -4.7; 2031 -3.9; 2234 -3.2; 2457 -3.3; 2703 -3.5; 2973 -3.7; 3270 -4.0; 3597 -4.3; 3957 -4.1; 4353 -3.3; 4788 -2.7; 5267 -2.5; 5793 -2.6; 6373 -2.8; 7010 -3.8; 7711 -6.8; 8482 -7.2; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lypertek Bevi GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lypertek Bevi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.66 | 4.6 dB  |
| Peaking | 53 Hz   | 0.8  | 1.9 dB  |
| Peaking | 236 Hz  | 0.58 | -2.0 dB |
| Peaking | 2478 Hz | 2.68 | 2.2 dB  |
| Peaking | 5288 Hz | 2.49 | 3.1 dB  |
| Peaking | 920 Hz  | 3.19 | 1.1 dB  |
| Peaking | 1385 Hz | 3.89 | -1.6 dB |
| Peaking | 6688 Hz | 5.42 | 1.7 dB  |
| Peaking | 8043 Hz | 5.22 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Lypertek%20Bevi/Lypertek%20Bevi.png)