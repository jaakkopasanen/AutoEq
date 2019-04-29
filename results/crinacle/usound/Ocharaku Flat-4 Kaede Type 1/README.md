# Ocharaku Flat-4 Kaede Type 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.5; 25 -3.0; 28 -3.6; 31 -4.1; 34 -4.6; 37 -4.9; 41 -5.4; 45 -5.8; 49 -6.1; 54 -6.3; 60 -6.6; 66 -7.0; 72 -7.4; 79 -7.8; 87 -8.2; 96 -8.9; 106 -9.2; 116 -9.5; 128 -9.7; 141 -9.9; 155 -10.2; 170 -10.2; 187 -10.1; 206 -10.0; 227 -9.8; 249 -9.6; 274 -9.4; 302 -9.1; 332 -8.6; 365 -8.1; 402 -7.7; 442 -7.3; 486 -7.1; 535 -6.5; 588 -6.0; 647 -5.5; 712 -5.1; 783 -4.9; 861 -4.8; 947 -4.9; 1042 -5.4; 1146 -6.1; 1261 -6.5; 1387 -5.9; 1526 -4.2; 1678 -1.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -3.3; 3270 -5.1; 3597 -4.3; 3957 -3.9; 4353 -4.4; 4788 -7.2; 5267 -9.7; 5793 -1.3; 6373 -1.4; 7010 -12.8; 7711 -19.8; 8482 -15.4; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -7.6; 13660 -7.0; 15026 -6.5; 16529 -7.1; 18182 -12.0; 20000 -14.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Flat-4 Kaede Type 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Flat-4 Kaede Type 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 19 Hz   |  0.82 | 4.7 dB   |
| Peaking | 165 Hz  |  0.75 | -4.0 dB  |
| Peaking | 2209 Hz |  1.46 | 6.8 dB   |
| Peaking | 6236 Hz |  6.92 | 10.0 dB  |
| Peaking | 7709 Hz |  4.28 | -15.8 dB |
| Peaking | 789 Hz  |  2.16 | 1.7 dB   |
| Peaking | 1291 Hz |  5.04 | -2.2 dB  |
| Peaking | 4187 Hz |  5.84 | 1.7 dB   |
| Peaking | 5108 Hz | 11.33 | -4.9 dB  |
| Peaking | 9713 Hz |  7.31 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ocharaku%20Flat-4%20Kaede%20Type%201/Ocharaku%20Flat-4%20Kaede%20Type%201.png)