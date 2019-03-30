# Ultrasone IQ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.9; 25 -2.6; 28 -3.6; 31 -4.3; 34 -4.8; 37 -5.3; 41 -5.8; 45 -6.1; 49 -6.5; 54 -6.7; 60 -7.0; 66 -7.2; 72 -7.2; 79 -7.2; 87 -7.4; 96 -7.2; 106 -7.2; 116 -7.2; 128 -7.1; 141 -6.9; 155 -6.9; 170 -6.9; 187 -6.6; 206 -6.4; 227 -6.0; 249 -5.7; 274 -5.3; 302 -4.8; 332 -4.4; 365 -3.9; 402 -3.4; 442 -2.9; 486 -2.5; 535 -2.0; 588 -1.6; 647 -1.2; 712 -0.8; 783 -0.7; 861 -0.5; 947 -0.6; 1042 -0.8; 1146 -1.2; 1261 -1.9; 1387 -2.8; 1526 -3.9; 1678 -4.9; 1846 -5.6; 2031 -5.7; 2234 -5.4; 2457 -4.3; 2703 -2.6; 2973 -1.2; 3270 -2.0; 3597 -4.3; 3957 -6.0; 4353 -7.3; 4788 -8.0; 5267 -7.9; 5793 -7.0; 6373 -6.5; 7010 -6.7; 7711 -5.8; 8482 -4.2; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone IQ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone IQ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.11 | 4.8 dB  |
| Peaking | 90 Hz   | 0.32 | -3.4 dB |
| Peaking | 885 Hz  | 0.7  | 5.2 dB  |
| Peaking | 3039 Hz | 2.25 | 10.6 dB |
| Peaking | 3084 Hz | 0.72 | -8.1 dB |
| Peaking | 1232 Hz | 4.65 | 0.5 dB  |
| Peaking | 1763 Hz | 5.39 | -0.6 dB |
| Peaking | 3892 Hz | 3.01 | 1.3 dB  |
| Peaking | 4751 Hz | 1.71 | -1.3 dB |
| Peaking | 9380 Hz | 1.97 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20IQ/Ultrasone%20IQ.png)