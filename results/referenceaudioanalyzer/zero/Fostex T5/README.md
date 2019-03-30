# Fostex T5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.7; 54 -2.7; 60 -3.6; 66 -4.3; 72 -4.7; 79 -5.1; 87 -5.4; 96 -5.4; 106 -5.5; 116 -5.5; 128 -5.4; 141 -5.4; 155 -5.2; 170 -5.0; 187 -4.7; 206 -4.5; 227 -4.2; 249 -4.0; 274 -3.8; 302 -3.7; 332 -3.7; 365 -3.7; 402 -3.7; 442 -3.8; 486 -4.0; 535 -4.4; 588 -5.2; 647 -6.4; 712 -7.5; 783 -7.6; 861 -6.8; 947 -7.2; 1042 -8.6; 1146 -8.7; 1261 -7.6; 1387 -6.2; 1526 -4.9; 1678 -3.8; 1846 -3.1; 2031 -3.1; 2234 -3.7; 2457 -4.9; 2703 -6.2; 2973 -7.7; 3270 -9.2; 3597 -10.5; 3957 -11.2; 4353 -11.3; 4788 -11.1; 5267 -11.0; 5793 -11.7; 6373 -11.9; 7010 -10.5; 7711 -8.5; 8482 -7.5; 9330 -7.7; 10263 -8.2; 11289 -8.9; 12418 -11.0; 13660 -12.6; 15026 -10.2; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.76 | 6.7 dB  |
| Peaking | 320 Hz   | 1.21 | 3.1 dB  |
| Peaking | 2086 Hz  | 2.4  | 5.3 dB  |
| Peaking | 4745 Hz  | 0.88 | -5.4 dB |
| Peaking | 13653 Hz | 2.62 | -6.3 dB |
| Peaking | 742 Hz   | 3.62 | -3.2 dB |
| Peaking | 938 Hz   | 0.88 | 2.4 dB  |
| Peaking | 1098 Hz  | 2.97 | -4.8 dB |
| Peaking | 6490 Hz  | 5.66 | -1.9 dB |
| Peaking | 8388 Hz  | 3.76 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.9 dB |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fostex%20T5/Fostex%20T5.png)