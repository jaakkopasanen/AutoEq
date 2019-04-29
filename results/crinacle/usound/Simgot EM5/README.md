# Simgot EM5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.8; 25 -4.2; 28 -4.7; 31 -5.0; 34 -5.3; 37 -5.6; 41 -5.8; 45 -6.1; 49 -6.3; 54 -6.6; 60 -6.9; 66 -7.2; 72 -7.6; 79 -8.0; 87 -8.3; 96 -8.8; 106 -9.1; 116 -9.4; 128 -9.6; 141 -9.8; 155 -10.0; 170 -10.0; 187 -10.0; 206 -9.9; 227 -9.7; 249 -9.5; 274 -9.2; 302 -8.8; 332 -8.5; 365 -8.1; 402 -7.6; 442 -7.2; 486 -6.7; 535 -6.1; 588 -5.5; 647 -4.9; 712 -4.2; 783 -3.5; 861 -2.9; 947 -2.6; 1042 -2.6; 1146 -3.1; 1261 -3.8; 1387 -4.3; 1526 -4.6; 1678 -4.6; 1846 -4.5; 2031 -4.0; 2234 -3.4; 2457 -3.0; 2703 -1.3; 2973 -0.5; 3270 -0.6; 3597 -0.7; 3957 -2.1; 4353 -3.4; 4788 -2.2; 5267 -1.7; 5793 -2.1; 6373 -4.5; 7010 -3.5; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Simgot EM5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Simgot EM5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 1.1  | 2.6 dB  |
| Peaking | 176 Hz  | 0.47 | -5.0 dB |
| Peaking | 905 Hz  | 1.68 | 3.3 dB  |
| Peaking | 3170 Hz | 2.13 | 4.8 dB  |
| Peaking | 5385 Hz | 3.81 | 2.9 dB  |
| Peaking | 599 Hz  | 4.29 | 0.2 dB  |
| Peaking | 9014 Hz | 3.88 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Simgot%20EM5/Simgot%20EM5.png)