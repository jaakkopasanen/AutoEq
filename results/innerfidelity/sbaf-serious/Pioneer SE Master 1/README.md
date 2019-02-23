# Pioneer SE Master 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.8; 28 -2.4; 31 -2.9; 34 -3.1; 37 -3.3; 41 -3.7; 45 -4.4; 49 -5.1; 54 -5.9; 60 -6.6; 66 -7.2; 72 -7.8; 79 -8.3; 87 -8.8; 96 -9.3; 106 -9.7; 116 -9.9; 128 -10.2; 141 -10.3; 155 -10.4; 170 -10.2; 187 -10.2; 206 -10.0; 227 -9.6; 249 -9.3; 274 -8.9; 302 -8.4; 332 -8.0; 365 -7.5; 402 -7.1; 442 -6.5; 486 -6.2; 535 -5.7; 588 -4.8; 647 -4.6; 712 -4.4; 783 -3.9; 861 -3.8; 947 -3.5; 1042 -3.1; 1146 -2.2; 1261 -1.2; 1387 -1.1; 1526 -1.6; 1678 -1.9; 1846 -2.8; 2031 -4.3; 2234 -5.5; 2457 -5.6; 2703 -6.0; 2973 -6.0; 3270 -4.4; 3597 -2.8; 3957 -2.6; 4353 -4.7; 4788 -6.5; 5267 -7.6; 5793 -12.7; 6373 -13.5; 7010 -7.6; 7711 -6.2; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.9; 18182 -12.6; 20000 -14.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer SE Master 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE Master 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 15 Hz   | 0.43 | 6.5 dB   |
| Peaking | 143 Hz  | 0.62 | -4.7 dB  |
| Peaking | 1277 Hz | 1.11 | 5.1 dB   |
| Peaking | 3827 Hz | 5.22 | 4.1 dB   |
| Peaking | 6074 Hz | 6.69 | -10.2 dB |
| Peaking | 621 Hz  | 3.04 | 1.1 dB   |
| Peaking | 1048 Hz | 4.54 | -1.0 dB  |
| Peaking | 1720 Hz | 2.32 | 1.3 dB   |
| Peaking | 2421 Hz | 1.84 | -1.5 dB  |
| Peaking | 3431 Hz | 9.83 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20SE%20Master%201/Pioneer%20SE%20Master%201.png)