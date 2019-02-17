# Apple EarPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.2; 49 -2.4; 54 -3.7; 60 -5.2; 66 -6.5; 72 -7.6; 79 -8.6; 87 -9.5; 96 -10.1; 106 -10.4; 116 -10.6; 128 -10.6; 141 -10.4; 155 -10.4; 170 -10.2; 187 -9.9; 206 -9.6; 227 -9.4; 249 -9.2; 274 -9.1; 302 -8.9; 332 -8.9; 365 -8.9; 402 -8.9; 442 -8.7; 486 -8.6; 535 -8.4; 588 -8.3; 647 -7.8; 712 -7.1; 783 -6.4; 861 -6.1; 947 -6.2; 1042 -6.7; 1146 -7.4; 1261 -8.4; 1387 -9.5; 1526 -10.6; 1678 -11.4; 1846 -11.9; 2031 -11.8; 2234 -11.1; 2457 -10.2; 2703 -9.4; 2973 -8.7; 3270 -7.9; 3597 -7.7; 3957 -8.0; 4353 -9.0; 4788 -10.1; 5267 -11.9; 5793 -14.4; 6373 -14.4; 7010 -12.1; 7711 -10.5; 8482 -9.2; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -7.1; 13660 -11.4; 15026 -10.4; 16529 -6.7; 18182 -6.5; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple EarPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.43 | 13.9 dB  |
| Peaking | 82 Hz    | 0.43 | -12.1 dB |
| Peaking | 1919 Hz  | 1.9  | -5.6 dB  |
| Peaking | 6144 Hz  | 2.35 | -8.3 dB  |
| Peaking | 14243 Hz | 3.8  | -5.9 dB  |
| Peaking | 576 Hz   | 1.18 | -1.4 dB  |
| Peaking | 864 Hz   | 1.76 | 2.1 dB   |
| Peaking | 1447 Hz  | 4.47 | -1.1 dB  |
| Peaking | 11055 Hz | 4.07 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Apple%20EarPods/Apple%20EarPods.png)