# Grado SR325i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.7; 60 -2.8; 66 -3.8; 72 -4.5; 79 -5.2; 87 -5.9; 96 -6.4; 106 -6.6; 116 -6.7; 128 -6.7; 141 -6.6; 155 -6.6; 170 -6.3; 187 -6.0; 206 -5.7; 227 -5.4; 249 -5.3; 274 -5.0; 302 -5.0; 332 -4.9; 365 -4.6; 402 -4.4; 442 -3.9; 486 -4.2; 535 -4.3; 588 -3.9; 647 -3.8; 712 -4.0; 783 -3.8; 861 -4.0; 947 -4.2; 1042 -4.2; 1146 -4.4; 1261 -5.0; 1387 -6.0; 1526 -7.3; 1678 -8.0; 1846 -9.5; 2031 -13.0; 2234 -11.7; 2457 -9.4; 2703 -7.7; 2973 -5.3; 3270 -3.8; 3597 -3.4; 3957 -6.5; 4353 -12.7; 4788 -9.0; 5267 -6.0; 5793 -5.3; 6373 -5.5; 7010 -7.9; 7711 -9.4; 8482 -11.7; 9330 -14.6; 10263 -11.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.91 | 7.0 dB   |
| Peaking | 2068 Hz  | 1.96 | -10.8 dB |
| Peaking | 2818 Hz  | 0.2  | 4.9 dB   |
| Peaking | 4436 Hz  | 6.38 | -9.9 dB  |
| Peaking | 9126 Hz  | 2.12 | -11.1 dB |
| Peaking | 31 Hz    | 1.73 | -4.4 dB  |
| Peaking | 47 Hz    | 0.22 | 3.8 dB   |
| Peaking | 105 Hz   | 0.74 | -4.4 dB  |
| Peaking | 3525 Hz  | 7.84 | 2.2 dB   |
| Peaking | 15982 Hz | 2.43 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR325i/Grado%20SR325i.png)