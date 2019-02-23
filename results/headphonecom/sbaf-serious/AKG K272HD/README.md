# AKG K272HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.1; 54 -1.9; 60 -3.4; 66 -4.7; 72 -5.4; 79 -5.3; 87 -4.6; 96 -3.7; 106 -4.6; 116 -6.4; 128 -7.5; 141 -8.2; 155 -8.7; 170 -8.1; 187 -7.6; 206 -7.2; 227 -7.4; 249 -7.4; 274 -7.6; 302 -7.5; 332 -7.5; 365 -7.8; 402 -8.1; 442 -8.2; 486 -8.2; 535 -8.4; 588 -8.9; 647 -10.1; 712 -7.6; 783 -6.5; 861 -6.1; 947 -6.4; 1042 -7.0; 1146 -7.6; 1261 -8.2; 1387 -9.0; 1526 -10.2; 1678 -10.8; 1846 -10.1; 2031 -6.4; 2234 -3.5; 2457 -3.0; 2703 -3.8; 2973 -3.9; 3270 -3.9; 3597 -2.5; 3957 -1.9; 4353 -2.7; 4788 -2.0; 5267 -0.5; 5793 -0.5; 6373 -3.4; 7010 -4.1; 7711 -6.2; 8482 -9.4; 9330 -13.5; 10263 -10.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K272HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K272HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 32 Hz   | 0.7  | 6.8 dB   |
| Peaking | 1889 Hz | 0.48 | -39.7 dB |
| Peaking | 2061 Hz | 0.46 | 37.7 dB  |
| Peaking | 5328 Hz | 1.08 | 5.4 dB   |
| Peaking | 9314 Hz | 3.54 | -9.2 dB  |
| Peaking | 73 Hz   | 4.97 | -1.4 dB  |
| Peaking | 99 Hz   | 4.34 | 2.4 dB   |
| Peaking | 147 Hz  | 3.03 | -2.0 dB  |
| Peaking | 643 Hz  | 4.28 | -3.1 dB  |
| Peaking | 824 Hz  | 2.48 | 2.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K272HD/AKG%20K272HD.png)