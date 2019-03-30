# Focal Spirit Professional
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.4; 25 -8.5; 28 -8.6; 31 -8.6; 34 -8.6; 37 -8.5; 41 -8.4; 45 -8.3; 49 -8.2; 54 -8.1; 60 -8.3; 66 -8.4; 72 -8.5; 79 -9.0; 87 -9.4; 96 -9.8; 106 -9.9; 116 -10.0; 128 -10.1; 141 -9.9; 155 -9.6; 170 -9.4; 187 -9.0; 206 -8.5; 227 -7.9; 249 -7.3; 274 -6.8; 302 -6.3; 332 -5.6; 365 -5.0; 402 -4.6; 442 -4.5; 486 -4.3; 535 -4.2; 588 -4.3; 647 -4.0; 712 -3.4; 783 -3.2; 861 -3.5; 947 -3.6; 1042 -3.3; 1146 -3.0; 1261 -2.8; 1387 -2.4; 1526 -2.0; 1678 -1.3; 1846 -0.6; 2031 -0.5; 2234 -1.4; 2457 -3.1; 2703 -4.5; 2973 -5.6; 3270 -6.7; 3597 -7.6; 3957 -7.8; 4353 -8.1; 4788 -10.3; 5267 -12.6; 5793 -12.7; 6373 -9.7; 7010 -3.9; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -6.9; 13660 -6.2; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit Professional GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit Professional ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.74 | -2.8 dB |
| Peaking | 133 Hz   | 0.66 | -4.8 dB |
| Peaking | 687 Hz   | 0.51 | 2.2 dB  |
| Peaking | 1911 Hz  | 2.38 | 4.6 dB  |
| Peaking | 5345 Hz  | 2.84 | -8.2 dB |
| Peaking | 3577 Hz  | 2.23 | -3.2 dB |
| Peaking | 4756 Hz  | 0.75 | 1.9 dB  |
| Peaking | 6149 Hz  | 4.63 | -3.6 dB |
| Peaking | 6996 Hz  | 6.69 | 3.6 dB  |
| Peaking | 12676 Hz | 4.26 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Focal%20Spirit%20Professional/Focal%20Spirit%20Professional.png)