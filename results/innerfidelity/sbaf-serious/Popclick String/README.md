# Popclick String
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.6; 23 -14.6; 25 -14.6; 28 -14.6; 31 -14.5; 34 -14.4; 37 -14.3; 41 -14.2; 45 -14.1; 49 -14.0; 54 -13.9; 60 -13.7; 66 -13.7; 72 -13.6; 79 -13.5; 87 -13.4; 96 -13.3; 106 -13.0; 116 -12.7; 128 -12.5; 141 -12.1; 155 -11.8; 170 -11.3; 187 -10.8; 206 -10.2; 227 -9.6; 249 -9.0; 274 -8.3; 302 -7.7; 332 -7.0; 365 -6.3; 402 -5.7; 442 -5.0; 486 -4.6; 535 -4.1; 588 -3.6; 647 -3.5; 712 -3.5; 783 -3.1; 861 -3.0; 947 -3.6; 1042 -4.1; 1146 -4.5; 1261 -5.1; 1387 -6.2; 1526 -7.4; 1678 -8.4; 1846 -9.0; 2031 -9.6; 2234 -10.2; 2457 -9.9; 2703 -8.1; 2973 -4.8; 3270 -1.9; 3597 -0.5; 3957 -1.1; 4353 -4.0; 4788 -6.5; 5267 -10.0; 5793 -12.5; 6373 -6.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Popclick String GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Popclick String ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.21 | -8.0 dB  |
| Peaking | 145 Hz  | 0.76 | -3.0 dB  |
| Peaking | 2000 Hz | 1.22 | -13.0 dB |
| Peaking | 2048 Hz | 0.36 | 9.0 dB   |
| Peaking | 5603 Hz | 5.31 | -10.5 dB |
| Peaking | 1417 Hz | 1.61 | -4.3 dB  |
| Peaking | 1701 Hz | 0.95 | 4.0 dB   |
| Peaking | 2523 Hz | 3.38 | -4.4 dB  |
| Peaking | 3525 Hz | 4.86 | 3.6 dB   |
| Peaking | 9699 Hz | 1.44 | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Popclick%20String/Popclick%20String.png)