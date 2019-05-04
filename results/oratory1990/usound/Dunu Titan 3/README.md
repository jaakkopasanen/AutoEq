# Dunu Titan 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.8; 28 -0.9; 31 -1.0; 34 -1.1; 37 -1.2; 41 -1.3; 45 -1.4; 49 -1.6; 54 -1.9; 60 -2.4; 66 -2.8; 72 -3.0; 79 -3.5; 87 -3.7; 96 -3.7; 106 -4.3; 116 -4.4; 128 -5.0; 141 -5.1; 155 -5.3; 170 -5.6; 187 -6.0; 206 -6.2; 227 -6.5; 249 -6.7; 274 -6.9; 302 -7.1; 332 -7.2; 365 -6.0; 402 -7.2; 442 -7.4; 486 -7.4; 535 -7.4; 588 -7.1; 647 -6.8; 712 -6.1; 783 -5.5; 861 -5.2; 947 -5.0; 1042 -5.3; 1146 -6.0; 1261 -7.0; 1387 -7.7; 1526 -8.0; 1678 -8.0; 1846 -8.0; 2031 -8.3; 2234 -9.2; 2457 -10.2; 2703 -10.5; 2973 -9.4; 3270 -8.0; 3597 -7.0; 3957 -6.9; 4353 -8.1; 4788 -11.4; 5267 -11.8; 5793 -6.1; 6373 -2.0; 7010 -4.0; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Titan 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.49 | 5.5 dB  |
| Peaking | 64 Hz   | 0.81 | 2.0 dB  |
| Peaking | 2538 Hz | 2.49 | -4.0 dB |
| Peaking | 5086 Hz | 5.57 | -7.1 dB |
| Peaking | 6423 Hz | 5.02 | 5.8 dB  |
| Peaking | 595 Hz  | 0.88 | -1.7 dB |
| Peaking | 914 Hz  | 1.34 | 3.0 dB  |
| Peaking | 1434 Hz | 2.45 | -1.7 dB |
| Peaking | 3775 Hz | 6.9  | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | 1.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Dunu%20Titan%203/Dunu%20Titan%203.png)