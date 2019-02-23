# Shure SE310
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.2; 25 -3.3; 28 -3.4; 31 -3.5; 34 -3.6; 37 -3.7; 41 -3.9; 45 -4.2; 49 -4.3; 54 -4.5; 60 -4.8; 66 -5.2; 72 -5.7; 79 -6.0; 87 -6.3; 96 -6.6; 106 -6.8; 116 -7.1; 128 -7.4; 141 -7.7; 155 -7.9; 170 -8.1; 187 -8.2; 206 -8.3; 227 -8.3; 249 -8.3; 274 -8.3; 302 -8.2; 332 -8.1; 365 -7.9; 402 -7.8; 442 -7.6; 486 -7.4; 535 -7.2; 588 -7.1; 647 -7.0; 712 -7.0; 783 -7.2; 861 -7.5; 947 -8.1; 1042 -8.8; 1146 -9.5; 1261 -10.3; 1387 -11.2; 1526 -12.1; 1678 -12.6; 1846 -12.6; 2031 -12.2; 2234 -11.1; 2457 -9.1; 2703 -6.4; 2973 -3.3; 3270 -0.6; 3597 -0.5; 3957 -0.7; 4353 -3.5; 4788 -3.4; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE310 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE310 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.5  | 3.3 dB  |
| Peaking | 205 Hz  | 0.78 | -2.1 dB |
| Peaking | 1869 Hz | 1.22 | -7.5 dB |
| Peaking | 3421 Hz | 2.2  | 8.3 dB  |
| Peaking | 5850 Hz | 3.29 | 6.1 dB  |
| Peaking | 758 Hz  | 2.65 | 0.7 dB  |
| Peaking | 1270 Hz | 3.46 | -0.5 dB |
| Peaking | 8181 Hz | 4.91 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE310/Shure%20SE310.png)