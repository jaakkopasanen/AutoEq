# Earsonics SM3v2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -13.6; 25 -13.7; 28 -13.8; 31 -13.9; 34 -13.9; 37 -14.0; 41 -14.0; 45 -13.9; 49 -13.9; 54 -13.9; 60 -13.9; 66 -13.9; 72 -13.9; 79 -13.9; 87 -13.8; 96 -13.6; 106 -13.5; 116 -13.3; 128 -13.3; 141 -13.4; 155 -13.7; 170 -13.5; 187 -13.3; 206 -13.1; 227 -12.8; 249 -12.6; 274 -12.3; 302 -12.0; 332 -11.8; 365 -11.5; 402 -11.2; 442 -10.8; 486 -10.4; 535 -10.0; 588 -9.5; 647 -9.1; 712 -8.7; 783 -8.2; 861 -7.8; 947 -7.4; 1042 -7.0; 1146 -6.7; 1261 -6.3; 1387 -6.0; 1526 -5.7; 1678 -5.5; 1846 -5.2; 2031 -4.9; 2234 -4.4; 2457 -3.5; 2703 -2.4; 2973 -1.6; 3270 -0.8; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics SM3v2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics SM3v2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 0.78 | -6.3 dB |
| Peaking | 43 Hz   | 0.38 | -6.2 dB |
| Peaking | 239 Hz  | 0.44 | -5.1 dB |
| Peaking | 4106 Hz | 0.96 | 6.8 dB  |
| Peaking | 4155 Hz | 3    | -1.9 dB |
| Peaking | 4633 Hz | 1.1  | 1.5 dB  |
| Peaking | 6273 Hz | 3.17 | 4.4 dB  |
| Peaking | 7368 Hz | 1.4  | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Earsonics%20SM3v2/Earsonics%20SM3v2.png)