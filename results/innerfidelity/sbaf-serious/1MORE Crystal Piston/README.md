# 1MORE Crystal Piston
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.8; 25 -8.2; 28 -8.6; 31 -8.9; 34 -9.2; 37 -9.5; 41 -9.7; 45 -9.8; 49 -10.0; 54 -10.2; 60 -10.4; 66 -10.6; 72 -10.8; 79 -10.9; 87 -11.1; 96 -11.2; 106 -11.2; 116 -10.9; 128 -10.9; 141 -10.8; 155 -10.6; 170 -10.2; 187 -9.9; 206 -9.4; 227 -8.9; 249 -8.4; 274 -7.8; 302 -7.2; 332 -6.6; 365 -5.9; 402 -5.3; 442 -4.5; 486 -3.9; 535 -3.3; 588 -2.4; 647 -1.8; 712 -1.4; 783 -0.8; 861 -0.8; 947 -0.7; 1042 -0.9; 1146 -0.9; 1261 -0.5; 1387 -0.8; 1526 -1.3; 1678 -2.4; 1846 -3.6; 2031 -3.8; 2234 -3.4; 2457 -2.8; 2703 -2.7; 2973 -2.3; 3270 -2.0; 3597 -2.2; 3957 -3.3; 4353 -5.8; 4788 -7.6; 5267 -8.6; 5793 -8.8; 6373 -6.9; 7010 -5.0; 7711 -4.9; 8482 -6.2; 9330 -5.5; 10263 -1.6; 11289 -1.0; 12418 -1.0; 13660 -1.0; 15026 -1.0; 16529 -1.0; 18182 -1.0; 20000 -1.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Crystal Piston GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Crystal Piston ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.33 | -8.0 dB |
| Peaking | 144 Hz   | 0.73 | -5.2 dB |
| Peaking | 292 Hz   | 1.29 | -2.8 dB |
| Peaking | 5465 Hz  | 1.85 | -8.0 dB |
| Peaking | 8782 Hz  | 4.99 | -4.3 dB |
| Peaking | 466 Hz   | 2.26 | -1.0 dB |
| Peaking | 1056 Hz  | 0.71 | 1.4 dB  |
| Peaking | 2000 Hz  | 2.32 | -3.1 dB |
| Peaking | 3542 Hz  | 5.82 | 1.3 dB  |
| Peaking | 10989 Hz | 4.97 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.4 dB |
| Peaking | 62 Hz    | 1.41 | -7.3 dB |
| Peaking | 125 Hz   | 1.41 | -8.2 dB |
| Peaking | 250 Hz   | 1.41 | -6.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | -5.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Crystal%20Piston/1MORE%20Crystal%20Piston.png)