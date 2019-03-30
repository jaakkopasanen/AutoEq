# Apple EarPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.7; 1042 -1.8; 1146 -3.4; 1261 -5.5; 1387 -8.2; 1526 -11.6; 1678 -15.4; 1846 -19.1; 2031 -21.7; 2234 -23.0; 2457 -23.2; 2703 -22.9; 2973 -21.3; 3270 -18.9; 3597 -16.2; 3957 -14.1; 4353 -13.2; 4788 -13.3; 5267 -14.6; 5793 -17.1; 6373 -18.3; 7010 -16.8; 7711 -13.8; 8482 -9.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple EarPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 52 Hz   | 0.08 | 6.1 dB   |
| Peaking | 695 Hz  | 0.81 | 4.0 dB   |
| Peaking | 1083 Hz | 1.65 | 6.2 dB   |
| Peaking | 2329 Hz | 1.04 | -19.4 dB |
| Peaking | 6497 Hz | 3.24 | -9.4 dB  |
| Peaking | 1902 Hz | 3.69 | -4.1 dB  |
| Peaking | 2140 Hz | 1.33 | 6.4 dB   |
| Peaking | 3201 Hz | 0.84 | -6.7 dB  |
| Peaking | 4087 Hz | 1.98 | 5.5 dB   |
| Peaking | 9916 Hz | 2.4  | 2.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 4.3 dB   |
| Peaking | 125 Hz   | 1.41 | 4.5 dB   |
| Peaking | 250 Hz   | 1.41 | 4.6 dB   |
| Peaking | 500 Hz   | 1.41 | 4.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 9.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -17.8 dB |
| Peaking | 4000 Hz  | 1.41 | -6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB  |
| Peaking | 16000 Hz | 1.41 | 1.3 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Apple%20EarPods/Apple%20EarPods.png)