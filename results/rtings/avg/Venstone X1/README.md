# Venstone X1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -9.3; 25 -9.8; 28 -10.3; 31 -10.8; 34 -11.2; 37 -11.5; 41 -12.0; 45 -12.4; 49 -12.7; 54 -13.1; 60 -13.6; 66 -14.1; 72 -14.5; 79 -14.9; 87 -15.3; 96 -15.8; 106 -16.3; 116 -16.7; 128 -17.1; 141 -17.3; 155 -17.4; 170 -17.3; 187 -17.2; 206 -17.0; 227 -16.6; 249 -16.3; 274 -16.2; 302 -16.1; 332 -15.7; 365 -15.2; 402 -14.4; 442 -13.4; 486 -12.3; 535 -11.1; 588 -10.0; 647 -9.0; 712 -8.4; 783 -8.1; 861 -7.5; 947 -6.8; 1042 -6.1; 1146 -5.4; 1261 -4.5; 1387 -3.4; 1526 -2.1; 1678 -0.9; 1846 -0.5; 2031 -1.6; 2234 -3.5; 2457 -5.4; 2703 -5.7; 2973 -5.6; 3270 -6.1; 3597 -7.3; 3957 -9.1; 4353 -10.5; 4788 -13.3; 5267 -17.6; 5793 -15.1; 6373 -9.6; 7010 -6.6; 7711 -9.4; 8482 -12.3; 9330 -7.8; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -8.4; 15026 -10.4; 16529 -13.1; 18182 -13.6; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venstone X1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venstone X1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 124 Hz   | 0.36 | -9.8 dB  |
| Peaking | 322 Hz   | 1.01 | -3.8 dB  |
| Peaking | 1737 Hz  | 1.67 | 6.6 dB   |
| Peaking | 5305 Hz  | 3.25 | -11.5 dB |
| Peaking | 17586 Hz | 1.14 | -8.2 dB  |
| Peaking | 28 Hz    | 2.07 | -0.9 dB  |
| Peaking | 5841 Hz  | 6.93 | -1.5 dB  |
| Peaking | 6926 Hz  | 4.51 | 3.5 dB   |
| Peaking | 8455 Hz  | 4.08 | -7.0 dB  |
| Peaking | 9955 Hz  | 1.75 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -8.6 dB |
| Peaking | 250 Hz   | 1.41 | -8.9 dB |
| Peaking | 500 Hz   | 1.41 | -4.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.7 dB |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -6.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Venstone%20X1/Venstone%20X1.png)