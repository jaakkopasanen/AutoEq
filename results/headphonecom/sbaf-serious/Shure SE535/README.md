# Shure SE535
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.4; 25 -3.5; 28 -3.6; 31 -3.7; 34 -3.8; 37 -3.9; 41 -4.1; 45 -4.2; 49 -4.4; 54 -4.6; 60 -4.9; 66 -5.2; 72 -5.7; 79 -6.0; 87 -6.3; 96 -6.6; 106 -6.9; 116 -7.1; 128 -7.4; 141 -7.7; 155 -8.0; 170 -8.1; 187 -8.3; 206 -8.4; 227 -8.4; 249 -8.4; 274 -8.4; 302 -8.3; 332 -8.2; 365 -7.8; 402 -7.7; 442 -7.6; 486 -7.5; 535 -7.1; 588 -6.9; 647 -6.7; 712 -6.5; 783 -6.3; 861 -6.3; 947 -6.5; 1042 -6.7; 1146 -6.8; 1261 -6.9; 1387 -7.2; 1526 -7.6; 1678 -7.6; 1846 -7.5; 2031 -7.2; 2234 -6.4; 2457 -4.7; 2703 -3.1; 2973 -1.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE535 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.67 | 3.0 dB  |
| Peaking | 52 Hz   | 1.38 | 1.1 dB  |
| Peaking | 223 Hz  | 0.73 | -2.1 dB |
| Peaking | 1866 Hz | 1.83 | -3.1 dB |
| Peaking | 4048 Hz | 0.98 | 7.1 dB  |
| Peaking | 791 Hz  | 4.12 | 0.6 dB  |
| Peaking | 3156 Hz | 3.51 | 2.1 dB  |
| Peaking | 3716 Hz | 1.51 | -1.5 dB |
| Peaking | 6289 Hz | 2.43 | 5.1 dB  |
| Peaking | 7467 Hz | 1.57 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE535/Shure%20SE535.png)