# Corsair Void RGB
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.2; 34 -2.2; 37 -3.2; 41 -4.6; 45 -5.9; 49 -7.0; 54 -8.0; 60 -9.0; 66 -9.7; 72 -10.0; 79 -10.2; 87 -10.2; 96 -10.0; 106 -9.6; 116 -9.2; 128 -8.8; 141 -8.4; 155 -8.0; 170 -7.5; 187 -7.0; 206 -6.4; 227 -6.3; 249 -7.5; 274 -6.7; 302 -6.0; 332 -5.6; 365 -5.5; 402 -5.6; 442 -6.1; 486 -6.1; 535 -6.0; 588 -5.9; 647 -6.0; 712 -6.4; 783 -7.2; 861 -8.3; 947 -10.2; 1042 -11.3; 1146 -10.5; 1261 -9.1; 1387 -9.2; 1526 -8.2; 1678 -6.8; 1846 -5.9; 2031 -5.4; 2234 -4.7; 2457 -3.7; 2703 -2.8; 2973 -2.5; 3270 -2.8; 3597 -3.5; 3957 -3.2; 4353 -3.9; 4788 -6.1; 5267 -7.8; 5793 -8.6; 6373 -10.3; 7010 -10.2; 7711 -7.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair Void RGB GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair Void RGB ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.99 | 7.0 dB  |
| Peaking | 76 Hz   | 1.06 | -4.9 dB |
| Peaking | 1107 Hz | 2.49 | -5.1 dB |
| Peaking | 3178 Hz | 1.32 | 4.4 dB  |
| Peaking | 6431 Hz | 3.03 | -4.9 dB |
| Peaking | 360 Hz  | 3.36 | 1.2 dB  |
| Peaking | 937 Hz  | 1.12 | 2.1 dB  |
| Peaking | 950 Hz  | 3.45 | -2.8 dB |
| Peaking | 1472 Hz | 4.58 | -2.1 dB |
| Peaking | 8124 Hz | 8.98 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Corsair%20Void%20RGB/Corsair%20Void%20RGB.png)