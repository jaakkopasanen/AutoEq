# Audeze LCD-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.7; 31 -2.5; 34 -3.0; 37 -3.5; 41 -4.0; 45 -4.2; 49 -4.3; 54 -4.4; 60 -4.5; 66 -4.7; 72 -4.9; 79 -5.1; 87 -5.5; 96 -5.9; 106 -6.3; 116 -6.7; 128 -7.1; 141 -7.4; 155 -7.7; 170 -7.9; 187 -8.1; 206 -8.2; 227 -8.3; 249 -8.3; 274 -8.3; 302 -8.1; 332 -7.9; 365 -7.7; 402 -7.6; 442 -7.6; 486 -7.7; 535 -7.6; 588 -7.5; 647 -7.5; 712 -7.5; 783 -7.5; 861 -7.4; 947 -7.3; 1042 -7.0; 1146 -6.8; 1261 -6.7; 1387 -6.8; 1526 -6.5; 1678 -6.1; 1846 -5.8; 2031 -6.0; 2234 -5.8; 2457 -5.3; 2703 -4.6; 2973 -4.6; 3270 -4.4; 3597 -4.5; 3957 -4.4; 4353 -3.4; 4788 -3.5; 5267 -2.9; 5793 -2.9; 6373 -3.7; 7010 -3.9; 7711 -5.8; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.3; 12418 -9.1; 13660 -10.0; 15026 -10.2; 16529 -13.2; 18182 -18.6; 20000 -26.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.78 | 6.0 dB   |
| Peaking | 72 Hz    | 1.06 | 2.4 dB   |
| Peaking | 180 Hz   | 0.22 | -2.3 dB  |
| Peaking | 3304 Hz  | 1.54 | 1.6 dB   |
| Peaking | 5544 Hz  | 2.61 | 3.2 dB   |
| Peaking | 236 Hz   | 2.4  | -0.3 dB  |
| Peaking | 400 Hz   | 3.16 | 0.5 dB   |
| Peaking | 9700 Hz  | 0.79 | 1.3 dB   |
| Peaking | 19793 Hz | 0.6  | -19.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB   |
| Peaking | 62 Hz    | 1.41 | 1.0 dB   |
| Peaking | 125 Hz   | 1.41 | -0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -10.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-X/Audeze%20LCD-X.png)