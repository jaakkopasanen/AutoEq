# Ultrasone DJ 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.5; 25 -2.3; 28 -3.7; 31 -4.7; 34 -5.3; 37 -5.6; 41 -5.9; 45 -6.1; 49 -6.4; 54 -6.8; 60 -7.4; 66 -7.7; 72 -7.7; 79 -7.6; 87 -7.3; 96 -6.7; 106 -6.0; 116 -5.3; 128 -4.3; 141 -2.9; 155 -1.5; 170 -0.6; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.7; 365 -3.3; 402 -5.5; 442 -6.8; 486 -7.5; 535 -7.7; 588 -7.4; 647 -6.9; 712 -6.8; 783 -7.2; 861 -7.6; 947 -7.9; 1042 -8.2; 1146 -8.2; 1261 -8.0; 1387 -8.2; 1526 -8.4; 1678 -8.0; 1846 -6.8; 2031 -5.3; 2234 -5.7; 2457 -7.3; 2703 -7.5; 2973 -7.2; 3270 -9.4; 3597 -11.8; 3957 -11.9; 4353 -9.6; 4788 -10.2; 5267 -13.3; 5793 -12.9; 6373 -8.0; 7010 -6.7; 7711 -11.0; 8482 -15.0; 9330 -15.6; 10263 -14.0; 11289 -13.5; 12418 -14.2; 13660 -12.8; 15026 -8.2; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone DJ 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone DJ 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 2.6  | 5.7 dB  |
| Peaking | 223 Hz   | 1.39 | 7.1 dB  |
| Peaking | 4241 Hz  | 1.55 | -3.9 dB |
| Peaking | 10659 Hz | 1.09 | -8.5 dB |
| Peaking | 22050 Hz | 2.06 | -7.2 dB |
| Peaking | 73 Hz    | 2.6  | -2.1 dB |
| Peaking | 324 Hz   | 4.54 | 3.9 dB  |
| Peaking | 595 Hz   | 0.71 | -1.8 dB |
| Peaking | 6894 Hz  | 8.48 | 5.3 dB  |
| Peaking | 8652 Hz  | 6.32 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 7.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB |
| Peaking | 8000 Hz  | 1.41 | -6.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20DJ%201/Ultrasone%20DJ%201.png)