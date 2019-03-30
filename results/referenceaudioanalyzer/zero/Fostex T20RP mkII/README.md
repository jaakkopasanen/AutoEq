# Fostex T20RP mkII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.2; 96 -2.7; 106 -4.2; 116 -5.6; 128 -6.7; 141 -7.4; 155 -7.9; 170 -8.3; 187 -8.6; 206 -8.9; 227 -8.9; 249 -9.1; 274 -9.3; 302 -9.3; 332 -9.3; 365 -9.3; 402 -9.3; 442 -9.3; 486 -9.0; 535 -8.5; 588 -8.3; 647 -8.2; 712 -7.7; 783 -7.1; 861 -7.9; 947 -9.3; 1042 -10.4; 1146 -11.1; 1261 -10.9; 1387 -9.7; 1526 -8.0; 1678 -7.0; 1846 -7.2; 2031 -7.0; 2234 -5.8; 2457 -4.4; 2703 -3.8; 2973 -2.9; 3270 -1.9; 3597 -2.0; 3957 -2.0; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.0; 8482 -8.6; 9330 -8.6; 10263 -7.8; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T20RP mkII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T20RP mkII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 69 Hz   | 0.34 | 10.2 dB |
| Peaking | 171 Hz  | 0.46 | -8.5 dB |
| Peaking | 1219 Hz | 2.17 | -4.9 dB |
| Peaking | 5898 Hz | 0.76 | 9.3 dB  |
| Peaking | 8452 Hz | 1.37 | -8.4 dB |
| Peaking | 20 Hz   | 1.26 | 2.1 dB  |
| Peaking | 53 Hz   | 0.64 | -1.2 dB |
| Peaking | 81 Hz   | 3.28 | 2.1 dB  |
| Peaking | 788 Hz  | 8.35 | 1.3 dB  |
| Peaking | 2000 Hz | 8.05 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 6.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -3.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fostex%20T20RP%20mkII/Fostex%20T20RP%20mkII.png)