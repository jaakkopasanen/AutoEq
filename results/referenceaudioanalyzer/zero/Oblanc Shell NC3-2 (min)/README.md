# Oblanc Shell NC3-2 (min)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -1.0; 31 -2.0; 34 -3.1; 37 -4.1; 41 -5.0; 45 -5.6; 49 -6.0; 54 -6.6; 60 -7.1; 66 -7.8; 72 -8.5; 79 -9.1; 87 -9.6; 96 -9.9; 106 -10.0; 116 -10.0; 128 -9.7; 141 -9.4; 155 -9.2; 170 -8.9; 187 -8.7; 206 -8.5; 227 -8.2; 249 -8.0; 274 -7.8; 302 -7.6; 332 -7.3; 365 -6.8; 402 -6.3; 442 -5.8; 486 -5.3; 535 -4.4; 588 -3.3; 647 -2.2; 712 -2.1; 783 -2.7; 861 -3.6; 947 -4.2; 1042 -4.7; 1146 -4.7; 1261 -3.8; 1387 -2.5; 1526 -1.4; 1678 -0.6; 1846 -0.5; 2031 -0.5; 2234 -0.6; 2457 -2.0; 2703 -3.6; 2973 -4.7; 3270 -6.6; 3597 -9.6; 3957 -12.3; 4353 -14.0; 4788 -15.0; 5267 -15.1; 5793 -13.1; 6373 -9.4; 7010 -8.1; 7711 -8.1; 8482 -7.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oblanc Shell NC3-2 (min) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oblanc Shell NC3-2 (min) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.84 | 6.7 dB   |
| Peaking | 107 Hz  | 0.6  | -3.9 dB  |
| Peaking | 672 Hz  | 2.32 | 4.3 dB   |
| Peaking | 2031 Hz | 1.22 | 7.2 dB   |
| Peaking | 4746 Hz | 1.86 | -10.4 dB |
| Peaking | 3136 Hz | 4.4  | 0.8 dB   |
| Peaking | 3163 Hz | 1.02 | -0.9 dB  |
| Peaking | 3900 Hz | 3.68 | -2.5 dB  |
| Peaking | 4722 Hz | 1.06 | 2.8 dB   |
| Peaking | 5519 Hz | 4.99 | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -8.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Oblanc%20Shell%20NC3-2%20(min)/Oblanc%20Shell%20NC3-2%20(min).png)