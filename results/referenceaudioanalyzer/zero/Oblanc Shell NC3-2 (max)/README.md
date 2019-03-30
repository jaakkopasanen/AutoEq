# Oblanc Shell NC3-2 (max)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -5.0; 25 -6.3; 28 -7.9; 31 -9.3; 34 -10.4; 37 -11.3; 41 -12.2; 45 -12.9; 49 -13.3; 54 -13.8; 60 -14.5; 66 -15.0; 72 -15.5; 79 -15.8; 87 -15.9; 96 -15.8; 106 -15.4; 116 -15.1; 128 -14.9; 141 -14.4; 155 -14.0; 170 -13.7; 187 -13.3; 206 -12.8; 227 -12.3; 249 -11.8; 274 -11.3; 302 -10.7; 332 -10.0; 365 -9.1; 402 -8.2; 442 -7.2; 486 -6.1; 535 -4.8; 588 -3.0; 647 -1.3; 712 -0.6; 783 -0.8; 861 -1.4; 947 -1.9; 1042 -2.4; 1146 -2.3; 1261 -1.4; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -1.3; 2973 -2.5; 3270 -4.4; 3597 -7.4; 3957 -10.1; 4353 -11.7; 4788 -12.8; 5267 -12.9; 5793 -10.8; 6373 -7.2; 7010 -5.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oblanc Shell NC3-2 (max) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oblanc Shell NC3-2 (max) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 70 Hz   | 0.82 | -5.7 dB  |
| Peaking | 165 Hz  | 0.44 | -6.0 dB  |
| Peaking | 686 Hz  | 2.01 | 5.2 dB   |
| Peaking | 2577 Hz | 0.45 | 8.5 dB   |
| Peaking | 4604 Hz | 1.51 | -13.1 dB |
| Peaking | 17 Hz   | 1.47 | 5.8 dB   |
| Peaking | 36 Hz   | 2.11 | -1.9 dB  |
| Peaking | 5664 Hz | 6.75 | -2.4 dB  |
| Peaking | 6762 Hz | 3    | 2.1 dB   |
| Peaking | 9855 Hz | 1.03 | -0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -8.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Oblanc%20Shell%20NC3-2%20(max)/Oblanc%20Shell%20NC3-2%20(max).png)