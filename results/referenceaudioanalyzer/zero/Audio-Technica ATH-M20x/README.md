# Audio-Technica ATH-M20x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.9; 25 -3.7; 28 -4.8; 31 -5.8; 34 -6.7; 37 -7.6; 41 -8.8; 45 -9.7; 49 -10.5; 54 -11.3; 60 -11.9; 66 -12.0; 72 -11.7; 79 -11.1; 87 -10.5; 96 -9.9; 106 -9.8; 116 -9.5; 128 -9.4; 141 -8.9; 155 -8.1; 170 -6.9; 187 -5.1; 206 -3.0; 227 -1.1; 249 -0.5; 274 -1.4; 302 -2.6; 332 -3.4; 365 -4.1; 402 -4.7; 442 -5.1; 486 -5.4; 535 -5.8; 588 -5.9; 647 -6.2; 712 -6.2; 783 -5.9; 861 -5.9; 947 -5.9; 1042 -5.9; 1146 -6.4; 1261 -6.7; 1387 -7.1; 1526 -7.4; 1678 -7.7; 1846 -8.0; 2031 -8.5; 2234 -8.9; 2457 -9.1; 2703 -8.6; 2973 -7.7; 3270 -6.4; 3597 -5.1; 3957 -4.6; 4353 -5.3; 4788 -7.1; 5267 -7.4; 5793 -6.9; 6373 -8.7; 7010 -8.9; 7711 -6.1; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M20x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M20x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.69 | 8.1 dB  |
| Peaking | 54 Hz   | 0.41 | -7.8 dB |
| Peaking | 247 Hz  | 1.84 | 7.3 dB  |
| Peaking | 2210 Hz | 1.95 | -3.3 dB |
| Peaking | 6676 Hz | 5.21 | -3.5 dB |
| Peaking | 97 Hz   | 4.9  | 1.0 dB  |
| Peaking | 152 Hz  | 4.02 | -0.9 dB |
| Peaking | 2878 Hz | 3.52 | -1.4 dB |
| Peaking | 3974 Hz | 2.17 | 2.6 dB  |
| Peaking | 4918 Hz | 4.35 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -6.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | 5.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-M20x/Audio-Technica%20ATH-M20x.png)