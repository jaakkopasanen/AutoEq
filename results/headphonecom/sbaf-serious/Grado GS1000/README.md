# Grado GS1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -2.0; 54 -3.7; 60 -5.3; 66 -6.7; 72 -7.9; 79 -9.0; 87 -10.0; 96 -10.7; 106 -10.9; 116 -10.8; 128 -10.4; 141 -9.9; 155 -9.4; 170 -8.7; 187 -8.0; 206 -7.2; 227 -6.5; 249 -5.9; 274 -5.7; 302 -5.6; 332 -5.2; 365 -4.7; 402 -4.3; 442 -4.1; 486 -4.0; 535 -3.8; 588 -3.6; 647 -3.2; 712 -3.0; 783 -3.0; 861 -3.1; 947 -3.1; 1042 -3.3; 1146 -3.4; 1261 -3.5; 1387 -3.9; 1526 -4.5; 1678 -3.8; 1846 -4.5; 2031 -4.5; 2234 -4.6; 2457 -4.3; 2703 -4.5; 2973 -4.6; 3270 -4.1; 3597 -6.7; 3957 -8.5; 4353 -6.5; 4788 -9.0; 5267 -10.3; 5793 -11.1; 6373 -13.2; 7010 -13.5; 7711 -12.8; 8482 -11.3; 9330 -10.4; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GS1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.49 | 8.6 dB  |
| Peaking | 95 Hz    | 0.76 | -8.8 dB |
| Peaking | 749 Hz   | 0.38 | 3.6 dB  |
| Peaking | 2995 Hz  | 3.15 | 1.8 dB  |
| Peaking | 6903 Hz  | 1.56 | -7.6 dB |
| Peaking | 9548 Hz  | 3.64 | -2.0 dB |
| Peaking | 10736 Hz | 3.14 | 1.9 dB  |
| Peaking | 12982 Hz | 1.27 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | -6.6 dB |
| Peaking | 16000 Hz | 1.41 | 1.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GS1000/Grado%20GS1000.png)