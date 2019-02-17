# Grado PS500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.6; 34 -2.6; 37 -3.5; 41 -4.5; 45 -5.6; 49 -6.5; 54 -7.5; 60 -8.6; 66 -9.4; 72 -10.1; 79 -10.4; 87 -10.7; 96 -11.1; 106 -11.1; 116 -11.0; 128 -10.8; 141 -10.5; 155 -10.3; 170 -9.8; 187 -9.5; 206 -9.2; 227 -8.8; 249 -8.4; 274 -8.0; 302 -7.5; 332 -7.1; 365 -6.7; 402 -6.4; 442 -6.3; 486 -5.9; 535 -5.8; 588 -5.5; 647 -5.5; 712 -5.6; 783 -5.6; 861 -5.9; 947 -6.2; 1042 -6.6; 1146 -7.0; 1261 -7.7; 1387 -8.9; 1526 -10.0; 1678 -10.1; 1846 -9.2; 2031 -11.3; 2234 -9.6; 2457 -6.0; 2703 -3.4; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -2.7; 4353 -2.0; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -10.5; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.95 | 6.9 dB  |
| Peaking | 100 Hz  | 0.74 | -5.4 dB |
| Peaking | 2057 Hz | 1.84 | -7.1 dB |
| Peaking | 3084 Hz | 1.7  | 8.0 dB  |
| Peaking | 5578 Hz | 2.91 | 5.8 dB  |
| Peaking | 225 Hz  | 1.8  | -0.8 dB |
| Peaking | 627 Hz  | 0.91 | 1.4 dB  |
| Peaking | 1473 Hz | 5.47 | -1.9 dB |
| Peaking | 6501 Hz | 9.72 | 2.0 dB  |
| Peaking | 9368 Hz | 5.42 | -5.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20PS500/Grado%20PS500.png)