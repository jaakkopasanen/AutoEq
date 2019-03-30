# Audio-Technica ATH-TAD400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -1.4; 72 -2.0; 79 -2.7; 87 -3.4; 96 -3.9; 106 -4.2; 116 -4.5; 128 -4.6; 141 -4.9; 155 -4.9; 170 -4.6; 187 -4.6; 206 -4.5; 227 -4.2; 249 -4.2; 274 -4.2; 302 -4.2; 332 -4.2; 365 -4.2; 402 -4.0; 442 -3.9; 486 -4.1; 535 -4.3; 588 -4.2; 647 -4.2; 712 -4.3; 783 -4.6; 861 -4.7; 947 -4.9; 1042 -5.3; 1146 -5.6; 1261 -5.8; 1387 -5.9; 1526 -6.2; 1678 -6.5; 1846 -7.1; 2031 -8.2; 2234 -9.6; 2457 -10.6; 2703 -10.8; 2973 -10.1; 3270 -8.6; 3597 -6.5; 3957 -4.6; 4353 -4.5; 4788 -6.0; 5267 -10.5; 5793 -15.6; 6373 -17.3; 7010 -15.6; 7711 -11.9; 8482 -8.4; 9330 -6.5; 10263 -6.5; 11289 -7.6; 12418 -7.8; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-TAD400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-TAD400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.52 | 6.6 dB   |
| Peaking | 516 Hz   | 0.48 | 2.4 dB   |
| Peaking | 2668 Hz  | 1.98 | -5.1 dB  |
| Peaking | 4305 Hz  | 2.53 | 5.7 dB   |
| Peaking | 6305 Hz  | 2.62 | -12.5 dB |
| Peaking | 61 Hz    | 0.95 | -1.5 dB  |
| Peaking | 61 Hz    | 1.95 | 2.4 dB   |
| Peaking | 7376 Hz  | 6.82 | -1.6 dB  |
| Peaking | 9208 Hz  | 4.4  | 2.1 dB   |
| Peaking | 21003 Hz | 1.64 | 0.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-TAD400/Audio-Technica%20ATH-TAD400.png)