# Grado SR225i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -1.8; 45 -2.8; 49 -3.6; 54 -4.5; 60 -5.2; 66 -6.0; 72 -6.7; 79 -7.4; 87 -7.9; 96 -8.3; 106 -8.5; 116 -8.5; 128 -8.6; 141 -8.6; 155 -8.4; 170 -8.2; 187 -8.1; 206 -7.9; 227 -7.5; 249 -7.2; 274 -6.9; 302 -6.9; 332 -6.9; 365 -6.6; 402 -6.8; 442 -6.5; 486 -6.5; 535 -6.4; 588 -6.1; 647 -6.1; 712 -6.2; 783 -6.0; 861 -6.2; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -7.3; 1387 -8.2; 1526 -9.5; 1678 -10.4; 1846 -12.4; 2031 -15.1; 2234 -14.1; 2457 -11.9; 2703 -10.6; 2973 -9.9; 3270 -8.6; 3597 -10.1; 3957 -8.9; 4353 -7.0; 4788 -7.1; 5267 -8.8; 5793 -7.7; 6373 -9.1; 7010 -12.3; 7711 -12.4; 8482 -13.9; 9330 -15.9; 10263 -11.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 28 Hz    |  0.68 | 6.8 dB   |
| Peaking | 105 Hz   |  0.82 | -3.2 dB  |
| Peaking | 2114 Hz  |  2.38 | -8.4 dB  |
| Peaking | 9353 Hz  |  1.74 | -12.5 dB |
| Peaking | 11055 Hz |  1.93 | 6.5 dB   |
| Peaking | 793 Hz   |  1.38 | 0.9 dB   |
| Peaking | 3784 Hz  |  4.29 | -3.0 dB  |
| Peaking | 4301 Hz  |  3.3  | 2.3 dB   |
| Peaking | 7071 Hz  | 12.2  | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i/Grado%20SR225i.png)