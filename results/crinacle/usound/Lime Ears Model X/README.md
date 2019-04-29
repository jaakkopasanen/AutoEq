# Lime Ears Model X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.9; 28 -1.2; 31 -1.4; 34 -1.5; 37 -1.7; 41 -1.8; 45 -2.0; 49 -2.2; 54 -2.5; 60 -2.7; 66 -3.1; 72 -3.4; 79 -3.8; 87 -4.2; 96 -4.7; 106 -5.1; 116 -5.5; 128 -5.8; 141 -6.2; 155 -6.4; 170 -6.6; 187 -6.8; 206 -7.0; 227 -7.0; 249 -7.1; 274 -7.1; 302 -7.0; 332 -7.0; 365 -6.8; 402 -6.7; 442 -6.6; 486 -6.4; 535 -6.2; 588 -5.9; 647 -5.6; 712 -5.2; 783 -4.7; 861 -4.3; 947 -4.2; 1042 -4.4; 1146 -5.0; 1261 -5.8; 1387 -6.3; 1526 -6.4; 1678 -6.2; 1846 -6.0; 2031 -6.0; 2234 -6.0; 2457 -5.5; 2703 -4.6; 2973 -3.7; 3270 -3.6; 3597 -4.1; 3957 -3.8; 4353 -4.6; 4788 -7.2; 5267 -6.9; 5793 -4.6; 6373 -3.9; 7010 -5.9; 7711 -9.6; 8482 -10.7; 9330 -9.2; 10263 -6.5; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Model X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Model X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.94 | 5.2 dB  |
| Peaking | 56 Hz   | 1.6  | 2.5 dB  |
| Peaking | 920 Hz  | 3.66 | 2.1 dB  |
| Peaking | 3379 Hz | 2.4  | 2.6 dB  |
| Peaking | 8489 Hz | 4.42 | -5.5 dB |
| Peaking | 90 Hz   | 1.43 | 1.0 dB  |
| Peaking | 410 Hz  | 0.32 | -1.7 dB |
| Peaking | 703 Hz  | 0.94 | 1.7 dB  |
| Peaking | 5024 Hz | 9.25 | -2.4 dB |
| Peaking | 6269 Hz | 5.92 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Lime%20Ears%20Model%20X/Lime%20Ears%20Model%20X.png)