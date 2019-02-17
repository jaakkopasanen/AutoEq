# Grado SR325e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.1; 45 -2.1; 49 -2.9; 54 -3.6; 60 -4.5; 66 -5.3; 72 -5.9; 79 -6.4; 87 -6.9; 96 -7.2; 106 -7.3; 116 -7.4; 128 -7.5; 141 -7.5; 155 -7.5; 170 -7.3; 187 -7.2; 206 -7.1; 227 -6.8; 249 -6.6; 274 -6.7; 302 -6.6; 332 -6.3; 365 -6.0; 402 -5.8; 442 -6.4; 486 -6.3; 535 -6.2; 588 -5.8; 647 -5.7; 712 -6.0; 783 -5.7; 861 -6.0; 947 -6.2; 1042 -6.4; 1146 -6.7; 1261 -7.1; 1387 -8.1; 1526 -9.2; 1678 -9.9; 1846 -14.2; 2031 -15.1; 2234 -13.2; 2457 -10.5; 2703 -7.9; 2973 -5.2; 3270 -3.6; 3597 -5.4; 3957 -7.2; 4353 -6.2; 4788 -4.3; 5267 -1.7; 5793 -3.8; 6373 -5.0; 7010 -5.4; 7711 -7.7; 8482 -12.1; 9330 -15.1; 10263 -12.4; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 1.18 | 7.0 dB   |
| Peaking | 2017 Hz | 2.47 | -11.1 dB |
| Peaking | 4234 Hz | 0.27 | 2.5 dB   |
| Peaking | 5232 Hz | 7.04 | 3.2 dB   |
| Peaking | 9379 Hz | 3.16 | -11.2 dB |
| Peaking | 47 Hz   | 2.44 | 1.4 dB   |
| Peaking | 116 Hz  | 1.05 | -1.5 dB  |
| Peaking | 3339 Hz | 4.77 | 4.8 dB   |
| Peaking | 3752 Hz | 2.83 | -3.6 dB  |
| Peaking | 6279 Hz | 3.59 | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR325e/Grado%20SR325e.png)