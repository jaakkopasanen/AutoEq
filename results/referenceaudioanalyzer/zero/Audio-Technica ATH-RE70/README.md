# Audio-Technica ATH-RE70
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.9; 60 -3.1; 66 -4.1; 72 -5.0; 79 -5.8; 87 -6.4; 96 -6.8; 106 -7.1; 116 -7.4; 128 -7.4; 141 -7.3; 155 -7.1; 170 -7.0; 187 -6.7; 206 -6.3; 227 -5.9; 249 -5.5; 274 -5.4; 302 -5.0; 332 -4.6; 365 -3.9; 402 -3.4; 442 -2.8; 486 -2.3; 535 -1.6; 588 -0.9; 647 -1.0; 712 -2.5; 783 -4.3; 861 -5.8; 947 -6.7; 1042 -7.3; 1146 -7.7; 1261 -8.2; 1387 -8.8; 1526 -9.3; 1678 -9.7; 1846 -10.3; 2031 -10.6; 2234 -10.4; 2457 -9.2; 2703 -7.5; 2973 -5.9; 3270 -4.9; 3597 -4.1; 3957 -3.6; 4353 -4.0; 4788 -5.1; 5267 -5.9; 5793 -7.7; 6373 -10.0; 7010 -12.4; 7711 -13.1; 8482 -11.0; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-RE70 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-RE70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 1.02 | 7.1 dB  |
| Peaking | 578 Hz   | 1.49 | 6.3 dB  |
| Peaking | 2254 Hz  | 0.81 | -8.3 dB |
| Peaking | 3467 Hz  | 0.89 | 7.9 dB  |
| Peaking | 7352 Hz  | 2.53 | -8.2 dB |
| Peaking | 53 Hz    | 2.85 | 2.2 dB  |
| Peaking | 119 Hz   | 0.97 | -1.8 dB |
| Peaking | 321 Hz   | 1.08 | 0.8 dB  |
| Peaking | 522 Hz   | 6.42 | -0.9 dB |
| Peaking | 10048 Hz | 6.03 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 5.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-RE70/Audio-Technica%20ATH-RE70.png)