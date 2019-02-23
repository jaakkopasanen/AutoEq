# Panasonic RP-HC56
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.0; 25 -2.2; 28 -2.5; 31 -2.7; 34 -2.8; 37 -2.9; 41 -2.9; 45 -3.0; 49 -3.0; 54 -3.0; 60 -3.3; 66 -3.5; 72 -3.6; 79 -3.7; 87 -3.9; 96 -4.1; 106 -4.4; 116 -4.6; 128 -4.8; 141 -4.9; 155 -4.9; 170 -4.8; 187 -4.8; 206 -4.9; 227 -5.0; 249 -5.1; 274 -5.4; 302 -5.9; 332 -6.5; 365 -7.3; 402 -8.2; 442 -9.2; 486 -10.3; 535 -11.1; 588 -11.5; 647 -11.1; 712 -9.9; 783 -8.5; 861 -7.4; 947 -7.3; 1042 -7.8; 1146 -8.1; 1261 -7.5; 1387 -7.0; 1526 -6.1; 1678 -5.2; 1846 -4.3; 2031 -3.3; 2234 -1.9; 2457 -0.6; 2703 -0.5; 2973 -0.6; 3270 -1.4; 3597 -2.3; 3957 -2.4; 4353 -2.7; 4788 -3.4; 5267 -6.5; 5793 -9.1; 6373 -8.6; 7010 -7.7; 7711 -10.3; 8482 -15.6; 9330 -19.2; 10263 -19.5; 11289 -16.8; 12418 -14.6; 13660 -13.9; 15026 -11.1; 16529 -10.0; 18182 -10.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC56 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC56 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.38 | 3.8 dB   |
| Peaking | 92 Hz    | 0.18 | 2.2 dB   |
| Peaking | 584 Hz   | 1.16 | -6.0 dB  |
| Peaking | 3292 Hz  | 0.89 | 7.0 dB   |
| Peaking | 10389 Hz | 1.06 | -13.5 dB |
| Peaking | 1308 Hz  | 3.54 | -1.6 dB  |
| Peaking | 2404 Hz  | 5.59 | 1.6 dB   |
| Peaking | 7201 Hz  | 4.36 | 6.7 dB   |
| Peaking | 7494 Hz  | 1.73 | -3.1 dB  |
| Peaking | 17910 Hz | 2.25 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB   |
| Peaking | 62 Hz    | 1.41 | 2.4 dB   |
| Peaking | 125 Hz   | 1.41 | 1.1 dB   |
| Peaking | 250 Hz   | 1.41 | 2.3 dB   |
| Peaking | 500 Hz   | 1.41 | -4.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -10.4 dB |
| Peaking | 16000 Hz | 1.41 | -7.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC56/Panasonic%20RP-HC56.png)