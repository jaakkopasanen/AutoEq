# Shure SE420
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.5; 25 -1.8; 28 -2.1; 31 -2.4; 34 -2.7; 37 -3.0; 41 -3.3; 45 -3.6; 49 -3.9; 54 -4.3; 60 -4.7; 66 -5.2; 72 -5.5; 79 -6.0; 87 -6.3; 96 -6.6; 106 -7.1; 116 -7.4; 128 -7.7; 141 -8.0; 155 -8.2; 170 -8.4; 187 -8.5; 206 -8.6; 227 -8.6; 249 -8.7; 274 -8.5; 302 -8.3; 332 -8.2; 365 -7.9; 402 -7.7; 442 -7.6; 486 -7.3; 535 -7.1; 588 -6.6; 647 -6.4; 712 -6.2; 783 -6.1; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -7.0; 1261 -7.3; 1387 -7.8; 1526 -8.4; 1678 -8.7; 1846 -8.8; 2031 -9.0; 2234 -9.1; 2457 -8.5; 2703 -7.2; 2973 -5.4; 3270 -3.3; 3597 -1.8; 3957 -1.6; 4353 -1.8; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE420 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE420 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.77 | 5.0 dB  |
| Peaking | 46 Hz   | 1.16 | 1.5 dB  |
| Peaking | 204 Hz  | 0.83 | -2.4 dB |
| Peaking | 2105 Hz | 1.72 | -4.0 dB |
| Peaking | 4710 Hz | 1.25 | 6.6 dB  |
| Peaking | 772 Hz  | 0.75 | -1.1 dB |
| Peaking | 790 Hz  | 1.45 | 2.0 dB  |
| Peaking | 3494 Hz | 5.14 | 2.1 dB  |
| Peaking | 6207 Hz | 2.82 | 6.2 dB  |
| Peaking | 6539 Hz | 1.21 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE420/Shure%20SE420.png)