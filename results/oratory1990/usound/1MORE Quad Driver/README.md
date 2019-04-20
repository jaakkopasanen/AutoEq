# 1MORE Quad Driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.3; 25 -1.8; 28 -2.5; 31 -3.2; 34 -3.8; 37 -4.3; 41 -4.9; 45 -5.5; 49 -6.0; 54 -6.8; 60 -7.5; 66 -8.2; 72 -8.8; 79 -9.4; 87 -9.6; 96 -9.9; 106 -10.4; 116 -10.5; 128 -10.9; 141 -10.9; 155 -10.9; 170 -11.0; 187 -11.0; 206 -10.9; 227 -10.8; 249 -10.5; 274 -10.2; 302 -9.8; 332 -9.4; 365 -9.0; 402 -8.5; 442 -8.0; 486 -7.4; 535 -6.8; 588 -6.1; 647 -5.5; 712 -4.7; 783 -4.0; 861 -3.3; 947 -2.9; 1042 -2.8; 1146 -3.1; 1261 -3.5; 1387 -3.6; 1526 -3.7; 1678 -3.4; 1846 -3.1; 2031 -3.2; 2234 -3.6; 2457 -4.2; 2703 -4.6; 2973 -4.5; 3270 -4.1; 3597 -4.0; 3957 -4.8; 4353 -5.8; 4788 -4.9; 5267 -3.3; 5793 -1.5; 6373 -0.5; 7010 -4.0; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -8.0; 13660 -11.2; 15026 -12.9; 16529 -14.1; 18182 -15.4; 20000 -13.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Quad Driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Quad Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.35 | 6.3 dB   |
| Peaking | 198 Hz   | 0.24 | -6.6 dB  |
| Peaking | 921 Hz   | 0.5  | 5.3 dB   |
| Peaking | 6209 Hz  | 3.69 | 5.6 dB   |
| Peaking | 18183 Hz | 0.64 | -10.6 dB |
| Peaking | 1390 Hz  | 2.82 | -1.9 dB  |
| Peaking | 1419 Hz  | 1.38 | 1.1 dB   |
| Peaking | 7258 Hz  | 2.55 | -0.7 dB  |
| Peaking | 11443 Hz | 1.8  | 3.0 dB   |
| Peaking | 13923 Hz | 2.04 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB   |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -11.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/1MORE%20Quad%20Driver/1MORE%20Quad%20Driver.png)