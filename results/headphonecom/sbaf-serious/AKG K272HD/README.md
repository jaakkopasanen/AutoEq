# AKG K272HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -0.9; 54 -1.7; 60 -3.2; 66 -4.5; 72 -5.2; 79 -5.1; 87 -4.4; 96 -3.5; 106 -4.4; 116 -6.2; 128 -7.3; 141 -8.0; 155 -8.5; 170 -7.9; 187 -7.4; 206 -7.0; 227 -7.2; 249 -7.2; 274 -7.4; 302 -7.3; 332 -7.3; 365 -7.6; 402 -7.9; 442 -8.0; 486 -8.0; 535 -8.2; 588 -8.7; 647 -9.9; 712 -7.4; 783 -6.3; 861 -5.9; 947 -6.2; 1042 -6.8; 1146 -7.4; 1261 -8.0; 1387 -8.8; 1526 -10.0; 1678 -10.6; 1846 -9.9; 2031 -6.2; 2234 -3.3; 2457 -2.8; 2703 -3.6; 2973 -3.7; 3270 -3.7; 3597 -2.3; 3957 -1.7; 4353 -2.5; 4788 -1.8; 5267 -0.5; 5793 -0.5; 6373 -3.2; 7010 -4.1; 7711 -6.2; 8482 -9.2; 9330 -13.3; 10263 -10.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K272HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K272HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.87 | 6.9 dB  |
| Peaking | 1830 Hz | 1.76 | -8.9 dB |
| Peaking | 2205 Hz | 2.27 | 8.0 dB  |
| Peaking | 5167 Hz | 0.99 | 5.9 dB  |
| Peaking | 9329 Hz | 3.56 | -9.0 dB |
| Peaking | 99 Hz   | 5.18 | 2.6 dB  |
| Peaking | 149 Hz  | 2.26 | -2.3 dB |
| Peaking | 513 Hz  | 1    | -2.0 dB |
| Peaking | 656 Hz  | 4.93 | -4.0 dB |
| Peaking | 758 Hz  | 1.69 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K272HD/AKG%20K272HD.png)