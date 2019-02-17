# Shure SE535
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.5; 25 -2.6; 28 -2.8; 31 -2.9; 34 -3.0; 37 -3.1; 41 -3.3; 45 -3.5; 49 -3.6; 54 -3.9; 60 -4.2; 66 -4.6; 72 -4.9; 79 -5.3; 87 -5.8; 96 -6.3; 106 -6.7; 116 -7.1; 128 -7.6; 141 -7.9; 155 -8.2; 170 -8.4; 187 -8.6; 206 -8.7; 227 -8.9; 249 -8.9; 274 -9.0; 302 -8.9; 332 -8.7; 365 -8.6; 402 -8.5; 442 -8.4; 486 -8.2; 535 -7.9; 588 -7.7; 647 -7.4; 712 -7.0; 783 -6.7; 861 -6.5; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.4; 1387 -5.9; 1526 -5.2; 1678 -4.5; 1846 -3.9; 2031 -3.2; 2234 -1.9; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.9; 15026 -8.3; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE535 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.44 | 4.2 dB  |
| Peaking | 67 Hz    | 0.82 | 2.3 dB  |
| Peaking | 185 Hz   | 0.23 | -2.8 dB |
| Peaking | 4695 Hz  | 0.52 | 8.3 dB  |
| Peaking | 8744 Hz  | 0.82 | -4.7 dB |
| Peaking | 1343 Hz  | 3.25 | -1.0 dB |
| Peaking | 2505 Hz  | 4.72 | 1.6 dB  |
| Peaking | 5911 Hz  | 1.52 | -2.0 dB |
| Peaking | 6235 Hz  | 3.79 | 3.6 dB  |
| Peaking | 14742 Hz | 6.74 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20SE535/Shure%20SE535.png)