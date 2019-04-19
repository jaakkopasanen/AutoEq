# Focal Stellia
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.2; 25 -9.4; 28 -9.5; 31 -9.4; 34 -9.1; 37 -8.7; 41 -7.9; 45 -7.2; 49 -6.9; 54 -6.6; 60 -6.4; 66 -7.1; 72 -8.6; 79 -10.2; 87 -11.3; 96 -12.1; 106 -12.4; 116 -12.4; 128 -11.9; 141 -11.2; 155 -10.4; 170 -9.3; 187 -8.0; 206 -6.8; 227 -5.8; 249 -5.2; 274 -5.0; 302 -4.9; 332 -5.0; 365 -5.1; 402 -5.2; 442 -5.2; 486 -5.3; 535 -5.3; 588 -5.2; 647 -5.1; 712 -5.2; 783 -5.5; 861 -5.8; 947 -6.4; 1042 -6.8; 1146 -6.9; 1261 -6.6; 1387 -6.4; 1526 -6.4; 1678 -6.5; 1846 -7.2; 2031 -5.9; 2234 -3.9; 2457 -4.9; 2703 -5.9; 2973 -5.9; 3270 -3.9; 3597 -3.8; 3957 -0.5; 4353 -1.2; 4788 -4.6; 5267 -6.0; 5793 -8.1; 6373 -4.8; 7010 -3.8; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -8.0; 20000 -16.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Stellia GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Stellia ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 1.51 | -4.2 dB |
| Peaking | 111 Hz  | 1.51 | -7.5 dB |
| Peaking | 1288 Hz | 2.05 | -1.3 dB |
| Peaking | 4099 Hz | 4.75 | 5.8 dB  |
| Peaking | 5672 Hz | 9.11 | -3.2 dB |
| Peaking | 60 Hz   | 5.59 | 1.2 dB  |
| Peaking | 165 Hz  | 3.1  | -1.9 dB |
| Peaking | 270 Hz  | 1.06 | 1.5 dB  |
| Peaking | 2856 Hz | 7.18 | -0.6 dB |
| Peaking | 6845 Hz | 8.78 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -7.8 dB |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Stellia/Focal%20Stellia.png)