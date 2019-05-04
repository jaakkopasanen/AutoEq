# Philips SHP9500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.3; 49 -2.0; 54 -2.6; 60 -3.3; 66 -3.8; 72 -4.1; 79 -4.5; 87 -5.1; 96 -5.7; 106 -6.2; 116 -6.6; 128 -6.8; 141 -7.1; 155 -7.2; 170 -7.5; 187 -7.8; 206 -8.0; 227 -7.6; 249 -6.9; 274 -6.5; 302 -6.2; 332 -6.0; 365 -5.9; 402 -5.8; 442 -5.7; 486 -5.7; 535 -5.6; 588 -5.6; 647 -5.5; 712 -5.7; 783 -5.9; 861 -6.1; 947 -6.3; 1042 -6.4; 1146 -6.4; 1261 -6.4; 1387 -6.1; 1526 -5.5; 1678 -4.9; 1846 -4.2; 2031 -3.2; 2234 -2.2; 2457 -3.3; 2703 -4.8; 2973 -6.4; 3270 -5.5; 3597 -5.1; 3957 -7.3; 4353 -9.1; 4788 -10.7; 5267 -10.6; 5793 -14.0; 6373 -12.9; 7010 -7.5; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -7.2; 11289 -9.1; 12418 -12.6; 13660 -12.0; 15026 -8.9; 16529 -9.5; 18182 -11.4; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHP9500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHP9500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.85 | 6.8 dB  |
| Peaking | 2205 Hz  | 2.56 | 4.3 dB  |
| Peaking | 5807 Hz  | 3.66 | -7.9 dB |
| Peaking | 12833 Hz | 3.4  | -6.4 dB |
| Peaking | 18787 Hz | 0.89 | -5.2 dB |
| Peaking | 188 Hz   | 1.58 | -1.9 dB |
| Peaking | 458 Hz   | 1.05 | 1.0 dB  |
| Peaking | 3556 Hz  | 8.44 | 1.9 dB  |
| Peaking | 4514 Hz  | 4.96 | -2.1 dB |
| Peaking | 7663 Hz  | 4.64 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -5.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Philips%20SHP9500/Philips%20SHP9500.png)