# Sony MDR-1A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -9.8; 25 -9.7; 28 -9.5; 31 -9.2; 34 -8.9; 37 -8.6; 41 -8.2; 45 -8.1; 49 -8.5; 54 -9.5; 60 -10.6; 66 -11.0; 72 -11.5; 79 -12.4; 87 -13.0; 96 -13.1; 106 -12.8; 116 -12.2; 128 -11.4; 141 -10.5; 155 -9.4; 170 -8.2; 187 -6.9; 206 -5.4; 227 -4.1; 249 -3.4; 274 -3.0; 302 -2.2; 332 -1.4; 365 -0.7; 402 -0.5; 442 -0.5; 486 -0.7; 535 -1.0; 588 -1.3; 647 -1.6; 712 -1.8; 783 -1.8; 861 -1.8; 947 -1.7; 1042 -1.4; 1146 -1.1; 1261 -0.9; 1387 -0.7; 1526 -0.5; 1678 -0.5; 1846 -0.7; 2031 -1.1; 2234 -1.4; 2457 -1.7; 2703 -2.9; 2973 -5.1; 3270 -6.3; 3597 -6.5; 3957 -7.1; 4353 -7.5; 4788 -6.5; 5267 -5.3; 5793 -5.0; 6373 -5.7; 7010 -5.5; 7711 -3.5; 8482 -3.6; 9330 -3.6; 10263 -3.6; 11289 -3.6; 12418 -3.6; 13660 -3.6; 15026 -3.6; 16529 -3.6; 18182 -3.6; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 17 Hz   | 0.56 | -5.8 dB  |
| Peaking | 103 Hz  | 0.83 | -10.9 dB |
| Peaking | 715 Hz  | 0.15 | 3.5 dB   |
| Peaking | 4097 Hz | 1.36 | -5.8 dB  |
| Peaking | 166 Hz  | 3.98 | -1.0 dB  |
| Peaking | 398 Hz  | 1.56 | 1.5 dB   |
| Peaking | 780 Hz  | 1.23 | -1.6 dB  |
| Peaking | 1804 Hz | 1.73 | 1.0 dB   |
| Peaking | 6731 Hz | 8.77 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -8.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.6 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-1A/Sony%20MDR-1A.png)