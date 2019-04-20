# Oppo PM3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -2.4; 25 -2.3; 28 -2.1; 31 -1.9; 34 -1.6; 37 -1.3; 41 -0.8; 45 -0.5; 49 -0.7; 54 -1.5; 60 -2.4; 66 -3.2; 72 -4.0; 79 -4.8; 87 -5.4; 96 -6.1; 106 -6.8; 116 -7.2; 128 -7.3; 141 -7.4; 155 -7.3; 170 -6.8; 187 -6.2; 206 -5.7; 227 -4.9; 249 -3.9; 274 -3.0; 302 -2.2; 332 -1.6; 365 -1.3; 402 -1.5; 442 -1.8; 486 -2.3; 535 -2.9; 588 -3.2; 647 -3.2; 712 -3.3; 783 -3.3; 861 -3.3; 947 -3.4; 1042 -3.7; 1146 -4.6; 1261 -5.2; 1387 -5.3; 1526 -5.5; 1678 -6.0; 1846 -6.3; 2031 -5.8; 2234 -5.5; 2457 -6.0; 2703 -6.0; 2973 -5.2; 3270 -5.1; 3597 -4.0; 3957 -3.4; 4353 -3.9; 4788 -3.4; 5267 -2.3; 5793 -4.3; 6373 -8.4; 7010 -6.9; 7711 -7.0; 8482 -7.6; 9330 -4.6; 10263 -4.6; 11289 -4.6; 12418 -7.5; 13660 -7.6; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 0.74 | 6.0 dB  |
| Peaking | 130 Hz   | 0.45 | -5.3 dB |
| Peaking | 345 Hz   | 0.97 | 5.5 dB  |
| Peaking | 7396 Hz  | 3.08 | -3.0 dB |
| Peaking | 13248 Hz | 5.74 | -4.5 dB |
| Peaking | 914 Hz   | 2.27 | 1.4 dB  |
| Peaking | 1865 Hz  | 0.96 | -1.7 dB |
| Peaking | 5376 Hz  | 2.15 | 3.3 dB  |
| Peaking | 6302 Hz  | 6.7  | -4.4 dB |
| Peaking | 10679 Hz | 5.71 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Oppo%20PM3/Oppo%20PM3.png)