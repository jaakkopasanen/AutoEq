# Grado PS500e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.8; 49 -1.7; 54 -2.7; 60 -3.9; 66 -4.9; 72 -5.7; 79 -6.5; 87 -7.0; 96 -7.0; 106 -7.0; 116 -6.9; 128 -6.6; 141 -6.1; 155 -5.6; 170 -5.2; 187 -4.7; 206 -4.2; 227 -3.8; 249 -3.5; 274 -3.0; 302 -2.5; 332 -2.6; 365 -3.3; 402 -3.6; 442 -3.3; 486 -3.0; 535 -2.8; 588 -2.8; 647 -2.8; 712 -2.8; 783 -2.8; 861 -2.8; 947 -2.8; 1042 -3.1; 1146 -3.4; 1261 -3.8; 1387 -4.3; 1526 -4.9; 1678 -5.8; 1846 -7.1; 2031 -8.7; 2234 -9.7; 2457 -10.0; 2703 -9.7; 2973 -9.2; 3270 -8.3; 3597 -7.4; 3957 -9.9; 4353 -13.6; 4788 -14.7; 5267 -14.9; 5793 -15.7; 6373 -15.7; 7010 -13.3; 7711 -9.3; 8482 -6.8; 9330 -7.8; 10263 -10.7; 11289 -13.1; 12418 -13.7; 13660 -11.8; 15026 -7.3; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS500e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS500e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.08 | 7.1 dB  |
| Peaking | 302 Hz   | 1.54 | 3.3 dB  |
| Peaking | 791 Hz   | 1.04 | 4.1 dB  |
| Peaking | 5446 Hz  | 1.5  | -9.5 dB |
| Peaking | 12375 Hz | 2.66 | -7.5 dB |
| Peaking | 97 Hz    | 2.59 | -1.8 dB |
| Peaking | 2366 Hz  | 3.39 | -3.2 dB |
| Peaking | 3591 Hz  | 8.05 | 3.1 dB  |
| Peaking | 6640 Hz  | 6.77 | -2.5 dB |
| Peaking | 8442 Hz  | 5.18 | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | 3.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | -5.3 dB |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20PS500e/Grado%20PS500e.png)