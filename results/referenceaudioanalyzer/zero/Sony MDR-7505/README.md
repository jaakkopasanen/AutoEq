# Sony MDR-7505
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.7; 96 -1.4; 106 -2.3; 116 -3.0; 128 -3.7; 141 -4.2; 155 -4.6; 170 -4.9; 187 -5.1; 206 -5.3; 227 -4.9; 249 -4.6; 274 -4.7; 302 -5.3; 332 -5.8; 365 -5.7; 402 -5.6; 442 -5.7; 486 -6.0; 535 -6.1; 588 -5.8; 647 -5.8; 712 -6.7; 783 -7.4; 861 -7.7; 947 -7.9; 1042 -8.0; 1146 -8.4; 1261 -8.9; 1387 -9.2; 1526 -9.1; 1678 -8.3; 1846 -7.5; 2031 -6.8; 2234 -6.2; 2457 -5.6; 2703 -5.3; 2973 -5.3; 3270 -5.5; 3597 -6.2; 3957 -7.4; 4353 -8.6; 4788 -9.0; 5267 -8.8; 5793 -9.2; 6373 -10.5; 7010 -11.1; 7711 -10.2; 8482 -7.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -6.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7505 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7505 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.25 | 6.1 dB  |
| Peaking | 80 Hz   | 2.25 | 1.8 dB  |
| Peaking | 1372 Hz | 1.7  | -2.9 dB |
| Peaking | 2735 Hz | 2.38 | 2.1 dB  |
| Peaking | 6516 Hz | 1.9  | -4.5 dB |
| Peaking | 264 Hz  | 6.51 | 0.9 dB  |
| Peaking | 693 Hz  | 1.71 | 1.4 dB  |
| Peaking | 802 Hz  | 2.81 | -1.8 dB |
| Peaking | 4486 Hz | 7.21 | -1.5 dB |
| Peaking | 9262 Hz | 5.13 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 5.5 dB  |
| Peaking | 125 Hz   | 1.41 | 2.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-7505/Sony%20MDR-7505.png)