# Creative MA 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -20.8; 23 -20.9; 25 -20.9; 28 -21.0; 31 -21.0; 34 -21.0; 37 -21.0; 41 -20.9; 45 -20.7; 49 -20.5; 54 -20.3; 60 -20.0; 66 -19.7; 72 -19.4; 79 -19.0; 87 -18.6; 96 -18.1; 106 -17.6; 116 -17.1; 128 -16.5; 141 -15.9; 155 -15.2; 170 -14.5; 187 -13.8; 206 -13.1; 227 -12.2; 249 -11.4; 274 -10.6; 302 -9.9; 332 -9.3; 365 -8.7; 402 -8.2; 442 -7.5; 486 -6.6; 535 -5.7; 588 -4.9; 647 -4.0; 712 -3.2; 783 -2.4; 861 -1.6; 947 -1.0; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -2.0; 2703 -4.0; 2973 -6.3; 3270 -7.9; 3597 -8.0; 3957 -6.7; 4353 -5.0; 4788 -3.8; 5267 -4.1; 5793 -7.1; 6373 -11.4; 7010 -11.6; 7711 -7.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative MA 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative MA 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.08 | -15.2 dB |
| Peaking | 1218 Hz  | 0.12 | 10.3 dB  |
| Peaking | 3403 Hz  | 1.87 | -9.8 dB  |
| Peaking | 6626 Hz  | 3.35 | -10.1 dB |
| Peaking | 10421 Hz | 0.8  | -3.0 dB  |
| Peaking | 456 Hz   | 3.95 | -0.6 dB  |
| Peaking | 960 Hz   | 2.4  | 0.8 dB   |
| Peaking | 1541 Hz  | 3.09 | -0.7 dB  |
| Peaking | 5136 Hz  | 6.96 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -15.4 dB |
| Peaking | 62 Hz    | 1.41 | -9.6 dB  |
| Peaking | 125 Hz   | 1.41 | -8.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 16000 Hz | 1.41 | 0.3 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Creative%20MA%20200/Creative%20MA%20200.png)