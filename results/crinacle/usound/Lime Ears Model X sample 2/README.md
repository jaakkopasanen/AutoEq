# Lime Ears Model X sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -1.1; 31 -1.3; 34 -1.5; 37 -1.6; 41 -1.8; 45 -2.0; 49 -2.3; 54 -2.6; 60 -2.8; 66 -3.1; 72 -3.4; 79 -3.8; 87 -4.2; 96 -4.7; 106 -5.1; 116 -5.6; 128 -5.9; 141 -6.2; 155 -6.4; 170 -6.6; 187 -6.8; 206 -7.0; 227 -7.1; 249 -7.1; 274 -7.1; 302 -7.1; 332 -7.1; 365 -6.9; 402 -6.8; 442 -6.7; 486 -6.5; 535 -6.3; 588 -6.1; 647 -5.7; 712 -5.4; 783 -4.9; 861 -4.6; 947 -4.4; 1042 -4.7; 1146 -5.4; 1261 -6.3; 1387 -6.9; 1526 -7.1; 1678 -7.0; 1846 -7.0; 2031 -7.1; 2234 -7.0; 2457 -6.1; 2703 -5.0; 2973 -4.3; 3270 -4.9; 3597 -6.1; 3957 -5.7; 4353 -6.5; 4788 -9.4; 5267 -8.3; 5793 -4.9; 6373 -3.6; 7010 -4.9; 7711 -9.0; 8482 -12.3; 9330 -12.4; 10263 -9.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Model X sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Model X sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.78 | 5.7 dB  |
| Peaking | 60 Hz    | 1.4  | 2.4 dB  |
| Peaking | 906 Hz   | 2.93 | 2.3 dB  |
| Peaking | 6559 Hz  | 5.49 | 4.4 dB  |
| Peaking | 8848 Hz  | 3.31 | -7.1 dB |
| Peaking | 253 Hz   | 1.48 | -0.9 dB |
| Peaking | 2244 Hz  | 1.69 | -2.3 dB |
| Peaking | 2823 Hz  | 1.87 | 3.3 dB  |
| Peaking | 4909 Hz  | 8.01 | -4.0 dB |
| Peaking | 11354 Hz | 5.9  | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Lime%20Ears%20Model%20X%20sample%202/Lime%20Ears%20Model%20X%20sample%202.png)