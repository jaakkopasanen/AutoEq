# Fischer Audio Spiritoso
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.9; 25 -13.0; 28 -13.1; 31 -13.1; 34 -13.1; 37 -13.1; 41 -13.1; 45 -13.0; 49 -12.9; 54 -12.8; 60 -12.7; 66 -12.6; 72 -12.4; 79 -12.4; 87 -12.1; 96 -11.9; 106 -11.7; 116 -11.4; 128 -11.1; 141 -10.8; 155 -10.4; 170 -10.0; 187 -9.5; 206 -9.0; 227 -8.5; 249 -8.1; 274 -7.7; 302 -7.3; 332 -6.9; 365 -6.4; 402 -5.9; 442 -5.3; 486 -4.7; 535 -4.1; 588 -3.4; 647 -2.8; 712 -2.3; 783 -1.8; 861 -1.4; 947 -1.0; 1042 -0.8; 1146 -0.7; 1261 -0.5; 1387 -0.7; 1526 -0.8; 1678 -1.4; 1846 -2.3; 2031 -3.7; 2234 -5.4; 2457 -7.4; 2703 -9.3; 2973 -10.3; 3270 -10.0; 3597 -8.8; 3957 -7.3; 4353 -6.5; 4788 -6.2; 5267 -6.8; 5793 -10.8; 6373 -15.2; 7010 -14.4; 7711 -7.9; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Spiritoso GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Spiritoso ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.14 | -6.9 dB  |
| Peaking | 1888 Hz | 0.35 | 8.0 dB   |
| Peaking | 2923 Hz | 1.45 | -11.2 dB |
| Peaking | 6639 Hz | 3.21 | -12.3 dB |
| Peaking | 8084 Hz | 5.2  | 2.3 dB   |
| Peaking | 5237 Hz | 5.46 | 1.2 dB   |
| Peaking | 5926 Hz | 9.96 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Spiritoso/Fischer%20Audio%20Spiritoso.png)