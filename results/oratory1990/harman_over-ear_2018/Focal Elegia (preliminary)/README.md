# Focal Elegia (preliminary)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.3; 25 -5.3; 28 -5.3; 31 -5.1; 34 -4.6; 37 -4.1; 41 -3.9; 45 -3.9; 49 -3.6; 54 -3.7; 60 -4.9; 66 -5.8; 72 -6.3; 79 -6.7; 87 -6.9; 96 -6.9; 106 -6.6; 116 -6.2; 128 -5.7; 141 -5.2; 155 -4.7; 170 -4.3; 187 -4.4; 206 -4.7; 227 -5.2; 249 -5.5; 274 -5.8; 302 -5.9; 332 -5.8; 365 -5.7; 402 -5.6; 442 -5.5; 486 -5.6; 535 -5.8; 588 -6.0; 647 -5.9; 712 -5.8; 783 -5.8; 861 -6.0; 947 -6.4; 1042 -6.5; 1146 -6.4; 1261 -5.8; 1387 -5.8; 1526 -6.2; 1678 -6.5; 1846 -5.8; 2031 -2.7; 2234 -0.7; 2457 -1.2; 2703 -1.7; 2973 -1.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.1; 5267 -5.0; 5793 -6.1; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.0; 20000 -19.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elegia (preliminary) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elegia (preliminary) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 43 Hz   |  1.95 | 3.1 dB  |
| Peaking | 188 Hz  |  1.82 | 2.1 dB  |
| Peaking | 2292 Hz |  4.48 | 4.1 dB  |
| Peaking | 3778 Hz |  1.41 | 6.3 dB  |
| Peaking | 9540 Hz |  2.76 | -0.5 dB |
| Peaking | 10 Hz   |  0.47 | 1.2 dB  |
| Peaking | 90 Hz   |  2.71 | -1.1 dB |
| Peaking | 1627 Hz |  0.16 | 0.4 dB  |
| Peaking | 1693 Hz |  3.89 | -1.8 dB |
| Peaking | 5545 Hz | 12.62 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Elegia%20(preliminary)/Focal%20Elegia%20(preliminary).png)