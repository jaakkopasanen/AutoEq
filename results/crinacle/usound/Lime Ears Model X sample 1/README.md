# Lime Ears Model X sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -0.9; 31 -1.1; 34 -1.2; 37 -1.3; 41 -1.5; 45 -1.7; 49 -1.8; 54 -2.0; 60 -2.3; 66 -2.6; 72 -3.0; 79 -3.3; 87 -3.8; 96 -4.3; 106 -4.7; 116 -5.1; 128 -5.4; 141 -5.8; 155 -6.1; 170 -6.3; 187 -6.4; 206 -6.5; 227 -6.6; 249 -6.6; 274 -6.6; 302 -6.5; 332 -6.5; 365 -6.3; 402 -6.2; 442 -6.1; 486 -5.8; 535 -5.6; 588 -5.3; 647 -5.0; 712 -4.5; 783 -4.1; 861 -3.7; 947 -3.5; 1042 -3.7; 1146 -4.3; 1261 -5.0; 1387 -5.4; 1526 -5.3; 1678 -5.0; 1846 -4.7; 2031 -4.5; 2234 -4.6; 2457 -4.5; 2703 -3.8; 2973 -2.7; 3270 -2.1; 3597 -1.7; 3957 -1.4; 4353 -2.4; 4788 -4.5; 5267 -5.0; 5793 -3.9; 6373 -3.8; 7010 -6.6; 7711 -9.9; 8482 -8.7; 9330 -5.7; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Model X sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Model X sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.6  | 4.3 dB  |
| Peaking | 58 Hz   | 1.13 | 1.7 dB  |
| Peaking | 224 Hz  | 0.92 | -1.9 dB |
| Peaking | 3666 Hz | 1.94 | 3.7 dB  |
| Peaking | 7852 Hz | 5.23 | -5.8 dB |
| Peaking | 904 Hz  | 1.59 | 3.7 dB  |
| Peaking | 962 Hz  | 0.79 | -2.0 dB |
| Peaking | 5077 Hz | 4.7  | -3.3 dB |
| Peaking | 5570 Hz | 2.13 | 2.4 dB  |
| Peaking | 8591 Hz | 9.1  | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Lime%20Ears%20Model%20X%20sample%201/Lime%20Ears%20Model%20X%20sample%201.png)