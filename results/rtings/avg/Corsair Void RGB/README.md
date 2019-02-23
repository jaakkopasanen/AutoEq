# Corsair Void RGB
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.4; 34 -2.4; 37 -3.4; 41 -4.8; 45 -6.1; 49 -7.1; 54 -8.2; 60 -9.2; 66 -9.9; 72 -10.2; 79 -10.4; 87 -10.4; 96 -10.2; 106 -9.8; 116 -9.4; 128 -9.0; 141 -8.6; 155 -8.2; 170 -7.7; 187 -7.2; 206 -6.6; 227 -6.2; 249 -7.8; 274 -6.6; 302 -6.0; 332 -5.7; 365 -5.5; 402 -5.7; 442 -6.1; 486 -6.0; 535 -6.0; 588 -5.9; 647 -5.9; 712 -6.2; 783 -7.0; 861 -8.2; 947 -10.1; 1042 -11.2; 1146 -10.4; 1261 -8.8; 1387 -9.1; 1526 -8.0; 1678 -6.6; 1846 -5.5; 2031 -5.0; 2234 -3.9; 2457 -2.8; 2703 -2.2; 2973 -2.4; 3270 -3.1; 3597 -3.7; 3957 -3.6; 4353 -4.2; 4788 -5.6; 5267 -7.4; 5793 -8.7; 6373 -11.2; 7010 -10.1; 7711 -6.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair Void RGB GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair Void RGB ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.02 | 7.0 dB  |
| Peaking | 78 Hz   | 1.02 | -5.1 dB |
| Peaking | 1109 Hz | 2.52 | -5.1 dB |
| Peaking | 2946 Hz | 1.33 | 4.5 dB  |
| Peaking | 6506 Hz | 4.19 | -5.8 dB |
| Peaking | 257 Hz  | 8.2  | -1.3 dB |
| Peaking | 340 Hz  | 1.57 | 1.2 dB  |
| Peaking | 639 Hz  | 3.84 | 1.0 dB  |
| Peaking | 1479 Hz | 6.12 | -1.4 dB |
| Peaking | 2430 Hz | 7.61 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.8 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Corsair%20Void%20RGB/Corsair%20Void%20RGB.png)