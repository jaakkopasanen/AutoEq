# Panasonic RP-HC56
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.7; 25 -6.9; 28 -7.2; 31 -7.4; 34 -7.5; 37 -7.6; 41 -7.6; 45 -7.6; 49 -7.6; 54 -7.6; 60 -7.5; 66 -7.4; 72 -7.4; 79 -7.3; 87 -7.2; 96 -7.0; 106 -6.8; 116 -6.6; 128 -6.3; 141 -5.9; 155 -5.6; 170 -5.2; 187 -4.9; 206 -4.7; 227 -4.7; 249 -4.8; 274 -5.1; 302 -5.6; 332 -6.2; 365 -7.1; 402 -8.0; 442 -9.0; 486 -10.1; 535 -10.9; 588 -11.4; 647 -11.0; 712 -9.9; 783 -8.4; 861 -7.3; 947 -7.2; 1042 -7.6; 1146 -8.0; 1261 -7.5; 1387 -6.8; 1526 -6.1; 1678 -5.2; 1846 -4.3; 2031 -3.5; 2234 -2.5; 2457 -1.3; 2703 -0.6; 2973 -0.5; 3270 -0.9; 3597 -1.7; 3957 -1.9; 4353 -2.1; 4788 -3.6; 5267 -6.7; 5793 -8.7; 6373 -7.4; 7010 -7.5; 7711 -10.9; 8482 -15.0; 9330 -17.3; 10263 -18.6; 11289 -17.2; 12418 -14.4; 13660 -12.7; 15026 -10.1; 16529 -9.4; 18182 -9.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC56 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC56 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 250 Hz   | 1.41 | 2.7 dB   |
| Peaking | 577 Hz   | 1.28 | -5.1 dB  |
| Peaking | 3244 Hz  | 1.04 | 7.0 dB   |
| Peaking | 10380 Hz | 1.28 | -12.9 dB |
| Peaking | 17759 Hz | 1.77 | -2.7 dB  |
| Peaking | 50 Hz    | 0.95 | -1.3 dB  |
| Peaking | 872 Hz   | 4.74 | 1.4 dB   |
| Peaking | 1207 Hz  | 3.32 | -1.6 dB  |
| Peaking | 6907 Hz  | 2.11 | -3.0 dB  |
| Peaking | 6969 Hz  | 4.73 | 5.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB   |
| Peaking | 250 Hz   | 1.41 | 3.1 dB   |
| Peaking | 500 Hz   | 1.41 | -4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -10.0 dB |
| Peaking | 16000 Hz | 1.41 | -6.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC56/Panasonic%20RP-HC56.png)