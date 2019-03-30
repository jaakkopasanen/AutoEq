# Sony MDR-XB300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.6; 28 -2.9; 31 -4.1; 34 -5.1; 37 -5.9; 41 -6.8; 45 -7.5; 49 -8.0; 54 -8.7; 60 -9.6; 66 -10.3; 72 -10.7; 79 -11.0; 87 -11.4; 96 -11.6; 106 -11.8; 116 -11.7; 128 -11.4; 141 -10.9; 155 -10.4; 170 -10.0; 187 -9.7; 206 -9.2; 227 -8.7; 249 -8.2; 274 -7.7; 302 -7.2; 332 -6.6; 365 -5.6; 402 -4.6; 442 -3.7; 486 -2.8; 535 -2.2; 588 -1.7; 647 -1.2; 712 -0.9; 783 -1.3; 861 -2.7; 947 -4.7; 1042 -6.5; 1146 -7.8; 1261 -8.9; 1387 -9.6; 1526 -9.8; 1678 -9.5; 1846 -9.1; 2031 -8.7; 2234 -8.3; 2457 -7.8; 2703 -7.1; 2973 -6.2; 3270 -5.2; 3597 -4.3; 3957 -3.6; 4353 -3.0; 4788 -1.7; 5267 -1.7; 5793 -8.3; 6373 -12.3; 7010 -11.6; 7711 -7.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.22 | 6.5 dB  |
| Peaking | 102 Hz  | 0.64 | -5.6 dB |
| Peaking | 616 Hz  | 1.9  | 6.4 dB  |
| Peaking | 5007 Hz | 2.95 | 7.4 dB  |
| Peaking | 6399 Hz | 3.64 | -8.6 dB |
| Peaking | 444 Hz  | 2.79 | 1.5 dB  |
| Peaking | 619 Hz  | 3.39 | -2.2 dB |
| Peaking | 806 Hz  | 2.1  | 4.1 dB  |
| Peaking | 1443 Hz | 0.97 | -4.2 dB |
| Peaking | 3585 Hz | 3.01 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 5.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-XB300/Sony%20MDR-XB300.png)