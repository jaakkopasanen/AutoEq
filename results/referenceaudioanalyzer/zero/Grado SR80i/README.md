# Grado SR80i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.0; 49 -1.9; 54 -2.9; 60 -3.8; 66 -4.5; 72 -5.0; 79 -5.4; 87 -5.6; 96 -5.6; 106 -5.6; 116 -5.4; 128 -5.2; 141 -5.0; 155 -4.8; 170 -4.6; 187 -4.3; 206 -4.1; 227 -3.8; 249 -3.7; 274 -3.4; 302 -3.3; 332 -3.1; 365 -2.8; 402 -2.5; 442 -2.4; 486 -2.8; 535 -3.0; 588 -3.0; 647 -3.0; 712 -2.9; 783 -2.7; 861 -2.7; 947 -2.9; 1042 -3.0; 1146 -3.3; 1261 -3.6; 1387 -4.1; 1526 -4.8; 1678 -6.6; 1846 -9.8; 2031 -11.8; 2234 -11.9; 2457 -10.9; 2703 -9.9; 2973 -8.5; 3270 -6.6; 3597 -5.0; 3957 -8.7; 4353 -14.4; 4788 -15.9; 5267 -14.9; 5793 -14.5; 6373 -16.1; 7010 -15.8; 7711 -11.8; 8482 -7.2; 9330 -6.5; 10263 -7.2; 11289 -8.3; 12418 -7.1; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR80i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR80i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 30 Hz   | 0.87 | 6.8 dB   |
| Peaking | 340 Hz  | 0.8  | 2.7 dB   |
| Peaking | 2146 Hz | 1.93 | -11.2 dB |
| Peaking | 3113 Hz | 0.29 | 8.6 dB   |
| Peaking | 5588 Hz | 1.04 | -16.9 dB |
| Peaking | 3707 Hz | 4.34 | 7.5 dB   |
| Peaking | 4449 Hz | 1.77 | -6.5 dB  |
| Peaking | 5541 Hz | 3.32 | 6.4 dB   |
| Peaking | 6956 Hz | 3.3  | -4.0 dB  |
| Peaking | 8708 Hz | 4.19 | 3.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | -4.0 dB |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20SR80i/Grado%20SR80i.png)