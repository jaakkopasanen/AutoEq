# CyberHome KUBT 803
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.1; 23 -13.2; 25 -13.3; 28 -13.3; 31 -13.3; 34 -13.4; 37 -13.4; 41 -13.4; 45 -13.4; 49 -13.3; 54 -13.3; 60 -13.3; 66 -13.3; 72 -13.3; 79 -13.3; 87 -13.1; 96 -12.9; 106 -12.7; 116 -12.5; 128 -12.3; 141 -12.3; 155 -12.6; 170 -13.0; 187 -13.5; 206 -13.9; 227 -14.3; 249 -14.7; 274 -15.3; 302 -15.9; 332 -16.3; 365 -16.6; 402 -16.6; 442 -16.4; 486 -15.9; 535 -15.2; 588 -14.1; 647 -12.9; 712 -11.4; 783 -9.8; 861 -8.0; 947 -6.1; 1042 -3.7; 1146 -1.8; 1261 -1.0; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.6; 2703 -1.6; 2973 -1.3; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.9; 5793 -5.8; 6373 -8.3; 7010 -6.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`CyberHome KUBT 803 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `CyberHome KUBT 803 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 0.32 | -6.8 dB  |
| Peaking | 489 Hz  | 0.5  | -13.0 dB |
| Peaking | 1352 Hz | 0.62 | 11.2 dB  |
| Peaking | 4804 Hz | 1.42 | 6.1 dB   |
| Peaking | 6271 Hz | 2.98 | -6.1 dB  |
| Peaking | 143 Hz  | 5.11 | 0.5 dB   |
| Peaking | 1154 Hz | 3.59 | 1.9 dB   |
| Peaking | 1229 Hz | 1.06 | -1.7 dB  |
| Peaking | 1581 Hz | 0.48 | 0.7 dB   |
| Peaking | 9908 Hz | 1.96 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -5.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -6.4 dB  |
| Peaking | 500 Hz   | 1.41 | -10.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/CyberHome%20KUBT%20803/CyberHome%20KUBT%20803.png)