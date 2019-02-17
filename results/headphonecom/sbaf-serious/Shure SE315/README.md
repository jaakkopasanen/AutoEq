# Shure SE315
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.2; 25 -2.3; 28 -2.3; 31 -2.3; 34 -2.5; 37 -2.6; 41 -2.8; 45 -2.9; 49 -3.1; 54 -3.3; 60 -3.6; 66 -3.9; 72 -4.1; 79 -4.5; 87 -4.8; 96 -5.1; 106 -5.3; 116 -5.6; 128 -5.6; 141 -5.9; 155 -6.2; 170 -6.3; 187 -6.2; 206 -6.3; 227 -6.4; 249 -6.2; 274 -6.1; 302 -6.1; 332 -5.8; 365 -5.5; 402 -5.4; 442 -5.3; 486 -5.2; 535 -5.1; 588 -4.8; 647 -4.7; 712 -4.8; 783 -5.0; 861 -5.3; 947 -6.0; 1042 -6.8; 1146 -7.6; 1261 -8.5; 1387 -9.6; 1526 -10.6; 1678 -11.2; 1846 -10.8; 2031 -9.2; 2234 -6.7; 2457 -3.5; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE315 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.65 | 4.1 dB  |
| Peaking | 57 Hz   | 1.05 | 1.7 dB  |
| Peaking | 666 Hz  | 1.15 | 2.0 dB  |
| Peaking | 1753 Hz | 1.47 | -9.4 dB |
| Peaking | 3292 Hz | 0.75 | 8.7 dB  |
| Peaking | 2174 Hz | 5.87 | -0.8 dB |
| Peaking | 2676 Hz | 5.33 | 1.8 dB  |
| Peaking | 3597 Hz | 2.91 | -1.2 dB |
| Peaking | 6324 Hz | 2.21 | 5.4 dB  |
| Peaking | 7341 Hz | 1.45 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 9.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE315/Shure%20SE315.png)