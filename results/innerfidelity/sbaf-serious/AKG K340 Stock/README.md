# AKG K340 Stock
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.4; 72 -2.3; 79 -3.3; 87 -4.4; 96 -5.3; 106 -6.1; 116 -6.7; 128 -7.4; 141 -7.9; 155 -8.2; 170 -8.4; 187 -8.8; 206 -9.0; 227 -9.0; 249 -9.1; 274 -9.1; 302 -9.0; 332 -8.8; 365 -8.4; 402 -8.2; 442 -7.5; 486 -6.8; 535 -5.6; 588 -4.7; 647 -4.4; 712 -4.2; 783 -3.4; 861 -4.4; 947 -5.3; 1042 -5.9; 1146 -3.1; 1261 -0.7; 1387 -4.2; 1526 -6.7; 1678 -7.0; 1846 -6.9; 2031 -6.6; 2234 -9.6; 2457 -10.4; 2703 -8.5; 2973 -5.8; 3270 -4.1; 3597 -3.3; 3957 -4.1; 4353 -2.7; 4788 -3.5; 5267 -2.9; 5793 -4.4; 6373 -6.1; 7010 -4.1; 7711 -6.8; 8482 -12.5; 9330 -13.6; 10263 -9.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.1; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K340 Stock GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K340 Stock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.91 | 7.3 dB  |
| Peaking | 1236 Hz | 8.07 | 5.8 dB  |
| Peaking | 2440 Hz | 2.44 | -7.4 dB |
| Peaking | 3742 Hz | 0.59 | 4.5 dB  |
| Peaking | 9013 Hz | 3.83 | -9.7 dB |
| Peaking | 37 Hz   | 1.44 | -7.1 dB |
| Peaking | 44 Hz   | 0.48 | 6.9 dB  |
| Peaking | 177 Hz  | 0.37 | -4.3 dB |
| Peaking | 667 Hz  | 1.67 | 3.8 dB  |
| Peaking | 1594 Hz | 7.64 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K340%20Stock/AKG%20K340%20Stock.png)