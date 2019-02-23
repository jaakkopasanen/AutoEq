# Yamaha Pro400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.5; 25 -9.0; 28 -9.5; 31 -9.9; 34 -10.2; 37 -10.4; 41 -10.6; 45 -10.7; 49 -10.9; 54 -11.1; 60 -11.2; 66 -10.3; 72 -7.8; 79 -9.5; 87 -12.4; 96 -12.9; 106 -9.8; 116 -12.4; 128 -13.9; 141 -14.5; 155 -14.3; 170 -12.8; 187 -13.2; 206 -11.1; 227 -8.0; 249 -4.8; 274 -2.4; 302 -1.9; 332 -2.6; 365 -3.2; 402 -4.0; 442 -4.8; 486 -6.2; 535 -6.9; 588 -7.7; 647 -8.7; 712 -9.7; 783 -10.0; 861 -10.3; 947 -10.1; 1042 -9.6; 1146 -9.1; 1261 -8.7; 1387 -8.8; 1526 -9.2; 1678 -9.1; 1846 -8.2; 2031 -7.0; 2234 -6.1; 2457 -4.9; 2703 -3.2; 2973 -1.5; 3270 -2.0; 3597 -5.0; 3957 -5.0; 4353 -3.9; 4788 -2.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.8; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha Pro400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha Pro400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.71 | -4.3 dB |
| Peaking | 145 Hz  | 2.32 | -7.9 dB |
| Peaking | 3044 Hz | 5.58 | 5.6 dB  |
| Peaking | 5590 Hz | 2.86 | 6.8 dB  |
| Peaking | 198 Hz  | 3.2  | -5.2 dB |
| Peaking | 295 Hz  | 1.5  | 6.5 dB  |
| Peaking | 839 Hz  | 1.41 | -4.3 dB |
| Peaking | 1609 Hz | 3.99 | -2.3 dB |
| Peaking | 9311 Hz | 6.36 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -8.7 dB |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20Pro400/Yamaha%20Pro400.png)