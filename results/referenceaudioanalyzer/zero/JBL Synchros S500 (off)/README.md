# JBL Synchros S500 (off)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.1; 23 -15.0; 25 -14.8; 28 -14.6; 31 -14.3; 34 -14.0; 37 -13.7; 41 -13.3; 45 -13.2; 49 -13.1; 54 -13.2; 60 -13.6; 66 -14.5; 72 -15.5; 79 -16.2; 87 -16.3; 96 -16.0; 106 -15.6; 116 -15.1; 128 -14.5; 141 -13.8; 155 -13.0; 170 -11.9; 187 -10.8; 206 -9.7; 227 -8.6; 249 -8.0; 274 -7.4; 302 -6.4; 332 -4.9; 365 -3.5; 402 -2.3; 442 -1.3; 486 -0.7; 535 -0.5; 588 -0.6; 647 -1.0; 712 -1.6; 783 -2.8; 861 -4.4; 947 -5.5; 1042 -5.7; 1146 -5.0; 1261 -3.7; 1387 -2.6; 1526 -2.5; 1678 -2.5; 1846 -2.6; 2031 -3.0; 2234 -3.4; 2457 -3.8; 2703 -4.8; 2973 -6.2; 3270 -6.7; 3597 -6.7; 3957 -7.4; 4353 -7.9; 4788 -7.3; 5267 -6.7; 5793 -7.9; 6373 -10.3; 7010 -10.2; 7711 -6.7; 8482 -6.1; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Synchros S500 (off) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Synchros S500 (off) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.91 | -6.7 dB |
| Peaking | 98 Hz   | 0.66 | -9.6 dB |
| Peaking | 509 Hz  | 1.28 | 7.0 dB  |
| Peaking | 1746 Hz | 2.23 | 3.9 dB  |
| Peaking | 14 Hz   | 1.19 | -2.4 dB |
| Peaking | 1000 Hz | 4.63 | -2.2 dB |
| Peaking | 2873 Hz | 0.26 | 0.8 dB  |
| Peaking | 4077 Hz | 2.04 | -2.3 dB |
| Peaking | 6630 Hz | 4.66 | -5.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.1 dB |
| Peaking | 125 Hz   | 1.41 | -8.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 6.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JBL%20Synchros%20S500%20(off)/JBL%20Synchros%20S500%20(off).png)