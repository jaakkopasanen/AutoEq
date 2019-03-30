# Sony MDR-7506
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.7; 34 -2.6; 37 -3.3; 41 -4.0; 45 -4.4; 49 -4.6; 54 -4.5; 60 -4.2; 66 -4.1; 72 -4.3; 79 -4.7; 87 -5.0; 96 -5.3; 106 -5.4; 116 -5.3; 128 -5.0; 141 -4.4; 155 -3.9; 170 -3.3; 187 -2.7; 206 -2.2; 227 -2.2; 249 -2.5; 274 -2.4; 302 -2.4; 332 -2.5; 365 -3.2; 402 -4.2; 442 -4.9; 486 -5.3; 535 -5.6; 588 -5.7; 647 -5.7; 712 -5.7; 783 -5.7; 861 -5.7; 947 -5.6; 1042 -5.4; 1146 -5.4; 1261 -5.4; 1387 -5.7; 1526 -6.1; 1678 -6.5; 1846 -6.9; 2031 -7.4; 2234 -8.0; 2457 -8.3; 2703 -8.5; 2973 -8.4; 3270 -8.3; 3597 -8.7; 3957 -10.6; 4353 -12.3; 4788 -12.3; 5267 -10.4; 5793 -8.3; 6373 -8.7; 7010 -10.4; 7711 -11.6; 8482 -12.3; 9330 -13.3; 10263 -14.1; 11289 -12.4; 12418 -7.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7506 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.14 | 6.3 dB  |
| Peaking | 65 Hz    | 3.43 | 1.4 dB  |
| Peaking | 252 Hz   | 0.91 | 4.4 dB  |
| Peaking | 4453 Hz  | 2.31 | -5.4 dB |
| Peaking | 9698 Hz  | 1.86 | -7.7 dB |
| Peaking | 1209 Hz  | 2.43 | 1.2 dB  |
| Peaking | 2426 Hz  | 3.15 | -1.4 dB |
| Peaking | 5958 Hz  | 7    | 1.6 dB  |
| Peaking | 7375 Hz  | 5.31 | -1.4 dB |
| Peaking | 13264 Hz | 4.41 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 4.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | -6.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-7506/Sony%20MDR-7506.png)