# Sony Fake MDR-V700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -2.8; 25 -4.1; 28 -5.8; 31 -7.1; 34 -8.2; 37 -9.1; 41 -10.0; 45 -10.7; 49 -11.1; 54 -11.3; 60 -11.3; 66 -11.3; 72 -11.3; 79 -11.3; 87 -11.3; 96 -11.2; 106 -11.0; 116 -11.0; 128 -10.9; 141 -10.7; 155 -10.7; 170 -10.4; 187 -10.3; 206 -10.4; 227 -10.7; 249 -10.7; 274 -10.4; 302 -9.9; 332 -9.3; 365 -8.9; 402 -8.7; 442 -8.7; 486 -8.6; 535 -8.2; 588 -7.7; 647 -7.4; 712 -6.9; 783 -5.6; 861 -4.6; 947 -5.4; 1042 -7.4; 1146 -8.9; 1261 -9.7; 1387 -9.5; 1526 -8.4; 1678 -7.1; 1846 -5.6; 2031 -3.3; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -1.0; 3270 -0.6; 3597 -0.5; 3957 -1.7; 4353 -3.8; 4788 -3.3; 5267 -2.0; 5793 -3.0; 6373 -6.2; 7010 -7.5; 7711 -6.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony Fake MDR-V700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony Fake MDR-V700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.17 | 8.1 dB  |
| Peaking | 51 Hz   | 0.53 | -5.2 dB |
| Peaking | 224 Hz  | 0.53 | -3.1 dB |
| Peaking | 2421 Hz | 4.13 | 4.9 dB  |
| Peaking | 3585 Hz | 1.71 | 5.7 dB  |
| Peaking | 871 Hz  | 4.12 | 3.3 dB  |
| Peaking | 1306 Hz | 2.72 | -4.0 dB |
| Peaking | 4455 Hz | 3.64 | -4.1 dB |
| Peaking | 5405 Hz | 1.69 | 5.7 dB  |
| Peaking | 6726 Hz | 2.5  | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20Fake%20MDR-V700/Sony%20Fake%20MDR-V700.png)