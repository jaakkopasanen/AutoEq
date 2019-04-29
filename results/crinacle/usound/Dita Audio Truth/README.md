# Dita Audio Truth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.2; 25 -6.4; 28 -6.8; 31 -7.0; 34 -7.1; 37 -7.3; 41 -7.4; 45 -7.6; 49 -7.6; 54 -7.7; 60 -7.8; 66 -8.0; 72 -8.2; 79 -8.4; 87 -8.7; 96 -9.0; 106 -9.2; 116 -9.4; 128 -9.6; 141 -9.8; 155 -9.9; 170 -9.9; 187 -9.9; 206 -9.9; 227 -10.1; 249 -9.9; 274 -9.7; 302 -9.6; 332 -9.4; 365 -9.2; 402 -8.9; 442 -8.7; 486 -8.4; 535 -8.0; 588 -7.5; 647 -7.1; 712 -6.5; 783 -5.8; 861 -5.2; 947 -4.7; 1042 -4.5; 1146 -4.7; 1261 -5.3; 1387 -5.0; 1526 -4.3; 1678 -3.1; 1846 -1.4; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.8; 3270 -2.0; 3597 -3.4; 3957 -4.7; 4353 -6.0; 4788 -7.7; 5267 -9.5; 5793 -8.7; 6373 -6.5; 7010 -6.2; 7711 -9.1; 8482 -9.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -8.7; 15026 -6.9; 16529 -7.1; 18182 -10.8; 20000 -12.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Audio Truth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Audio Truth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 196 Hz   | 0.45 | -3.7 dB |
| Peaking | 2788 Hz  | 0.83 | 9.1 dB  |
| Peaking | 4130 Hz  | 3.02 | 2.3 dB  |
| Peaking | 4547 Hz  | 1.06 | -7.3 dB |
| Peaking | 19438 Hz | 0.99 | -6.2 dB |
| Peaking | 19 Hz    | 2.22 | 0.9 dB  |
| Peaking | 943 Hz   | 3.13 | 1.3 dB  |
| Peaking | 1381 Hz  | 4.51 | -1.5 dB |
| Peaking | 6728 Hz  | 7.25 | 2.6 dB  |
| Peaking | 8110 Hz  | 7.68 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Dita%20Audio%20Truth/Dita%20Audio%20Truth.png)