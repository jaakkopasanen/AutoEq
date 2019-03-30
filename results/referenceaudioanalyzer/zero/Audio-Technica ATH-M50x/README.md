# Audio-Technica ATH-M50x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.7; 25 -11.2; 28 -11.8; 31 -12.3; 34 -12.7; 37 -12.9; 41 -13.0; 45 -12.9; 49 -12.5; 54 -11.5; 60 -9.9; 66 -8.5; 72 -8.9; 79 -10.7; 87 -12.1; 96 -12.6; 106 -12.6; 116 -12.1; 128 -11.9; 141 -11.8; 155 -11.4; 170 -10.6; 187 -9.6; 206 -8.1; 227 -6.3; 249 -4.6; 274 -3.0; 302 -1.5; 332 -0.6; 365 -0.5; 402 -1.1; 442 -2.1; 486 -3.2; 535 -4.0; 588 -4.6; 647 -5.0; 712 -5.3; 783 -5.5; 861 -5.7; 947 -5.6; 1042 -5.4; 1146 -5.5; 1261 -6.0; 1387 -6.1; 1526 -5.5; 1678 -4.4; 1846 -3.3; 2031 -2.8; 2234 -3.3; 2457 -4.7; 2703 -6.3; 2973 -7.7; 3270 -9.1; 3597 -11.2; 3957 -13.1; 4353 -13.2; 4788 -11.5; 5267 -9.4; 5793 -8.3; 6373 -7.6; 7010 -6.4; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 1.11 | -6.3 dB |
| Peaking | 133 Hz  | 0.86 | -6.4 dB |
| Peaking | 340 Hz  | 1.32 | 7.6 dB  |
| Peaking | 2074 Hz | 2.53 | 4.3 dB  |
| Peaking | 4142 Hz | 2.36 | -7.6 dB |
| Peaking | 50 Hz   | 3.34 | -1.4 dB |
| Peaking | 68 Hz   | 3.09 | 3.2 dB  |
| Peaking | 90 Hz   | 2.06 | -2.0 dB |
| Peaking | 126 Hz  | 4.04 | 1.2 dB  |
| Peaking | 7421 Hz | 6.03 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -7.3 dB |
| Peaking | 250 Hz   | 1.41 | 3.2 dB  |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-M50x/Audio-Technica%20ATH-M50x.png)