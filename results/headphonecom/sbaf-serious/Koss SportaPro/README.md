# Koss SportaPro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.3; 45 -2.4; 49 -3.4; 54 -4.5; 60 -5.5; 66 -6.1; 72 -7.0; 79 -7.6; 87 -7.9; 96 -8.5; 106 -8.7; 116 -8.8; 128 -9.0; 141 -9.0; 155 -8.6; 170 -8.2; 187 -8.1; 206 -8.1; 227 -8.0; 249 -7.7; 274 -7.3; 302 -7.1; 332 -6.7; 365 -6.3; 402 -6.0; 442 -5.7; 486 -5.5; 535 -5.2; 588 -5.0; 647 -4.8; 712 -4.6; 783 -4.5; 861 -4.5; 947 -4.7; 1042 -4.9; 1146 -5.0; 1261 -5.4; 1387 -6.1; 1526 -7.1; 1678 -7.8; 1846 -8.4; 2031 -9.2; 2234 -9.5; 2457 -8.9; 2703 -7.2; 2973 -5.9; 3270 -6.0; 3597 -7.7; 3957 -9.4; 4353 -5.7; 4788 -9.5; 5267 -5.7; 5793 -3.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.7; 9330 -13.6; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss SportaPro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss SportaPro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.75 | 6.8 dB  |
| Peaking | 108 Hz  | 0.93 | -3.5 dB |
| Peaking | 4653 Hz | 0.93 | -2.1 dB |
| Peaking | 6310 Hz | 3.76 | 7.6 dB  |
| Peaking | 9297 Hz | 6.51 | -7.9 dB |
| Peaking | 245 Hz  | 1.56 | -1.1 dB |
| Peaking | 1048 Hz | 0.53 | 2.9 dB  |
| Peaking | 2161 Hz | 1.14 | -4.5 dB |
| Peaking | 3034 Hz | 3.75 | 3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20SportaPro/Koss%20SportaPro.png)