# Yamaha Pro400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -5.1; 25 -5.6; 28 -6.2; 31 -6.6; 34 -6.8; 37 -7.1; 41 -7.3; 45 -7.4; 49 -7.6; 54 -7.8; 60 -7.9; 66 -7.0; 72 -4.5; 79 -6.2; 87 -9.1; 96 -9.5; 106 -6.4; 116 -9.1; 128 -10.6; 141 -11.2; 155 -11.0; 170 -9.4; 187 -9.8; 206 -7.8; 227 -4.7; 249 -1.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.7; 442 -1.4; 486 -2.9; 535 -3.6; 588 -4.4; 647 -5.4; 712 -6.4; 783 -6.7; 861 -7.0; 947 -6.8; 1042 -6.3; 1146 -5.8; 1261 -5.4; 1387 -5.5; 1526 -5.9; 1678 -5.8; 1846 -4.9; 2031 -3.7; 2234 -2.8; 2457 -1.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.6; 3957 -1.6; 4353 -0.7; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha Pro400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha Pro400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.52 | 2.1 dB  |
| Peaking | 163 Hz  | 1.28 | -7.0 dB |
| Peaking | 303 Hz  | 1.22 | 8.7 dB  |
| Peaking | 2894 Hz | 1.83 | 5.7 dB  |
| Peaking | 5311 Hz | 2.01 | 5.9 dB  |
| Peaking | 56 Hz   | 1.36 | -1.4 dB |
| Peaking | 73 Hz   | 7.62 | 4.0 dB  |
| Peaking | 446 Hz  | 4.5  | 1.3 dB  |
| Peaking | 823 Hz  | 2.79 | -1.6 dB |
| Peaking | 8326 Hz | 4.29 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | 4.3 dB  |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20Pro400/Yamaha%20Pro400.png)