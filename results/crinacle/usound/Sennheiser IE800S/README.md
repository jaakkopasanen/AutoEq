# Sennheiser IE800S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.7; 25 -8.8; 28 -9.0; 31 -9.1; 34 -9.3; 37 -9.4; 41 -9.5; 45 -9.6; 49 -9.7; 54 -9.8; 60 -10.0; 66 -10.1; 72 -10.3; 79 -10.5; 87 -10.6; 96 -10.8; 106 -11.0; 116 -11.1; 128 -11.1; 141 -11.1; 155 -11.1; 170 -10.9; 187 -10.7; 206 -10.5; 227 -10.3; 249 -10.0; 274 -9.7; 302 -9.4; 332 -9.1; 365 -8.8; 402 -8.6; 442 -8.4; 486 -8.1; 535 -7.9; 588 -7.7; 647 -7.5; 712 -7.3; 783 -7.0; 861 -6.9; 947 -7.0; 1042 -7.4; 1146 -8.1; 1261 -8.7; 1387 -8.7; 1526 -8.5; 1678 -7.7; 1846 -6.4; 2031 -4.7; 2234 -3.1; 2457 -1.3; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.3; 5267 -5.2; 5793 -7.0; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -10.8; 15026 -13.5; 16529 -11.7; 18182 -8.9; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE800S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE800S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.03 | -1.0 dB |
| Peaking | 126 Hz   | 0.29 | -4.3 dB |
| Peaking | 3525 Hz  | 1.33 | 7.1 dB  |
| Peaking | 12440 Hz | 1.26 | 4.6 dB  |
| Peaking | 14906 Hz | 1.03 | -9.3 dB |
| Peaking | 983 Hz   | 0.8  | 1.4 dB  |
| Peaking | 1405 Hz  | 1.49 | -4.0 dB |
| Peaking | 2468 Hz  | 4    | 2.7 dB  |
| Peaking | 5702 Hz  | 9.43 | -4.3 dB |
| Peaking | 6492 Hz  | 7.71 | 4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -7.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sennheiser%20IE800S/Sennheiser%20IE800S.png)