# Westone W30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.2; 25 -6.4; 28 -6.6; 31 -6.8; 34 -7.0; 37 -7.2; 41 -7.4; 45 -7.6; 49 -7.8; 54 -8.1; 60 -8.4; 66 -8.7; 72 -9.0; 79 -9.4; 87 -9.8; 96 -10.3; 106 -10.7; 116 -11.0; 128 -11.3; 141 -11.6; 155 -11.9; 170 -12.1; 187 -12.2; 206 -12.2; 227 -12.2; 249 -12.1; 274 -12.1; 302 -11.9; 332 -11.8; 365 -11.5; 402 -11.3; 442 -11.0; 486 -10.6; 535 -10.2; 588 -9.8; 647 -9.2; 712 -8.5; 783 -7.9; 861 -7.2; 947 -6.7; 1042 -6.5; 1146 -6.8; 1261 -7.0; 1387 -6.9; 1526 -6.3; 1678 -5.1; 1846 -3.8; 2031 -2.3; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.3; 8482 -11.4; 9330 -9.5; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -7.3; 16529 -6.5; 18182 -6.5; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.9  | 1.1 dB  |
| Peaking | 155 Hz   | 0.61 | -1.2 dB |
| Peaking | 263 Hz   | 0.35 | -4.9 dB |
| Peaking | 4048 Hz  | 0.55 | 7.3 dB  |
| Peaking | 8564 Hz  | 3.2  | -8.8 dB |
| Peaking | 1473 Hz  | 4.06 | -1.8 dB |
| Peaking | 2318 Hz  | 3.1  | 2.2 dB  |
| Peaking | 5437 Hz  | 0.71 | -1.4 dB |
| Peaking | 6170 Hz  | 2.89 | 2.9 dB  |
| Peaking | 20048 Hz | 1.84 | -5.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Westone%20W30/Westone%20W30.png)