# Fostex T40RP mkII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.8; 49 -0.7; 54 -0.8; 60 -1.5; 66 -2.4; 72 -3.1; 79 -3.7; 87 -4.4; 96 -4.9; 106 -5.3; 116 -5.6; 128 -5.6; 141 -5.6; 155 -5.6; 170 -5.9; 187 -5.9; 206 -6.2; 227 -6.3; 249 -6.2; 274 -6.3; 302 -6.7; 332 -7.4; 365 -8.5; 402 -9.7; 442 -10.5; 486 -11.0; 535 -11.1; 588 -10.7; 647 -9.9; 712 -9.3; 783 -9.7; 861 -10.9; 947 -11.8; 1042 -12.1; 1146 -12.0; 1261 -11.3; 1387 -10.4; 1526 -10.1; 1678 -9.9; 1846 -9.0; 2031 -7.6; 2234 -6.3; 2457 -5.2; 2703 -4.2; 2973 -3.3; 3270 -3.0; 3597 -3.0; 3957 -2.5; 4353 -1.6; 4788 -1.4; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.5; 10263 -7.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T40RP mkII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T40RP mkII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.55 | 6.6 dB  |
| Peaking | 487 Hz  | 2.38 | -3.9 dB |
| Peaking | 1186 Hz | 1    | -6.0 dB |
| Peaking | 6090 Hz | 0.68 | 10.1 dB |
| Peaking | 8430 Hz | 0.99 | -7.9 dB |
| Peaking | 57 Hz   | 4.3  | 1.0 dB  |
| Peaking | 104 Hz  | 2.72 | -0.7 dB |
| Peaking | 272 Hz  | 4.13 | 0.7 dB  |
| Peaking | 1807 Hz | 6.9  | -1.0 dB |
| Peaking | 2838 Hz | 5.26 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.0 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | -3.5 dB |
| Peaking | 1000 Hz  | 1.41 | -4.8 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fostex%20T40RP%20mkII/Fostex%20T40RP%20mkII.png)