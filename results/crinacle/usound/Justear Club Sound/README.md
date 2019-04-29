# Justear Club Sound
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.8; 25 -2.2; 28 -2.6; 31 -3.0; 34 -3.3; 37 -3.6; 41 -4.0; 45 -4.4; 49 -4.8; 54 -5.2; 60 -5.8; 66 -6.4; 72 -6.9; 79 -7.5; 87 -8.1; 96 -8.8; 106 -9.4; 116 -9.9; 128 -10.3; 141 -10.6; 155 -10.7; 170 -10.6; 187 -10.4; 206 -10.0; 227 -9.5; 249 -9.0; 274 -8.4; 302 -7.9; 332 -7.4; 365 -6.9; 402 -6.5; 442 -6.1; 486 -5.8; 535 -5.5; 588 -5.3; 647 -5.0; 712 -4.6; 783 -4.1; 861 -3.8; 947 -3.8; 1042 -4.3; 1146 -5.3; 1261 -6.5; 1387 -7.4; 1526 -7.7; 1678 -7.7; 1846 -7.9; 2031 -8.4; 2234 -9.3; 2457 -10.0; 2703 -9.2; 2973 -6.9; 3270 -4.4; 3597 -2.5; 3957 -1.2; 4353 -0.5; 4788 -3.0; 5267 -7.4; 5793 -7.3; 6373 -2.6; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Justear Club Sound GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Justear Club Sound ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.38 | 5.3 dB  |
| Peaking | 149 Hz  | 0.83 | -4.9 dB |
| Peaking | 832 Hz  | 1.33 | 3.1 dB  |
| Peaking | 2473 Hz | 1.27 | -4.7 dB |
| Peaking | 3935 Hz | 2.24 | 7.5 dB  |
| Peaking | 1433 Hz | 3.23 | -2.3 dB |
| Peaking | 1436 Hz | 1.54 | 1.4 dB  |
| Peaking | 4616 Hz | 6.11 | 3.2 dB  |
| Peaking | 5487 Hz | 2.92 | -4.6 dB |
| Peaking | 6512 Hz | 5.81 | 5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Justear%20Club%20Sound/Justear%20Club%20Sound.png)