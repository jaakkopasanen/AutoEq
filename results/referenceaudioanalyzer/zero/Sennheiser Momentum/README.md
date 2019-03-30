# Sennheiser Momentum
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.3; 25 -2.9; 28 -3.6; 31 -4.2; 34 -4.6; 37 -5.0; 41 -5.3; 45 -5.4; 49 -5.4; 54 -5.3; 60 -5.4; 66 -5.8; 72 -6.4; 79 -7.0; 87 -7.2; 96 -7.4; 106 -7.7; 116 -8.1; 128 -8.3; 141 -8.5; 155 -8.3; 170 -8.1; 187 -7.8; 206 -7.4; 227 -6.8; 249 -6.1; 274 -5.3; 302 -4.4; 332 -3.8; 365 -3.6; 402 -3.3; 442 -3.3; 486 -3.3; 535 -3.4; 588 -3.8; 647 -4.4; 712 -5.1; 783 -5.7; 861 -5.9; 947 -5.9; 1042 -5.9; 1146 -5.9; 1261 -6.0; 1387 -6.2; 1526 -6.0; 1678 -5.5; 1846 -4.8; 2031 -4.1; 2234 -3.6; 2457 -3.7; 2703 -3.9; 2973 -3.9; 3270 -3.9; 3597 -3.4; 3957 -2.0; 4353 -0.5; 4788 -3.9; 5267 -6.3; 5793 -5.8; 6373 -3.7; 7010 -2.7; 7711 -4.7; 8482 -5.0; 9330 -5.2; 10263 -6.4; 11289 -7.4; 12418 -8.6; 13660 -8.7; 15026 -6.1; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.5  | 3.8 dB  |
| Peaking | 147 Hz   | 0.76 | -3.7 dB |
| Peaking | 387 Hz   | 1.58 | 2.9 dB  |
| Peaking | 4196 Hz  | 4.76 | 4.6 dB  |
| Peaking | 12929 Hz | 2.31 | -4.3 dB |
| Peaking | 560 Hz   | 3.63 | 1.2 dB  |
| Peaking | 1521 Hz  | 0.78 | -2.1 dB |
| Peaking | 2234 Hz  | 1.41 | 2.7 dB  |
| Peaking | 5393 Hz  | 5.99 | -2.5 dB |
| Peaking | 6791 Hz  | 6.2  | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20Momentum/Sennheiser%20Momentum.png)