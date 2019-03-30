# Ultrasone TIO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.1; 28 -3.0; 31 -3.8; 34 -4.3; 37 -4.8; 41 -5.3; 45 -5.6; 49 -5.9; 54 -6.2; 60 -6.5; 66 -6.6; 72 -6.7; 79 -6.9; 87 -7.0; 96 -7.0; 106 -7.0; 116 -7.0; 128 -6.9; 141 -6.7; 155 -6.6; 170 -6.6; 187 -6.4; 206 -6.3; 227 -6.3; 249 -6.0; 274 -6.0; 302 -5.8; 332 -5.7; 365 -5.7; 402 -5.6; 442 -5.4; 486 -5.3; 535 -5.3; 588 -5.3; 647 -5.3; 712 -5.5; 783 -5.7; 861 -5.7; 947 -5.9; 1042 -6.1; 1146 -6.3; 1261 -6.7; 1387 -7.1; 1526 -7.7; 1678 -8.4; 1846 -9.2; 2031 -10.1; 2234 -11.0; 2457 -11.7; 2703 -12.1; 2973 -11.8; 3270 -10.9; 3597 -9.7; 3957 -8.7; 4353 -8.1; 4788 -7.6; 5267 -6.9; 5793 -5.4; 6373 -2.8; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone TIO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone TIO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.02 | 6.6 dB  |
| Peaking | 88 Hz   | 0.61 | -1.1 dB |
| Peaking | 635 Hz  | 0.53 | 1.2 dB  |
| Peaking | 2656 Hz | 1.24 | -6.2 dB |
| Peaking | 6564 Hz | 5.1  | 4.9 dB  |
| Peaking | 7768 Hz | 5.71 | -0.4 dB |
| Peaking | 8196 Hz | 0.91 | 0.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20TIO/Ultrasone%20TIO.png)