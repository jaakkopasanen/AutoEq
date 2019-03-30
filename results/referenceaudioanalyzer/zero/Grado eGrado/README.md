# Grado eGrado
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.2; 72 -2.2; 79 -3.0; 87 -3.8; 96 -4.5; 106 -4.9; 116 -5.2; 128 -5.6; 141 -5.6; 155 -5.5; 170 -5.6; 187 -5.6; 206 -5.6; 227 -5.6; 249 -5.6; 274 -5.5; 302 -5.2; 332 -4.9; 365 -4.6; 402 -4.3; 442 -4.3; 486 -4.3; 535 -4.5; 588 -4.7; 647 -4.6; 712 -4.6; 783 -4.7; 861 -5.0; 947 -5.0; 1042 -5.3; 1146 -5.6; 1261 -6.0; 1387 -6.5; 1526 -7.1; 1678 -7.9; 1846 -8.8; 2031 -9.7; 2234 -10.6; 2457 -10.9; 2703 -10.6; 2973 -9.5; 3270 -7.7; 3597 -5.3; 3957 -3.2; 4353 -3.8; 4788 -8.0; 5267 -11.4; 5793 -13.0; 6373 -12.8; 7010 -10.8; 7711 -6.9; 8482 -6.5; 9330 -6.5; 10263 -9.0; 11289 -10.4; 12418 -9.1; 13660 -6.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado eGrado GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado eGrado ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.47 | 6.5 dB  |
| Peaking | 2482 Hz  | 2.38 | -5.0 dB |
| Peaking | 4094 Hz  | 3.99 | 5.9 dB  |
| Peaking | 5877 Hz  | 2.85 | -7.6 dB |
| Peaking | 11439 Hz | 4.12 | -4.1 dB |
| Peaking | 61 Hz    | 2.3  | 2.1 dB  |
| Peaking | 99 Hz    | 0.49 | -1.4 dB |
| Peaking | 550 Hz   | 0.55 | 2.2 dB  |
| Peaking | 1852 Hz  | 2.56 | -1.3 dB |
| Peaking | 8344 Hz  | 6.01 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20eGrado/Grado%20eGrado.png)