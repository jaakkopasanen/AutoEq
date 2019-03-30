# Fostex T50RP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.5; 25 -2.4; 28 -3.6; 31 -4.6; 34 -5.4; 37 -6.0; 41 -6.5; 45 -7.0; 49 -7.7; 54 -8.5; 60 -9.3; 66 -9.9; 72 -10.5; 79 -11.0; 87 -11.5; 96 -11.9; 106 -12.0; 116 -12.0; 128 -12.0; 141 -12.0; 155 -12.0; 170 -12.0; 187 -12.0; 206 -11.8; 227 -11.6; 249 -11.3; 274 -11.3; 302 -11.3; 332 -11.1; 365 -10.8; 402 -10.5; 442 -10.0; 486 -9.6; 535 -9.4; 588 -8.9; 647 -8.4; 712 -8.6; 783 -8.6; 861 -8.4; 947 -8.9; 1042 -9.8; 1146 -10.0; 1261 -9.6; 1387 -8.6; 1526 -7.2; 1678 -6.1; 1846 -5.7; 2031 -5.5; 2234 -4.9; 2457 -4.0; 2703 -3.0; 2973 -2.0; 3270 -0.9; 3597 -0.7; 3957 -0.7; 4353 -0.7; 4788 -0.7; 5267 -0.7; 5793 -0.8; 6373 -1.3; 7010 -4.2; 7711 -6.4; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T50RP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.02 | 7.5 dB  |
| Peaking | 93 Hz   | 0.81 | -3.7 dB |
| Peaking | 253 Hz  | 0.53 | -4.1 dB |
| Peaking | 1172 Hz | 2.59 | -3.4 dB |
| Peaking | 4148 Hz | 0.99 | 6.9 dB  |
| Peaking | 3198 Hz | 3.79 | 0.9 dB  |
| Peaking | 4123 Hz | 3.3  | -1.0 dB |
| Peaking | 6309 Hz | 2.72 | 4.7 dB  |
| Peaking | 7396 Hz | 1.54 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fostex%20T50RP/Fostex%20T50RP.png)