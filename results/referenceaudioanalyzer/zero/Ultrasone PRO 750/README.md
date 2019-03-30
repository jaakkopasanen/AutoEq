# Ultrasone PRO 750
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.2; 49 -1.5; 54 -1.7; 60 -1.9; 66 -2.4; 72 -2.9; 79 -3.4; 87 -3.7; 96 -3.7; 106 -3.4; 116 -3.2; 128 -3.1; 141 -2.7; 155 -2.0; 170 -1.0; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -1.2; 365 -3.7; 402 -5.7; 442 -7.1; 486 -7.9; 535 -7.9; 588 -7.3; 647 -7.0; 712 -7.5; 783 -7.8; 861 -7.7; 947 -7.6; 1042 -7.4; 1146 -7.1; 1261 -7.0; 1387 -7.4; 1526 -7.7; 1678 -8.0; 1846 -7.7; 2031 -6.5; 2234 -4.7; 2457 -4.5; 2703 -6.4; 2973 -8.2; 3270 -8.8; 3597 -9.2; 3957 -10.6; 4353 -13.0; 4788 -14.2; 5267 -13.5; 5793 -13.5; 6373 -15.4; 7010 -15.4; 7711 -12.4; 8482 -8.9; 9330 -8.8; 10263 -11.0; 11289 -12.3; 12418 -12.0; 13660 -10.6; 15026 -9.0; 16529 -6.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 750 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.39 | 6.1 dB  |
| Peaking | 228 Hz   | 1.44 | 6.4 dB  |
| Peaking | 5885 Hz  | 1.31 | -8.5 dB |
| Peaking | 12360 Hz | 1.95 | -5.2 dB |
| Peaking | 22050 Hz | 2.23 | -3.9 dB |
| Peaking | 325 Hz   | 4.25 | 3.4 dB  |
| Peaking | 472 Hz   | 1.8  | -2.3 dB |
| Peaking | 2006 Hz  | 0.39 | -1.2 dB |
| Peaking | 2391 Hz  | 3.48 | 4.4 dB  |
| Peaking | 8174 Hz  | 2.64 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 7.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.8 dB |
| Peaking | 8000 Hz  | 1.41 | -6.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20PRO%20750/Ultrasone%20PRO%20750.png)