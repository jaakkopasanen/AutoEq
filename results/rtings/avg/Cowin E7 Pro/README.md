# Cowin E7 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.9; 37 -2.1; 41 -4.0; 45 -5.5; 49 -6.6; 54 -7.5; 60 -8.6; 66 -9.8; 72 -10.1; 79 -9.1; 87 -8.2; 96 -7.7; 106 -7.5; 116 -7.4; 128 -7.4; 141 -7.3; 155 -7.1; 170 -6.9; 187 -6.6; 206 -6.2; 227 -5.7; 249 -5.4; 274 -5.0; 302 -4.3; 332 -3.1; 365 -1.8; 402 -0.9; 442 -1.6; 486 -2.9; 535 -3.5; 588 -3.4; 647 -3.2; 712 -3.6; 783 -3.8; 861 -4.9; 947 -6.3; 1042 -7.8; 1146 -9.5; 1261 -11.7; 1387 -13.2; 1526 -13.9; 1678 -13.3; 1846 -11.1; 2031 -9.3; 2234 -7.2; 2457 -4.5; 2703 -2.7; 2973 -1.7; 3270 -1.7; 3597 -2.3; 3957 -3.7; 4353 -5.8; 4788 -7.5; 5267 -8.9; 5793 -7.1; 6373 -8.6; 7010 -10.5; 7711 -10.0; 8482 -10.7; 9330 -12.2; 10263 -11.6; 11289 -9.3; 12418 -8.0; 13660 -10.1; 15026 -14.3; 16529 -14.6; 18182 -12.0; 20000 -13.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 2.21 | 7.2 dB  |
| Peaking | 462 Hz   | 1.2  | 5.0 dB  |
| Peaking | 1483 Hz  | 3.01 | -8.7 dB |
| Peaking | 9034 Hz  | 2.48 | -4.6 dB |
| Peaking | 17161 Hz | 0.75 | -8.0 dB |
| Peaking | 38 Hz    | 2.85 | 3.0 dB  |
| Peaking | 69 Hz    | 1.25 | -3.6 dB |
| Peaking | 788 Hz   | 3.74 | 2.1 dB  |
| Peaking | 2933 Hz  | 0.57 | -4.2 dB |
| Peaking | 3130 Hz  | 1.62 | 10.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 5.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | -9.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20E7%20Pro/Cowin%20E7%20Pro.png)