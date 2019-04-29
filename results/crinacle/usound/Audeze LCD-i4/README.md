# Audeze LCD-i4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.7; 28 -1.0; 31 -1.3; 34 -1.5; 37 -1.7; 41 -1.9; 45 -2.1; 49 -2.4; 54 -2.7; 60 -3.1; 66 -3.5; 72 -3.8; 79 -4.3; 87 -4.8; 96 -5.3; 106 -5.8; 116 -6.2; 128 -6.6; 141 -7.1; 155 -7.4; 170 -7.7; 187 -8.0; 206 -8.3; 227 -8.4; 249 -8.5; 274 -8.7; 302 -8.9; 332 -8.9; 365 -9.1; 402 -9.2; 442 -9.5; 486 -9.6; 535 -9.8; 588 -10.2; 647 -10.7; 712 -11.2; 783 -11.4; 861 -10.6; 947 -9.8; 1042 -10.1; 1146 -10.6; 1261 -11.2; 1387 -11.5; 1526 -12.0; 1678 -12.5; 1846 -11.1; 2031 -8.7; 2234 -5.2; 2457 -1.7; 2703 -1.5; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -6.6; 9330 -6.5; 10263 -7.4; 11289 -8.1; 12418 -7.8; 13660 -9.7; 15026 -13.0; 16529 -13.5; 18182 -10.7; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-i4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-i4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 26 Hz    |  0.46 | 5.8 dB  |
| Peaking | 811 Hz   |  0.35 | -4.9 dB |
| Peaking | 1701 Hz  |  1.76 | -8.4 dB |
| Peaking | 3119 Hz  |  0.58 | 9.7 dB  |
| Peaking | 16198 Hz |  0.79 | -7.2 dB |
| Peaking | 766 Hz   |  8.38 | -1.2 dB |
| Peaking | 2434 Hz  | 10.92 | 2.0 dB  |
| Peaking | 6082 Hz  |  2.33 | 6.6 dB  |
| Peaking | 6754 Hz  |  1.26 | -4.8 dB |
| Peaking | 12959 Hz |  3.75 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | -4.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 9.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -8.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Audeze%20LCD-i4/Audeze%20LCD-i4.png)