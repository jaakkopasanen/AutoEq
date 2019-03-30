# Pioneer HDJ-500-K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.3; 49 -2.0; 54 -2.7; 60 -3.3; 66 -3.7; 72 -4.0; 79 -4.2; 87 -4.4; 96 -4.5; 106 -4.8; 116 -4.8; 128 -4.8; 141 -4.5; 155 -4.4; 170 -4.2; 187 -4.1; 206 -3.8; 227 -3.6; 249 -3.5; 274 -3.8; 302 -3.8; 332 -3.6; 365 -3.4; 402 -4.1; 442 -5.2; 486 -5.9; 535 -6.3; 588 -6.4; 647 -6.8; 712 -7.3; 783 -7.6; 861 -7.8; 947 -8.0; 1042 -8.2; 1146 -8.1; 1261 -8.0; 1387 -8.0; 1526 -7.6; 1678 -7.0; 1846 -6.1; 2031 -5.1; 2234 -4.1; 2457 -3.1; 2703 -2.1; 2973 -1.3; 3270 -0.7; 3597 -1.3; 3957 -2.3; 4353 -4.6; 4788 -13.1; 5267 -17.9; 5793 -19.0; 6373 -19.0; 7010 -18.6; 7711 -15.7; 8482 -9.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.6; 13660 -12.7; 15026 -11.9; 16529 -8.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-500-K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-500-K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.55 | 6.3 dB   |
| Peaking | 259 Hz   | 1.27 | 3.0 dB   |
| Peaking | 3526 Hz  | 1.81 | 10.1 dB  |
| Peaking | 5920 Hz  | 1.86 | -16.3 dB |
| Peaking | 14394 Hz | 3.02 | -6.6 dB  |
| Peaking | 380 Hz   | 4.63 | 1.7 dB   |
| Peaking | 1195 Hz  | 0.84 | -2.2 dB  |
| Peaking | 2357 Hz  | 2.43 | 2.1 dB   |
| Peaking | 7501 Hz  | 4.76 | -5.8 dB  |
| Peaking | 9148 Hz  | 2.36 | 4.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 3.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -9.7 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Pioneer%20HDJ-500-K/Pioneer%20HDJ-500-K.png)