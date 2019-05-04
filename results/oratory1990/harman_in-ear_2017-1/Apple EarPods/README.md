# Apple EarPods
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.8; 87 -1.7; 96 -2.5; 106 -3.0; 116 -3.3; 128 -3.4; 141 -3.5; 155 -3.5; 170 -3.4; 187 -3.2; 206 -3.1; 227 -3.1; 249 -3.1; 274 -3.1; 302 -3.1; 332 -3.0; 365 -3.0; 402 -3.2; 442 -3.3; 486 -3.4; 535 -3.5; 588 -3.6; 647 -3.9; 712 -4.1; 783 -4.4; 861 -4.7; 947 -5.2; 1042 -5.8; 1146 -6.5; 1261 -7.4; 1387 -8.6; 1526 -10.0; 1678 -11.3; 1846 -12.2; 2031 -12.3; 2234 -11.8; 2457 -11.4; 2703 -11.0; 2973 -10.3; 3270 -9.3; 3597 -8.4; 3957 -8.1; 4353 -8.4; 4788 -9.5; 5267 -11.5; 5793 -13.1; 6373 -9.9; 7010 -6.6; 7711 -6.2; 8482 -8.1; 9330 -10.1; 10263 -8.9; 11289 -6.5; 12418 -8.1; 13660 -17.6; 15026 -22.6; 16529 -18.7; 18182 -14.8; 20000 -14.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple EarPods GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.36 | 6.3 dB   |
| Peaking | 2114 Hz  | 0.58 | -15.0 dB |
| Peaking | 3683 Hz  | 0.1  | 10.0 dB  |
| Peaking | 5663 Hz  | 3.05 | -8.3 dB  |
| Peaking | 15548 Hz | 0.78 | -21.7 dB |
| Peaking | 121 Hz   | 3.5  | -0.8 dB  |
| Peaking | 7381 Hz  | 5.69 | 1.8 dB   |
| Peaking | 9474 Hz  | 2.8  | -4.8 dB  |
| Peaking | 11887 Hz | 2.25 | 5.8 dB   |
| Peaking | 14069 Hz | 4.16 | -5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 5.1 dB   |
| Peaking | 125 Hz   | 1.41 | 1.7 dB   |
| Peaking | 250 Hz   | 1.41 | 2.7 dB   |
| Peaking | 500 Hz   | 1.41 | 2.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 16000 Hz | 1.41 | -17.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Apple%20EarPods/Apple%20EarPods.png)