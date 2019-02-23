# V-Moda LP2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.6; 25 -11.0; 28 -11.4; 31 -11.7; 34 -12.0; 37 -12.2; 41 -12.3; 45 -12.5; 49 -12.6; 54 -12.7; 60 -12.9; 66 -13.0; 72 -12.9; 79 -12.5; 87 -12.6; 96 -13.9; 106 -14.5; 116 -14.6; 128 -14.5; 141 -14.7; 155 -14.6; 170 -14.1; 187 -14.2; 206 -13.5; 227 -12.6; 249 -11.2; 274 -10.5; 302 -8.6; 332 -6.6; 365 -5.1; 402 -4.2; 442 -3.3; 486 -2.7; 535 -2.4; 588 -3.0; 647 -4.3; 712 -5.9; 783 -7.1; 861 -7.6; 947 -7.7; 1042 -7.8; 1146 -7.7; 1261 -7.6; 1387 -8.0; 1526 -7.9; 1678 -7.7; 1846 -7.0; 2031 -6.5; 2234 -7.1; 2457 -8.5; 2703 -8.9; 2973 -9.9; 3270 -8.5; 3597 -6.3; 3957 -4.3; 4353 -3.0; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.4; 10263 -8.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda LP2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda LP2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 1.64 | -1.8 dB  |
| Peaking | 37 Hz   | 1.65 | -1.7 dB  |
| Peaking | 297 Hz  | 0.24 | -15.2 dB |
| Peaking | 467 Hz  | 0.67 | 18.4 dB  |
| Peaking | 5373 Hz | 2.4  | 7.6 dB   |
| Peaking | 84 Hz   | 6.14 | 1.6 dB   |
| Peaking | 2013 Hz | 3.59 | 1.9 dB   |
| Peaking | 3023 Hz | 2.98 | -3.4 dB  |
| Peaking | 4018 Hz | 2.79 | 1.7 dB   |
| Peaking | 9980 Hz | 5.4  | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -7.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | 6.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20LP2/V-Moda%20LP2.png)