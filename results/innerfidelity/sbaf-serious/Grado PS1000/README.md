# Grado PS1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.9; 54 -3.2; 60 -4.7; 66 -5.8; 72 -6.9; 79 -7.8; 87 -8.5; 96 -9.0; 106 -9.0; 116 -8.7; 128 -8.3; 141 -7.9; 155 -7.4; 170 -6.9; 187 -6.3; 206 -5.9; 227 -5.3; 249 -4.9; 274 -4.4; 302 -4.0; 332 -4.1; 365 -3.7; 402 -3.7; 442 -3.6; 486 -3.6; 535 -3.5; 588 -3.3; 647 -3.2; 712 -3.4; 783 -3.1; 861 -3.5; 947 -3.5; 1042 -3.8; 1146 -4.3; 1261 -4.8; 1387 -5.5; 1526 -5.9; 1678 -5.3; 1846 -5.6; 2031 -4.9; 2234 -4.9; 2457 -5.0; 2703 -5.4; 2973 -5.5; 3270 -6.1; 3597 -4.6; 3957 -8.2; 4353 -10.2; 4788 -9.7; 5267 -11.0; 5793 -12.5; 6373 -15.6; 7010 -13.7; 7711 -10.6; 8482 -11.2; 9330 -14.0; 10263 -12.0; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.47 | 8.7 dB  |
| Peaking | 92 Hz    | 0.69 | -7.9 dB |
| Peaking | 487 Hz   | 0.31 | 3.5 dB  |
| Peaking | 6340 Hz  | 2.27 | -8.6 dB |
| Peaking | 9560 Hz  | 4.93 | -7.0 dB |
| Peaking | 1518 Hz  | 1.93 | -2.6 dB |
| Peaking | 1861 Hz  | 0.78 | 1.6 dB  |
| Peaking | 3638 Hz  | 7.65 | 3.0 dB  |
| Peaking | 4219 Hz  | 4.73 | -3.2 dB |
| Peaking | 11715 Hz | 5.79 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -7.6 dB |
| Peaking | 16000 Hz | 1.41 | 1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20PS1000/Grado%20PS1000.png)