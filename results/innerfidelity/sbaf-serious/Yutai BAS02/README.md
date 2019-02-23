# Yutai BAS02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.6; 25 -7.7; 28 -7.8; 31 -8.0; 34 -8.1; 37 -8.2; 41 -8.3; 45 -8.4; 49 -8.6; 54 -8.8; 60 -8.9; 66 -9.2; 72 -9.5; 79 -9.8; 87 -10.1; 96 -10.4; 106 -10.6; 116 -10.7; 128 -10.9; 141 -11.0; 155 -11.1; 170 -11.1; 187 -11.0; 206 -10.9; 227 -10.8; 249 -10.6; 274 -10.4; 302 -10.1; 332 -9.9; 365 -9.6; 402 -9.3; 442 -8.8; 486 -8.6; 535 -8.1; 588 -7.5; 647 -7.1; 712 -6.8; 783 -6.3; 861 -6.4; 947 -6.5; 1042 -6.6; 1146 -6.7; 1261 -6.9; 1387 -7.2; 1526 -7.5; 1678 -7.5; 1846 -7.3; 2031 -6.8; 2234 -6.7; 2457 -6.6; 2703 -6.8; 2973 -6.3; 3270 -3.4; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yutai BAS02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yutai BAS02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 66 Hz   | 0.39 | -1.6 dB |
| Peaking | 160 Hz  | 0.7  | -3.3 dB |
| Peaking | 330 Hz  | 1.32 | -1.7 dB |
| Peaking | 2576 Hz | 1.28 | -2.9 dB |
| Peaking | 4396 Hz | 1.22 | 7.8 dB  |
| Peaking | 1446 Hz | 0.95 | 1.4 dB  |
| Peaking | 1512 Hz | 2.08 | -2.0 dB |
| Peaking | 4597 Hz | 6.87 | -1.3 dB |
| Peaking | 6377 Hz | 3.01 | 4.2 dB  |
| Peaking | 7452 Hz | 1.74 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yutai%20BAS02/Yutai%20BAS02.png)