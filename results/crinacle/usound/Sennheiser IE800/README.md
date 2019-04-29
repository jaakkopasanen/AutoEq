# Sennheiser IE800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -6.9; 25 -6.9; 28 -6.9; 31 -6.9; 34 -6.8; 37 -6.8; 41 -6.8; 45 -6.7; 49 -6.7; 54 -6.6; 60 -6.7; 66 -6.8; 72 -6.9; 79 -7.1; 87 -7.3; 96 -7.6; 106 -7.8; 116 -8.0; 128 -8.2; 141 -8.4; 155 -8.6; 170 -8.6; 187 -8.7; 206 -8.8; 227 -8.8; 249 -8.8; 274 -8.8; 302 -8.8; 332 -8.8; 365 -8.8; 402 -8.8; 442 -8.8; 486 -8.7; 535 -8.7; 588 -8.6; 647 -8.5; 712 -8.3; 783 -8.1; 861 -8.0; 947 -8.0; 1042 -8.4; 1146 -8.9; 1261 -9.5; 1387 -9.6; 1526 -9.0; 1678 -7.9; 1846 -6.4; 2031 -4.7; 2234 -3.1; 2457 -1.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.5; 5267 -4.9; 5793 -7.7; 6373 -2.2; 7010 -4.4; 7711 -6.4; 8482 -7.1; 9330 -8.0; 10263 -7.9; 11289 -6.5; 12418 -7.0; 13660 -10.9; 15026 -14.4; 16529 -15.3; 18182 -14.0; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 302 Hz   | 0.39 | -2.4 dB |
| Peaking | 1421 Hz  | 1.95 | -3.5 dB |
| Peaking | 2592 Hz  | 2.07 | 4.1 dB  |
| Peaking | 3913 Hz  | 1.37 | 5.7 dB  |
| Peaking | 17364 Hz | 0.78 | -9.5 dB |
| Peaking | 5712 Hz  | 8.74 | -4.5 dB |
| Peaking | 6539 Hz  | 8.5  | 4.4 dB  |
| Peaking | 12107 Hz | 4.36 | 3.0 dB  |
| Peaking | 14901 Hz | 3.58 | -2.4 dB |
| Peaking | 19811 Hz | 3.54 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB   |
| Peaking | 125 Hz   | 1.41 | -1.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -10.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sennheiser%20IE800/Sennheiser%20IE800.png)