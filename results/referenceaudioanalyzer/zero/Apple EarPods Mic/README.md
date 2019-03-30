# Apple EarPods Mic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -1.0; 947 -1.9; 1042 -3.1; 1146 -4.8; 1261 -7.0; 1387 -9.8; 1526 -13.3; 1678 -17.5; 1846 -22.0; 2031 -25.6; 2234 -27.0; 2457 -25.9; 2703 -22.7; 2973 -18.9; 3270 -15.7; 3597 -13.4; 3957 -12.1; 4353 -11.5; 4788 -12.1; 5267 -13.8; 5793 -15.2; 6373 -15.1; 7010 -12.9; 7711 -9.7; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple EarPods Mic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods Mic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 58 Hz   | 0.08 | 6.1 dB   |
| Peaking | 692 Hz  | 0.94 | 4.3 dB   |
| Peaking | 1063 Hz | 1.81 | 4.7 dB   |
| Peaking | 2202 Hz | 1.47 | -23.4 dB |
| Peaking | 6174 Hz | 3.8  | -6.9 dB  |
| Peaking | 1330 Hz | 7.55 | 1.0 dB   |
| Peaking | 2739 Hz | 7.71 | -2.0 dB  |
| Peaking | 4028 Hz | 1.79 | 3.7 dB   |
| Peaking | 4661 Hz | 0.68 | -2.4 dB  |
| Peaking | 9082 Hz | 1.75 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 4.3 dB   |
| Peaking | 125 Hz   | 1.41 | 4.5 dB   |
| Peaking | 250 Hz   | 1.41 | 4.6 dB   |
| Peaking | 500 Hz   | 1.41 | 5.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 10.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -22.8 dB |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 16000 Hz | 1.41 | 0.8 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Apple%20EarPods%20Mic/Apple%20EarPods%20Mic.png)