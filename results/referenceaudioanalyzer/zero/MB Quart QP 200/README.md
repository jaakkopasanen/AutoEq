# MB Quart QP 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.7; 60 -1.8; 66 -2.9; 72 -3.8; 79 -4.4; 87 -4.9; 96 -5.5; 106 -5.9; 116 -6.1; 128 -6.4; 141 -6.4; 155 -6.4; 170 -6.6; 187 -6.4; 206 -6.4; 227 -6.2; 249 -6.0; 274 -5.8; 302 -5.7; 332 -5.7; 365 -5.7; 402 -5.7; 442 -5.6; 486 -5.4; 535 -5.4; 588 -5.4; 647 -5.4; 712 -5.5; 783 -5.9; 861 -6.4; 947 -6.7; 1042 -7.2; 1146 -7.6; 1261 -7.6; 1387 -6.5; 1526 -4.8; 1678 -3.7; 1846 -4.4; 2031 -6.3; 2234 -8.6; 2457 -10.5; 2703 -10.7; 2973 -8.1; 3270 -3.5; 3597 -3.7; 3957 -5.9; 4353 -5.5; 4788 -3.5; 5267 -3.2; 5793 -5.0; 6373 -7.3; 7010 -9.7; 7711 -11.7; 8482 -12.1; 9330 -11.2; 10263 -10.3; 11289 -9.4; 12418 -7.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MB Quart QP 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MB Quart QP 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.74 | 6.9 dB  |
| Peaking | 1727 Hz | 5.68 | 3.2 dB  |
| Peaking | 2569 Hz | 3.96 | -6.3 dB |
| Peaking | 5652 Hz | 0.85 | 6.4 dB  |
| Peaking | 7983 Hz | 1.29 | -9.9 dB |
| Peaking | 31 Hz   | 3.74 | -0.7 dB |
| Peaking | 563 Hz  | 1.32 | 1.2 dB  |
| Peaking | 1176 Hz | 2.68 | -2.1 dB |
| Peaking | 2049 Hz | 1.18 | 1.2 dB  |
| Peaking | 2231 Hz | 3.1  | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/MB%20Quart%20QP%20200/MB%20Quart%20QP%20200.png)