# Focal Spirit One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.3; 25 -3.9; 28 -4.7; 31 -5.2; 34 -5.6; 37 -5.9; 41 -6.1; 45 -6.3; 49 -6.4; 54 -6.3; 60 -6.1; 66 -6.5; 72 -7.5; 79 -8.8; 87 -9.8; 96 -10.1; 106 -10.1; 116 -10.1; 128 -10.3; 141 -10.5; 155 -10.3; 170 -9.9; 187 -9.2; 206 -8.5; 227 -7.6; 249 -6.6; 274 -5.7; 302 -5.6; 332 -6.0; 365 -6.7; 402 -6.9; 442 -6.9; 486 -7.1; 535 -7.2; 588 -7.2; 647 -7.0; 712 -6.8; 783 -6.5; 861 -5.9; 947 -5.2; 1042 -5.0; 1146 -4.8; 1261 -4.2; 1387 -3.5; 1526 -3.0; 1678 -2.5; 1846 -2.2; 2031 -1.9; 2234 -1.6; 2457 -1.3; 2703 -1.0; 2973 -0.5; 3270 -0.8; 3597 -2.3; 3957 -4.8; 4353 -7.3; 4788 -9.1; 5267 -9.2; 5793 -7.1; 6373 -5.5; 7010 -6.2; 7711 -6.4; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.6  | 3.9 dB  |
| Peaking | 125 Hz  | 1.05 | -5.1 dB |
| Peaking | 618 Hz  | 1.88 | -1.8 dB |
| Peaking | 3041 Hz | 0.79 | 6.5 dB  |
| Peaking | 4869 Hz | 2.05 | -7.5 dB |
| Peaking | 90 Hz   | 2.73 | -3.4 dB |
| Peaking | 96 Hz   | 1.21 | 2.9 dB  |
| Peaking | 196 Hz  | 0.76 | -1.5 dB |
| Peaking | 281 Hz  | 2.78 | 2.4 dB  |
| Peaking | 7480 Hz | 6.82 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Focal%20Spirit%20One/Focal%20Spirit%20One.png)