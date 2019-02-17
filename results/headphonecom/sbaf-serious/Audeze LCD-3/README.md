# Audeze LCD-3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.0; 25 -5.1; 28 -5.6; 31 -6.0; 34 -5.8; 37 -5.8; 41 -6.4; 45 -6.8; 49 -7.4; 54 -7.4; 60 -7.3; 66 -7.4; 72 -7.6; 79 -7.8; 87 -8.1; 96 -8.3; 106 -8.5; 116 -8.7; 128 -8.9; 141 -9.1; 155 -9.3; 170 -9.6; 187 -9.8; 206 -10.0; 227 -10.0; 249 -10.2; 274 -10.0; 302 -9.3; 332 -8.7; 365 -8.5; 402 -8.9; 442 -9.5; 486 -9.5; 535 -9.1; 588 -8.9; 647 -8.9; 712 -8.6; 783 -8.8; 861 -8.7; 947 -7.2; 1042 -6.0; 1146 -5.4; 1261 -6.8; 1387 -6.9; 1526 -7.3; 1678 -6.6; 1846 -5.2; 2031 -3.9; 2234 -5.7; 2457 -4.8; 2703 -4.9; 2973 -5.2; 3270 -4.2; 3597 -1.4; 3957 -0.5; 4353 -0.5; 4788 -2.4; 5267 -5.0; 5793 -5.4; 6373 -4.1; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.1; 16529 -12.6; 18182 -14.6; 20000 -11.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 201 Hz   | 0.66 | -3.3 dB |
| Peaking | 606 Hz   | 1.46 | -2.0 dB |
| Peaking | 2030 Hz  | 5.87 | 2.0 dB  |
| Peaking | 4118 Hz  | 2.23 | 6.4 dB  |
| Peaking | 18376 Hz | 1.1  | -9.1 dB |
| Peaking | 25 Hz    | 1.83 | 1.4 dB  |
| Peaking | 1096 Hz  | 4.51 | 3.2 dB  |
| Peaking | 1123 Hz  | 1.59 | -1.4 dB |
| Peaking | 6318 Hz  | 2.53 | 0.8 dB  |
| Peaking | 13796 Hz | 2.93 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -5.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-3/Audeze%20LCD-3.png)