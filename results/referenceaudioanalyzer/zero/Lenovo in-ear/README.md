# Lenovo in-ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.1; 23 -15.1; 25 -15.1; 28 -15.1; 31 -15.1; 34 -15.1; 37 -15.0; 41 -14.9; 45 -14.8; 49 -14.6; 54 -14.5; 60 -14.2; 66 -14.0; 72 -13.9; 79 -13.7; 87 -13.4; 96 -13.0; 106 -12.8; 116 -12.4; 128 -12.0; 141 -11.6; 155 -11.1; 170 -10.5; 187 -9.8; 206 -9.1; 227 -8.6; 249 -8.8; 274 -8.6; 302 -8.1; 332 -7.7; 365 -7.3; 402 -6.7; 442 -5.9; 486 -5.1; 535 -4.3; 588 -3.6; 647 -2.9; 712 -2.3; 783 -1.8; 861 -1.3; 947 -0.8; 1042 -0.5; 1146 -0.5; 1261 -0.8; 1387 -1.4; 1526 -2.0; 1678 -2.6; 1846 -3.1; 2031 -3.7; 2234 -4.6; 2457 -5.7; 2703 -6.3; 2973 -5.9; 3270 -5.2; 3597 -4.5; 3957 -4.5; 4353 -6.0; 4788 -8.0; 5267 -9.4; 5793 -10.3; 6373 -10.9; 7010 -10.4; 7711 -7.3; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lenovo in-ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lenovo in-ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.14 | -9.2 dB |
| Peaking | 1026 Hz | 0.9  | 5.9 dB  |
| Peaking | 3886 Hz | 6.13 | 2.1 dB  |
| Peaking | 6088 Hz | 2.31 | -5.6 dB |
| Peaking | 213 Hz  | 3.22 | 1.1 dB  |
| Peaking | 292 Hz  | 0.92 | -0.6 dB |
| Peaking | 566 Hz  | 2.91 | 0.7 dB  |
| Peaking | 2649 Hz | 6.33 | -1.5 dB |
| Peaking | 8501 Hz | 5.94 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.7 dB |
| Peaking | 62 Hz    | 1.41 | -6.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Lenovo%20in-ear/Lenovo%20in-ear.png)