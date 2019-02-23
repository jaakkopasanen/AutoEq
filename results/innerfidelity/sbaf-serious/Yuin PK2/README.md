# Yuin PK2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.7; 187 -1.0; 206 -1.2; 227 -1.3; 249 -1.6; 274 -1.3; 302 -1.4; 332 -1.5; 365 -1.8; 402 -2.4; 442 -3.6; 486 -2.8; 535 -4.0; 588 -3.9; 647 -4.2; 712 -4.7; 783 -5.0; 861 -5.6; 947 -6.3; 1042 -6.6; 1146 -7.2; 1261 -8.2; 1387 -9.3; 1526 -10.8; 1678 -12.3; 1846 -13.2; 2031 -13.3; 2234 -14.7; 2457 -14.3; 2703 -12.2; 2973 -10.0; 3270 -7.4; 3597 -6.9; 3957 -7.4; 4353 -9.8; 4788 -10.5; 5267 -10.6; 5793 -12.1; 6373 -15.0; 7010 -14.0; 7711 -12.6; 8482 -12.0; 9330 -12.6; 10263 -12.4; 11289 -8.6; 12418 -6.5; 13660 -8.3; 15026 -12.5; 16529 -11.0; 18182 -7.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin PK2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.11 | 5.9 dB  |
| Peaking | 246 Hz   | 0.4  | 4.3 dB  |
| Peaking | 2046 Hz  | 1.67 | -8.3 dB |
| Peaking | 7255 Hz  | 1.34 | -7.5 dB |
| Peaking | 15697 Hz | 2.45 | -6.2 dB |
| Peaking | 2559 Hz  | 5.81 | -2.1 dB |
| Peaking | 3532 Hz  | 3.61 | 3.5 dB  |
| Peaking | 8141 Hz  | 2.79 | 5.2 dB  |
| Peaking | 9950 Hz  | 0.99 | -5.8 dB |
| Peaking | 12156 Hz | 2.46 | 6.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 4.7 dB  |
| Peaking | 250 Hz   | 1.41 | 4.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.5 dB |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yuin%20PK2/Yuin%20PK2.png)