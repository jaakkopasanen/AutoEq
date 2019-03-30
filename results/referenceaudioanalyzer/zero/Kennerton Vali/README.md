# Kennerton Vali
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.9; 28 -2.7; 31 -3.4; 34 -3.9; 37 -4.4; 41 -4.9; 45 -5.3; 49 -5.6; 54 -5.9; 60 -6.2; 66 -6.3; 72 -6.4; 79 -6.3; 87 -6.3; 96 -6.4; 106 -6.1; 116 -6.0; 128 -5.7; 141 -5.5; 155 -5.2; 170 -5.0; 187 -4.9; 206 -4.7; 227 -4.6; 249 -4.4; 274 -4.4; 302 -4.4; 332 -4.4; 365 -4.4; 402 -4.4; 442 -4.4; 486 -4.4; 535 -4.7; 588 -4.9; 647 -5.3; 712 -5.9; 783 -6.7; 861 -7.6; 947 -8.0; 1042 -8.0; 1146 -7.7; 1261 -6.7; 1387 -5.4; 1526 -3.7; 1678 -2.0; 1846 -0.8; 2031 -1.8; 2234 -4.0; 2457 -5.0; 2703 -4.8; 2973 -4.1; 3270 -3.7; 3597 -3.9; 3957 -3.9; 4353 -3.7; 4788 -3.7; 5267 -4.5; 5793 -6.3; 6373 -5.3; 7010 -2.2; 7711 -4.0; 8482 -4.3; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -4.3; 13660 -4.3; 15026 -4.3; 16529 -4.3; 18182 -4.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kennerton Vali GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kennerton Vali ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.17 | 4.6 dB  |
| Peaking | 72 Hz   | 0.62 | -2.4 dB |
| Peaking | 516 Hz  | 0.52 | 0.7 dB  |
| Peaking | 1004 Hz | 1.42 | -4.5 dB |
| Peaking | 1805 Hz | 3.72 | 4.6 dB  |
| Peaking | 20 Hz   | 0.91 | 0.4 dB  |
| Peaking | 2508 Hz | 6.51 | -1.4 dB |
| Peaking | 4885 Hz | 1.39 | 1.2 dB  |
| Peaking | 5926 Hz | 3.99 | -3.2 dB |
| Peaking | 6888 Hz | 8.83 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Kennerton%20Vali/Kennerton%20Vali.png)