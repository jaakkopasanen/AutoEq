# Lime Ears Model X Bass sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -4.9; 25 -5.0; 28 -5.1; 31 -5.3; 34 -5.4; 37 -5.5; 41 -5.7; 45 -5.9; 49 -6.0; 54 -6.2; 60 -6.5; 66 -6.8; 72 -7.1; 79 -7.5; 87 -7.9; 96 -8.4; 106 -8.7; 116 -9.0; 128 -9.3; 141 -9.6; 155 -9.8; 170 -9.9; 187 -10.0; 206 -10.0; 227 -9.9; 249 -9.8; 274 -9.7; 302 -9.4; 332 -9.2; 365 -8.9; 402 -8.6; 442 -8.3; 486 -7.9; 535 -7.5; 588 -7.0; 647 -6.5; 712 -5.8; 783 -5.2; 861 -4.6; 947 -4.2; 1042 -4.2; 1146 -4.6; 1261 -5.1; 1387 -5.2; 1526 -4.9; 1678 -4.3; 1846 -3.6; 2031 -3.1; 2234 -2.9; 2457 -2.7; 2703 -2.1; 2973 -1.3; 3270 -0.9; 3597 -0.9; 3957 -0.5; 4353 -0.9; 4788 -2.7; 5267 -2.9; 5793 -1.5; 6373 -1.3; 7010 -4.2; 7711 -7.8; 8482 -6.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Model X Bass sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Model X Bass sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 213 Hz  | 0.53 | -4.4 dB |
| Peaking | 918 Hz  | 2.37 | 2.0 dB  |
| Peaking | 3477 Hz | 1    | 5.1 dB  |
| Peaking | 6388 Hz | 3.98 | 4.1 dB  |
| Peaking | 7665 Hz | 3.71 | -4.1 dB |
| Peaking | 18 Hz   | 1.35 | 1.0 dB  |
| Peaking | 35 Hz   | 1.39 | 0.5 dB  |
| Peaking | 1094 Hz | 4.97 | 0.5 dB  |
| Peaking | 1724 Hz | 1.33 | -1.0 dB |
| Peaking | 1868 Hz | 2.86 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Lime%20Ears%20Model%20X%20Bass%20sample%201/Lime%20Ears%20Model%20X%20Bass%20sample%201.png)