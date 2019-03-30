# Erzetich Mania
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.4; 45 -3.3; 49 -5.1; 54 -7.2; 60 -9.2; 66 -10.9; 72 -12.1; 79 -13.0; 87 -13.2; 96 -12.8; 106 -12.3; 116 -11.7; 128 -11.2; 141 -10.7; 155 -10.4; 170 -10.0; 187 -9.6; 206 -9.3; 227 -9.3; 249 -9.3; 274 -9.3; 302 -9.3; 332 -9.6; 365 -9.3; 402 -8.9; 442 -8.1; 486 -7.1; 535 -5.8; 588 -5.0; 647 -5.1; 712 -5.3; 783 -5.5; 861 -5.5; 947 -5.1; 1042 -4.0; 1146 -2.5; 1261 -1.4; 1387 -1.1; 1526 -1.4; 1678 -2.2; 1846 -2.7; 2031 -2.6; 2234 -2.2; 2457 -1.8; 2703 -2.0; 2973 -2.7; 3270 -3.1; 3597 -3.0; 3957 -5.4; 4353 -8.1; 4788 -12.1; 5267 -16.6; 5793 -17.2; 6373 -13.4; 7010 -8.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Erzetich Mania GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Erzetich Mania ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.41 | 18.0 dB  |
| Peaking | 72 Hz    | 0.49 | -19.4 dB |
| Peaking | 1314 Hz  | 3.18 | 2.9 dB   |
| Peaking | 3310 Hz  | 0.44 | 6.0 dB   |
| Peaking | 5512 Hz  | 2.39 | -16.7 dB |
| Peaking | 215 Hz   | 1.28 | 1.3 dB   |
| Peaking | 389 Hz   | 0.88 | -2.0 dB  |
| Peaking | 573 Hz   | 2.55 | 2.9 dB   |
| Peaking | 1944 Hz  | 6.83 | -0.5 dB  |
| Peaking | 12429 Hz | 2.35 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 9.7 dB  |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Erzetich%20Mania/Erzetich%20Mania.png)