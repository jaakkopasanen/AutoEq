# Cowin E8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.1; 25 -2.4; 28 -3.0; 31 -3.5; 34 -4.1; 37 -4.6; 41 -5.3; 45 -5.9; 49 -6.5; 54 -7.1; 60 -7.8; 66 -8.4; 72 -9.0; 79 -9.5; 87 -10.1; 96 -10.6; 106 -11.1; 116 -11.4; 128 -11.7; 141 -11.8; 155 -11.7; 170 -11.5; 187 -11.1; 206 -10.7; 227 -10.3; 249 -9.9; 274 -9.0; 302 -8.6; 332 -8.5; 365 -8.3; 402 -8.2; 442 -8.1; 486 -8.3; 535 -8.4; 588 -8.7; 647 -9.1; 712 -9.1; 783 -6.5; 861 -3.9; 947 -7.6; 1042 -9.6; 1146 -7.6; 1261 -5.3; 1387 -3.1; 1526 -1.5; 1678 -2.2; 1846 -2.0; 2031 -1.1; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.6; 3597 -0.7; 3957 -0.9; 4353 -2.0; 4788 -5.5; 5267 -14.3; 5793 -13.9; 6373 -7.3; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 0.24 | 6.4 dB   |
| Peaking | 104 Hz  | 0.38 | -7.1 dB  |
| Peaking | 2047 Hz | 1.59 | 4.3 dB   |
| Peaking | 3954 Hz | 1.13 | 6.6 dB   |
| Peaking | 5469 Hz | 5.01 | -14.7 dB |
| Peaking | 314 Hz  | 2.26 | 1.2 dB   |
| Peaking | 706 Hz  | 2.84 | -3.0 dB  |
| Peaking | 855 Hz  | 4.9  | 5.6 dB   |
| Peaking | 1021 Hz | 4.07 | -4.8 dB  |
| Peaking | 1469 Hz | 6.02 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20E8/Cowin%20E8.png)