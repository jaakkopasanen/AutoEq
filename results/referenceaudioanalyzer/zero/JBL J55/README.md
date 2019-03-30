# JBL J55
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.8; 23 -13.8; 25 -13.8; 28 -13.8; 31 -13.8; 34 -13.8; 37 -13.8; 41 -13.8; 45 -13.8; 49 -13.9; 54 -14.1; 60 -14.1; 66 -14.1; 72 -14.1; 79 -14.1; 87 -14.3; 96 -14.5; 106 -14.7; 116 -14.7; 128 -14.7; 141 -14.7; 155 -14.4; 170 -13.8; 187 -12.8; 206 -11.6; 227 -11.4; 249 -12.3; 274 -13.1; 302 -13.4; 332 -13.3; 365 -12.6; 402 -11.4; 442 -9.8; 486 -8.4; 535 -7.1; 588 -6.1; 647 -5.5; 712 -5.3; 783 -5.6; 861 -6.2; 947 -6.8; 1042 -7.0; 1146 -6.6; 1261 -6.0; 1387 -6.2; 1526 -7.2; 1678 -6.7; 1846 -3.5; 2031 -2.1; 2234 -4.3; 2457 -4.5; 2703 -2.4; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.5; 5793 -5.4; 6373 -6.0; 7010 -5.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL J55 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL J55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.29 | -7.2 dB |
| Peaking | 135 Hz  | 1.01 | -5.1 dB |
| Peaking | 326 Hz  | 2.36 | -5.6 dB |
| Peaking | 3310 Hz | 1.47 | 6.0 dB  |
| Peaking | 4775 Hz | 4.29 | 4.0 dB  |
| Peaking | 417 Hz  | 4.88 | -1.2 dB |
| Peaking | 661 Hz  | 2.68 | 2.1 dB  |
| Peaking | 1868 Hz | 2.21 | -3.4 dB |
| Peaking | 1948 Hz | 5.54 | 6.6 dB  |
| Peaking | 8275 Hz | 1.46 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JBL%20J55/JBL%20J55.png)