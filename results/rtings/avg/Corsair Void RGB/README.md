# Corsair Void RGB
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.6; 49 -2.7; 54 -3.8; 60 -4.8; 66 -5.4; 72 -5.8; 79 -6.0; 87 -6.0; 96 -5.8; 106 -5.4; 116 -5.0; 128 -4.6; 141 -4.2; 155 -3.8; 170 -3.3; 187 -2.7; 206 -2.1; 227 -1.8; 249 -3.4; 274 -2.2; 302 -1.6; 332 -1.3; 365 -1.1; 402 -1.3; 442 -1.7; 486 -1.6; 535 -1.6; 588 -1.5; 647 -1.5; 712 -1.8; 783 -2.6; 861 -3.8; 947 -5.7; 1042 -6.8; 1146 -6.0; 1261 -4.3; 1387 -4.7; 1526 -3.6; 1678 -2.2; 1846 -1.1; 2031 -0.6; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.2; 5267 -2.9; 5793 -4.2; 6373 -6.7; 7010 -5.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair Void RGB GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair Void RGB ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.01 | 6.8 dB  |
| Peaking | 198 Hz  | 1.81 | 3.1 dB  |
| Peaking | 372 Hz  | 1.5  | 4.6 dB  |
| Peaking | 635 Hz  | 2.68 | 3.7 dB  |
| Peaking | 2957 Hz | 0.88 | 6.8 dB  |
| Peaking | 16 Hz   | 2.3  | 2.0 dB  |
| Peaking | 1058 Hz | 6.48 | -2.5 dB |
| Peaking | 1928 Hz | 3.31 | 2.1 dB  |
| Peaking | 4606 Hz | 2.05 | 5.6 dB  |
| Peaking | 4797 Hz | 0.85 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 3.6 dB  |
| Peaking | 500 Hz   | 1.41 | 5.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Corsair%20Void%20RGB/Corsair%20Void%20RGB.png)