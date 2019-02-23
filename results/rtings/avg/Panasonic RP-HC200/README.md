# Panasonic RP-HC200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.7; 60 -1.3; 66 -1.3; 72 -2.0; 79 -3.0; 87 -3.8; 96 -4.6; 106 -5.3; 116 -5.9; 128 -6.4; 141 -6.6; 155 -6.6; 170 -6.6; 187 -6.7; 206 -6.5; 227 -6.4; 249 -6.3; 274 -6.3; 302 -5.8; 332 -5.4; 365 -5.4; 402 -5.4; 442 -5.6; 486 -6.1; 535 -7.0; 588 -8.0; 647 -9.3; 712 -10.5; 783 -11.3; 861 -11.6; 947 -11.1; 1042 -10.9; 1146 -10.5; 1261 -9.3; 1387 -9.3; 1526 -8.7; 1678 -7.4; 1846 -6.0; 2031 -4.8; 2234 -3.6; 2457 -4.0; 2703 -4.2; 2973 -4.2; 3270 -4.6; 3597 -3.3; 3957 -1.2; 4353 -0.5; 4788 -0.5; 5267 -0.8; 5793 -4.7; 6373 -6.3; 7010 -5.0; 7711 -9.5; 8482 -14.0; 9330 -10.0; 10263 -6.5; 11289 -6.5; 12418 -7.3; 13660 -12.6; 15026 -16.0; 16529 -13.2; 18182 -6.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.64 | 6.8 dB   |
| Peaking | 934 Hz   | 1.6  | -5.6 dB  |
| Peaking | 4447 Hz  | 1.24 | 6.0 dB   |
| Peaking | 8429 Hz  | 5.25 | -9.0 dB  |
| Peaking | 15292 Hz | 2.13 | -10.7 dB |
| Peaking | 142 Hz   | 2.38 | -1.2 dB  |
| Peaking | 401 Hz   | 2.03 | 2.1 dB   |
| Peaking | 2229 Hz  | 4.26 | 2.8 dB   |
| Peaking | 3165 Hz  | 0.09 | -0.5 dB  |
| Peaking | 11181 Hz | 2.93 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -8.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC200/Panasonic%20RP-HC200.png)