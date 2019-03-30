# Philips SHG 7980
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -11.9; 25 -13.8; 28 -16.3; 31 -18.2; 34 -19.8; 37 -21.0; 41 -22.1; 45 -22.9; 49 -23.5; 54 -23.8; 60 -23.5; 66 -22.9; 72 -22.7; 79 -23.2; 87 -23.8; 96 -23.7; 106 -23.2; 116 -23.1; 128 -23.1; 141 -22.6; 155 -21.6; 170 -20.3; 187 -19.5; 206 -19.9; 227 -20.7; 249 -20.8; 274 -20.4; 302 -19.6; 332 -18.6; 365 -17.6; 402 -16.1; 442 -14.5; 486 -13.1; 535 -12.1; 588 -10.9; 647 -9.4; 712 -7.8; 783 -5.7; 861 -3.1; 947 -0.6; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.5; 3957 -2.2; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.5; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHG 7980 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHG 7980 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 44 Hz   | 0.92 | -11.7 dB |
| Peaking | 102 Hz  | 0.68 | -11.4 dB |
| Peaking | 306 Hz  | 0.65 | -10.3 dB |
| Peaking | 1062 Hz | 1.28 | 6.9 dB   |
| Peaking | 3073 Hz | 0.58 | 6.0 dB   |
| Peaking | 190 Hz  | 7.09 | 1.3 dB   |
| Peaking | 241 Hz  | 5.01 | -0.7 dB  |
| Peaking | 3861 Hz | 5.47 | -2.1 dB  |
| Peaking | 5812 Hz | 1.78 | 5.0 dB   |
| Peaking | 7284 Hz | 1.2  | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.4 dB  |
| Peaking | 62 Hz    | 1.41 | -14.5 dB |
| Peaking | 125 Hz   | 1.41 | -11.8 dB |
| Peaking | 250 Hz   | 1.41 | -11.2 dB |
| Peaking | 500 Hz   | 1.41 | -6.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20SHG%207980/Philips%20SHG%207980.png)