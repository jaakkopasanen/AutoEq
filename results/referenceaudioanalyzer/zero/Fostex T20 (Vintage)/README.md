# Fostex T20 (Vintage)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.2; 96 -1.9; 106 -2.5; 116 -3.0; 128 -3.5; 141 -3.8; 155 -4.1; 170 -4.4; 187 -4.5; 206 -4.6; 227 -4.9; 249 -4.9; 274 -4.9; 302 -4.9; 332 -4.8; 365 -4.6; 402 -4.5; 442 -4.3; 486 -4.0; 535 -3.7; 588 -3.4; 647 -3.3; 712 -3.6; 783 -4.3; 861 -5.1; 947 -5.7; 1042 -6.1; 1146 -6.4; 1261 -6.6; 1387 -6.9; 1526 -7.2; 1678 -7.5; 1846 -7.9; 2031 -8.2; 2234 -8.6; 2457 -9.5; 2703 -10.7; 2973 -11.7; 3270 -12.6; 3597 -13.1; 3957 -13.0; 4353 -12.1; 4788 -11.0; 5267 -9.4; 5793 -7.6; 6373 -6.7; 7010 -6.3; 7711 -6.5; 8482 -7.0; 9330 -7.9; 10263 -9.1; 11289 -10.2; 12418 -10.2; 13660 -8.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T20 (Vintage) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T20 (Vintage) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.34 | 6.5 dB  |
| Peaking | 604 Hz   | 1.43 | 3.1 dB  |
| Peaking | 3555 Hz  | 1.51 | -7.0 dB |
| Peaking | 11881 Hz | 2.7  | -4.2 dB |
| Peaking | 16 Hz    | 1.44 | 1.5 dB  |
| Peaking | 57 Hz    | 0.55 | -0.8 dB |
| Peaking | 76 Hz    | 2.35 | 1.4 dB  |
| Peaking | 4716 Hz  | 4.46 | -1.3 dB |
| Peaking | 6648 Hz  | 2.72 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 2.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | -6.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fostex%20T20%20(Vintage)/Fostex%20T20%20(Vintage).png)