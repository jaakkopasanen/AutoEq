# Corsair HS50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.5; 25 -3.9; 28 -4.3; 31 -4.7; 34 -5.0; 37 -5.3; 41 -5.6; 45 -5.9; 49 -6.0; 54 -6.1; 60 -6.3; 66 -6.7; 72 -7.1; 79 -7.5; 87 -7.9; 96 -8.2; 106 -8.4; 116 -8.6; 128 -8.6; 141 -8.5; 155 -8.3; 170 -7.8; 187 -7.1; 206 -6.4; 227 -5.4; 249 -4.6; 274 -4.0; 302 -3.1; 332 -2.5; 365 -2.1; 402 -2.1; 442 -2.5; 486 -3.1; 535 -3.7; 588 -4.2; 647 -4.5; 712 -4.8; 783 -4.9; 861 -4.1; 947 -2.1; 1042 -2.5; 1146 -2.7; 1261 -2.1; 1387 -2.3; 1526 -2.6; 1678 -2.5; 1846 -2.7; 2031 -2.9; 2234 -2.8; 2457 -2.8; 2703 -2.7; 2973 -2.3; 3270 -2.0; 3597 -3.0; 3957 -2.0; 4353 -1.5; 4788 -3.5; 5267 -7.5; 5793 -5.2; 6373 -0.5; 7010 -1.7; 7711 -5.7; 8482 -10.7; 9330 -9.1; 10263 -6.8; 11289 -8.7; 12418 -9.8; 13660 -6.1; 15026 -4.2; 16529 -4.2; 18182 -4.3; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair HS50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair HS50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 95 Hz    | 0.9  | -4.2 dB |
| Peaking | 159 Hz   | 1.78 | -3.2 dB |
| Peaking | 1360 Hz  | 0.06 | 1.5 dB  |
| Peaking | 8723 Hz  | 5.29 | -7.8 dB |
| Peaking | 12064 Hz | 2.61 | -6.7 dB |
| Peaking | 17 Hz    | 2.32 | 1.3 dB  |
| Peaking | 374 Hz   | 3.27 | 1.6 dB  |
| Peaking | 699 Hz   | 3.2  | -2.2 dB |
| Peaking | 5358 Hz  | 8.04 | -5.5 dB |
| Peaking | 6518 Hz  | 6.61 | 4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Corsair%20HS50/Corsair%20HS50.png)