# Dita Audio Dream sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.5; 25 -9.4; 28 -9.1; 31 -8.9; 34 -8.7; 37 -8.5; 41 -8.3; 45 -8.1; 49 -7.9; 54 -7.8; 60 -7.7; 66 -7.6; 72 -7.6; 79 -7.7; 87 -7.7; 96 -7.9; 106 -8.0; 116 -8.2; 128 -8.3; 141 -8.4; 155 -8.4; 170 -8.4; 187 -8.3; 206 -8.3; 227 -8.1; 249 -8.0; 274 -7.8; 302 -7.5; 332 -7.1; 365 -6.8; 402 -6.4; 442 -6.1; 486 -5.7; 535 -5.3; 588 -4.8; 647 -4.2; 712 -3.7; 783 -3.1; 861 -2.6; 947 -2.3; 1042 -2.3; 1146 -2.8; 1261 -3.3; 1387 -3.5; 1526 -3.2; 1678 -2.6; 1846 -1.8; 2031 -1.2; 2234 -0.7; 2457 -0.5; 2703 -0.6; 2973 -1.1; 3270 -2.0; 3597 -3.1; 3957 -4.7; 4353 -6.6; 4788 -7.9; 5267 -6.4; 5793 -5.4; 6373 -3.2; 7010 -3.0; 7711 -5.6; 8482 -9.8; 9330 -10.9; 10263 -9.4; 11289 -8.2; 12418 -6.4; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Audio Dream sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Audio Dream sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.48 | -4.4 dB |
| Peaking | 184 Hz  | 0.52 | -3.1 dB |
| Peaking | 916 Hz  | 1.32 | 3.0 dB  |
| Peaking | 2452 Hz | 1.8  | 5.0 dB  |
| Peaking | 9540 Hz | 2.96 | -6.2 dB |
| Peaking | 3255 Hz | 4.39 | 1.2 dB  |
| Peaking | 3889 Hz | 3.6  | 1.1 dB  |
| Peaking | 4686 Hz | 2.63 | -3.9 dB |
| Peaking | 6801 Hz | 3.44 | 3.9 dB  |
| Peaking | 8531 Hz | 7.55 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Dita%20Audio%20Dream%20sample%202/Dita%20Audio%20Dream%20sample%202.png)