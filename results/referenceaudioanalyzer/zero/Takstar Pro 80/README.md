# Takstar Pro 80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.7; 25 -6.2; 28 -7.0; 31 -7.8; 34 -8.4; 37 -8.8; 41 -9.0; 45 -9.1; 49 -9.1; 54 -9.1; 60 -9.2; 66 -9.2; 72 -9.0; 79 -8.9; 87 -8.9; 96 -8.9; 106 -9.3; 116 -9.6; 128 -9.8; 141 -9.8; 155 -9.4; 170 -8.6; 187 -7.7; 206 -6.7; 227 -5.8; 249 -5.1; 274 -4.6; 302 -4.3; 332 -4.0; 365 -4.0; 402 -4.0; 442 -4.0; 486 -4.0; 535 -4.0; 588 -4.0; 647 -4.0; 712 -4.2; 783 -4.3; 861 -4.3; 947 -3.9; 1042 -3.7; 1146 -3.7; 1261 -3.7; 1387 -3.7; 1526 -4.2; 1678 -5.0; 1846 -6.0; 2031 -6.9; 2234 -7.7; 2457 -8.2; 2703 -7.8; 2973 -6.9; 3270 -5.4; 3597 -2.6; 3957 -0.5; 4353 -6.6; 4788 -10.9; 5267 -11.7; 5793 -10.8; 6373 -10.2; 7010 -8.7; 7711 -6.0; 8482 -5.7; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Takstar Pro 80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Takstar Pro 80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 0.85 | -3.5 dB |
| Peaking | 139 Hz  | 1.28 | -4.9 dB |
| Peaking | 957 Hz  | 0.11 | 2.4 dB  |
| Peaking | 2349 Hz | 2.71 | -4.8 dB |
| Peaking | 5633 Hz | 2.63 | -8.0 dB |
| Peaking | 771 Hz  | 3.51 | -0.8 dB |
| Peaking | 3020 Hz | 3.94 | -1.9 dB |
| Peaking | 3926 Hz | 4.69 | 6.8 dB  |
| Peaking | 4427 Hz | 6.06 | -2.1 dB |
| Peaking | 4767 Hz | 7.12 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Takstar%20Pro%2080/Takstar%20Pro%2080.png)