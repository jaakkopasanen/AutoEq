# Skullcandy SK Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -1.0; 37 -2.1; 41 -3.9; 45 -5.3; 49 -6.4; 54 -7.4; 60 -8.1; 66 -8.4; 72 -8.2; 79 -8.1; 87 -8.1; 96 -8.1; 106 -8.1; 116 -7.9; 128 -7.6; 141 -7.5; 155 -7.3; 170 -7.1; 187 -7.2; 206 -7.2; 227 -6.9; 249 -6.8; 274 -7.0; 302 -7.2; 332 -7.5; 365 -7.5; 402 -7.8; 442 -7.9; 486 -8.1; 535 -8.4; 588 -8.5; 647 -8.8; 712 -8.8; 783 -8.5; 861 -7.9; 947 -6.7; 1042 -5.1; 1146 -3.8; 1261 -4.6; 1387 -6.7; 1526 -8.1; 1678 -8.5; 1846 -7.8; 2031 -6.6; 2234 -5.1; 2457 -3.8; 2703 -3.0; 2973 -2.4; 3270 -2.2; 3597 -2.6; 3957 -4.4; 4353 -7.0; 4788 -9.3; 5267 -11.0; 5793 -13.5; 6373 -13.9; 7010 -10.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy SK Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy SK Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 1.45 | 8.3 dB  |
| Peaking | 252 Hz  | 0.06 | -1.6 dB |
| Peaking | 1149 Hz | 5.49 | 4.5 dB  |
| Peaking | 3145 Hz | 1.99 | 6.2 dB  |
| Peaking | 5938 Hz | 3.3  | -8.4 dB |
| Peaking | 20 Hz   | 0.27 | 0.8 dB  |
| Peaking | 65 Hz   | 1.72 | -1.8 dB |
| Peaking | 233 Hz  | 1.78 | 1.2 dB  |
| Peaking | 1675 Hz | 5.91 | -1.8 dB |
| Peaking | 7675 Hz | 8.07 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Skullcandy%20SK%20Pro/Skullcandy%20SK%20Pro.png)