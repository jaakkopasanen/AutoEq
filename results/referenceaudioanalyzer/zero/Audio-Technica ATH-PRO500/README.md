# Audio-Technica ATH-PRO500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.2; 37 -2.1; 41 -3.2; 45 -4.0; 49 -4.6; 54 -5.1; 60 -5.3; 66 -5.7; 72 -6.4; 79 -7.0; 87 -7.5; 96 -7.8; 106 -8.1; 116 -8.3; 128 -8.5; 141 -8.5; 155 -8.5; 170 -8.3; 187 -8.0; 206 -7.6; 227 -6.9; 249 -5.9; 274 -4.3; 302 -2.8; 332 -2.2; 365 -2.4; 402 -3.2; 442 -4.2; 486 -5.3; 535 -6.3; 588 -6.9; 647 -7.2; 712 -7.2; 783 -7.2; 861 -7.2; 947 -7.1; 1042 -7.3; 1146 -7.5; 1261 -7.5; 1387 -7.4; 1526 -7.1; 1678 -6.8; 1846 -6.4; 2031 -6.1; 2234 -5.7; 2457 -5.4; 2703 -4.6; 2973 -2.3; 3270 -0.5; 3597 -1.7; 3957 -4.2; 4353 -7.7; 4788 -11.4; 5267 -12.8; 5793 -11.9; 6373 -9.5; 7010 -6.9; 7711 -6.2; 8482 -6.5; 9330 -7.7; 10263 -9.4; 11289 -10.6; 12418 -12.0; 13660 -13.1; 15026 -12.4; 16529 -9.9; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-PRO500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-PRO500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 1.55 | 7.0 dB  |
| Peaking | 348 Hz   | 3.44 | 5.0 dB  |
| Peaking | 3367 Hz  | 3.14 | 7.2 dB  |
| Peaking | 5226 Hz  | 3.4  | -7.4 dB |
| Peaking | 13952 Hz | 1.37 | -7.2 dB |
| Peaking | 50 Hz    | 1.1  | 1.3 dB  |
| Peaking | 173 Hz   | 0.6  | -3.7 dB |
| Peaking | 288 Hz   | 0.97 | 3.1 dB  |
| Peaking | 1008 Hz  | 0.97 | -1.1 dB |
| Peaking | 7794 Hz  | 4.85 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | -6.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-PRO500/Audio-Technica%20ATH-PRO500.png)