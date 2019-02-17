# Thinksound TS01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.6; 25 -11.7; 28 -11.8; 31 -11.9; 34 -12.0; 37 -12.1; 41 -12.2; 45 -12.3; 49 -12.4; 54 -12.7; 60 -12.9; 66 -13.0; 72 -13.3; 79 -13.6; 87 -13.7; 96 -14.0; 106 -14.0; 116 -14.1; 128 -14.2; 141 -14.2; 155 -14.2; 170 -14.1; 187 -13.9; 206 -13.6; 227 -13.2; 249 -12.8; 274 -12.3; 302 -11.7; 332 -11.0; 365 -10.2; 402 -9.5; 442 -8.9; 486 -8.4; 535 -7.6; 588 -6.8; 647 -6.0; 712 -5.3; 783 -4.7; 861 -4.3; 947 -4.1; 1042 -4.4; 1146 -3.3; 1261 -3.2; 1387 -3.5; 1526 -3.7; 1678 -3.7; 1846 -3.4; 2031 -3.2; 2234 -3.0; 2457 -2.9; 2703 -3.2; 2973 -3.4; 3270 -2.3; 3597 -0.5; 3957 -0.5; 4353 -2.5; 4788 -4.2; 5267 -6.2; 5793 -11.7; 6373 -10.4; 7010 -5.8; 7711 -4.4; 8482 -7.0; 9330 -9.5; 10263 -5.0; 11289 -4.3; 12418 -4.3; 13660 -4.3; 15026 -4.3; 16529 -4.3; 18182 -4.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thinksound TS01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound TS01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.23 | -7.3 dB |
| Peaking | 154 Hz  | 0.7  | -5.5 dB |
| Peaking | 313 Hz  | 1.18 | -3.4 dB |
| Peaking | 3846 Hz | 1.65 | 4.1 dB  |
| Peaking | 5989 Hz | 3.92 | -9.5 dB |
| Peaking | 1192 Hz | 2.11 | 1.2 dB  |
| Peaking | 2566 Hz | 1.54 | 0.8 dB  |
| Peaking | 2957 Hz | 4.91 | -1.9 dB |
| Peaking | 7419 Hz | 3.98 | 1.8 dB  |
| Peaking | 9138 Hz | 5.38 | -5.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.2 dB |
| Peaking | 125 Hz   | 1.41 | -8.2 dB |
| Peaking | 250 Hz   | 1.41 | -7.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Thinksound%20TS01/Thinksound%20TS01.png)