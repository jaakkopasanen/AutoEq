# Dita Audio Dream sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.0; 25 -8.9; 28 -8.6; 31 -8.3; 34 -8.1; 37 -7.8; 41 -7.6; 45 -7.4; 49 -7.1; 54 -6.8; 60 -6.6; 66 -6.6; 72 -6.5; 79 -6.6; 87 -6.7; 96 -6.8; 106 -6.9; 116 -7.1; 128 -7.1; 141 -7.2; 155 -7.3; 170 -7.3; 187 -7.3; 206 -7.2; 227 -7.2; 249 -7.1; 274 -7.0; 302 -6.9; 332 -6.7; 365 -6.5; 402 -6.3; 442 -6.1; 486 -5.9; 535 -5.6; 588 -5.3; 647 -5.1; 712 -4.5; 783 -3.8; 861 -3.4; 947 -3.1; 1042 -3.2; 1146 -3.6; 1261 -4.0; 1387 -4.1; 1526 -3.7; 1678 -2.9; 1846 -2.1; 2031 -1.3; 2234 -0.8; 2457 -0.5; 2703 -0.6; 2973 -1.0; 3270 -1.8; 3597 -2.9; 3957 -4.2; 4353 -5.8; 4788 -6.7; 5267 -5.3; 5793 -6.1; 6373 -5.5; 7010 -6.6; 7711 -10.3; 8482 -11.0; 9330 -6.4; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -6.7; 15026 -6.6; 16529 -7.0; 18182 -10.5; 20000 -13.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Audio Dream sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Audio Dream sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.74 | -3.8 dB |
| Peaking | 202 Hz   | 0.51 | -2.1 dB |
| Peaking | 917 Hz   | 2.02 | 2.1 dB  |
| Peaking | 2474 Hz  | 1.69 | 5.1 dB  |
| Peaking | 8169 Hz  | 4.19 | -6.8 dB |
| Peaking | 1852 Hz  | 6.91 | 0.5 dB  |
| Peaking | 3341 Hz  | 5.1  | 1.1 dB  |
| Peaking | 4635 Hz  | 5.23 | -2.2 dB |
| Peaking | 10325 Hz | 2.78 | 1.4 dB  |
| Peaking | 19699 Hz | 0.78 | -8.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Dita%20Audio%20Dream%20sample%201/Dita%20Audio%20Dream%20sample%201.png)