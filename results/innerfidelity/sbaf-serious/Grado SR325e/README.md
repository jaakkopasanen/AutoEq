# Grado SR325e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.3; 49 -2.0; 54 -2.8; 60 -3.7; 66 -4.5; 72 -5.0; 79 -5.6; 87 -6.1; 96 -6.4; 106 -6.5; 116 -6.6; 128 -6.7; 141 -6.7; 155 -6.7; 170 -6.5; 187 -6.4; 206 -6.3; 227 -6.0; 249 -5.8; 274 -5.9; 302 -5.8; 332 -5.5; 365 -5.2; 402 -4.9; 442 -5.6; 486 -5.5; 535 -5.3; 588 -5.0; 647 -4.9; 712 -5.1; 783 -4.9; 861 -5.2; 947 -5.4; 1042 -5.6; 1146 -5.9; 1261 -6.3; 1387 -7.3; 1526 -8.4; 1678 -9.1; 1846 -13.3; 2031 -14.2; 2234 -12.4; 2457 -9.6; 2703 -7.1; 2973 -4.4; 3270 -2.8; 3597 -4.6; 3957 -6.4; 4353 -5.4; 4788 -3.5; 5267 -1.5; 5793 -3.0; 6373 -4.2; 7010 -4.6; 7711 -6.9; 8482 -11.3; 9330 -14.2; 10263 -11.6; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.96 | 6.9 dB   |
| Peaking | 2002 Hz | 2.42 | -11.1 dB |
| Peaking | 2892 Hz | 0.21 | 2.9 dB   |
| Peaking | 5617 Hz | 2.68 | 2.4 dB   |
| Peaking | 9214 Hz | 3.15 | -10.4 dB |
| Peaking | 51 Hz   | 2.69 | 1.1 dB   |
| Peaking | 106 Hz  | 1.13 | -1.0 dB  |
| Peaking | 371 Hz  | 3.9  | 0.8 dB   |
| Peaking | 3318 Hz | 5.37 | 3.6 dB   |
| Peaking | 3865 Hz | 4.94 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR325e/Grado%20SR325e.png)