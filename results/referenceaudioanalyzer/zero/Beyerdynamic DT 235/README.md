# Beyerdynamic DT 235
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.8; 49 -2.9; 54 -4.1; 60 -5.2; 66 -6.1; 72 -6.8; 79 -7.3; 87 -7.7; 96 -7.9; 106 -8.3; 116 -8.5; 128 -8.4; 141 -8.2; 155 -8.7; 170 -8.9; 187 -8.7; 206 -8.5; 227 -8.3; 249 -8.5; 274 -8.6; 302 -8.8; 332 -8.8; 365 -8.8; 402 -8.5; 442 -8.2; 486 -8.2; 535 -8.5; 588 -8.8; 647 -9.2; 712 -9.6; 783 -9.8; 861 -9.8; 947 -9.1; 1042 -7.7; 1146 -5.9; 1261 -4.4; 1387 -3.4; 1526 -4.8; 1678 -7.3; 1846 -8.0; 2031 -6.5; 2234 -4.0; 2457 -2.3; 2703 -1.7; 2973 -1.7; 3270 -2.1; 3597 -3.3; 3957 -3.8; 4353 -4.7; 4788 -8.1; 5267 -9.7; 5793 -8.0; 6373 -4.5; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 235 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 235 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.82 | 8.2 dB  |
| Peaking | 301 Hz  | 0.1  | -2.7 dB |
| Peaking | 1338 Hz | 4.89 | 5.1 dB  |
| Peaking | 2991 Hz | 1.55 | 6.5 dB  |
| Peaking | 5155 Hz | 6.93 | -4.7 dB |
| Peaking | 797 Hz  | 0.86 | 2.9 dB  |
| Peaking | 803 Hz  | 1.73 | -4.2 dB |
| Peaking | 1849 Hz | 5.19 | -2.6 dB |
| Peaking | 2386 Hz | 6.93 | 1.2 dB  |
| Peaking | 6759 Hz | 8.87 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20235/Beyerdynamic%20DT%20235.png)