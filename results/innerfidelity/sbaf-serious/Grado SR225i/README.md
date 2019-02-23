# Grado SR225i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.4; 54 -2.2; 60 -3.0; 66 -3.8; 72 -4.5; 79 -5.2; 87 -5.7; 96 -6.1; 106 -6.3; 116 -6.3; 128 -6.4; 141 -6.3; 155 -6.2; 170 -6.0; 187 -5.8; 206 -5.6; 227 -5.3; 249 -5.0; 274 -4.7; 302 -4.7; 332 -4.7; 365 -4.4; 402 -4.5; 442 -4.2; 486 -4.3; 535 -4.2; 588 -3.9; 647 -3.8; 712 -4.0; 783 -3.7; 861 -4.0; 947 -4.2; 1042 -4.3; 1146 -4.5; 1261 -5.1; 1387 -6.0; 1526 -7.3; 1678 -8.2; 1846 -10.2; 2031 -12.9; 2234 -11.9; 2457 -9.7; 2703 -8.4; 2973 -7.7; 3270 -6.4; 3597 -7.8; 3957 -6.7; 4353 -4.8; 4788 -4.8; 5267 -6.6; 5793 -5.5; 6373 -6.9; 7010 -10.1; 7711 -10.2; 8482 -11.7; 9330 -13.6; 10263 -9.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.87 | 6.9 dB  |
| Peaking | 733 Hz   | 0.54 | 2.9 dB  |
| Peaking | 2078 Hz  | 2.69 | -7.4 dB |
| Peaking | 4583 Hz  | 4.9  | 2.4 dB  |
| Peaking | 8930 Hz  | 3.03 | -7.2 dB |
| Peaking | 51 Hz    | 2.82 | 1.1 dB  |
| Peaking | 105 Hz   | 1.75 | -1.0 dB |
| Peaking | 5913 Hz  | 8.58 | 1.6 dB  |
| Peaking | 7076 Hz  | 8.43 | -2.3 dB |
| Peaking | 11191 Hz | 5.83 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i/Grado%20SR225i.png)