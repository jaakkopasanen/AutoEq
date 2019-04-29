# Simgot EM5H
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.5; 25 -2.9; 28 -3.4; 31 -3.9; 34 -4.2; 37 -4.5; 41 -4.9; 45 -5.2; 49 -5.5; 54 -5.8; 60 -6.1; 66 -6.6; 72 -7.0; 79 -7.4; 87 -7.9; 96 -8.4; 106 -8.9; 116 -9.3; 128 -9.7; 141 -10.0; 155 -10.3; 170 -10.5; 187 -10.7; 206 -10.8; 227 -10.9; 249 -10.9; 274 -10.9; 302 -10.8; 332 -10.8; 365 -10.7; 402 -10.6; 442 -10.5; 486 -10.3; 535 -10.1; 588 -9.9; 647 -9.6; 712 -9.1; 783 -8.6; 861 -8.1; 947 -7.6; 1042 -7.3; 1146 -7.4; 1261 -7.5; 1387 -7.5; 1526 -7.1; 1678 -6.6; 1846 -6.1; 2031 -5.9; 2234 -5.9; 2457 -6.2; 2703 -6.4; 2973 -5.0; 3270 -2.0; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.0; 5267 -5.4; 5793 -4.4; 6373 -2.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Simgot EM5H GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Simgot EM5H ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 0.27 | 5.1 dB  |
| Peaking | 255 Hz  | 0.38 | -4.7 dB |
| Peaking | 4138 Hz | 1.94 | 8.0 dB  |
| Peaking | 5844 Hz | 1.56 | -3.1 dB |
| Peaking | 6430 Hz | 4.95 | 5.8 dB  |
| Peaking | 602 Hz  | 3.01 | -0.4 dB |
| Peaking | 976 Hz  | 4.39 | 0.7 dB  |
| Peaking | 2118 Hz | 2.96 | 1.3 dB  |
| Peaking | 2785 Hz | 1.89 | -2.0 dB |
| Peaking | 3347 Hz | 6.34 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Simgot%20EM5H/Simgot%20EM5H.png)