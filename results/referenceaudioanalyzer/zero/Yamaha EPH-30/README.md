# Yamaha EPH-30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -10.8; 25 -10.8; 28 -10.8; 31 -10.8; 34 -10.8; 37 -10.8; 41 -10.8; 45 -10.8; 49 -10.8; 54 -10.8; 60 -11.0; 66 -11.1; 72 -11.1; 79 -11.1; 87 -11.1; 96 -11.1; 106 -11.1; 116 -10.9; 128 -10.8; 141 -11.1; 155 -10.9; 170 -10.8; 187 -10.5; 206 -10.6; 227 -11.4; 249 -11.9; 274 -12.1; 302 -12.1; 332 -12.1; 365 -11.8; 402 -11.8; 442 -11.5; 486 -11.4; 535 -11.2; 588 -11.1; 647 -10.9; 712 -10.6; 783 -10.3; 861 -9.9; 947 -9.4; 1042 -8.7; 1146 -8.0; 1261 -7.0; 1387 -5.9; 1526 -4.8; 1678 -3.6; 1846 -2.2; 2031 -0.8; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.4; 6373 -7.5; 7010 -10.0; 7711 -7.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha EPH-30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha EPH-30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.51 | -3.8 dB |
| Peaking | 79 Hz    | 0.72 | -2.6 dB |
| Peaking | 562 Hz   | 0.31 | -6.2 dB |
| Peaking | 2840 Hz  | 0.52 | 8.7 dB  |
| Peaking | 7074 Hz  | 3.96 | -7.3 dB |
| Peaking | 194 Hz   | 8.1  | 0.7 dB  |
| Peaking | 2039 Hz  | 2.4  | 2.7 dB  |
| Peaking | 2355 Hz  | 0.97 | -1.8 dB |
| Peaking | 5309 Hz  | 4.27 | 2.6 dB  |
| Peaking | 10851 Hz | 1.32 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -4.3 dB |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Yamaha%20EPH-30/Yamaha%20EPH-30.png)