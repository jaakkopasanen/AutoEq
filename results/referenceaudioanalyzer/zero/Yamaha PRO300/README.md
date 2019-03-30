# Yamaha PRO300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.0; 60 -1.5; 66 -1.9; 72 -2.2; 79 -2.7; 87 -3.3; 96 -3.8; 106 -4.2; 116 -4.6; 128 -5.1; 141 -5.6; 155 -6.0; 170 -6.3; 187 -6.5; 206 -6.4; 227 -6.0; 249 -5.2; 274 -4.4; 302 -4.4; 332 -4.8; 365 -5.4; 402 -6.1; 442 -6.9; 486 -7.3; 535 -7.1; 588 -6.9; 647 -7.2; 712 -7.7; 783 -8.1; 861 -8.5; 947 -9.1; 1042 -9.7; 1146 -10.3; 1261 -10.8; 1387 -11.1; 1526 -11.3; 1678 -11.6; 1846 -11.5; 2031 -10.7; 2234 -9.4; 2457 -7.9; 2703 -6.5; 2973 -5.4; 3270 -4.4; 3597 -3.2; 3957 -1.4; 4353 -0.5; 4788 -0.6; 5267 -4.4; 5793 -6.3; 6373 -5.6; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha PRO300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha PRO300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.52 | 6.6 dB  |
| Peaking | 304 Hz   | 3.83 | 2.3 dB  |
| Peaking | 1564 Hz  | 1.03 | -5.6 dB |
| Peaking | 4182 Hz  | 2.08 | 7.0 dB  |
| Peaking | 20943 Hz | 1.99 | -0.3 dB |
| Peaking | 15 Hz    | 2.04 | 1.4 dB  |
| Peaking | 178 Hz   | 3.68 | -1.1 dB |
| Peaking | 2088 Hz  | 3.12 | -1.8 dB |
| Peaking | 2331 Hz  | 1.7  | 1.4 dB  |
| Peaking | 5720 Hz  | 9.68 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Yamaha%20PRO300/Yamaha%20PRO300.png)