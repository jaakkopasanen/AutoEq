# Focal Elegia (preliminary)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.2; 25 -8.2; 28 -8.0; 31 -7.8; 34 -7.4; 37 -7.0; 41 -6.7; 45 -6.5; 49 -6.4; 54 -6.6; 60 -7.6; 66 -8.6; 72 -9.1; 79 -9.5; 87 -9.7; 96 -9.7; 106 -9.4; 116 -9.0; 128 -8.5; 141 -8.0; 155 -7.5; 170 -7.1; 187 -7.1; 206 -7.5; 227 -7.9; 249 -8.3; 274 -8.5; 302 -8.6; 332 -8.6; 365 -8.5; 402 -8.4; 442 -8.3; 486 -8.4; 535 -8.6; 588 -8.7; 647 -8.7; 712 -8.6; 783 -8.6; 861 -8.8; 947 -9.2; 1042 -9.3; 1146 -9.2; 1261 -8.6; 1387 -8.6; 1526 -9.0; 1678 -9.3; 1846 -8.6; 2031 -5.5; 2234 -3.5; 2457 -4.0; 2703 -4.5; 2973 -4.4; 3270 -1.8; 3597 -1.8; 3957 -0.9; 4353 -0.5; 4788 -4.4; 5267 -8.0; 5793 -8.6; 6373 -4.5; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -10.5; 20000 -22.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elegia (preliminary) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elegia (preliminary) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 91 Hz   | 1.54 | -3.2 dB |
| Peaking | 1402 Hz | 0.29 | -3.6 dB |
| Peaking | 3442 Hz | 0.82 | 6.5 dB  |
| Peaking | 4284 Hz | 3.97 | 3.2 dB  |
| Peaking | 5420 Hz | 5.64 | -5.7 dB |
| Peaking | 23 Hz   | 2.29 | -1.7 dB |
| Peaking | 286 Hz  | 4.57 | -0.9 dB |
| Peaking | 1777 Hz | 3.48 | -4.2 dB |
| Peaking | 2130 Hz | 2.19 | 3.8 dB  |
| Peaking | 2856 Hz | 5.21 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Elegia%20(preliminary)/Focal%20Elegia%20(preliminary).png)