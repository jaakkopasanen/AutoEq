# Audio-Technica ATH-ES7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.8; 60 -1.6; 66 -2.0; 72 -2.2; 79 -2.3; 87 -2.6; 96 -2.9; 106 -3.1; 116 -3.4; 128 -3.5; 141 -3.7; 155 -3.6; 170 -3.4; 187 -3.1; 206 -3.1; 227 -2.8; 249 -2.8; 274 -2.9; 302 -3.1; 332 -3.0; 365 -2.5; 402 -2.0; 442 -1.1; 486 -0.5; 535 -0.5; 588 -0.5; 647 -2.3; 712 -5.6; 783 -8.2; 861 -9.9; 947 -10.9; 1042 -11.3; 1146 -11.6; 1261 -11.9; 1387 -12.1; 1526 -12.4; 1678 -12.5; 1846 -12.5; 2031 -12.2; 2234 -11.7; 2457 -10.8; 2703 -9.4; 2973 -8.2; 3270 -7.3; 3597 -7.2; 3957 -8.5; 4353 -10.3; 4788 -10.3; 5267 -7.5; 5793 -3.0; 6373 -1.5; 7010 -5.2; 7711 -9.4; 8482 -11.6; 9330 -10.8; 10263 -8.0; 11289 -6.9; 12418 -9.5; 13660 -12.6; 15026 -12.2; 16529 -8.3; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ES7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ES7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.16 | 6.2 dB   |
| Peaking | 560 Hz   | 0.86 | 12.8 dB  |
| Peaking | 1002 Hz  | 0.57 | -11.1 dB |
| Peaking | 14271 Hz | 1.85 | -6.7 dB  |
| Peaking | 22050 Hz | 1.99 | -4.1 dB  |
| Peaking | 2133 Hz  | 3.09 | -1.7 dB  |
| Peaking | 3429 Hz  | 2.49 | 2.6 dB   |
| Peaking | 4672 Hz  | 2.9  | -4.8 dB  |
| Peaking | 6185 Hz  | 3.3  | 7.9 dB   |
| Peaking | 8430 Hz  | 3.73 | -5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 1.8 dB  |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 7.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.6 dB |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-ES7/Audio-Technica%20ATH-ES7.png)